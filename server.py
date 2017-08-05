from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def reply():
    user_name = request.form["name"]
    # lenguage = request.form["value"]
    return render_template('result.html', name=user_name)

app.run(debug=True)
