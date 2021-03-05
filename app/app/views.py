from app import app

from flask import render_template, request, redirect, jsonify, make_response

from app import logger


@app.route("/")
def index():
    app.logger.info("Rendering index.html")
    return render_template("public/index.html")


@app.route("/root")
def root():
    logger.info("Running square root function")
    return render_template("public/index.html")


@app.route("/factorial")
def factorial():
    app.logger.info("Running factorial function")
    return render_template("public/index.html")


@app.route("/log")
def log():
    app.logger.info("Running log function")
    return render_template("public/index.html")


@app.route("/power")
def power():
    app.logger.info("Running Power function")
    return render_template("public/index.html")