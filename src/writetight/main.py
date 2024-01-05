import re

from writetight.input_validation import (
    get_text_file,
    replace_markdown_style_operators,
)
from writetight.pattern_questions import pattern_question
from writetight.spacy import get_language_model, get_matcher


def main():
    """
    Better explanation here.
    """
    # Get the raw text, and remove the markdown stlye operators.
    text = get_text_file()
    text_clean = re.sub(r"(_|\*)", replace_markdown_style_operators, text)

    # Transform the raw text to a spaCy Doc to get the Token objects and matches.
    nlp = get_language_model()
    doc = nlp(text)
    text_tokens = [token.text for token in doc]
    matcher = get_matcher(nlp)
    matches = matcher(doc)

    # Split the raw text into lines to display the line number and column number of each match.
    text_lines = text_clean.splitlines()
    text_lines_numbered = [
        (line_number, line) for line_number, line in enumerate(text_lines)
    ]

    # The 'matches' object contains a list of matches in ascending order of the text.
    # Therefore the text can be analyzed efficiently line for line until all the matches
    # are consumed. A new match starts from the beginning of the sentence of the last match
    # to control for multiple matches in a single sentence.
    current_match = matches.pop(0)
    current_line_num = 0

    while matches:
        pattern_id, match_start_token, match_end_token = current_match
        pattern = nlp.vocab.strings[pattern_id]
        match = " ".join(text_tokens[match_start_token:match_end_token])

        current_line = text_lines_numbered[current_line_num][1]

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
