# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:16:09 2020

@author: Fabi
"""
import time
import csv
import serial

#Abrir el puerto COM6

ser = serial.Serial('/dev/ttyACM0', 9600)

count = 0
elapsed_time = 0
with open(r'Baseline_file_01.csv', 'a') as b:
    Datos = csv.writer(b,delimiter=',')
    Datos.writerow(['Baseline value TVOC[HEX]','Baseline value eCO2[HEX]'])

while True:
    line = ser.readline()
    print(line)
    line_str = str(line)
    largo = len(line_str)
    line_fix=line_str[2:largo-5]
    print(line_fix)
    
    with open(r'Baseline_file_01.csv', 'a') as b:
        Datos = csv.writer(b,delimiter=' ')
        Datos.writerow([line_fix])        
        

##    elapsed_time +=1
    time.sleep(1)
        
##    if elapsed_time == 20:
##        break
##        
