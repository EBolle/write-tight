"""Define the rule-based patterns."""


# style patterns
ambiguous_openings = [
    {"TEXT": {"IN": ["It", "There"]}},
    {"LEMMA": "be"},
]
ambiguous_pronouns = [
    {
        "POS": "PRON",
        "TEXT": {"IN": ["it", "that", "there", "these", "those", "this"]},
    }
]
ly_adverbs = [{"TEXT": {"REGEX": r"\w+ly$"}, "POS": "ADV"}]
passive_voice = [{"LEMMA": "be"}, {"POS": "VERB"}]
