import serial
from Remapper_defines import *
import Keypresser

winPress = Keypresser.keypresser()

def isBitSet(src, bit):
    return src & bit == bit

def selectPort():
    print("Select COM port to connect to:")
    for i in range(5):
        print("{0}: for COM{1}".format(i, i+1))

    return int(input("Select port: "))

def main():
    ser = serial.Serial(selectPort())
    running = True

    while running:
        serialInput = int(ser.readline())
        
        for btn in buttons:
            if isBitSet(serialInput, btn.mask):
                winPress.keyDown(btn.winVal)
            else:
                winPress.keyUp(btn.winVal)

    ser.close()

if __name__ == "__main__":
    main()
