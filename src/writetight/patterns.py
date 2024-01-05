# Define the patterns


ambiguous_pronouns = [
    {
        "POS": "PRON",
        "TEXT": {"IN": ["it", "that", "there", "these", "those", "this"]},
    }
]
ambiguous_openings = [
    {"TEXT": {"IN": ["It", "There"]}},
    {"LEMMA": "be"},
]
passive_voice = [{"LEMMA": "be"}, {"POS": "VERB"}]
ly_adverbs = [{"TEXT": {"REGEX": r"\w+ly$"}, "POS": "ADV"}]
