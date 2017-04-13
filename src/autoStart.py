#!/usr/bin/env python
import subprocess
import os
import signal
import time
import RPi.GPIO as GPIO

time.sleep(10)

# Use broadcom pin numbers
GPIO.setmode(GPIO.BCM)

# Don't forget to use a pull-up resistor 
GPIO.setup(24, GPIO.IN)
# For the 'this script is running' LED
GPIO.setup(23, GPIO.OUT)
# For the 'logging data' LED
GPIO.setup(17, GPIO.OUT)
GPIO.setup(17, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)

def startRecording():
    myproc = subprocess.Popen('../build/Logger2', shell=False, cwd='../build')
    GPIO.output(17, GPIO.HIGH)
    return myproc

def stopRecording(myproc):
    myproc.send_signal(signal.SIGINT)
    GPIO.output(17, GPIO.LOW) 

def scpFileToBlueisland():
    # Authentication happens using ssh keys
    myproc = subprocess.Popen(['scp', '-i', '/home/henry/.ssh/id_rsa','/home/henry/Kinect_Logs/rs.klg',
                               'henry@172.17.34.17:~/poll_kinect_log_folder'])
    print 'Copying the file...'
    # Wait til the scp is finished
    myproc.wait()
    print 'Done copying the file.'

while True: 
    # Falling edge will happen the instant the button is pressed
    GPIO.wait_for_edge(24, GPIO.RISING)
    myproc = startRecording()
    # So we don't trigger a stop at the same time
    time.sleep(2)
    GPIO.wait_for_edge(24, GPIO.RISING)
    stopRecording(myproc)
    time.sleep(2)
    scpFileToBlueisland()

GPIO.cleanup()

