from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# API gốc (x10.mx – hay bị chặn nếu gọi trực tiếp)
OLD_API_URL = "http://abcdxyz310107.x10.mx/apifl.php"

@app.route("/")
def home():
    return "API proxy is running"

@app.route("/apifl", methods=["GET"])
def apifl():
    fl1 = request.args.get("fl1")
    if not fl1:
        return jsonify({
            "status": "error",
            "message": "missing fl1"
        }), 400

    try:
        # Gọi API cũ từ server Render (KHÔNG bị chặn)
        r = requests.get(
            OLD_API_URL,
            params={"fl1": fl1},
            headers={
                "User-Agent": "Mozilla/5.0",
                "Accept": "*/*"
            },
            timeout=20
        )

        # Trả thẳng kết quả API cũ
        return jsonify({
            "status": "success",
            "data": r.text.strip()
        }), 200

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": "failed to call old api"
        }), 500
