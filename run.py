from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    #resp = twilio.twiml.Response()
    #resp.message("yo homie im playing nes")

    print request.form['Body']
    print request.form['From']

    with open("input.txt", "w") as f:
        f.write(request.form['From'] + ":" + request.form['Body']+"\n")
    #return str(resp)
    return 'recieved'

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
