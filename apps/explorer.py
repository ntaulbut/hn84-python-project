from utils import inc_b, dec_b
import keyboard
from colorama import Fore, Back, Style

def formatSelected(text):
    return (Back.WHITE + Fore.BLACK + text + Style.RESET_ALL)

def getSelectionIndex(numOptions):
    while True:
        selectionIndex = 0
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            match event.name.lower():
                case "down":
                    selectionIndex = dec_b(selectionIndex, 0)
                case "up":
                    if selectionIndex > 0:
                        selectionIndex = inc_b(selectionIndex, numOptions)
                case "enter":
                    return selectionIndex
                case "q":
                    return -1

def explorer():
    lineLength = 80
    numPossFiles = 17
    path = "~/"
    workingDirectory = "~"
    directories = ["games"]
    games = [
        "game1 by Beve Stagley",
        "game2 by James Flycross",
        "game3 by Mason Flatkin",
        "game4 by Wax Killson",
        "game5 by Largahan Waygum",
    ]

    enterOptions = ["Play Game", "Open Directory"]

    template = """┌────────────────────────────────────────────────────────────────────────────────┐
│File Explorer                                                                   │
│{}|
├────────────────────────────────────────────────────────────────────────────────┤
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
│{}│
├────────────────────────────────────────────────────────────────────────────────┤
│[q] Quit  [Enter] {}│
└────────────────────────────────────────────────────────────────────────────────┘"""

    match workingDirectory:
        case "~":
            directoriesToPrint = [
                directories[i].ljust(lineLength) for i in range(len(directories))
            ]

            print(
                template.format(
                    path,
                    *[i for i in directoriesToPrint],
                    *[
                        " " * lineLength
                        for _ in range(numPossFiles - len(directoriesToPrint))
                    ],
                    enterOptions[1],
                )
            )
            numDirectories = len(directories)
            selectionIndex = getSelectionIndex(numDirectories)
            if selectionIndex == -1:
                return None
            elif selectionIndex == None:
                print("something went wrong :(")
            else:

                workingDirectory = directories[selectionIndex]
                path += workingDirectory
        case "games":
            gamesToPrint = [games[i].ljust(lineLength) for i in range(len(games))]
            print(template.format(path, *gamesToPrint, enterOptions[0]))
            numGames = len(games)
            selectionIndex = getSelectionIndex(numGames)
            if selectionIndex == -1:
                return None
            elif selectionIndex == None:
                print("something went wrong :(")
            else:
                selectedGame = games[selectionIndex]
                # call selected game

def app():
    explorer()


if __name__ == "__main__":
    app()
