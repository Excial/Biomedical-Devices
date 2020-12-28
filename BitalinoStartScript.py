''' PRETEXT'''
'''
This script is to run Opensignals and activate the EDA Sensor on the bitalino.
The timing input required on the variable 'Video_time' is the time of the recording in miliseconds.
'''
''' END '''



import time
from bitalino import BITalino

# The macAddress variable on Windows can be "XX:XX:XX:XX:XX:XX" or "COMX"
# while on Mac OS can be "/dev/tty.BITalino-XX-XX-DevB" for devices ending with the last 4 digits of the MAC address or "/dev/tty.BITalino-DevB" for the remaining
macAddress = "/dev/tty.BITalino-60-61-DevB"

# This example will collect data for 5 sec.
Video_time = 20
    
batteryThreshold = 30
acqChannels = [1,2,3,4,5]
samplingRate = 1
nSamples = 100
digitalOutput = [1,1]

# Connect to BITalino
device = BITalino(macAddress)
    
# Start Acquisition
device.start(samplingRate, acqChannels)

start = time.time()
end = time.time()
while (end - start) < Video_time:
    print(device.read(nSamples))
    end = time.time()
 
# Stop acquisition
device.stop()
    
# Close connection
device.close()