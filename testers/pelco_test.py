# test script for using pelco-d in python
# currently not useful

def pelcod(camera, camera_options, pan_speed, tilt_speed):

    command1 = 0

    command2 = 0
    command2 += camera_options.tilt_down*16
    command2 += camera_options.tilt_up*8
    command2 += camera_options.pan_left*4
    command2 += camera_options.pan_right*2

    checksum = (camera + command1 + command2 + pan_speed + tilt_speed) % 256

    return [camera, command1, command2, pan_speed, tilt_speed, checksum]
