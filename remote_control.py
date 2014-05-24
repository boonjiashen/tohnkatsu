# Run both motors for a while then stops
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

if __name__ == "__main__":

#    0: both motors reverse
#    1: both motors stop
#    2: both motors forward
    while True:
        char = raw_input("Input 'j' to reverse, 'k' for forward: ");
        if char not in ['j', 'k']:
            continue

        if char == 'k':
            writeNumber(2)  # move forward
            print 'Moving forward'
            time.sleep(1)
            writeNumber(1)  # stop
        else:
            writeNumber(0)  # move forward
            print 'Reversing'
            time.sleep(1)
            writeNumber(1)  # stop
