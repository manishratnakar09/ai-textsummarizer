import os
from flask import Flask, request, jsonify, send_from_directory
from image_utils import validate, prepare, MAX_MB
from model_handler import predict

FRONTEND = os.path.join(os.path.dirname(__file__), "..", "frontend")
app = Flask(__name__, static_folder=FRONTEND, static_url_path="")
app.config["MAX_CONTENT_LENGTH"] = (MAX_MB + 1) * 1024 * 1024
LOW_CONF = 50  # % threshold for warning


@app.route("/")
def index():
    return send_from_directory(FRONTEND, "index.html")


@app.route("/predict", methods=["POST"])
def predict_route():
    file = request.files.get("image")
    if file is None:
        return jsonify(error="Koi image nahi mili."), 400
    try:
        data = validate(file)          # processed in memory -> nothing stored on disk
        img = prepare(data)
        top = max(3, min(5, int(request.form.get("top", 5))))
        results = predict(img, top)
    except ValueError as e:
        return jsonify(error=str(e)), 400
    warning = None
    if results[0]["confidence"] < LOW_CONF:
        warning = "Low confidence: model ko image ka object clearly samajh nahi aaya."
    return jsonify(predictions=results, warning=warning)


@app.errorhandler(413)
def too_large(_):
    return jsonify(error=f"File too large. Max size {MAX_MB} MB hai."), 413


if __name__ == "__main__":
    app.run(debug=True)
