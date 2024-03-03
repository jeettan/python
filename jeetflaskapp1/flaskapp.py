from flask import Flask, redirect, url_for, render_template, request, session, flash
import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False) 

app = Flask(__name__)
app.secret_key = "Hello"

@app.route("/register", methods=["POST","GET"])
def register():
    if request.method == "POST":
        cursor = conn.cursor()
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("INSERT INTO info (username,password) VALUES (?,?)", (username, password))
        conn.commit()
        cursor.close()
        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        cursor = conn.cursor()
        username = request.form["username"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM info WHERE username = ?", (username,))
        result = cursor.fetchone()
        if result:
            stored_password = result[1]  
            if stored_password == password:
                cursor.close()
                session["user"] = username
                return redirect(url_for("welcome"))
            else:
                flash("Incorrect password")
        else:
            flash("No such username exists")

    return render_template("home.html")    

@app.route("/welcome")
def welcome():
    if "user" in session:
        user = session["user"]
        return render_template("welcome.html", user=user)
    else:
        return "<h1> You have not logged in successfully </h1>"

@app.route("/logout")
def logout():
    session.pop("user",None)
    flash("You have logged out")
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)
    
