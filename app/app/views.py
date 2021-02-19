from app import app

from flask import render_template, request, redirect, jsonify, make_response

@app.route("/")
def index():
    return render_template("public/index.html")


@app.route("/root")
def root():
    return render_template("public/index.html")


@app.route("/factorial")
def factorial():
    return render_template("public/index.html")


@app.route("/log")
def log():
    return render_template("public/index.html")


@app.route("/power")
def power():
    return render_template("public/index.html")