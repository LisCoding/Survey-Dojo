from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def reply():
    user_name = request.form["name"]
    leng = request.form["leng"]
    location = request.form["locations"]
    comment = request.form["comment"]
    return render_template('result.html', name=user_name, leng=leng, location = location, comment = comment)

@app.route("/back", methods=["POST"])
def go_back():
    return redirect("/")
app.run(debug=True)
