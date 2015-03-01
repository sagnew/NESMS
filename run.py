from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        reply = 'command received'
        resp = twilio.twiml.Response()
        command_list = {
            'magicsword': ['0657', '03'],
            'invincible': ['04f0', '04'],
            'infiniterupees': ['066d', 'ff'],
            'infinitekeys': ['066E', '09'],
            'boomerang': ['0674', '01'],
            'infinitehitpoints': ['066f', 'FF'],
            'changeTrack1' : ['0600', '80'],
            'changeTrack2' : ['0600', '40'],
            'changeTrack3' : ['0600', '20'],
            'changeTrack4' : ['0600', '10'],
            'changeTrack5' : ['0600', '01'],
        }

        msg = request.form['Body'].lower().split()
        print request.form['From']
        print msg
        address, value = "None", "None"
        if 'nesms' in msg[0]:
            reply = ("Welcome to NESMS!\n"
                       "To start rom hacking, activate cheats with\n" 
                       "cheat <command>\n"
                       "cheats list: magicSword, invincible, infiniteRupees"
                       ", boomerang, infiniteKeys, infiniteHitPoints. "
                       "To input values into hex memory addresses, use\n"
                       "hack <address> <value>\n"
            )
        elif 'cheat' in msg[0] and len(msg) is 2:   #cheat address value
            cheat_address = command_list.get(msg[1])
            cheat_value = command_list.get(msg[1])
            if not cheat_address:
                reply = ("Sorry dude. Thats not a valid cheat."
                          "Check out our cheat by sending nesms or"
                          "use the hack command to input your own values!"
                )
            else:
                address = cheat_address[0]
                value = cheat_value[1]
            
        elif 'hack' in msg[0] and len(msg) is 3:
            address = msg[1]
            value = msg[2]

        with open("address.txt", "w") as f:
            f.write(address + "\n")
        
        with open("value.txt", "w") as f:
            f.write(value + "\n")

        with open("input.txt", "w") as f:
            f.write(request.form['From'] + ":" + request.form['Body']+"\n")

        resp.message(reply)
        return str(resp)
    else:
        return 'hello'

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
