from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def textarea():
    return render_template("index.html")


@app.route("/", methods=["POST"])
def textarea_post():
    return f"You entered {request.form['text']}"


if __name__ == "__main__":
    app.run(debug=True)
