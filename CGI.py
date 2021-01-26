# Imports
import webbrowser
import platform
from colorama import Fore

# Current OS
os = platform.system()

# Default Login
user = "user"
passwd = "d666"

# Exit Codes

# Auth Error
# AUTH-01 : Bad credentials (Username)
# AUTH-02 : Bad credentials (Password)

# Text Color
print(Fore.MAGENTA)

# Starting
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-= Welcome =-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print(" ")
print("Your current Operating System is: " + os)

print("\nOpen Readme.txt file, the creds are here")
print("\nPlease sign in")

# Username verification
username = input("Enter Username: ")
if username != user:
    exit("✗ | Authentication Error (Exit Code : AUTH-01)")
elif username == user:
    print("\n✓ | Success")

# Password verification
password = input("\nEnter your password: ")
if password != passwd:
    exit("\n✗ | Authentication Error (Exit Code: AUTH-02)")
if password =="d666":
    print("\n✓ | Success")

# Options
option = "1"
print("-=-=-=-=-=-=-=-=-=-=-=-=-=-= Options =-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("\n\n1- Cracked games\n2- Soon...\n3- Soon...\n4- Soon...\n5- Soon...")
input("\nEnter your Choice")
if option =="1":
    webbrowser.open("https://drive.google.com/drive/folders/1M8vQ-aEX9LtWZqwVi1r8jEVH0T1RMjJK?usp=sharing%22")
