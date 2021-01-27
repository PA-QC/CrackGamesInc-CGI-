# Imports
import webbrowser
import platform
from colorama import Fore
import time
import os

# Current OS
os = platform.system()

# Default Login
user = "user"
passwd = "d666"

# Exit Codes

# Auth Error
# AUTH-01 : Bad credentials (Username)
# AUTH-02 : Bad credentials (Password)

# Other Errors
# ERR-01 : Content Unavailable

# Text Color
print(Fore.LIGHTMAGENTA_EX)

# Starting
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-= Welcome =-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" ")
print("Your current Operating System is: " + os)

print("\nOpen Readme.txt file")
print("\nPlease sign in")

# Username verification
username = input("Enter Username: ")
if username != user:
    exit("\n✗ | Authentication Error (Exit Code : AUTH-01)")
elif username == user:
    print("\n✓ | Success")

# Password verification
password = input("\nEnter your password: ")
if password != passwd:
    exit("\n✗ | Authentication Error (Exit Code: AUTH-02)")
if password =="d666":
    print("\n✓ | Success")

# Options
print(Fore.LIGHTGREEN_EX)
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-= Options =-=-=-=-=-=-=-=-=-=-=-=-=-=-")

print("\n1- Cracked games")
time.sleep(0.1)
print("2- Money-Maker")
time.sleep(0.1)
print("3-Network Analyser/DDOS")
time.sleep(0.1)
print("4- Soon...")
time.sleep(0.1)
print("5- Soon...")
time.sleep(0.1)
print("h- Help")
print(Fore.LIGHTGREEN_EX)
time.sleep(0.1)
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
time.sleep(0.1)
print(Fore.LIGHTMAGENTA_EX)
option = input("Choose an option:")
# Selection
if option == "1":
    webbrowser.open("http://aorracer.com/A2C2 %s")
    exit("OPT-1C")
elif option == "2":
    webbrowser.open("http://aorracer.com/8iCX")
elif option == "h":
    print(Fore.LIGHTYELLOW_EX)
    print("Contact us on [ crackedgamesinc.help@gmail.com ] ")
elif option == "H":
    print(Fore.LIGHTWHITE_EX)
    print("Contact us on [ crackedgamesinc.help@gmail.com ] ")
    print(Fore.LIGHTMAGENTA_EX)
elif option == "3":
    print("DDOS SCRIPT")
