
from flask import Flask, request, redirect
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse


app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/sms", methods= ['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("I think Javascript is the best!")
    return str(resp)



# Your Account SID from twilio.com/console
account_sid = ""
# Your Auth Token from twilio.com/console
auth_token  = ""

client = Client(account_sid, auth_token)

message = client.messages.create(
to="+",
from_="+",
body="James says Python is the best!!")

print(message.sid)

if __name__ == "__main__":
    app.run(debug=True)
