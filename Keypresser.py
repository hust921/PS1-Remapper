from Keypresser_defines import *

class keypresser:
    def __init__(self):
        pass

    def keyDown(self, key):
        keyboardInput = Input_I()
        keyboardInput.ki = KeyBdInput(key, 0, 0, 0, None)

        nInput = Input(INPUT_KEYBOARD, keyboardInput)
        user32.SendInput(1, byref(nInput), sizeof(nInput))

    def keyUp(self, key):
        keyboardInput = Input_I()
        keyboardInput.ki = KeyBdInput(key, 0, KEYEVENTF_KEYUP, 0, None)

        nInput = Input(INPUT_KEYBOARD, keyboardInput)
        user32.SendInput(1, byref(nInput), sizeof(nInput))
