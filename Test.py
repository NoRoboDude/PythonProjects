from dronekit import connect, VehicleMode, LocationGlobalRelative

vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
vehicle.armed = True
vehicle.mode = VehicleMode("GUIDED")
vehicle.simple_takeoff(alt=10)
vehicle.wait_for_alt(10, epsilon=0.1 , rel=True, timeout=None)
a_location = LocationGlobalRelative(-35.367114, 149.196022, 0)
vehicle.simple_goto(a_location)