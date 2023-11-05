from utils import inc_b, dec_b, clear
import keyboard
from colorama import Fore, Back, Style
from apps.maze import maze
from apps.mail import mail_app
from apps.battleships import battleships
from apps.top_secret import top_secret
from apps.glidybird import bird

# Constants
LINE_LENGTH = 80
MAX_FILES = 17
NAME_FUNCION_ASSOCIATION_DICT = {
    "Beve's Coke Crusade - Beve Stagley":maze,
    "C Shanty - Mason Flatkin":battleships,
    "Mail":mail_app,
    "TOP SECRET":top_secret,
    "Glidy Bird - James Flycross":bird
}


def formatSelected(text: str, selected: bool = False) -> str:
    text = text.ljust(LINE_LENGTH)
    return Back.WHITE + Fore.BLACK + text + Style.RESET_ALL if selected else text


def explorer(username) -> None:
    selectionIndex = 0

    path = "~/"
    workingDirectory = "~"
    directories = ["Games", "Apps", "Mysterious Folder"]

    games = [
        "Beve's Coke Crusade - Beve Stagley",
        "C Shanty - Mason Flatkin",
        "Glidy Bird - James Flycross",
    ]

    apps = [
        "Mail"
    ]

    mysterious = [
        "TOP SECRET"
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
            case "Apps":
                print(
                    template.format(
                        path.ljust(LINE_LENGTH),
                        *[
                            formatSelected(app, selectionIndex == index)
                            for index, app in enumerate(apps)
                        ],
                        *[" " * LINE_LENGTH for _ in range(MAX_FILES - len(apps))],
                        "Run App".ljust(LINE_LENGTH),
                    )
                )
            case "Mysterious Folder":
                print(
                    template.format(
                        path.ljust(LINE_LENGTH),
                        *[
                            formatSelected(app, selectionIndex == index)
                            for index, app in enumerate(mysterious)
                        ],
                        *[" " * LINE_LENGTH for _ in range(MAX_FILES - len(mysterious))],
                        "Run App".ljust(LINE_LENGTH),
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
                            NAME_FUNCION_ASSOCIATION_DICT[selectedGame]()
                case "Apps":
                    match event.name:
                        case "down":
                            selectionIndex = inc_b(selectionIndex, len(apps)-1)
                        case "enter":
                            selectedApp = apps[selectionIndex]
                            match selectedApp:
                                case "Mail":
                                    NAME_FUNCION_ASSOCIATION_DICT[selectedGame](username)

                case "Mysterious Folder":
                    match event.name:
                        case "down":
                            selectionIndex = inc_b(selectionIndex, len(mysterious) - 1)
                        case "enter":
                            selectedFile = mysterious[selectionIndex]
                            NAME_FUNCION_ASSOCIATION_DICT[selectedFile]()
                             
            # All menus
            match event.name.lower():
                case "up":
                    selectionIndex = dec_b(selectionIndex, 0)
                case "q":
                    path = "~/"
                    workingDirectory = "~"
                    clear()
                    return


if __name__ == "__main__":
    explorer("user")
