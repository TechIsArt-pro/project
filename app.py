from flask import Flask, redirect, render_template, session, request, url_for
from cs50 import SQL
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime;

from helpers import login_required

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

db = SQL("sqlite:///chemistry.db")

@app.route('/')
@login_required
def welcome():
    return render_template("welcome.html")

@app.route('/periodictable')
@login_required
def index():
    user = session["user_id"]
    username = db.execute(
        "SELECT username FROM users WHERE id = ?", user)    
    return render_template("index.html", username=username)

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not username or not password or not confirmation:
            return render_template("apology.html")
        elif not (password == confirmation):
            return render_template("apology.html")

        check = db.execute("SELECT username FROM users WHERE username = ?", username)
        if check:
            return render_template("apology.html")
        hashedpassword = generate_password_hash(password, method='pbkdf2', salt_length=16)

        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, hashedpassword)

        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    return render_template("register.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    session.clear()

    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("apology.html")
        elif not request.form.get("password"):
            return render_template("apology.html")
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return render_template("apology.html")

        session["user_id"] = rows[0]["id"]

        return redirect("/")

    else:
        return render_template("login.html")
    
@app.route("/logout")
@login_required
def logout():
    session.clear()
    return redirect("/")

@app.route("/labbook")
@login_required
def labbook():
    user = session["user_id"]
    entries = db.execute("SELECT id, title, date FROM lab_book_entry WHERE user_id = ?", user)
    return render_template("labbook.html", entries=entries, user=user)

@app.route("/entry", methods=["GET", "POST"])
@login_required
def entry():
    date = datetime.now().strftime("%D")
    user = session["user_id"]
    if request.method == "POST":
        title = request.form.get("title")
        main_reagent = request.form.get("name1")
        main_weight = request.form.get("weight1")
        main_moles = request.form.get("moles1")
        reagent = request.form.get("name2")
        weight = request.form.get("weight2")
        moles = request.form.get("moles2")
        content = request.form.get("text")
        content = request.form.get("text")

        if not title or not main_reagent or not main_weight or not main_moles or not reagent or not weight or not moles or not content:
            return render_template("apology.html")
        
        db.execute("INSERT INTO lab_book_entry (title, content, main_reagent, main_weight, main_moles, reagent, weight, moles, user_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", title, content, main_reagent, main_weight, main_moles, reagent, weight, moles, user)

        return redirect("/labbook")
       
    return render_template("entry.html", date=date)

@app.route("/edit/<int:entry_id>", methods=["GET", "POST"])
@login_required
def edit(entry_id):
    user = session["user_id"]
    if request.method == "GET":
        entry = db.execute("SELECT * FROM lab_book_entry WHERE id = ?", entry_id)
        return render_template("edit.html", entry=entry)
    
    elif request.method == "POST":
        title = request.form.get("title")
        main_reagent = request.form.get("name1")
        main_weight = request.form.get("weight1")
        main_moles = request.form.get("moles1")
        reagent = request.form.get("name2")
        weight = request.form.get("weight2")
        moles = request.form.get("moles2")
        content = request.form.get("text")

        if not title or not main_reagent or not main_weight or not main_moles or not reagent or not weight or not moles or not content:
            return render_template("apology.html")

        
        db.execute("UPDATE lab_book_entry SET title = ?, content = ?, main_reagent = ?, main_weight = ?, main_moles = ?, reagent = ?, weight = ?, moles = ? WHERE id = ?", title, content, main_reagent, main_weight, main_moles, reagent, weight, moles, entry_id)

        return redirect("/labbook")
    return render_template("edit.html", entry=entry)
    
    

    

if __name__ == "__main__":
    app.run(debug=True)