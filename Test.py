from dronekit import connect, VehicleMode, LocationGlobalRelative
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
b_location = vehicle.home_location
print("Home Location:",  b_location)
c_location = vehicle.location.global_relative_frame
print("Current Location", c_location)
vehicle.armed = True
vehicle.mode = VehicleMode("GUIDED")
b_location = vehicle.home_location
vehicle.simple_takeoff(alt=10)
vehicle.wait_for_alt(10, epsilon=0.1 , rel=True, timeout=None)
a_location = LocationGlobalRelative(-35.363114, 149.166022, 10)
vehicle.simple_goto(a_location)
print("WP location:", a_location)
if c_location == a_location:
    vehicle.simple_goto(b_location)