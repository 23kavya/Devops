from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "secret123"

# Dummy user
USER = {
    "username": "student",
    "password": "1234"
}

complaints = []

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USER["username"] and password == USER["password"]:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid credentials")

    return render_template("login.html")

@app.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template("dashboard.html", complaints=complaints)

@app.route("/complaint", methods=["POST"])
def complaint():
    if "user" not in session:
        return redirect(url_for("login"))

    title = request.form["title"]
    description = request.form["description"]

    complaints.append({
        "title": title,
        "description": description,
        "status": "Pending"
    })

    return redirect(url_for("dashboard"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
