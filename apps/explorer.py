from utils import inc_b, dec_b, clear
import keyboard
from colorama import Fore, Back, Style

# Constants
LINE_LENGTH = 80
MAX_FILES = 17


def formatSelected(text: str, selected: bool = False) -> str:
    text = text.ljust(LINE_LENGTH)
    return Back.WHITE + Fore.BLACK + text + Style.RESET_ALL if selected else text


def explorer() -> None:
    selectionIndex = 0

    path = "~/"
    workingDirectory = "~"
    directories = ["Games", "Code", "Documents"]
    games = [
        "Beve's Coke Crusade - Beve Stagley",
        "C Shanty - James Flycross",
        "game3 - Mason Flatkin",
        "game4 - Wax Killson",
        "game5 - Warjahan Maygum",
    ]

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
    while True:
        clear()

        # Print
        match workingDirectory:
            case "~":
                print(
                    template.format(
                        path.ljust(LINE_LENGTH),
                        *[
                            formatSelected(directory, selectionIndex == index)
                            for index, directory in enumerate(directories)
                        ],
                        *[
                            " " * LINE_LENGTH
                            for _ in range(MAX_FILES - len(directories))
                        ],
                        "Open Directory".ljust(LINE_LENGTH),
                    )
                )
            case "Games":
                print(
                    template.format(
                        path.ljust(LINE_LENGTH),
                        *[
                            formatSelected(game, selectionIndex == index)
                            for index, game in enumerate(games)
                        ],
                        *[" " * LINE_LENGTH for _ in range(MAX_FILES - len(games))],
                        "Play Game".ljust(LINE_LENGTH),
                    )
                )

        # Input
        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            match workingDirectory:
                case "~":
                    match event.name:
                        case "enter":
                            workingDirectory = directories[selectionIndex]
                            path += workingDirectory
                        case "down":
                            selectionIndex = inc_b(selectionIndex, len(directories) - 1)
                case "Games":
                    match event.name:
                        case "down":
                            selectionIndex = inc_b(selectionIndex, len(games) - 1)
                        case "enter":
                            selectedGame = games[selectionIndex]
                            # TODO: run selected game
                            return
            # All menus
            match event.name.lower():
                case "up":
                    selectionIndex = dec_b(selectionIndex, 0)
                case "q":
                    return


if __name__ == "__main__":
    explorer()
