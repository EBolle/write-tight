"""These patterns need additional logic but adhere to
the same Pattern interface.
"""
import re

import spacy

from writetight.src.pattern import Pattern


nlp = spacy.load("en_core_web_sm")


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
        return nlp(word)[0].pos_ == "VERB"


passive_voice = PassiveVoicePattern(
    name="passive-voice",
    pattern=re.compile(
        r"\b(am|are|is|was|were|been|being)\b\s+(\w+)\b",
        flags=re.IGNORECASE,
    ),
)


class RepeatedWordsPattern(Pattern):
    def __init__(self, name: str, pattern: re.Pattern[str]):
        super().__init__(name, pattern)

    def match_and_replace(self, html_content: str) -> str:
        return re.sub(self.pattern, self.add_span_element, html_content)

    def add_span_element(self, match: re.Match[str]) -> str:
        "Due to re.IGNORECASE it still makes sense to split the words."
        first_word, second_word = match.group().split()

        return f"{first_word} <span class={self.name}>{second_word}</span>"


repeated_words = RepeatedWordsPattern(
    name="repeated-words",
    pattern=re.compile(r"\b(\w+)\s+\1\b", flags=re.IGNORECASE),
)


class AdverbsEndingWithLy(Pattern):
    def __init__(self, name: str, pattern: re.Pattern[str]):
        super().__init__(name, pattern)

    def match_and_replace(self, html_content: str) -> str:
        return re.sub(self.pattern, self.add_span_element, html_content)

    def add_span_element(self, match: re.Match[str]) -> str:
        match_str = match.group()

        if self.is_adjective(match_str):
            return f"<span class={self.name}>{match_str}</span>"
        else:
            return match_str

    def is_adjective(self, word: str) -> bool:
        return nlp(word)[0].pos_ == "ADV"


words_ending_with_ly = AdverbsEndingWithLy(
    name="words-ending-with-ly", pattern=re.compile(r"\w+ly\b")
)
