import re

from flask import Flask, request
from twilio.twiml import Response

app = Flask(__name__)


@app.route('/', methods=['POST'])
def sms_reply():
    # Retrieve the body of the text message.
    message_body = request.form['Body']
    print message_body

    # Create a TwiML response object to respond to the text message.
    resp = Response()
    message_response = 'Message received! Manipulating memory now.'
    error_message = ('Please enter a 4 digit hex address and a 2 digit '
                     'hex value separated by a space. '
                     'For example: "066D FF"')

    # Create a list of all words in the message body.
    message_list = message_body.split(' ')

    # Create a regex for matching hex Strings.
    hex_pattern = re.compile('^[0-9a-fA-F]+$')

    # Check to see if the message is in the right format for Game Genie codes.
    if len(message_body) == 6 or len(message_body) == 8:
        # FCEUX will determine if the code is invalid by default.
        with open('cheat.txt', 'w') as f:
            f.write(message_body)
    # Make sure the message is in the right format.
    elif not len(message_list) == 2:
        message_response = error_message
    else:
        # The first word should be the hex address.
        address = message_list[0]

        # The second word should be the hex value to write to the address.
        value = message_list[1]

        # Check to see if the address and value are valid hexadecimal numbers.
        if hex_pattern.match(address) and hex_pattern.match(value):
            # Write the address and value to their respective text files.
            with open('address.txt', 'w') as f:
                f.write(address)

            with open('value.txt', 'w') as f:
                f.write(value)
        else:
            message_response = error_message

    resp.message(message_response)
    return str(resp)

if __name__ == '__main__':
    app.run(host='0.0.0.0')