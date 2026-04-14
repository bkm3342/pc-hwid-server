from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔥 APNA DISCORD WEBHOOK YAHAN DAAL
WEBHOOK_URL = "PUT_YOUR_NEW_WEBHOOK_HERE"


@app.route("/")
def home():
    return "BKM SERVER RUNNING 🔥"


@app.route("/log", methods=["POST"])
def log():
    try:
        # ✅ GET DATA
        data = request.get_json(force=True)
        print("RECEIVED DATA:", data)

        if not data:
            return jsonify({"error": "No data"}), 400

        # ✅ SIMPLE MESSAGE (NO EMBED)
        message = "🔥 BKM PC DETAILS\n\n"

        for key, value in data.items():
            message += f"{key.upper()}: {value}\n"

        # 🚀 SEND TO DISCORD
        r = requests.post(WEBHOOK_URL, json={
            "content": message
        })

        print("DISCORD STATUS:", r.status_code)
        print("DISCORD RESPONSE:", r.text)

        return jsonify({"status": "ok"})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 🔥 TEST ROUTE (VERY IMPORTANT)
@app.route("/test")
def test():
    r = requests.post(WEBHOOK_URL, json={
        "content": "🔥 BKM TEST SUCCESS"
    })
    return f"Test Sent → {r.status_code}"


# 🔥 HOSTING
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
