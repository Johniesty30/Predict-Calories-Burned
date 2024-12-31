from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

# Route untuk halaman contact
@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Get input data from form
        input_data = [
            float(request.form.get("Age")),
            float(request.form.get("Gender")),
            float(request.form.get("Weight")),
            float(request.form.get("Height")),
            float(request.form.get("Max_BPM")),
            float(request.form.get("Avg_BPM")),
            float(request.form.get("Resting_BPM")),
            float(request.form.get("Session_Duration")),
            float(request.form.get("Workout_Type")),
            float(request.form.get("Fat_Percentage")),
            float(request.form.get("Water_Intake")),
            float(request.form.get("Workout_Frequency")),
            float(request.form.get("Experience_Level")),
            float(request.form.get("BMI"))
        ]

        # Reshape data and make prediction
        prediction = model.predict([input_data])
        result = f"Estimated Calories Burned: {prediction[0]:.2f}"

        return render_template("predict.html", result=result)

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True)
