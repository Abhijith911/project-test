import json

SLOT_FILE = "parking_slots.json"


def load_slots():
    with open(SLOT_FILE, "r") as f:
        return json.load(f)


def save_slots(data):
    with open(SLOT_FILE, "w") as f:
        json.dump(data, f, indent=4)


def allocate_slot(vehicle_number):
    data = load_slots()

    for slot in data["slots"]:
        if slot["status"] == "free" and slot["type"] == "normal":
            slot["status"] = "pending"
            slot["plate"] = vehicle_number
            slot["ir_confirmed"] = False

            save_slots(data)

            print(f"[ALLOCATED] Vehicle {vehicle_number} → Slot {slot['slot_id']}")
            return slot["slot_id"]

    print(f"[FULL] No free slot for vehicle {vehicle_number}")
    return None


def free_slot(vehicle_number):
    data = load_slots()

    for slot in data["slots"]:
        if slot["plate"] == vehicle_number:
            slot["status"] = "free"
            slot["plate"] = None
            slot["ir_confirmed"] = False

            save_slots(data)

            print(f"[FREED] Vehicle {vehicle_number} → Slot {slot['slot_id']}")
            return slot["slot_id"]

    print(f"[WARNING] No slot found for vehicle {vehicle_number}")
    return None