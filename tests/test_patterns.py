from spacy.matcher import Matcher

from writetight.patterns import (
    ambiguous_openings,
    ambiguous_pronouns,
    ly_adverbs,
    passive_voice,
)


def test_pattern(nlp, text, pattern, pattern_name):
    """
    Avoid boilerplate by using a simple function just for the tests.
    """
    pass


def test_ambiguous_openings(nlp):
    """
    Who or what was amazing? The weather? The food? Or something else?
    This sentence could be improved by simply removing 'It was amazing out'.
    Or by specifying 'It': 'The wedding was amazing'.
    """
    text = "The weather was great and the food was lovely. It was amazing."
    doc = nlp(text)
    text_tokens = [token.text for token in doc]

    matcher = Matcher(nlp.vocab)
    matcher.add("ambiguous-openings", [ambiguous_openings])
    matches = matcher(doc)

    _, match_start_token, match_end_token = matches[0]
    match = " ".join(text_tokens[match_start_token:match_end_token])

    assert match == "It was"


def test_ambiguous_pronouns(nlp):
    """
    What does 'this' refer to? The more specifc, the better.
    'Please read the README.md file before you start.
    """
    text = "Please read this before you start."
    doc = nlp(text)
    text_tokens = [token.text for token in doc]

    matcher = Matcher(nlp.vocab)
    matcher.add("ambiguous-pronouns", [ambiguous_pronouns])
    matches = matcher(doc)

    _, match_start_token, match_end_token = matches[0]
    match = " ".join(text_tokens[match_start_token:match_end_token])

    assert match == "this"


def test_ly_adverbs(nlp):
    """
    Concise writing is better writing. Alternatives like great
    or awesome are better.
    """
    text = "That movie is really good."
    doc = nlp(text)
    text_tokens = [token.text for token in doc]

    matcher = Matcher(nlp.vocab)
    matcher.add("ly-adverbs", [ly_adverbs])
    matches = matcher(doc)

    _, match_start_token, match_end_token = matches[0]
    match = " ".join(text_tokens[match_start_token:match_end_token])

    assert match == "really"
