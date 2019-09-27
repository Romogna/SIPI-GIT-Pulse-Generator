#!/usr/bin/python3

# Basic file for PThat pulse wave generator

from PTHmodule import *
import time

PT = PTHAT() #create a PThat object
#PT.DEBUG = True
S = PT.GetVersion
#ADC = PT.GetADC1
#Relay = PT.GetAUX1
print(S)

#PT.ToggleMotorEnable()

while input("test axis [input Q to quit] ") != "Q": # Q to quit

    A = input("Axis  (X,Y,Z,E) ")

    if A in "xX":
        axis = PT.GetXaxis
        axis.StepsPerUnit =  100 * 16 * 4 #200 * 16 * 4

    elif A in "yY":
        axis = PT.GetYaxis
        axis.StepsPerUnit = 100 * 16 * 3
    elif A in "zZ":
        axis = PT.GetZaxis
        axis.StepsPerUnit = 400 * 8 #16
    elif A in "eE":
        axis = PT.GetEaxis
        axis.StepsPerUnit = 100 * 32 # 200 * 16

    axis.ADCLink = 0

    AD = input("Acceleration Time (Seconds) ")
    if  AD !="":
        Ramp = AD

    sRPM=input(" RPM ")

    if sRPM !="":
        RPM = float(sRPM)

    sRevs = input(" REVS ")
    if sRevs !="" :
         Revs= float(sRevs)

    D = input(' Direction (or A for auto reverse) ')
    AR=0
    if D in "aA":
        AR = float(input(" Reverse after Revs " ))
        Direction = False #True

    else:
        Direction = float(D) >0

    #ZMotorEnable = PT.GetAUX3 #used as a Z enable on testbox
    #ZMotorEnable.SetAux()

    axis.MotorEnable = True
    axis.AccelerationTime = float(Ramp)

    axis.SetMove(Revs, RPM, bool(Direction))

    if AR >0 :
        axis.SetAutoReverse(AR)

    axis.Start()
    print('Running')
    X=True
    while axis.IsRunning:
        x = PT.Pollport # must poll the port to read the serial data
        if x : print(x) # PT.pollport returns a fault code
        #print(axis.IsRunning)

    axis.MotorEnable = False #disable motors while waitiing for user

    axis.SetMove(0,0,False)

    print('Stopped')
    #PT.Reset()
