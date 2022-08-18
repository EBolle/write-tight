import re

import pytest

from writetight.src.non_default_patterns import passive_voice, repeated_words


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
def test_passive_voice(test_input: str, expected: str):
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
def test_repeated_words(test_input: str, expected: str):
    assert (
        next(re.finditer(repeated_words.pattern, test_input)).group()
        == expected
    )
