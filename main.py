import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    bus.write_byte(address, value)
    # bus.write_byte_data(address, 0, value)
    return -1

def readNumber():
    number = bus.read_byte(address)
    # number = bus.read_byte_data(address, 1)
    return number

"""
Instructions:
------------------
Press Q/A/Z for left motor to go forward/stop/backwards
Press W/S/X for right motor to go forward/stop/backwards
"""
lmotor_state, rmotor_state = 1, 1
import Getch
getch = Getch._Getch()
print "Enter Q/A/Z/W/S/X to control motors (or ESC to escape):"
while True:

    # Receive user input
    keystroke = getch().upper()
    esc = '\x1b'
    if keystroke == esc:
        digit_to_kill_motors = 4
        writeNumber(digit_to_kill_motors)
        break

    # Parse user input
    if keystroke not in 'QAZWSX': 
        continue
    if 'ZAQ'.find(keystroke) != -1:
        lmotor_state = 'ZAQ'.find(keystroke)
    if 'XSW'.find(keystroke) != -1:
        rmotor_state = 'XSW'.find(keystroke)
    digit = lmotor_state * 3 + rmotor_state

    # Send command to Arduino
    writeNumber(digit)

    def base_3_digit_to_keystroke(digit):
        assert digit in [0, 1, 2]
        if digit == 0:
            return 'v'  # moving backwards
        elif digit == 1:
            return '-'  # staying still
        else:
            return '^'  # moving forward
    # Print status
    print "RPI: read keystroke %c, send Arduino %i " % (keystroke, digit)
    print 'Left motor: %c | right motor: %c' %  \
            (base_3_digit_to_keystroke(lmotor_state),  \
            base_3_digit_to_keystroke(rmotor_state))

    # Sleep one second
    time.sleep(.01)
