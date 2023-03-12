from dronekit import connect, VehicleMode
from pymavlink import mavutil
def goto_position_target_local_ned(north, east, down):
    """
    Send SET_POSITION_TARGET_LOCAL_NED command to request the vehicle fly to a specified
    location in the North, East, Down frame.
    """
    msg = vehicle.message_factory.set_position_target_local_ned_encode(
        0,       # time_boot_ms (not used)
        0, 0,    # target system, target component
        mavutil.mavlink.MAV_FRAME_LOCAL_NED, # frame
        0b0000111111111000, # type_mask (only positions enabled)
        north, east, down,
        0, 0, 0, # x, y, z velocity in m/s  (not used)
        0, 0, 0, # x, y, z acceleration (not supported yet, ignored in GCS_Mavlink)
        0, 0)    # yaw, yaw_rate (not supported yet, ignored in GCS_Mavlink)
    # send command to vehicle
    vehicle.send_mavlink(msg)
vehicle = connect('tcp:127.0.0.1:5762', wait_ready=True)
cmds = vehicle.commands
cmds.download()
cmds.wait_ready()
vehicle.mode = VehicleMode("GUIDED")
vehicle.armed = True
vehicle.arm(wait=True, timeout=10)
vehicle.simple_takeoff(alt=10)
vehicle.wait_for_alt(10, epsilon=0.1 , rel=True, timeout=None)
metersNorth = vehicle.location.local_frame.north # used for the y position
metersEast = vehicle.location.local_frame.east # used for the x position
altitude = vehicle.location.local_frame.down # used for the z position
print("y:", metersNorth)
print("x:", metersEast)
print("z:", altitude)
goto_position_target_local_ned(metersNorth + 3, metersEast + 2,10)
