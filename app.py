from flask import Flask, render_template_string

app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return render_template_string("Hello {{ name }}!", name=name)
