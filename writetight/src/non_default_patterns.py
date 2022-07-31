"""These patterns need additional logic but adhere to
the same Pattern interface.
"""
import re

from nltk.corpus import wordnet as wn  # type: ignore

from writetight.src.pattern import Pattern


class PassiveVoicePattern(Pattern):
    def __init__(self, name: str, pattern: re.Pattern[str]):
        super().__init__(name, pattern)

    def match_and_replace(self, html_content: str) -> str:
        return re.sub(self.pattern, self.add_span_element, html_content)

    def add_span_element(self, match: re.Match[str]) -> str:
        """Combine the matches to avoid whitespace or newline characters
        within the string leading to errors.
        """
        match_words = f"{match.group(1)} {match.group(2)}"

        return self.validate(match_words)

    def validate(self, match_words: str) -> str:
        """Only keep the match words of which the second word of the match
        is a verb.
        """
        second_word = match_words.split()[1]

        if self.is_verb(second_word):
            return f"<span class='{self.name}'>{match_words}</span>"
        else:
            return match_words

    def is_verb(self, word: str) -> bool:
        return bool(wn.synsets(word, pos=wn.VERB))


passive_voice = PassiveVoicePattern(
    name="passive-voice",
    pattern=re.compile(
        r"\b(am|are|is|was|were|been|being)\b\s+(\w+)\b",
        flags=re.IGNORECASE,
    ),
)
