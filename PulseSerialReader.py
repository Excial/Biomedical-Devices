'''CODE EXPLANATION:
This code is just for reading a pulse sensor attached to the arduino
Use the code in the Arduino to read sensor values.



'''




from serial import Serial
import time as t
from datetime import date,datetime
import clock
import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter import Tk


BT_Port = '/dev/cu.HC-06-SerialPort'
file_deposit = '/Users/nicolelau/Documents/OpenSignals (r)evolution/files/'

state = 0

def read_arduino(file_deposit):

    ser = Serial('{}'.format(BT_Port),9600)
    i = 0
    lst_BPM = []
    lst_time = []
    counter = int(input('Length of video:')) 

    #By default, this should retrieve the length of video instead.
    
    today = date.today()
    today = str(today)
    today = ',({})'.format(today)

    now = datetime.now()
    time_current =now.strftime("%H%M")
    time_current = ',({})'.format(time_current)

    f = open(file_deposit + 'Pulse data' + today + time_current + '.txt', 'w+')
    filename = file_deposit + 'Pulse data' + today + time_current + '.txt'

    start_time = t.time()
    
    while i < counter:

        BPM = str(ser.readline() ,  'utf8') # Reads data off the serial monitor in the arduino IDE.
        time = (t.time() - start_time)*1000 # Gives time in miliseconds.

        if time%500 == 0:   # Saves a BPM every 0.5 seconds
            lst_BPM.append(BPM)
            print(BPM)
            lst_time.append(round(time,3))
            print(round(time,3))

        i += 1

    write_to_file(lst_time,lst_BPM,filename)
    write_data(lst_time,lst_BPM)

def write_to_file(lst_time,lst_BPM,filename):
    f = open(filename, 'a')
    for i in range(len(lst_time)-1):
        f.write(str(lst_time[i]) + '\n' + lst_BPM[i] + '\n')

def read_data(): # This is for saving the data in a txt to the file directory.
    lst_time = []
    lst_BPM = []
    Tk().withdraw()
    filename_BPM = askopenfilename()
    f = open(filename_BPM,'r')
    i = 0
    for line in f.readlines:
        if i%2 == 0:
            lst_time.append(line)
        else:
            lst_BPM.append(line)

    write_data(lst_time,lst_BPM)
        

def write_data(lst_time, lst_BPM):

    lst_data = []

    for element in lst_BPM:
        clean = element[:-2]
        lst_data.append(clean)
    
    df_master = pd.DataFrame({'Time interval:':lst_time, 'BPM:': lst_data})
    print(df_master)

read_arduino(file_deposit)

if state == 1:
    read_data()
else:
    pass
