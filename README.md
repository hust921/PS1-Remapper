#PS1-Remapper
Using the PSXLibrary to read information from a Playstation 1 controller. Information is receiver via pyserial and redirected to keyboard inputs, using ctypes and the windows api.
Using this code, you will be able to play games using a PS1 controller.

Demo: https://www.youtube.com/watch?v=pn_Li9lcNQs
##Version 1.0
Stable, working version.

##Documentation:
Serial communication is using pyserial to read from the virtual COM port. Ctypes is used to import SendInput (https://msdn.microsoft.com/en-us/library/windows/desktop/ms646310(v=vs.85).aspx) and simulate keypresses. Mappings can be changed in Remapper_defines.py. Virtual key-codes: (https://msdn.microsoft.com/en-us/library/windows/desktop/dd375731(v=vs.85).aspx)

A WORD (int16) is sent over serial connection. And bitmasks are used to determine keypresses. These are also in Remapper_defines.py.

##Dependencies:
All available via pip.
- PSXLibrary (http://playground.arduino.cc/Main/PSXLibrary)
- pyserial (http://pyserial.sourceforge.net/)
- ctypes <3 (http://starship.python.net/crew/theller/ctypes/)
- PSXLibrary (http://playground.arduino.cc/Main/PSXLibrary)

##Installation instructions:
#####Step 1: Install dependencies.
#####Step 2: Wire the board.
WARNING! Before connecting your controller: Make sure to "clear" the board for any previous code, to make sure that power isen't accedently directed wrongly into the controller.

*Note you might have more/different depending on vibration, etc. Ignore these.
- 2 : brown (data) 
- 4 : orange (command) 
- 6 : yellow (attention) 
- 8 : blue (clock) 
- GND : black 
- 3.3V : red

#####Step 3: Deploy Ps1_Controller.ino
#####Step 4: Optional, configure mappings in Remapper_defines.py
#####Step 5: Run Remapper.py
######Hint: You can find your COM port using the arduino software.

##Credit:
- Author Morten Lund <92morten@gmail.com>
- PSXLibrary
    - The Arduino Project (http://playground.arduino.cc/Main/PSXLibrary)
    - Andrew J McCubbin (http://www.gamesx.com/controldata/psxcont/psxcont.htm)

##Disclaimer:
See LICENSE(MIT)

This code is totally free for use and modification. Note that I take no responsibility for damage done to your Arduino, other microcontroller, playstation- or other controller. This a purely experimental and for educational purposes.
