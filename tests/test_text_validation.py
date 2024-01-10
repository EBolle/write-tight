"""Test text validation functionality."""

import pytest

import writetight
from writetight.main import _path_exists, clean_text_file


def test_path_exists_empty_string_raises():
    "Validate that an empty string as path exists the program."
    with pytest.raises(SystemExit):
        _path_exists("")


def test_path_exists_bogus_path():
    "Validate that a non existing file exists the program."
    bogus_path = "this_file_does_not_exist.md"
    with pytest.raises(SystemExit):
        _path_exists(bogus_path)


def test_path_exists_real_path():
    "If the path of the input file exists, _path_exists returns the path."
    real_path = writetight.main.__file__
    assert _path_exists(real_path) == real_path


def test_clean_text_file():
    """
    clean_text() removes markdown styling operators '_' and '*' but does not
    transform HTML special characters.
    """
    str_with_md_styling_and_html_tags = """
    &ldquo;I am _very_ **outraged** by this!&rdquo; -> What does _very_ add to this sentence?
    """
    expected = """
    &ldquo;I am very outraged by this!&rdquo; -> What does very add to this sentence?
    """
    assert clean_text_file(str_with_md_styling_and_html_tags) == expected
