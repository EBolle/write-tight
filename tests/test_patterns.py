from spacy.matcher import Matcher

from writetight.patterns import (
    ambiguous_openings,
    ambiguous_pronouns,
    ly_adverbs,
    passive_voice,
)


def get_match(nlp, text, pattern):
    """
    Boilerplate code for getting the match. This function 
    only returns the first match found.
    """
    doc = nlp(text)
    text_tokens = [token.text for token in doc]

    matcher = Matcher(nlp.vocab)
    # the name of the pattern is not relevant for the tests
    matcher.add("default", [pattern])
    matches = matcher(doc)

    _, match_start_token, match_end_token = matches[0]
    match = " ".join(text_tokens[match_start_token:match_end_token])

    return match


def test_ambiguous_openings(nlp):
    """
    Who or what was amazing? The weather? The food? Or something else?
    This sentence could be improved by simply removing 'It was amazing out'.
    Or by specifying 'It': 'The wedding was amazing'.
    """
    text = "The weather was great and the food was lovely. It was amazing."
    match = get_match(nlp, text, ambiguous_openings)

    assert match == "It was"


def test_ambiguous_pronouns(nlp):
    """
    What does 'this' refer to? The more specifc, the better.
    'Please read the README.md file before you start.'
    """
    text = "Please read this before you start."
    match = get_match(nlp, text, ambiguous_pronouns)

    assert match == "this"


def test_ly_adverbs(nlp):
    """
    Concise writing is better writing. Alternatives like 'great'
    or 'awesome' are better.
    """
    text = "That movie is really good."
    match = get_match(nlp, text, ly_adverbs)

    assert match == "really"


def test_passive_voice(nlp):
    """
    Who are what modified the README.md file? 
    'John Doe modified the README.md file.'
    """
    text = "The README.md file was modified with new content."
    match = get_match(nlp, text, passive_voice)

    assert match == "was modified"