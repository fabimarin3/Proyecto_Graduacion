# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:16:09 2020

@author: Fabi
"""
import time
import csv
#import sys
import serial

#Abrir el puerto COM6

ser = serial.Serial('/dev/ttyACM0', 9600)

#with open("datafile.csv", "w") as new_file:
 #   csv_writer = csv.writer(new_file)


  #  while True:
   #     line = ser.readline()
    #    new_file.writerows([line])

count = 0
elapsed_time = 0
with open(r'Data_file_01.csv', 'a') as b:
    Datos = csv.writer(b,delimiter=',')
    Datos.writerow(['TVOC','eCO2'])

while True:
    line = ser.readline()
    print(line)
    with open(r'Data_file_01.csv', 'a') as b:
        Datos = csv.writer(b)
        Datos.writerow([line])        
        

    elapsed_time +=1
    time.sleep(1)
        
    if elapsed_time == 20:
        break
        
