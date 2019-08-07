from time import gmtime, strftime
import time
import sys

file = open("config.txt", "r")
if file.mode == 'r':
    contents = file.readline()
    #contents = "Wed, 07 Aug 2019 14:04"
    #print(contents)

while True:
    current_time = strftime("%a, %d %b %Y %H:%M", gmtime())
    if (current_time == contents):
        print("Alarm!\n")
    elif (current_time != contents):
        pass
    else:
        print("Error: Cannot get time from system or 'config.txt'")
        sys.exit()
    
    time.sleep(2)
