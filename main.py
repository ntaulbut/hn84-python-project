from maskpass import askpass
from time import sleep
from colorama import init
from utils import *
from apps.explorer import explorer
from apps.mail import mail_app
from apps.maze import maze

# Initialise colorama
init()

# Login screen
clear()
print("Welcome to the Machine: Wimbows84 © 1984. Please authenticate.")
print("==============================================================")
username = input("Username: ")
password = askpass("Password: ", mask="*")
dprint("Connecting", end="", flush=True)
for _ in range(3):
    dprint(".", 0.5, end="", flush=True)

# Terminal loop
dprint(f"\n\nWelcome {username}! You have 2 unread message(s).", 2, 1)

while True:
    inp = input(f"{username}@mainframe:~$ ")

    match inp:
        case "mail":
            mail_app(username)
        case "explorer":
            explorer(username)
        case "logout":
            dprint("Goodbye :)", after=1)
            exit(1)
        case "maze":
            maze()
            clear()
            dprint(f"\n\nWelcome {username}! You have 2 unread message(s).", 2, 1)
        case "help":
            print(
                """Commands:
    - mail: open mailbox
    - help: list all commands
    - explorer: run file explorer
    - logout: close session"""
            )
        case _:
            print(
                f"{inp.split()[0]}: command not found. Enter 'help' for a list of commands."
            )
    if password == "NottsRulez":
        if inp == "max":
            print_art("max")
        elif inp == "nathaniel":
            print_art("frog")
        elif inp == "mayukhi":
            print_art("mayukhi")
        elif inp == "oli":
            print_art("blahaj")

        
