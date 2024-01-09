import argparse
import re
import sys
from collections import namedtuple
from pathlib import Path
from typing import Generator, Optional

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
    """
    Return the path string if the path refers to a file.
    """
    if Path(path).is_file():
        return path
    else:
        print(f"Could not find the specified path: {path}.")
        sys.exit(1)


def get_text_file(path: str) -> str:
    """
    Return the text file if the path argument exists.
    """
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
    """
    Helper function for clean_text_file().
    """
    if match_object.group(0) in ("-", "*"):
        return ""
    

def text_to_numbered_lines(text: str) -> list[namedtuple]:
    """
    Transforms a raw string of text into a list of namedtuples 
    with fields number and text. 
    """
    text_lines = text.splitlines()
    TextLine = namedtuple("TextLine", ["number", "line"])
    output = [TextLine(number, line) for number, line in enumerate(text_lines, start=1)]

    return output


def _matches_generator(matches: list) -> Generator[list, None, None]:
    """
    Transforms the matches list into a generator to leverage the
    next() function. This simplifies understanding the main functionality.
    """
    for match in matches:
        yield match


def main():
    """
    Better explanation here.
    """
    parser = get_parser()
    args = parser.parse_args()

    # Get the raw text, and remove the markdown stlye operators.
    text = get_text_file(args.path)
    text_clean = clean_text_file(text)

    # Transform the raw text to a spaCy Doc to get the Token objects and matches.
    nlp = get_language_model()
    doc = nlp(text_clean)
    text_tokens = [token.text for token in doc]
    matcher = get_matcher(nlp)
    matches = matcher(doc)

    text_in_numbered_lines = text_to_numbered_lines(text_clean)
    matches_generator = _matches_generator(matches)

    # *** main functionality *** # 

    current_match = next(matches_generator)
    current_line_number = 0 # the text_in_numbered_lines is a list which starts at index 0   
    matches_left = True 

    while matches_left:
        pattern_id, match_start_token, match_end_token = current_match
        # Move the pattern to the print statement where you use it
        pattern = nlp.vocab.strings[pattern_id]
        match = " ".join(text_tokens[match_start_token:match_end_token])

        current_line = text_in_numbered_lines[current_line_number].line 

        found_match = re.search(rf"\b{match}\b", current_line)
        if found_match:
            print(
                f"Ln {str(text_in_numbered_lines[current_line_number].number).rjust(3)},"
                f"Col {str(found_match.start() + 1).rjust(3)}: "
                f"{pattern}['{match}'], {pattern_question(pattern, match)}"
            )
            try:
                current_match = next(matches_generator)
            except StopIteration:
                matches_left = False 
        else:
            current_line_number += 1