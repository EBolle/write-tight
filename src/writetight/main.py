import re

import spacy
from spacy.matcher import Matcher

from writetight.input_validation import (
    get_text_file,
    replace_markdown_style_operators,
)
from writetight.patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    passive_voice,
    ly_adverbs,
)
from writetight.pattern_questions import pattern_question


try:
    nlp = spacy.load("en_core_web_sm")
except IOError as err:
    print(f"You need the 'en_core_web_sm' language model from spaCy for write-tight to work.\n"
          f"Please enter the following command in your terminal with your virtual environment activated: \n"
          f"python -m spacy download en_core_web_sm\n"
          f"Check the README for more info.")


matcher = Matcher(nlp.vocab)
matcher.add("ambiguous-pronouns", [ambiguous_pronouns])
matcher.add("ambiguous-openings", [ambiguous_openings])
matcher.add("passive-voice", [passive_voice])
matcher.add("ly-adverbs", [ly_adverbs])


def main():
    """
    This function reads a text file, which is processed in three ways.

    1. As an nlp doc instance to get every pattern match and its location in the text file.
    2. As a list of tokens to get the string match based on the match location.
    3. As a list of line numbers and lines to link the location of the string match to the exact line number and column.

    The matcher instance returns a list of matches with the start token of the match in ascending order.
    This ascending order is leveraged to only try to match the first match found with the first line of the text file.
    If there is a match, the second match is initialized. If there is no match, the second line of the text file is processed.
    """
    text = get_text_file()
    text_clean = re.sub(r"(_|\*)", replace_markdown_style_operators, text)
    text_lines = text_clean.splitlines()
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

        match_position = re.search(rf"\b{match}\b", current_line)
        if match_position is not None:
            print(
                f"Ln {str(current_line_num + 1).rjust(3)},"
                f"Col {str(match_position.start() + 1).rjust(3)}: "
                f"{pattern}['{match}'], {pattern_question(pattern, match)}"
            )
            current_match = matches.pop(0)
        else:
            current_line_num += 1
