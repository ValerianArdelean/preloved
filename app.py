from flask import Flask, jsonify

app = Flask(name)

@app.route('/')
def index():
    return jsonify({'response': 'Sarah preloved website'})
