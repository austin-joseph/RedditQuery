import sys
import json
import schedule
import time
import subprocess
import _thread

def runProgram(prgm):
    try:
        _thread.start_new_thread(executeThread,(prgm, ))
    except:
        print("Error: unable to start thread")

def executeThread(prgm):
    subprocess.run(prgm["command"], cwd=prgm["dir"])

if len(sys.argv) != 2:
    print("The program expects a config file as the first and only argument. You can find documentation on how to open the config file in the README.txt file in the root directory of the project.")
    exit()

with open(sys.argv[1]) as configHandle:
    configFile = json.load(configHandle)

if configFile == None:
    print("Error loading config file aborting")
    exit()

for x in configFile["schedule"]:
    runProgram(x)
    schedule.every(int(x["interval"])).seconds.do(runProgram, prgm=x)

while True:
    schedule.run_pending()
    time.sleep(1)
