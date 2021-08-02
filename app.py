from flask import Flask, redirect, url_for, render_template, request
from twilio.rest import Client
import time
import schedule
from datetime import datetime

app = Flask(__name__)

account = "AC84f950f6bae2ef652bddd8d2200011d9"
token = "c67cd225bfc1694ac6c52f6fce26b12b"
client = Client(account, token)
twilio_number = "18587269285"
test_msg = "this is a test"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=["GET", "POST"])
def form():
    sms_desc = request.form.get("description")
    sms_time = request.form.get("time")
    sms_num = request.form.get("phone")
    sms_msg = sms_desc + " " + "today" + " at " + sms_time
    print(sms_desc, sms_time, sms_num, sms_msg)
    # schedule.every().day.at(sms_time).do(send_msg(sms_num, sms_desc))
    client.messages.create(to=sms_num, from_=twilio_number, body=sms_msg)
    return render_template('success.html', desc=sms_desc, time=sms_time, num=sms_num)

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

if __name__ == "__main__":
    app.run()



while True:
    schedule.run_pending()
    time.sleep(1)