import re

import pytest

from writetight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("https://ebolle.github.io/write-tight/styles.css", []),
        ("git it thatthere this THOSE", ["it", "this", "THOSE"]),
    ],
)
def test_ambiguous_pronouns_word_boundaries(test_input: str, expected: str):
    assert re.findall(ambiguous_pronouns.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Therefore is this a test.", []),
        ("It was an amazing experience.", [("It", "was")]),
        ("Hi there, it was amazing!", []),
        ("There  are spaces to consider.", []),
    ],
)
def test_ambiguous_openings(test_input: str, expected: str):
    assert re.findall(ambiguous_openings.pattern, test_input) == expected


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
def test_words_ending_with_ly(test_input: str, expected: str):
    assert re.findall(words_ending_with_ly.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Would of, Could of, should of", ["Would", "Could", "should"]),
        ("wouldn't you say so?", []),
        ("Would I say that in such a manner?", ["Would"]),
    ],
)
def test_subjunctive_mood(test_input: str, expected: str):
    assert re.findall(subjunctive_mood.pattern, test_input) == expected
