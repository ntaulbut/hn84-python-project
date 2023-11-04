from time import sleep
from sys import platform
from os import system


TOP_LINE = "┌" + "─" * 78 + "┐\n"
DIV_LINE = "├" + "─" * 78 + "┤\n"
BOTTOM_LINE = "└" + "─" * 78 + "┘"


def clear():
    # clears terminal
    if platform == "win32":
        _ = system("cls")
    else:
        _ = system("clear")


def dprint(text: str, before: int = 1, after: int = 0, *args, **kwargs):
    # Print with a delay before and/or after
    sleep(before)
    print(text, *args, **kwargs)
    sleep(after)


def print_art(name: str):
    with open(f"art/{name}.txt", "r", encoding="utf-8") as file:
        print(file.read())


def inc_b(old: int, max_i: int) -> int:
    # Increment a value keeping it below or equal to a maximum
    return min(old + 1, max_i)


def dec_b(old: int, min_i: int) -> int:
    # Increment a value keeping it above or equal to a minimum
    return max(old - 1, min_i)
