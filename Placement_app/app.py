from flask import Flask, render_template, request
from model import predict_student

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = [
        int(request.form["attendance"]),
        int(request.form["avg_marks"]),
        int(request.form["python"]),
        int(request.form["sql_skill"]),
        int(request.form["aptitude"]),
        int(request.form["communication"])
    ]

    result = predict_student(data)

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)
