from flask import Flask, render_template, redirect, request, url_for
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index() -> str:
    points = request.args.get("points")
    return render_template("index.html", points=points)

@app.route("/evaluate", methods="POST")
def evaluate() -> str:
    request_data = request.get_json()
    min_x = request_data["min_x"]
    max_x = request_data["max_x"]
    min_y = request_data["min_y"]
    max_y = request_data["max_y"]
    equation = request_data["equation"]

    points = []

    return redirect(url_for("/", points))
