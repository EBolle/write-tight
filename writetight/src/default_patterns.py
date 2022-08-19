"""The defualt patterns adhere to the Pattern interface and have a
straightforward implementation.
"""
import re

from writetight.src.pattern import Pattern


class DefaultPattern(Pattern):
    def __init__(self, name: str, pattern: re.Pattern[str]):
        super().__init__(name, pattern)

    def match_and_replace(self, html_content: str) -> str:
        return re.sub(self.pattern, self.add_span_element, html_content)

    def add_span_element(self, match: re.Match[str]) -> str:
        match_str = match.group()
        return f"<span class='{self.name}'>{match_str}</span>"


ambiguous_pronouns = DefaultPattern(
    name="ambiguous-pronouns",
    pattern=re.compile(
        r"\b(it|that|there|these|those|this)\b", flags=re.IGNORECASE
    ),
)

ambiguous_openings = DefaultPattern(
    name="ambiguous-openings",
    pattern=re.compile(
        r"\b(There|It)\b\s{1}\b(am|are|is|was|were|been|being)\b"
    ),
)

words_ending_with_ly = DefaultPattern(
    name="words-ending-with-ly", pattern=re.compile(r"\w+ly\b")
)

subjunctive_mood = DefaultPattern(
    name="subjunctive-mood",
    pattern=re.compile(r"\b(would|should|could)\b", flags=re.IGNORECASE),
)

personal_pronouns = DefaultPattern(
    name="personal-pronouns",
    pattern=re.compile(
        r"\b(i|me|mine|my|myself|personally)\b", flags=re.IGNORECASE
    ),
)
