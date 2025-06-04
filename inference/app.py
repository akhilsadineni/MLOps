from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("model/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["data"]
    prediction = model.predict(np.array(data).reshape(1, -1)).tolist()
    return jsonify({"prediction": prediction})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)