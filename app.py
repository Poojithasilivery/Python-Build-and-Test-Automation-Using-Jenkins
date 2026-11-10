
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

TOTAL_SLOTS = 5
PARKING_RATE = 20
parked_vehicles = {}


def park_vehicle(vehicle_number):
    if vehicle_number in parked_vehicles:
        return "Vehicle already parked"

    if len(parked_vehicles) >= TOTAL_SLOTS:
        return "Parking Full"

    occupied = parked_vehicles.values()
    slot = next(s for s in range(1, TOTAL_SLOTS + 1) if s not in occupied)

    parked_vehicles[vehicle_number] = slot
    return "Vehicle Parked Successfully"


def remove_vehicle(vehicle_number, hours):
    if vehicle_number not in parked_vehicles:
        return "Vehicle Not Found"

    if hours <= 0:
        raise ValueError("Hours must be greater than zero")

    charge = hours * PARKING_RATE
    del parked_vehicles[vehicle_number]
    return charge


def available_slots():
    return TOTAL_SLOTS - len(parked_vehicles)


@app.route("/")
def home():
    return render_template(
        "index.html",
        total_slots=TOTAL_SLOTS,
        available=available_slots(),
        occupied=len(parked_vehicles),
        vehicles=parked_vehicles,
        message=None
    )


@app.route("/park", methods=["POST"])
def park():
    vehicle_number = request.form.get("vehicle_number", "").upper().strip()

    if not vehicle_number:
        message = "Please enter a vehicle number"
    else:
        message = park_vehicle(vehicle_number)

    return render_template(
        "index.html",
        total_slots=TOTAL_SLOTS,
        available=available_slots(),
        occupied=len(parked_vehicles),
        vehicles=parked_vehicles,
        message=message
    )


@app.route("/remove", methods=["POST"])
def remove():
    vehicle_number = request.form.get("vehicle_number", "").upper().strip()

    try:
        hours = int(request.form.get("hours", "0"))
        result = remove_vehicle(vehicle_number, hours)

        if isinstance(result, int):
            message = f"Vehicle removed successfully! Parking Charge: Rs. {result}"
        else:
            message = result

    except ValueError:
        message = "Please enter valid parking hours greater than zero"

    return render_template(
        "index.html",
        total_slots=TOTAL_SLOTS,
        available=available_slots(),
        occupied=len(parked_vehicles),
        vehicles=parked_vehicles,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
