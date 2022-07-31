from flask import Flask, render_template, request
from markupsafe import Markup


app = Flask(__name__)


@app.route("/")
def textarea():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def textarea_post():
    """Be very careful with the markupsafe option. You first need to eliminate
    all HTML characters, and only return your own HTML as safe.
    """
    return render_template(
        "index.html",
        submit_text=Markup(f"{request.form['text']}"),
    )


if __name__ == "__main__":
    app.run(debug=True)
