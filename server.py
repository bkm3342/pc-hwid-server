from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

WEBHOOK_URL = "YOUR_WEBHOOK_HERE"


@app.route("/")
def home():
    return "BKM SERVER RUNNING 🔥"


@app.route("/log", methods=["POST"])
def log():
    try:
        data = request.get_json(force=True)

        print("DATA:", data)

        if not data:
            return jsonify({"error": "No data"}), 400

        embed = {
            "title": "BKM PC DETAILS",
            "color": 65280,
            "fields": [
                {"name": "HWID", "value": str(data.get("uuid")), "inline": False},
                {"name": "CPU", "value": str(data.get("cpu")), "inline": False},
                {"name": "User", "value": str(data.get("user")), "inline": True},
                {"name": "PC", "value": str(data.get("pc")), "inline": True},
                {"name": "IP", "value": str(data.get("ip")), "inline": False},
                {"name": "OS", "value": str(data.get("os")), "inline": False}
            ]
        }

        try:
            r = requests.post(WEBHOOK_URL, json={"embeds": [embed]})
            print("DISCORD:", r.status_code, r.text)
        except Exception as e:
            print("Webhook Error:", e)

        return jsonify({"status": "ok"})

    except Exception as e:
        print("SERVER ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
