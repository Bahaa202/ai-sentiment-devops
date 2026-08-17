"""
app.py
Flask API بسيطة لتصنيف المشاعر
Endpoints:
  - POST /predict  -> يرجع positive/negative
  - GET  /health    -> health check
  - GET  /metrics   -> Prometheus metrics
"""

from flask import Flask, request, jsonify
import joblib
from prometheus_client import Counter, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time

app = Flask(__name__)

# تحميل الموديل مرة واحدة عند تشغيل السيرفر
model = joblib.load("model.pkl")

# ----------------------------
# Prometheus metrics
# ----------------------------
REQUEST_COUNT = Counter(
    "predict_requests_total", "Total number of prediction requests", ["result"]
)
REQUEST_LATENCY = Histogram(
    "predict_request_latency_seconds", "Latency of prediction requests"
)


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"}), 200


@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(silent=True)
    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' field in JSON body"}), 400

    text = data["text"]

    start_time = time.time()
    prediction = model.predict([text])[0]
    duration = time.time() - start_time

    REQUEST_COUNT.labels(result=prediction).inc()
    REQUEST_LATENCY.observe(duration)

    return jsonify({"text": text, "sentiment": prediction}), 200


@app.route("/metrics", methods=["GET"])
def metrics():
    return generate_latest(), 200, {"Content-Type": CONTENT_TYPE_LATEST}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
