from flask import Flask, render_template

app = Flask("my first program")

@app.route("/page")
def page():
    return "<b>Hello world</b>"

@app.route("/")
def index():
    return render_template("index.html")

app.run()
