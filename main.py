from maskpass import askpass
from time import sleep
from colorama import init
from utils import *
from apps.explorer import explorer
from apps.mail import mail_app

# Initialise colorama
init()

# Login screen
clear()
print("Welcome to the Machine: Wimbows84 © 1984. Please authenticate.")
print("========================================================")
username = input("Username: ")
password = askpass("Password: ", mask="*")
dprint("Connecting", end="", flush=True)
for _ in range(3):
    dprint(".", 0.5, end="", flush=True)

# Terminal loop
dprint(f"\n\nWelcome {username}! You have 1 unread message(s).", 2, 1)

while True:
    inp = input(f"{username}@mainframe:~$ ")

    match inp:
        case "mail":
            mail_app()
        case "explorer":
            explorer()
        case "logout":
            dprint("Goodbye :)", after=1)
            exit(1)

        case "help":
            print(
                """Commands:
    - mail: open mailbox
    - help: list all commands
    - explorer: run file explorer
    - logout: close session"""
            )
        case "max":
            print_art("max")
        case "nathaniel":
            print_art("frog")
        case "mayukhi":
            print_art("mayukhi")
        case "oli":
            print_art("blahaj")

        case _:
            print(
                f"{inp.split()[0]}: command not found. Enter 'help' for a list of commands."
            )
