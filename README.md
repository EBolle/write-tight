# write-tight

This project improves your professional writing with the help of simple rule-based writing patterns. The inspiration of this project comes from two sources:

1. The book [Write Tight: Say Exactly What You Mean With Precision and Power][wt-book] by William Brohaugh.
2. The Udemy course [Business Writing & Technical Writing Immersion][udemy] by Paul Siegel (Starweaver Instructor Team).

Both sources emphasise that eliminating &lsquo;deadwood&rsquo; is critical to improve your writing.

> &ldquo;Deadwood is the the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing.&rdquo;
>
> _William Brohaugh_

Examples of deadwood writing patterns are:

1. Adverbs that end on &lsquo;ly&rsquo;

- &ldquo;I am _very_ outraged by this!&rdquo; -> What does _very_ add to this sentence?
- &ldquo;That movie is _really_ good.&rdquo; -> Words like _great_ or _awesome_ are better alternatives for &lsquo;really good&rsquo;.
- &ldquo;That is _basically_ a good idea.&rdquo; -> Just leave it out.

2. Passive voice

Active voice ensures clarity and achieves greater writing precision by answering _who_ or _what_ performs an action.

- &ldquo;The README.md file _was modified_ with new content.&rdquo; -> Passive voice, who or what modified the README.md file?
- &ldquo;John Doe modified the README.md file with new content.&rdquo; -> This sentence in active voice is more precise.

3. Ambiguous Openings

- &ldquo;The weather was great and the food was lovely. _It was_ amazing.&rdquo; -> What was amazing? The weather? the food? Something else?

All the patterns and their details are described in the [tests][patterns-tests].

Both sources provide detailed descriptions on how to detect and handle deadwood patterns. This project translates the descriptions to rule-based matching patterns with the help of [spaCy][spacy], and specifically the [spaCy Matcher][spacy-matcher].

## Getting started

Create and activate a new virtual environment, and install `write-tight` with pip.

```
pip install write-tight
```

This project depends on a trained spaCy pipeline called `en_core_web_sm`, and you need to download this pipeline manually if you do not already have it.

```
python -m spacy download en_core_web_sm
```

Please refer to the [spaCy installation page][spacy-usage] in case of any issues.

Write-tight provides a command line interface and prints the detected patterns and suggestions on how to improve your text. The only argument you have to provide is the path to your text file.

```
(venv) writetight <path_to_your_text_file>
```

![write-tight cli example][wt-cli-img]

Although this project is developed with Markdown (`.md`) files in mind, your text file is read as-is, so you are not limited to a certain format.

## Limitations

Only the English language is supported.

The suggestions are rule-based which make them easy to use and understand. The downside is that these rules do not cover every edge case, and are limited in the complexity they can handle. Furthermore, the rule-based suggestions adhere to a writing style that you might not like. If that is the case I hope the project is structured well enough so that you can easily modify the existing patterns to a writing style of your liking.

[wt-book]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[udemy]: https://www.udemy.com/course/business-writing-immersion/
[patterns-tests]: ./tests/test_patterns.py
[spacy]: https://www.spacy.io
[spacy-matcher]: https://spacy.io/api/matcher
[spacy-usage]: https://spacy.io/usage
[wt-cli-img]: https://github.com/EBolle/write-tight/blob/main/docs/write-tight-cli.png?raw=true
