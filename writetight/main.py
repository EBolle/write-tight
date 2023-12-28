import spacy
from spacy.matcher import Matcher

from writetight.src.input_validation import get_text_file
from writetight.src.patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    passive_voice,
    ly_adverbs,
)


nlp = spacy.load("en_core_web_sm")

matcher = Matcher(nlp.vocab)
matcher.add("ambiguous_pronouns", [ambiguous_pronouns])
matcher.add("ambiguous_openings", [ambiguous_openings])
matcher.add("passive_voice", [passive_voice])
matcher.add("ly_adverbs", [ly_adverbs])


def main():
    text = get_text_file()
    text_lines = text.splitlines()

    for line_num, line in enumerate(text_lines, start=1):
        print(line_num, line)