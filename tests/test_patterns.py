from spacy.matcher import Matcher

from writetight.patterns import (
    ambiguous_openings,
    ambiguous_pronouns,
    ly_adverbs,
    passive_voice,
)


def test_ambiguous_openings(nlp):
    """
    Who or what was amazing? The weather? The food? Or something else?
    This sentence could be improved by simply removing 'It was amazing out'.
    Or by specifying 'It': 'The wedding was amazing'.
    """
    text = """
    The weather was great and the food was lovely. It was amazing.
    """
    doc = nlp(text)
    text_tokens = [token.text for token in doc]

    matcher = Matcher(nlp.vocab)
    matcher.add("ambiguous-openings", [ambiguous_openings])
    matches = matcher(doc)

    _, match_start_token, match_end_token = matches[0]
    match = " ".join(text_tokens[match_start_token:match_end_token])

    assert match == "It was"
