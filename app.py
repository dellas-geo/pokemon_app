import json

from flask import Flask, render_template, url_for

app = Flask(__name__)

with open("data/data.json") as file:
    data = json.loads(file.read())


@app.route("/")
def home():
    return render_template("home.html", data=data)


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == ("__main__"):
    app.run(debug=True)
