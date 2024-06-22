import os
from flask import Flask
from flask_restful import Resource, Api
from flask import Flask, jsonify

app = Flask(__name__)

# Route to handle UptimeRobot requests
@app.route('/check', methods=['GET'])
def check():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(debug=True, port=5071)
