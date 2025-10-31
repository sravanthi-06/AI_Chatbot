from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

responses = {
    "hello": ["Hi there!", "Hello!", "Hey! How can I help you?"],
    "how are you": ["I'm just a bot, but I'm doing great!", "Feeling chatty today!"],
    "bye": ["Goodbye!", "See you soon!"],
    "default": ["Sorry, I didn't understand that.", "Can you rephrase?"]
}

def get_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = get_response(user_input)
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
