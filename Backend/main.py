from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Function to analyze distress level using TextBlob
def get_distress_level(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity

    if polarity < 0:
        distress_level = "High Distress"
    elif 0 <= polarity < 0.5:
        distress_level = "Moderate Distress"
    else:
        distress_level = "Low Distress or Neutral"

    return {"distress_level": distress_level, "polarity": polarity, "subjectivity": subjectivity}

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    result = get_distress_level(text) 
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
