import re

import pytest

from writetight.src.non_default_patterns import passive_voice


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
