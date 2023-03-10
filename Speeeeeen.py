from dronekit import connect, VehicleMode, time
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
start_time = time.time()
current_time = time.time()-start_time
spin_rate = 360/20
current_angle= (spin_rate * current_time)%360
vehicle.armed = True
vehicle.mode = VehicleMode("GUIDED")
vehicle.simple_takeoff(alt=10)
vehicle.wait_for_alt(10, epsilon=0.1 , rel=True, timeout=None)
vehicle.gimbal.rotate(0, 0, 10)
