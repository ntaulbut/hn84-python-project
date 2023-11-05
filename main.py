from maskpass import askpass
from colorama import init
from utils import *
from apps.explorer import explorer
from apps.mail import mail_app
from apps.maze import maze
from apps.top_secret import top_secret
from apps.battleships import battleships
from apps.glidybird import bird

# Initialise colorama
init()

userInput = ""

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
            clear()
        case "explorer":
            explorer(username)
            clear()
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
    - maze: opens maze
    - help: list all commands
    - explorer: run file explorer
    - battleships: play battleships
    - bird: play glidy bird
    - logout: close session
    - topSecret"""
            )
        case "max":
            print_art("max")
        case "nathaniel":
            print_art("frog")
        case "mayukhi":
            print_art("mayukhi")
        case "oli":
            print_art("blahaj")
        case "topSecret":
            top_secret()
        case "battleships":
            battleships()
        case "bird":
            bird()
        case _:
            try:
                print(
                    f"{inp.split()[0]}: command not found. Enter 'help' for a list of commands."
                )
            except IndexError:
                pass
