import os

from cs50 import SQL
# import sqlite3
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from datetime import datetime, date
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, usd
# lookup,


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
# app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
# db = SQL("sqlite:///finance.db")
db = SQL("sqlite:///test.db") 

@app.route("/")
@login_required
def index():
    # Get user account Info
    user_id = session["user_id"]
    today = date.today()
    the_date = today.strftime("%B %d, %Y")
    numRows = db.execute('SELECT COUNT(*) FROM (SELECT * FROM user)')
    rows = db.execute("SELECT * FROM user WHERE id = :user_id", user_id=user_id)
    print(numRows)
    # If no transaction are yet made
    if not rows:
        return render_template("index.html")
    else:
        for row in rows:
            username = row["username"]
    
    
    return render_template("index.html", user_id=user_id, username=username, the_date=the_date)
    


@app.route("/income")
@login_required
def income():
    # Check if this stock is in users Portfolio
    # user_id = session["user_id"]
    # today = date.today()
    today = "2021-03-08"
    # print(today)
    # rows = db.execute("SELECT date FROM income WHERE date = ?", today)
    numRows = db.execute('SELECT COUNT(*) FROM (SELECT * FROM income)')
    rows = db.execute("SELECT * FROM income WHERE date = :today", today=today)
    print(numRows)
    if not rows :
        print("not ROW")
    else:
        for row in rows:
            heute = row["date"]
            print("today:" + heute)
            print('Income Found')
    
    return render_template("income.html")

@app.route("/outcome")
@login_required
def outcome():
    # Check if this stock is in users Portfolio
    user_id = session["user_id"]
    
    return render_template("outcome.html")

@app.route("/staff")
@login_required
def staff():
    # Check if this stock is in users Portfolio
    user_id = session["user_id"]
    
    return render_template("staff.html")
    






















@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM user WHERE username = :username", username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")



def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)


# User can add cash in his account
# @app.route("/cash", methods=["GET", "POST"])
# @login_required
# def cash():
#     """Add Cash in your account"""
#     user_id = session["user_id"]
#     # Get the user cash ammount
#     cash_row = db.execute("SELECT * FROM budget WHERE user_id = :user_id", user_id=user_id)
#     cash = 0
#     for i in cash_row:
#         cash = i["cash"]
#         print("cash", cash)
#     if request.method == "GET":
#         return render_template("cash.html", cash=cash)
#     else:
#         new_cash = request.form.get("cash")
#         cash = round(float(cash) + float(new_cash), 2)
#         # Update the cash amount from user, in the budget table
#         sql_update_query = """UPDATE budget SET cash = ? WHERE user_id = ?"""
#         data = (cash, user_id)
#         db.execute(sql_update_query, data)
#         flash("CASH ADDED!")

#     return redirect("/")