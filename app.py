from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "API is running"

@app.route("/apifl")
def apifl():
    fl1 = request.args.get("fl1")
    if not fl1:
        return jsonify({"error": "missing fl1"}), 400

    return jsonify({
        "status": "success",
        "data": fl1
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
