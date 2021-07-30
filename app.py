from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)


@app.route('/, methods=["GET", "POST"]')
def home():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

# def send_sms():
#     sms_num = request.form.get("phone")
#     sms_sub = request.form.get("subject")
#     sms_desc = request.form.get("description")
#     sms_dt = request.form.get("date-time")


if __name__ == "__main__":
    app.run()
