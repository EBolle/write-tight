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

3. Ambiguous pronouns

- &ldquo;The weather was great and the food was lovely. _It_ was amazing.&rdquo; -> What was amazing? The weather? the food? Something else?
- &ldquo;Please read _this_ before you start.&rdquo; -> Please read the README.md file before you start.

Both sources provide detailed descriptions on how to detect and handle deadwood patterns. This project translates the descriptions to rule-based matching patterns with the help of [spaCy][spacy], and specifically the [spaCy Matcher][spacy-matcher].

## Getting started

Create and activate a new virtual environment, and install `write-tight` with pip.

```
pip install write-tight
```

Write-tight provides a command line interface and prints the detected patterns and suggestions on how to improve your text. The only argument you have to provide is the path to your text file. Although this project is developed with Markdown (`.md`) files in mind, your text file is read as-is, so you are not limited to a certain format.

<image>

The command line interface allows to stay in your code editor while you write and edit your digital content.

## Limitations

Only the English language is supported.

The suggestions are rule based and adhere to a certain style of writing. It is therefore likely that not every edge case will
be matched, and that you might disagree with the suggestions. However, if you like the rule based approach and the user interface, you
can easily modify the project to your own writing style.

[wt-book]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[udemy]: https://www.udemy.com/course/business-writing-immersion/
[spacy]: https://www.spacy.io
[spacy-matcher]: https://spacy.io/api/matcher
