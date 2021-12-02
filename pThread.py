# -*- coding: utf-8 -*-
"""
1. Thread 1 - Shuts down system or prints to user that this is happening
2. Thread 2 - Kills the timer for thread 1
3. Main process - (Thead 0) Displays countdown to user

"""
import threading
import time
import keyboard

def timer1():
    print("Shutting down")
    # for count in range(3,0,-1):
    #     time.sleep(1)
    #     print(count)

def killer1(m):
    keyboard.read_event()
    m.cancel()
    #print(m.is_alive())
    
time_till_activation = 3
t = threading.Timer(time_till_activation, timer1)
mylist = [t]
r = threading.Timer(0, killer1, args=mylist)
t.start()
r.start()

while time_till_activation >= 1 and t.is_alive():
    print(time_till_activation)
    time.sleep(1)
    time_till_activation -= 1 
"""
#print(t.is_alive())
while 1:
    #keyboard.read_event()
    t.cancel()
    #t.join()
    break
#print(t.is_alive())
"""
print("Countdown has stopped.")
time.sleep(2)