parking_slots = 5
parked_vehicles = {}


def park_vehicle(vehicle_number):
    if vehicle_number in parked_vehicles:
        return "Vehicle already parked"

    if len(parked_vehicles) >= parking_slots:
        return "Parking Full"

    parked_vehicles[vehicle_number] = 0
    return "Vehicle Parked Successfully"


def remove_vehicle(vehicle_number, hours):
    if vehicle_number not in parked_vehicles:
        return "Vehicle Not Found"

    if hours <= 0:
        raise ValueError("Hours must be greater than zero")

    charge = hours * 20
    del parked_vehicles[vehicle_number]

    return charge


def available_slots():
    return parking_slots - len(parked_vehicles)


def main():
    print("SMART PARKING MANAGEMENT SYSTEM")
    print("--------------------------------")

    print(park_vehicle("TS09AB1234"))
    print(park_vehicle("TS09CD5678"))

    print("Available Slots:", available_slots())

    charge = remove_vehicle("TS09AB1234", 3)

    print("Parking Charge: Rs.", charge)
    print("Available Slots:", available_slots())


if __name__ == "__main__":
    main()
