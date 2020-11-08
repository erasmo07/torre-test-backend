import requests
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
    return jsonify({'success': True})


@app.route('/user/<username>')
def get_person(username):
    response_proxy = requests.get(f'https://bio.torre.co/api/bios/{username}')
    return jsonify(response_proxy.json()) 


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)