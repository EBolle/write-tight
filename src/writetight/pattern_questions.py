"""Define questions based on the found pattern and match."""


def pattern_question(pattern: str, match: str) -> str:
    """
    Returns a question of which the answer should help the writer to
    improve his or her document.
    Turn this into a dictionary, possibily within a function, much better and faster.
    """
    questions = {
        "ambiguous-pronouns": ambiguous_pronouns_question(match),
        "ambiguous-openings": "Find who or what does the action and reconstruct the sentence.",
        "passive-voice": f"Who or what {match}? -> make the answer the subject of the verb.",
        "ly-adverbs": f"Does the adverb {match} provide value to your sentence?",
        "default": "No helper question available for this pattern.",
    }

    return questions.get(pattern, "default")


def ambiguous_pronouns_question(match: str) -> str:
    """
    Returns a different question based on the exact match of the pronoun. 
    """
    if match == "it":
        return "Does 'it' refer to the previous noun?"
    # "that", "there", "these", "those", "this"
    return f"{match} what? Is the answer inserted after the pronoun?"
