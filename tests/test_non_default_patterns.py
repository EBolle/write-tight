import re

import pytest

from writetight.src.non_default_patterns import (
    passive_voice,
    repeated_words,
    adverbs_ending_with_ly,
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Am I?", [("Am", "I")]),
        ("Aren't you the best?", []),
        ("We have been walking for hours now.", [("been", "walking")]),
        ("So how have you been? Great.", []),
        ("It was             amazing", [("was", "amazing")]),
    ],
)
def test_regex_passive_voice(test_input: str, expected: str):
    assert re.findall(passive_voice.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("this this is a repetition", "this this"),
        ("IGNORE ignore case is on", "IGNORE ignore"),
        ("more   more spaces is still a repeat", "more   more"),
        (
            "three three three or more repeats are not considered",
            "three three",
        ),
    ],
)
def test_regex_repeated_words(test_input: str, expected: str):
    assert (
        next(re.finditer(repeated_words.pattern, test_input)).group()
        == expected
    )


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("information on", []),
        ("with the world", []),
    ],
)
def test_regex_repeated_words_empty_return(test_input: str, expected: str):
    """Without the word boundaries on on and th th would match."""
    assert list(re.finditer(repeated_words.pattern, test_input)) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("ly", []),
        ("HappiLy", []),
        ("onlyyou", []),
        ("finally you showed up, you silly", ["finally", "silly"]),
        ("happillllllly ever after", ["happillllllly"]),
    ],
)
def test_regex_adverbs_ending_with_ly(test_input: str, expected: str):
    assert re.findall(adverbs_ending_with_ly.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("apply", "apply"),
        ("usually", "<span class=adverbs-ending-with-ly>usually</span>"),
    ],
)
def test_adverbs_ending_with_ly(test_input: str, expected: str):
    assert (
        adverbs_ending_with_ly.match_and_replace(html_content=test_input)
        == expected
    )
