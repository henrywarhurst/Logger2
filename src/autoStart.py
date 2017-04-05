import subprocess
import os
import signal
import time

myproc = subprocess.Popen('./Logger2', shell=False)
print "p = " + str(myproc.pid)
time.sleep(5)
#myproc.terminate()
os.killpg(os.getpgid(myproc.pid), signal.SIGINT)
#os.killpg(myproc.pid, signal.SIGINT)
#subprocess.call('./Logger2')
