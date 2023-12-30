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
    text_lines_num = [(line_num, line) for line_num, line in enumerate(text_lines)]

    doc = nlp(text)
    text_tokens = [token.text for token in doc]
    matches = matcher(doc)

    # matches is a list with matches in ascending order
    current_match = matches.pop(0)
    current_line_num = 0

    while matches:
        pattern_id = current_match[0]
        pattern = nlp.vocab.strings[pattern_id]

        match_start_token = current_match[1]
        match_end_token = current_match[2]        
        match = " ".join(text_tokens[match_start_token:match_end_token])

        current_line = text_lines_num[current_line_num][1]

        if match in current_line:
            print(current_line_num + 1, pattern, match, current_line)
            current_match = matches.pop(0)
        else:
            current_line_num += 1        