from flask import Flask, request, render_template, redirect

app = Flask(__name__)

@app.route("/", methods = ["GET","POST"])
def user_login():
    return render_template("login.html")

if __name__== "__main__":
    app.run(host='0.0.0.0', port= 5050, debug=True)