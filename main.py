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

while True:

    # Receive user input
    digit = input("Enter 0 - 8: ")
    if type(digit) is not int or digit not in range(9):
        continue

    # Send command to Arduino
    writeNumber(digit)

    # Print status
    print "RPI: Hi Arduino, I sent you ", digit
    def base_3_digit_to_char(digit):
        assert digit in [0, 1, 2]
        if digit == 0:
            return 'v'  # moving backwards
        elif digit == 1:
            return '-'  # staying still
        else:
            return '^'  # moving forward
    left_motor_digit = digit / 3
    right_motor_digit = digit % 3
    print 'Left motor: %c | right motor: %c' %  \
            (base_3_digit_to_char(left_motor_digit),  \
            base_3_digit_to_char(right_motor_digit))

    # Sleep one second
    time.sleep(1)
