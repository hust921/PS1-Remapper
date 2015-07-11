from collections import namedtuple
Button = namedtuple("Button", ["name", "winVal", "mask"])
buttons = [
        Button(name="psxLeft", winVal=0x25, mask=1),     # Arrow Left
        Button(name="psxDown", winVal=0x28, mask=2),     # Arrow Down
        Button(name="psxRight", winVal=0x27, mask=4),    # Arrow Right
        Button(name="psxUp", winVal=0x26, mask=8),       # Arrow Up
        Button(name="psxStrt", winVal=0x58, mask=16),    # X key
        Button(name="psxSlct", winVal=0x5a, mask=128),   # Z key
        Button(name="psxSqu", winVal=0x41, mask=256),    # A key
        Button(name="psxX", winVal=0x53, mask=512),      # S key
        Button(name="psxO", winVal=0x44, mask=1024),      # D key
        Button(name="psxTri", winVal=0x57, mask=2048),    # W key
        Button(name="psxR1", winVal=0x59, mask=4096),     # Y key
        Button(name="psxL1", winVal=0x54, mask=8192),     # T key
        Button(name="psxR2", winVal=0x48, mask=16384),    # H key
        Button(name="psxL2", winVal=0x47, mask=32768) ]   # G key
