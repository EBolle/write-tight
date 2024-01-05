import pytest

from writetight import input_validation


def test_path_exists_empty_string_raises():
    """
    The empty string translates to ("."), which actually exists.
    To make the input explicit, I have added len(path) > 1.
    """
    with pytest.raises(FileNotFoundError):
        input_validation.path_exists("")


def test_path_exists_bogus_path():
    bogus_path = "this_file_does_not_exist.md"
    with pytest.raises(FileNotFoundError):
        input_validation.path_exists(bogus_path)


def test_path_exists_real_path():
    """
    If the path of the input file exists, path_exists will simply return it.
    """
    real_path = input_validation.__file__
    assert input_validation.path_exists(real_path) == real_path


def test_clean_text_file():
    str_with_md_styling = """
    # A h1 header
    Shaken, **not** stirred. _James Bond_.
    """
    expected = """
    # A h1 header
    Shaken, not stirred. James Bond.
    """
    assert input_validation.clean_text_file(str_with_md_styling) == expected