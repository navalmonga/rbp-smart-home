from flask import Flask, request
import requests
import json
from dotenv import load_dotenv
import os
load_dotenv()

BRIDGE_IP = os.environ.get('BRIDGE_IP')
API_KEY = os.environ.get('API_KEY')

url = 'https://' + BRIDGE_IP + '/api/' + API_KEY
app = Flask(__name__)

@app.route('/')
def index():
  return "hello world\n" + url