from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key = 'KeepItSecretKeepItSafe'
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def reply():
    user_name = request.form["name"]
    leng = request.form["leng"]
    location = request.form["locations"]
    comment = request.form["comment"]
    if len(user_name) == 0:
        flash("Name can't be black")
        return redirect("/")
    elif not len(comment) > 121:
        flash("Comment has to be a least 120 characters")
        return redirect("/")
    else:
        flash("Thank you for your info")
        return redirect("/")
    # return render_template('result.html', name=user_name, leng=leng, location = location, comment = comment)

@app.route("/back", methods=["POST"])
def go_back():
    return redirect("/")
app.run(debug=True)
