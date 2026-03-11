from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

# Load artifacts
with open("model/burnout_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("model/features.pkl", "rb") as f:
    FEATURES = pickle.load(f)


def burnout_risk(predicted_grade):
    if predicted_grade >= 12:
        return "Low Risk"
    elif predicted_grade >= 8:
        return "Moderate Risk"
    else:
        return "High Risk"


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/assessment")
def assessment():
    return render_template("form.html")


@app.route("/predict", methods=["POST"])
def predict():
    input_data = []

    for feature in FEATURES:
        value = float(request.form[feature])
        input_data.append(value)

    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)

    predicted_g3 = model.predict(input_scaled)[0]
    risk = burnout_risk(predicted_g3)

    return render_template(
        "result.html",
        risk=risk,
        predicted=round(predicted_g3, 2)
    )


if __name__ == "__main__":
    app.run(debug=True)
