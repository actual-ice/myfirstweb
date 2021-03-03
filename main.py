from flask import Flask, redirect, url_for, render_template, request, session

app = Flask(__name__)
app.secret_key = "fensNKJB231&^**(6JHBbfhe&%"

@app.route("/", methods=["POST", "GET"])
def home():
    if request.method == "POST":
        if request.form["passwd"] == "gay":
            passwd = request.form["passwd"]
            session["passwd"] = passwd
            return redirect(url_for("enter"))
        else:
            return "<h1>INCORRECT PASSWORD</h1>"
    else:
        if "passwd" in session:
            return redirect(url_for("enter"))
        return render_template("password.html")
    


@app.route("/correct")
def enter():
    if not session:
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif session["passwd"] == "gay":
        return "<h1>congrats</h1>"

if __name__ == "__main__":
    app.run(debug=True)