# write-tight

This project aims to make you a better (business) writer with the help of simple rule based patterns. According to a [popular Udemy course on business writing][udemy] we should spend 50% of our writing time on post-writing. In this post-writing phase we make sure our documents are written as clear and concise as possible, which is sometimes referred to as tight writing.

There are certain patterns in our writing which we want to avoid if we want to write tight. These are patterns that indicate 'deadwood'. According to the [book on tight writing][write-tight] deadwood is the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing. A few examples:

- Words that end on 'ly'
- Passive voice
- Subjunctive mood
- Ambiguous pronouns
- Ambiguous openings

This project translated these writing patterns to regular expressions. In case of a match, the text is color highlighted so you can easily spot potential improvements. The following example text comes directly from one of my blog posts.

<img src="https://user-images.githubusercontent.com/49920622/182711607-b49c6918-b372-4634-8fcb-fc1a7d37e2d3.png" width=800>

More information and motivation about improving your (business) writing with regular expressions can be found in my series of posts on this topic.

- [Improve your writing with regular expressions (part 1)][blogpost-1]
- [Improve your writing with regular expressions (part 2)][blogpost-2]

## Getting started

Clone the repo and move into the top directory.

```bash
git clone https://github.com/EBolle/write-tight.git
cd write-tight
```

Create and activate a new virtual environment, and install the requirements. If you have Anaconda installed you can use the following commands.

```
conda create --name write-tight python=3.9
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

The current version only supports five patterns.

The suggestions are rule based and adhere to a certain style of writing. It is therefore likely that not every edge case will
be matched, and that you might disagree with the suggestions. However, if you like the rule based approach and the user interface, you
can easily modify the project to your own writing style.

The maximum number of characters is set to 1000 to keep the experience smooth. When more sentence- and paragraph patterns become
available this number will be increased.

Currently the project has only been tested on Linux with Google Chrome.

## What is next?

- [x] Me, myself, and I pattern
- [x] Repeated words pattern
- [ ] Sentence length variance
- [ ] Paragraph length variance
- [ ] Patterns build with the [spaCy Matcher][spacy-matcher]
- [ ] Many more..

## Docker

The Dockerfile is included for testing but you are welcome to use it for your own purposes.
If you run these commands locally the user interface is again available at `localhost:5000`.

```bash
docker build -t write-tight .
docker run -d -p 5000:5000 write-tight
```

[udemy]: https://www.udemy.com/course/business-writing-immersion/
[write-tight]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[blogpost-1]: https://www.ernst-bolle.com/posts/regex-part-1
[blogpost-2]: https://www.ernst-bolle.com/posts/regex-part-2
[spacy-matcher]: https://spacy.io/api/matcher
