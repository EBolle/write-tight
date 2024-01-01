# write-tight

This project will help you become a better (business) writer with the help of simple rule based writing patterns. The inspiration of this project comes from two sources:

1. The book "Write Tight: say exactly what you want with precision and power" by <author>
2. The Udemy course "Business writing immersion" by <author>

Both sources emphasise that eliminating deadwood is important to improve your writing.

> deadwood is the the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing
> Write Tight

Both sources provide numerous detailed descriptions of deadwood patterns, and how to detect and remove them. A few examples:

- Adverbs that end on 'ly'
- Passive voice
- Subjunctive mood
- Ambiguous pronouns
- Ambiguous openings
- More patterns will follow in future releases..

This project translated these (anti) writing patterns into rule based expressions using the [spaCy][spacy] matcher.

## How to use write-tight?

Write-tight provides a command-line interface and sends the found patterns to `stdout`, similar to `pylint` for example.

<image>

The reason for this setup is that I write most of my digital content (blog posts, web pages, technical instructions) in `VSCode`, and that I want to get feedback on my writing without having to copy-paste the content, and going back and forth between applications. The text file you provide as input is read as-is, so you are not limited to the Markdown `.md` format.

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

Run the following python command to start a local flask server.

```bash
python main.py
```

Finally open your browser, go to `localhost:5000` and either start typing or paste in your text.

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
