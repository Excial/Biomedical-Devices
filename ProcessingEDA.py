from tkinter.filedialog import askopenfilename
from tkinter import Tk
import numpy as np 
import matplotlib.pyplot as plt  
import pandas as pd

if __name__ == "__main__":

    def readlink():

        Tk().withdraw()
        filename_EDA = askopenfilename()
        readcsv(filename_EDA)

    #def readcsv(link_lst): # Both readings need to be generated per second.
    def readcsv(filename_EDA):

        #f1 = open("{}".format(link_lst[1]),"r") # Opens EDA txt file.

        f1 = open("{}".format(filename_EDA),"r")
        input_time = int(input('Lenght of video(s): ')) + 6 # Input video duration
    
        counter = 0 # total counter - 4 is the total duration of the reading in ms
        counter2 = 0.5
        time = 0
        lst_EDA = []
        lst_interval = []

        for line in f1.readlines():
            counter += 1
            if counter < 4: #Skip all the unimportant lines at the top
                pass
            elif counter < input_time: #Adjust counter for number of entries.
                index = line[0] + line[1]
                if line[2] == int:
                    index = index + index[2]
                else:
                    pass
                if int(index) < 10:
                    lst_EDA.append('' + line[10] +line[11] + line[12])
                elif int(index) < 100: 
                    lst_EDA.append('' + line[11] + line[12] + line[13])
                elif int(index) < 1000:
                    lst_EDA.append('' + line[12] + line[13] + line[14])

                lst_interval.append(counter2)
                counter2 += 1

        lst_interval.pop()
        evaluate(lst_EDA,lst_interval)

        
    def evaluate(lst_EDA,lst_interval):
        VCC = 3.3
        bits = 10  # or 6
        lst_EDA_clean = []
        for ADC in lst_EDA:
            ADC = int(ADC)
            EDA = ((ADC/2**bits)*VCC)/0.132
            EDA = round(EDA, 3)
            lst_EDA_clean.append(EDA)
        
        #print(lst_EDA_clean)

        lst_gradients = []
        labels = []
        LED_Alert = []

        for i in range(len(lst_EDA_clean) - 1 ):
            gradient = lst_EDA_clean[i] - lst_EDA_clean[i - 1]
            lst_gradients.append(gradient)
        
        for i in range(len(lst_gradients)):
            if lst_gradients[i] == 0: 
                labels.append('Red')
            if lst_gradients[i] > 0: 
                labels.append('Blue')
            elif lst_gradients[i] < 0:
                labels.append('Yellow')

        df_master = pd.DataFrame({'Time interval:':lst_interval, 'Gradients:': lst_gradients,'Label:': labels})
        pd.set_option('display.max_rows', df_master.shape[0]+1)

        print(df_master)

        graph_gradient(lst_interval, lst_gradients)
        graph_raw(lst_EDA_clean)

    def graph_raw(lst_EDA_clean): # Shows raw EDA graph

        counter = 0
        lst_time = []
        for element in lst_EDA_clean:
            lst_time.append(counter)
            counter += 1

        plt.plot(lst_time, lst_EDA_clean)
        plt.xlabel('Time/s')
        plt.ylabel('EDA raw/S')
        plt.show()


    def graph_gradient(lst_interval, lst_gradients): # Shows EDA gradients graph against time interval
        
        fig = plt.figure(figsize = (10, 5)) 
  
        plt.bar(lst_interval, lst_gradients, color ='maroon',  
        width = 0.4) 
  
        plt.xlabel("Time intervals/s") 
        plt.ylabel("EDA Gradients/S") 
        plt.title("Stress Analysis") 
        plt.show() 


readlink()