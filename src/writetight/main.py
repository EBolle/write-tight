# pylint: disable=missing-function-docstring
"""Write-tight - improve your writing with simple rule-based patterns."""


import argparse
import re
import sys
from collections import namedtuple
from pathlib import Path
from string import Template
from typing import Generator, Optional

from spacy.language import Language
from spacy.matcher import Matcher
from writetight.pattern_questions import pattern_question
from writetight.nlp import get_language_model, get_matcher


def get_parser():
    parser = argparse.ArgumentParser(
        prog="write-tight",
        description="This program validates whether your input text file exists.",
    )
    parser.add_argument("path", type=_path_exists, help="path to your text file.")

    return parser


def _path_exists(path: str) -> str:
    if Path(path).is_file():
        return path

    sys.exit(f"Could not find the specified path: {path}.")


def get_text_file(path: str) -> str:
    extension = path.rsplit(".")[-1]
    if extension.lower() != "md":
        print(
            "Warning: your input file is not recognized as Markdown. "
            "Write-tight might not function as expected.\n"
        )

    with open(Path(path), encoding="utf-8") as input_stream:
        input_file = input_stream.read()

    return input_file


def clean_text_file(text: str) -> str:
    """
    Markdown adds style operators like _ and * for italicized and bold words.
    These style operators must be removed since re.search looks for exact matches
    within word boundaries.
    """
    return re.sub(r"(_|\*)", _replace_markdown_style_operators, text)


def _replace_markdown_style_operators(match_object: re.Match) -> Optional[str]:
    if match_object.group(0) in ("_", "*"):
        return ""
    return None


def text_to_numbered_lines(text: str) -> list[namedtuple]:
    """
    Transforms a raw string of text into a list of namedtuples
    with fields number and text.
    """
    text_lines = text.splitlines()
    TextLine = namedtuple("TextLine", ["number", "line"])
    output = [TextLine(number, line) for number, line in enumerate(text_lines, start=1)]

    return output


def get_matches(
    text: str, nlp: Language, matcher: Matcher
) -> Generator[list, None, None]:
    """
    This function tries to find and return the matches of simple writing patterns in the
    user provided text. To aid the understanding of the main function the matches are returned
    as a generator. This provides the next(matches) functionality which signals that we
    exhaust the matches while going through the text.
    """
    doc = nlp(text)
    text_tokens = [token.text for token in doc]
    matches = matcher(doc)

    if not matches:
        sys.exit("Did not find any matches.")

    clean_matches = []

    for match in matches:
        pattern_id, match_start_token, match_end_token = match
        pattern = nlp.vocab.strings[pattern_id]
        match = " ".join(text_tokens[match_start_token:match_end_token])

        clean_matches.append((pattern, match))

    for clean_match in clean_matches:
        yield clean_match


def _print_found_matches(found_matches: list[tuple]) -> None:
    """
    Prints the found matches in a human readable format.
    """
    template_string = "Ln $line_number, Col $col_number: $pattern['$match']"
    for match in found_matches:
        pattern, match, numbered_line, match_object = match
        output = Template(template_string).substitute(
            pattern=pattern,
            match=match,
            line_number=str(numbered_line.number).rjust(3),
            col_number=str(match_object.start() + 1).rjust(3),
        )

        print(output)


def main() -> None: # pylint:disable=too-many-locals
    """
    The goal of this function is to find matches of simple writing patterns in the
    user provided text, and print any match and their location to stdout.
    """
    # Get and valdiate the input path to the text file
    parser = get_parser()
    args = parser.parse_args()

    # Clean the text file and split the text into a list of numbers and lines
    text = get_text_file(args.path)
    text_clean = clean_text_file(text)
    text_in_numbered_lines = text_to_numbered_lines(text_clean)

    # Get the pattern matches of the text, if any
    nlp = get_language_model()
    matcher = get_matcher(nlp)
    matches = get_matches(text_clean, nlp, matcher)

    # **** main functionality **** #

    current_match = next(matches)
    current_line_number = 0  # text_in_numbered_lines starts at index 0
    found_matches = []
    matches_left = True

    while matches_left:
        pattern, match = current_match
        current_line = text_in_numbered_lines[current_line_number].line

        found_match = re.search(rf"\b{match}\b", current_line)
        if found_match:
            found_matches.append(
                (
                    pattern,
                    match,
                    text_in_numbered_lines[current_line_number],
                    found_match,
                )
            )
            try:
                current_match = next(matches)
            except StopIteration:
                matches_left = False
        else:
            current_line_number += 1

    _print_found_matches(found_matches)
