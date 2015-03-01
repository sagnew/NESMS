from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    resp = twilio.twiml.Response()
    resp.message("yo homie yo")
    print request.form['Body']
    print request.form['From']
    return str(resp)

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
