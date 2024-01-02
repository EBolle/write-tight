# write-tight

This project improves your professional writing with the help of simple rule-based writing patterns. The inspiration of this project comes from two sources:

1. The book "Write Tight: Say Exactly What You Mean With Precision and Power" by William Brohaugh.
2. The Udemy course "Business Writing & Technical Writing Immersion" by Paul Siegel (Starweaver Instructor Team).

Both sources emphasise that eliminating &lsquo;deadwood&rsquo; is critical to improve your writing.

> &ldquo;Deadwood is the the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing.&rdquo;
>
> _William Brohaugh_

Examples of deadwood writing patterns are:

1. Adverbs that end on &lsquo;ly&rsquo;

- &ldquo;I am _very_ outraged by this!&rdquo; -> What does _very_ add to this sentence?
- &ldquo;That movie is _really_ good.&rdquo; -> Words like _great_ or _awesome_ are better alternatives for &lsquo;really good&rsquo;.
- &ldquo;That is _basically_ a good idea.&rdquo; -> Just leave it out.

- Passive voice

Explain

- Ambiguous pronouns

Explain

- Ambiguous openings

Explain

The detailed descriptions on how to detect and remove these deadwood patterns are translated into rule based expressions using the [spaCy][spacy] matcher.

## How to use write-tight?

Write-tight provides a command-line interface and sends the found patterns to `stdout`, similar to `pylint` for example.

<image>

The reason for the command-line interface is that I write most of my digital content (blog posts, web pages, technical instructions) in a code editor (`VSCode`), and that I want feedback on my writing without having to copy-paste the content, and going back and forth between different applications.

The only argument you have to provide is the path to your text file. Note that your text file is read as-is, so you are not limited to a certain format, for example Markdown (`.md`).

## Getting started

Clone the repo and move into the top directory.

```bash
git clone https://github.com/EBolle/write-tight.git
cd write-tight
```

Create and activate a new virtual environment, and install the requirements. If you have Anaconda installed you can use the following commands.

```
conda create --name write-tight python=3.11
conda activate write-tight

pip install -r requirements.txt
```

Run the following command.

```bash
wt your_text_file.md
```

## Limitations

Only the English language is supported.

The suggestions are rule based and adhere to a certain style of writing. It is therefore likely that not every edge case will
be matched, and that you might disagree with the suggestions. However, if you like the rule based approach and the user interface, you
can easily modify the project to your own writing style.

[udemy]: https://www.udemy.com/course/business-writing-immersion/
[write-tight]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[blogpost-1]: https://www.ernst-bolle.com/posts/regex-part-1
[blogpost-2]: https://www.ernst-bolle.com/posts/regex-part-2
[spacy]: https://www.spacy.io
[spacy-matcher]: https://spacy.io/api/matcher
[release-notes]: https://github.com/EBolle/write-tight/releases
