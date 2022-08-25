import re

import pytest

from writetight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    personal_pronouns,
    subjunctive_mood,
)


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("https://ebolle.github.io/write-tight/styles.css", []),
        ("git it thatthere this THOSE", ["it", "this", "THOSE"]),
    ],
)
def test_regex_ambiguous_pronouns_word_boundaries(
    test_input: str, expected: str
):
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
def test_regex_ambiguous_openings(test_input: str, expected: str):
    assert re.findall(ambiguous_openings.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Would of, Could of, should of", ["Would", "Could", "should"]),
        ("wouldn't you say so?", []),
        ("Would I say that in such a manner?", ["Would"]),
    ],
)
def test_regex_subjunctive_mood(test_input: str, expected: str):
    assert re.findall(subjunctive_mood.pattern, test_input) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("Meaning should not match", []),
        ("Personally myself and I should", ["Personally", "myself", "I"]),
        ("imemine should not match due to word boundaries, r i ght?", ["i"]),
    ],
)
def test_regex_personal_pronouns(test_input: str, expected: str):
    assert re.findall(personal_pronouns.pattern, test_input) == expected
