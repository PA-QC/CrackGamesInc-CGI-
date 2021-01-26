# Imports
import webbrowser
import platform
import os

#Process PID
pid = os.getpid()
#Current OS
os = platform.system()

print("-=-=-=-=-=-=-= Welcome =-=-=-=-=-=-=-")
print(" ")
print("Your Process ID is: " + str(pid))
print("Your current Operating System is: " + os)


