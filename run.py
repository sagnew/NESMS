from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        resp = twilio.twiml.Response()
        resp.message("yo")

        msg = request.form['Body'].lower().split()
        print request.form['From']
        print msg
        address, value = "None", "None"

        if "cheat" in msg[0] and len(msg) is 2:   #cheat address value
            command = msg[1]    
            #map command to address and value here
        elif "hack" in msg[0] and len(msg) is 3:
            address = msg[1]
            value = msg[2]

        with open("address.txt", "w") as f:
            f.write(address + "\n")
        
        with open("value.txt", "w") as f:
            f.write(value + "\n")

        with open("input.txt", "w") as f:
            f.write(request.form['From'] + ":" + request.form['Body']+"\n")

        return str(resp)
    else:
        return 'hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
