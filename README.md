# NESMS
A FCEUX NES emulator extension that receives SMS messages while you are playing a game, and allows the senders to manipulate the memory in real time. 

Text your Twilio number a memory address and a hex value to alter whatever game you are playing in real time. This allows you to enter cheat codes to help the player out, or even to corrupt the game's memory.

## How to use

You will need to install the Twilio and Flask python modules and run our Flask app.

```
pip install twilio
pip install flask
python app.py
```

You need to purchase and configure a Twilio phone number

![](https://raw.github.com/sagnew/NESMS/master/images/buy-a-twilio-number.gif)

You also need to expose your environment to the internet. This can be done with [Ngrok](https://ngrok.com). Run Ngrok to listen on port 5000 and you will get a generated url that you can add to your Twilio dashboard.

![](https://raw.github.com/sagnew/NESMS/master/images/ngrok.png)

![](https://raw.github.com/sagnew/NESMS/master/images/twilio_dashboard.png)

Now you need to run `nesms.lua` in FCEUX.

![](https://raw.github.com/sagnew/NESMS/master/images/HelloWorld.gif)

And watch as we can shoot a text message(in the form of a 4 digit hex address and a 2 digit hex value separated by a space such ass "0600 20") to make changes to our NES games in real time.

![](https://raw.github.com/sagnew/NESMS/master/images/kill_mario.gif)
