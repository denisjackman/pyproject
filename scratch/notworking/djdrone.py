'''
    This is a placeholder for drone programming

    reference:
        https://www.thedronegirl.com/2021/04/12/how-to-program-a-drone-using-python/
        https://dronekit-python.readthedocs.io/en/latest/
        https://dojofordrones.com/drone-programming/
        https://github.com/dronekit/dronekit-python

    Installation Notes:
        pip install dronekit
        pip install dronekit-sitl
'''
from dronekit import connect

DRONE_CONNECTION_STRING = '127.0.0.1:5760'

# Import DroneKit-Python

# Connect to the Vehicle.
print("Start simulator (SITL)")
print(f"Connecting to vehicle on: {DRONE_CONNECTION_STRING}")
vehicle = connect(DRONE_CONNECTION_STRING, wait_ready=True)

# Get some vehicle attributes (state)
print("Get some vehicle attribute values:")
print(f" GPS: {vehicle.gps_0}")
print(f" Battery: {vehicle.battery}")
print(f" Last Heartbeat: {vehicle.last_heartbeat}")
print(f" Is Armable?: {vehicle.is_armable}")
print(f" System status: {vehicle.system_status.state}")
print(f" Mode: {vehicle.mode.name}")

# Close vehicle object before exiting script
vehicle.close()

print("Completed")