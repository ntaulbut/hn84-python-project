from utils import print_art, clear
from maskpass import askpass

def top_secret():
    print("################################## TOP SECRET ##################################")
    password = askpass("Password: ",mask="*")
    if password.upper() == "MASSIVE":
        clear()
        print("Blahaj is love, Blahaj is life\n")
        print_art("blahaj")