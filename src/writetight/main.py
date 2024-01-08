import argparse
import re
import sys
from pathlib import Path
from typing import Optional

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

    # Split the raw text into lines to display the line number and column number of each match.
    text_lines = text_clean.splitlines()
    text_lines_numbered = [
        (line_number, line) for line_number, line in enumerate(text_lines)
    ]

    # The 'matches' object contains a list of matches in ascending order of the text.
    # Therefore the text can be analyzed efficiently line for line until all the matches
    # are consumed. A new match starts from the beginning of the sentence of the last match
    # to control for multiple matches in a single sentence.
    current_match = matches.pop(0)
    current_line_num = 0

    while matches:
        pattern_id, match_start_token, match_end_token = current_match
        pattern = nlp.vocab.strings[pattern_id]
        match = " ".join(text_tokens[match_start_token:match_end_token])

        current_line = text_lines_numbered[current_line_num][1]

        match_position = re.search(rf"\b{match}\b", current_line)
        if match_position is not None:
            print(
                f"Ln {str(current_line_num + 1).rjust(3)},"
                f"Col {str(match_position.start() + 1).rjust(3)}: "
                f"{pattern}['{match}'], {pattern_question(pattern, match)}"
            )
            current_match = matches.pop(0)
        else:
            current_line_num += 1
