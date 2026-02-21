from flask import Flask, render_template
import json
import os

app = Flask(__name__)

SLOT_FILE = os.path.join(os.path.dirname(__file__), "..", "parking_slots.json")


def load_slots():
    with open(SLOT_FILE, "r") as f:
        return json.load(f)["slots"]


@app.route("/")
def dashboard():

    slots = load_slots()

    total = len(slots)

    free = sum(1 for s in slots if s["status"] == "free")

    occupied = sum(1 for s in slots if s["status"] in ["pending", "occupied"])

    occupancy_rate = int((occupied / total) * 100) if total > 0 else 0

    return render_template(
        "dashboard.html",
        slots=slots,
        total=total,
        free=free,
        occupied=occupied,
        occupancy_rate=occupancy_rate,
    )


if __name__ == "__main__":
    app.run(debug=True)