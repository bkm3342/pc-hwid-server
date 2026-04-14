from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔥 APNA DISCORD WEBHOOK YAHAN DAAL
WEBHOOK_URL = "https://discord.com/api/webhooks/1486628249042948177/Sd7goOSOTneyDNHerFR5_ZPOHfCbk6rtcz0ei3Hgcd-PxzNCskU-aHFk13AY20GgiOzm"


@app.route("/")
def home():
    return "BKM SERVER RUNNING 🔥"


@app.route("/log", methods=["POST"])
def log():
    try:
        # ✅ FORCE JSON (fix issue)
        data = request.get_json(force=True)

        print("📥 RECEIVED DATA:", data)

        if not data:
            return jsonify({"error": "No data received"}), 400

        # 🔥 EMBED DESIGN
        embed = {
            "title": "💻 NEW PC FULL DETAILS",
            "color": 65280,
            "fields": [
                {"name": "🆔 HWID (UUID)", "value": str(data.get("uuid", "N/A")), "inline": False},
                {"name": "⚙️ CPU ID", "value": str(data.get("cpu", "N/A")), "inline": False},
                {"name": "📟 BIOS Serial", "value": str(data.get("bios", "N/A")), "inline": False},
                {"name": "🧩 Motherboard", "value": str(data.get("board", "N/A")), "inline": False},
                {"name": "🧠 RAM", "value": str(data.get("ram", "N/A")), "inline": False},
                {"name": "🎮 GPU", "value": str(data.get("gpu", "N/A")), "inline": False},
                {"name": "🌐 IP Address", "value": str(data.get("ip", "N/A")), "inline": False},
                {"name": "💻 PC Name", "value": str(data.get("pc", "N/A")), "inline": True},
                {"name": "👤 User", "value": str(data.get("user", "N/A")), "inline": True},
                {"name": "🖥️ OS", "value": str(data.get("os", "N/A")), "inline": False}
            ]
        }

        # 🚀 SEND TO DISCORD
        r = requests.post(WEBHOOK_URL, json={"embeds": [embed]})

        print("📤 DISCORD RESPONSE:", r.status_code, r.text)

        return jsonify({"status": "success"})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"error": str(e)}), 500


# 🔥 HOSTING COMPATIBLE RUN
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
