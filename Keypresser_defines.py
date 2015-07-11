from ctypes import *

user32 = windll.user32

# Keybaord input types (Input)
INPUT_MOUSE     = 0x0
INPUT_KEYBOARD  = 0x1
INPUT_HARDWARE  = 0x2

# Keyboard events (Input_I)
KEYEVENTF_EXTENDEDKEY = 0x1
KEYEVENTF_KEYUP       = 0x2
KEYEVENTF_SCANCODE    = 0x8
KEYEVENTF_UNICODE     = 0x4

class KeyBdInput(Structure):
    _fields_ = [
            ("wVk", c_ushort),
            ("wScan", c_ushort),
            ("dwFlags", c_ulong),
            ("time", c_ulong),
            ("dwExtraInfo", POINTER(c_ulong)) ]

class HardwareInput(Structure):
    _fields_ = [
            ("uMsg", c_ulong),
            ("wParamL", c_short),
            ("wParamH", c_ushort) ]

class MouseInput(Structure):
    _fields_ = [
            ("dx", c_long),
            ("dy", c_long),
            ("mouseData", c_ulong),
            ("dwFlags", c_ulong),
            ("time", c_ulong),
            ("dwExtraInfo", POINTER(c_ulong)) ]

class Input_I(Union):
    _fields_ = [
            ("ki", KeyBdInput),
            ("mi", MouseInput),
            ("hi", HardwareInput) ]

class Input(Structure):
    _fields_ = [
            ("type", c_ulong),
            ("ii", Input_I) ]
