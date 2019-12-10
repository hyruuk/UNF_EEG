import serial
from psychopy import core, visual
from random import choice
import egi.simple as egi


# Init trigger communication with EGI
ms_localtime = egi.ms_localtime # gives local time in ms
ns = egi.Netstation()
ns.connect('10.10.10.122', 55513)
time.sleep(1)
print('Connected.')

def sendTrigger(name):
#    name=int(name)
    print(name, type(name))
    ns.sync()
    ns.send_event(str(name))

#    ser = serial.Serial('COM1', 19200, timeout=1) 
#    ser.write(bytes([name]))
#    ser.close()
    return
    

# Set serial port and trigger values
#ser = serial.Serial('COM1', 19200, timeout=1)
whiteCode = 1
blackCode = 0

# Set windows experiment
win = visual.Window(monitor="testMonitor", fullscr=False, color='black')

# Experiment

while True:
    
    #Randomly change to white & send trigger 
    win.setColor('white')
    win.flip()
    win.callOnFlip(sendTrigger, whiteCode)
    
    core.wait(choice([2]))
    
    #Randomly change back to black & send trigger
    win.setColor('black')

    win.flip()
    win.callOnFlip(sendTrigger, blackCode)
    
    core.wait(choice([2]))