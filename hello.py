#!/usr/bin/python

from flask import Flask
app=Flask(__name__)
@app.route("/")

def greeting():
  return "Afternoon, Jordan. Today is 0224 Wed, now is 2:20pm"

app.run(host='0.0.0.0')
