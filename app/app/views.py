from app import app
from app import logger
from flask import render_template, request, redirect, jsonify, make_response, flash

import math

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"


@app.route("/")
def index():
    app.logger.info("Rendering index.html")
    return render_template("public/index.html")


@app.route("/root", methods=["GET", "POST"])
def root():

    app.logger.info("Running square root function")

    if request.method == "POST":

        req = request.form

        try:
            x = int(req.get("root_number"))

            if x<0:
                app.logger.error("Square root of negative numbers is not defined")
                flash("Square root of negative numbers is not defined", "danger")
                return redirect(request.url)
            
            if x>=0:
                answer = x**0.5
                app.logger.info(f"Square root of {x} is {answer}")
                flash(f"{answer} is the square root of {x}", "success")
                return redirect(request.url)


        except ValueError:
            app.logger.error("Improper form submission")
            flash("Please fill the form correctly", "warning")
            return redirect(request.url)

    return render_template("public/index.html")


@app.route("/factorial", methods=["GET", "POST"])
def factorial():

    app.logger.info("Running factorial function")

    if request.method == "POST":

        req = request.form

        try:
            x = int(req.get("fact_number"))

            if x<0:
                app.logger.error("Factorial of negative numbers is not defined")
                flash("Factorial of negative numbers is not defined", "danger")
                return redirect(request.url)
            
            if x>=0:
                answer = math.factorial(x)
                app.logger.info(f"Factorial of {x} is {answer}")
                flash(f"{answer} is the Factorial of {x}", "success")
                return redirect(request.url)


        except ValueError:
            app.logger.error("Improper form submission")
            flash("Please fill the form correctly", "warning")
            return redirect(request.url)

    return render_template("public/index.html")


@app.route("/log", methods=["GET", "POST"])
def log():

    app.logger.info("Running log function")

    if request.method == "POST":

        req = request.form

        try:
            x = int(req.get("log_number"))

            if x<=0:
                app.logger.error("Natural logarithm of non-positive numbers is not defined")
                flash("Natural logarithm of non-positive numbers is not defined", "danger")
                return redirect(request.url)
            
            if x>0:
                answer = math.log(x)
                app.logger.info(f"Natural logarithm of {x} is {answer}")
                flash(f"{answer} is the Natural logarithm of {x}", "success")
                return redirect(request.url)


        except ValueError:
            app.logger.error("Improper form submission")
            flash("Please fill the form correctly", "warning")
            return redirect(request.url)

    return render_template("public/index.html")


@app.route("/power", methods=["GET", "POST"])
def power():

    app.logger.info("Running power function")

    if request.method == "POST":

        req = request.form

        try:
            x = int(req.get("number"))
            y = int(req.get("power"))
            
            answer = pow(x, y)
            app.logger.info(f"Power of {x} raised to {y} is {answer}")
            flash(f"Power of {x} raised to {y} is {answer}", "success")
            return redirect(request.url)
            

        except ValueError:
            app.logger.error("Improper form submission")
            flash("Please fill the form correctly", "warning")
            return redirect(request.url)

    return render_template("public/index.html")