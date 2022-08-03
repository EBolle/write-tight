# write-tight

This project aims to make you a better business with the help of simple rule based patterns. According to a [popular Udemy course on business writing][udemy] we should spend 50% of our writing time on post-writing. In this post-writing phase we make sure our documents are written as clear and concise as possible, which is sometimes referred to as tight writing.

There are certain patterns in our writing which we want to avoid if we want to write tight. These are patterns that indicate 'deadwood'. According to the [book on tight writing][write-tight] deadwood is the unnecessarily difficult, long, or simply unnecessarily phrases or words that clog the arteries of professional writing. A few examples:

- Words that end on 'ly'
- Passive voice
- Subjunctive mood
- Ambiguous pronouns
- Ambiguous openings

All these writing patterns are translated to regular expressions, which are at the core of this project. In case of a match, the text is color highlighted so you can easily spot potential improvements.

<img src="https://user-images.githubusercontent.com/49920622/182711607-b49c6918-b372-4634-8fcb-fc1a7d37e2d3.png" width=800>

More information and motivation about improving your business writing with regular expressions can be found in my series of posts on this topic.

- [Improve your writing with regular expressions (part 1)][blogpost-1]
- [Improve your writing with regular expressions (part 2)][blogpost-2]

## Getting started

Start by cloning the Github repo and moving in the top directory.

```bash
git clone https://github.com/EBolle/write-tight.git
cd write-tight
```

Next create and activate a new virtual environment and run the following command, for example:

```
conda create --name write-tight python=3.9
conda activate write-tight

pip install -r requirements.txt
```

Next run the following python command to start the local flask server.

```bash
python main.py
```

Finally open your browser, go to `localhost:5000` and either start typing or pasting your text.

## Limitations

The current version only supports five patterns, but I intend to add many other useful patterns in the coming months.

The suggestions are rule based and adhere to a certain style of writing. It is therefore likely that not every edge case will
be matched, and that you might disagree with the suggestions. However, if you like the rule based approach and the interface, you
could easily modify the project to your own writing stlye.

[udemy]: https://www.udemy.com/course/business-writing-immersion/
[write-tight]: https://www.amazon.nl/Write-Tight-Exactly-Precision-Power/dp/1402210515
[blogpost-1]: https://www.ernst-bolle.com/posts/regex-part-1
[blogpost-2]: https://www.ernst-bolle.com/posts/regex-part-2
