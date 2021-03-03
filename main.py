from flask import Flask, redirect, url_for, render_template, request, session

#initialize the app
app = Flask(__name__)
app.secret_key = "fensNKJB231&^**(6JHBbfhe&%"


@app.route("/", methods=["POST", "GET"])
def home():
    """
    if the request was from posting a form, check the input, and if input is "gay"
    then redirect to "enter"
    """
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
    """
    if user entered correct password from "home" then render "congrats" on screen
    if user attemps to cheat and types /correct without entering correct password, redirect user
    to rick atsley
    """
    if not session:
        return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    elif session["passwd"] == "gay":
        return "<h1>congrats</h1>"

#driver functions
if __name__ == "__main__":
    app.run(debug=True)