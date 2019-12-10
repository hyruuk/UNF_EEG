import egi.simple as egi
import time

ms_localtime = egi.ms_localtime # gives local time in ms
ns = egi.Netstation()
ns.connect('10.10.10.122', 55513)
print('blabla')
time.sleep(1)
print('Connected.')


# # This sends some initialization info to NetStation for recording events.
ns.BeginSession()
# # This synchronizes the clocks of the stim computer and the NetStation computer.

while True:
    ns.sync()
    ns.send_event('evt1')
    time.sleep(1)
