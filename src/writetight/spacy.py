import sys

import spacy
from spacy.language import Language
from spacy.matcher import Matcher


from writetight.patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    passive_voice,
    ly_adverbs,
)


def get_language_model() -> Language:
    try:
        nlp = spacy.load("en_core_web_sm")
    except IOError:
        print(
            f"You need the 'en_core_web_sm' language model from spaCy for write-tight to work.\n"
            f"Please enter the following command in your terminal with your virtual environment activated: \n"
            f"python -m spacy download en_core_web_sm\n"
            f"Check the README for more info."
        )
        sys.exit(1)

    return nlp


def get_matcher(nlp: Language) -> Matcher:
    matcher = Matcher(nlp.vocab)
    matcher.add("ambiguous-pronouns", [ambiguous_pronouns])
    matcher.add("ambiguous-openings", [ambiguous_openings])
    matcher.add("passive-voice", [passive_voice])
    matcher.add("ly-adverbs", [ly_adverbs])

    return matcher
