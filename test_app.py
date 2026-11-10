
import unittest
import app


class TestParkingSystem(unittest.TestCase):

    def setUp(self):
        app.parked_vehicles.clear()

    def test_park_vehicle(self):
        result = app.park_vehicle("TS09AB1234")
        self.assertEqual(result, "Vehicle Parked Successfully")

    def test_duplicate_vehicle(self):
        app.park_vehicle("TS09AB1234")
        result = app.park_vehicle("TS09AB1234")
        self.assertEqual(result, "Vehicle already parked")

    def test_available_slots(self):
        app.park_vehicle("TS09AB1234")
        self.assertEqual(app.available_slots(), 4)

    def test_remove_vehicle(self):
        app.park_vehicle("TS09AB1234")
        charge = app.remove_vehicle("TS09AB1234", 3)
        self.assertEqual(charge, 60)

    def test_vehicle_not_found(self):
        result = app.remove_vehicle("TS09AB1234", 2)
        self.assertEqual(result, "Vehicle Not Found")

    def test_parking_full(self):
        for i in range(5):
            app.park_vehicle(f"Vehicle{i}")

        result = app.park_vehicle("Vehicle6")
        self.assertEqual(result, "Parking Full")


if __name__ == "__main__":
    unittest.main()
