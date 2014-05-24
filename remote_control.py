# Run both motors for a while then stops
import smbus
import time
# for RPI version 1, use "bus = smbus.SMBus(0)"
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

def writeNumber(value):
    try:
        bus.write_byte(address, value)
    except IOError:
        return False
    return True

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

        number = 2 if char == 'k' else 0
        if not writeNumber(number):
            print 'cannot write number'
            continue
        else:
            print 'moving'
            time.sleep(1)
            writeNumber(1)  # stop
