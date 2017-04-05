import subprocess
import os
import signal
import time
import RPi.GPIO as GPIO

# Use broadcom pin numbers
GPIO.setmode(GPIO.BCM)

# Don't forget to use a pull-up resistor 
GPIO.setup(24, GPIO.IN)

def startRecording():
    myproc = subprocess.Popen('./Logger2', shell=False)
    return myproc

def stopRecording(myproc):
    os.killpg(os.getpgid(myproc.pid), signal.SIGINT)

# Falling edge will happen the instant the button is pressed
GPIO.wait_for_edge(24, GPIO.RISING)
myproc = startRecording()
time.sleep(2)
GPIO.wait_for_edge(24, GPIO.RISING)
stopRecording(myproc)

GPIO.cleanup()

