from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OLD_API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

@app.route("/")
def home():
    return "API proxy is running"

@app.route("/apifl", methods=["GET"])
def apifl():
    username = request.args.get("username")
    if not username:
        return jsonify({
            "status": "error",
            "message": "missing username"
        }), 400

    try:
        # GHÉP ĐÚNG FORMAT API CŨ
        params = {
            "fl1": f"username={username}"
        }

        r = requests.get(
            OLD_API_URL,
            params=params,
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*"
            },
            timeout=20
        )

        return jsonify({
            "status": "success",
            "data": r.text.strip()
        }), 200

    except Exception:
        return jsonify({
            "status": "error",
            "message": "failed to call old api"
        }), 500
