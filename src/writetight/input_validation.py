import sys
from pathlib import Path
from re import Match
from typing import Optional


def get_text_file() -> str:
    if len(sys.argv) > 1:
        input_file_path = sys.argv[1]
    else:
        print("Please provide a path to the text file.")
        return

    if Path(input_file_path).exists():
        input_file_path_abs = Path(input_file_path).absolute()
        with open(input_file_path_abs, encoding="utf-8") as input_stream:
            input_file = input_stream.read()
        return input_file
    else:
        print("The path does not exist.")
        return


def replace_markdown_style_operators(match_object: Match) -> Optional[str]:
    """
    Markdown adds style operators like _ and * to for italicized and bold words.
    These style operators must be removed since re.search looks for matches within
    word boundaries.
    """
    if match_object.group(0) in ("-", "*"):
        return ""
