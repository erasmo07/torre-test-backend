import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/user/<username>')
def get_person(username):
    response_proxy = requests.get(f'https://bio.torre.co/api/bios/{username}')
    return jsonify(response_proxy.json()) 
