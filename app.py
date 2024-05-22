from flask import Flask, request, jsonify, send_from_directory
import requests

app = Flask(__name__)

RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = requests.post(RASA_URL, json={"message": user_message})
    return jsonify(response.json())

@app.route("/")
def index():
    return send_from_directory('', 'index.html')

if __name__ == "__main__":
    app.run(port=5000)
