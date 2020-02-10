# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 10:16:09 2020

@author: Fabi
"""
import time
import csv
#import sys
import serial
##
###Abrir el puerto COM6
##
##ser = serial.Serial('/dev/ttyACM0', 9600)
##count = 0
##elapsed_time = 0
##with open(r'Data_file_01.csv', 'a') as b:
##    Datos = csv.writer(b,delimiter=',')
##    Datos.writerow(['TVOC','eCO2'])
##
##while True:
##    line = ser.readline()
##    with open(r'Data_file_01.csv', 'a') as b:
##        Datos = csv.writer(b,delimiter=' ')
##        Datos.writerow([line])        
##        
##
##    elapsed_time +=1
##    time.sleep(1)
##        
##    if elapsed_time == 10:
##        break
##        

ser = serial.Serial('/dev/ttyACM0', 9600)
count = 0
elapsed_time = 0
with open(r'Data_file_01.csv', 'a') as b:
    Datos = csv.writer(b,delimiter=',')
    Datos.writerow(['Sample','TVOC','eCO2'])

while True:
    line = ser.readline()
    line_str = str(line)
    largo = len(line_str)
    line_fix=line_str[2:largo-5]
    data = str(elapsed_time)+','+line_fix
    print(line_fix)
    with open(r'Data_file_01.csv', 'a') as b:
       Datos = csv.writer(b,delimiter=' ')
       Datos.writerow([data])        
        

    elapsed_time +=1
    time.sleep(1)
        
    if elapsed_time == 100:
        break
        
