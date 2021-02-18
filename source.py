from flask import Flask,request, redirect, url_for, render_template
import smtplib

from flask_mail import Mail,Message


app = Flask(__name__)


@app.route('/welcome')
@app.route('/home')
@app.route("/")
def index():
    return render_template("index.html") #render a template


@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/explore")
def explore():
    return render_template("explore.html")

@app.route("/invest")
def invest():
    return render_template("invest.html")


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = "info.pipsmakerfx@gmail.com"
app.config['MAIL_PASSWORD'] = "Pipsmakerfx@1"
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)

@app.route('/contact')
def contact():
    return render_template("contact.html")


def sendContactForm(result):
    msg = Message("Contact Form From Website",
                    sender="[info.pipsmakerfx@gmail.com]",
                    recipients=["info.pipsmakerfx@gmail.com"])

    msg.body = """
    
    Hello there,

    You just received a contact form.

    name: {}
    contact: {}
    email: {}
    Message: {}


    regards,
    Pipsmaker FX

    
    """.format(result['name'], result['phone'], result['email'], result['message'])

    mail.send(msg)

@app.route('/send_message',methods=['GET', 'POST'])
def send_message():
    if request.method == "POST":
        result = {}


        result['name'] = request.form['name']
        result['phone'] = request.form['phone']
        result['email'] = request.form['email'].replace('','').lower()
        result['message'] = request.form['message']

        sendContactForm(result)


    return render_template("contact.html",)

if __name__ == "__main__":
    app.run(debug=True)
    TEMPLATES_AUTO_RELOAD = True
    app.secret_key = 'super_secret_key'
