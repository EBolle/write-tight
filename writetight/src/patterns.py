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


# def helper_questions(pattern: str, match: str) -> str:
#     """
#     Returns a question of which the answer should help the writer to
#     improve his or her document.
#     Turn this into a dictionary, possibily within a function, much better and faster.
#     """
#     if pattern == "ambiguous-pronouns" and match == "it":
#         output = "Does 'it' refer to the previous noun?"
#     elif pattern == "ambiguous-pronouns":
#         output = f"{match} what? Is the answer inserted after the pronoun?"
#     elif pattern == "ambiguous-openings":
#         output = "Find who or what does the action and reconstruct the sentence."
#     elif pattern == "passive-voice":
#         output = f"Who are what {match}? -> make the answer the subject of the verb."
#     elif pattern == "ly-adverbs":
#         output = "Does the adverb provide value to your sentence?"
#     else:
#         output = f"No helper question defined for this pattern: {pattern}."

#     return output


# Loop throough the input file and return the matches and helper questions

# for line_num, line in enumerate(text_lines, start=1):
#     doc = nlp(line)
#     text_list = [token.text for token in doc]
#     matches = matcher(doc)

#     for pattern_id, start, end in matches:
#         pattern = nlp.vocab.strings[pattern_id]
#         match = " ".join(text_list[start:end])
#         surrounding_text = " ".join(text_list[start - 3 : end + 3])

#         print(
#             f"line {line_num}: {pattern}['{match}'] '{surrounding_text}' -> "
#             f"{helper_questions(pattern, match)}"
#         )
