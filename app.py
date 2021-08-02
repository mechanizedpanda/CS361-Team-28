from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def form():
    default_name = "0"
    sms_sub = request.form.get("subject", default_name)
    sms_desc = request.form.get("description", default_name)
    sms_date = request.form.get("date", default_name)
    sms_time = request.form.get("time", default_name)
    sms_num = request.form.get("phone", default_name)
    print(sms_sub, sms_desc, sms_date, sms_time, sms_num)
    return render_template('success.html')

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run(debug=True)
