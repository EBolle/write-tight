from pathlib import Path

from flask import Flask, render_template, request
from markupsafe import escape, Markup

from writetight.src.default_patterns import (
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
)
from writetight.src.non_default_patterns import passive_voice


patterns = [
    ambiguous_pronouns,
    ambiguous_openings,
    words_ending_with_ly,
    subjunctive_mood,
    passive_voice,
]
TEMPLATE_PATH = Path(".") / "writetight" / "templates"
STATIC_PATH = Path(".") / "writetight" / "static"


app = Flask(__name__, template_folder=TEMPLATE_PATH, static_folder=STATIC_PATH)  # type: ignore


@app.route("/")
def textarea():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def textarea_post():
    text_input = request.form["text"]
    text_output = escape(text_input)

    for pattern in patterns:
        text_output = pattern.match_and_replace(text_output)

    return render_template("index.html", submit_text=Markup(text_output))


if __name__ == "__main__":
    app.run(debug=True)