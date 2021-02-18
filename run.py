from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/welcome')
@app.route('/home')
@app.route("/")
def index():
    return render_template("index.html") #render a template

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")


if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'