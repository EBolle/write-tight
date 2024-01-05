import argparse
import re
from pathlib import Path
from typing import Optional


def path_exists(path: str) -> str:
    """
    Return the path string if the path exists.
    """
    if Path(path).exists() and len(path) > 0:
        return path
    else:
        raise FileNotFoundError(path)


parser = argparse.ArgumentParser(
    prog="write-tight",
    description="this program validates whether your input text file exists.",
)
parser.add_argument("path", type=path_exists)


def get_text_file() -> str:
    """
    Return the text file if the path argument exists.
    """
    args = parser.parse_args()
    path: str = args.path

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
    return re.sub(r"(_|\*)", replace_markdown_style_operators, text)


def replace_markdown_style_operators(match_object: re.Match) -> Optional[str]:
    """
    Helper function for clean_text_file().
    """
    if match_object.group(0) in ("-", "*"):
        return ""
