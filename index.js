"use strict";

const express = require('express');
const bodyParser = require('body-parser');
const twilio = require('twilio');
const fs = require('fs');

const app = express();

app.use(bodyParser.urlencoded({extended: false}));

app.post('/sms', (req, res) => {
  let messageBody = req.body.Body;
  let twiml = new twilio.TwimlResponse();
  let messageList = messageBody.split(' ');
  let address = messageList[0];
  let value = messageList[1];
  let hexPattern = /^[0-9a-fA-F]+$/;

  console.log(messageBody);
  if(hexPattern.test(address) && hexPattern.test(value)) {
    twiml.message('Thanks for joining my demo!');
    fs.writeFileSync('address.txt', address, 'utf8');
    fs.writeFileSync('value.txt', value, 'utf8');
  } else {
    twiml.message('Please text a valid hex address and value');
  }

  res.send(twiml.toString());
});

app.listen(3000, console.log('Listening on port 3000'));
