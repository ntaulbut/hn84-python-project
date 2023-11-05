from typing import Self, Any
import keyboard
from enum import Enum
from utils import *
from random import randint, choice

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 10
SHIP_LENGTHS = [5, 4, 3, 3, 2]


class SquareState(Enum):
    EMPTY = " "
    SHIP = "#"
    MISS = "."
    HIT = "X"


class KnowledgeSquareState(Enum):
    UNKNOWN = " "
    MISS = "."
    HIT = "X"


class Orientation(Enum):
    N = (0, -1)
    E = (1, 0)
    S = (0, 1)
    W = (-1, 0)


def new_board(placeholder) -> list[list[Any]]:
    return [[placeholder for _ in range(10)] for _ in range(10)]


player_board = new_board(SquareState.EMPTY)
player_ships = []
player_knowledge = new_board(KnowledgeSquareState.UNKNOWN)

ai_board = new_board(SquareState.EMPTY)
ai_ships = []
ai_knowledge = new_board(KnowledgeSquareState.UNKNOWN)


class Ship:
    def __init__(self, *_):
        self.hits = 0
        self.sunk = False

    def __new__(
        cls,
        board: list[SquareState],
        ships: list[Self],
        root: tuple[int, int],
        orientation: Orientation,
        length: int,
    ) -> Self:
        obj = object.__new__(cls)
        # Extend squares for `length` in `orientation` from `root`
        obj.squares = []
        for i in range(length):
            obj.squares.append(
                (root[0] + orientation[0] * i, root[1] + orientation[1] * i)
            )
        # Confirm all squares are in the grid
        if any(
            [
                coord[0] > GRID_WIDTH - 1
                or coord[0] < 0
                or coord[1] > GRID_HEIGHT - 1
                or coord[1] < 0
                for coord in obj.squares
            ]
        ):
            return False
        # Check if any already placed ships' squares overlap with our squares
        if any(
            [
                len([square for square in obj.squares if square in ship.squares]) > 0
                for ship in ships
            ]
        ):
            return False

        # Place squares
        for square in obj.squares:
            board[square[1]][square[0]] = SquareState.SHIP

        return obj

    def on_hit(self):
        self.hits += 1
        if self.hits >= len(self.squares):
            self.sunk = True


def vec_add(a: tuple[int, int], b: tuple[int, int]):
    return (a[0] + b[0], a[1] + b[1])


def fire_missile(
    coord: tuple,
    target_board: list[list[SquareState]],
    attacker_knowledge: [list[list[KnowledgeSquareState]]],
    target_ships: list[Ship],
) -> bool:
    # If already fired at this square
    if attacker_knowledge[coord[1]][coord[0]] != KnowledgeSquareState.UNKNOWN:
        return False
    # Check if shot is a hit or a miss
    for ship in target_ships:
        if coord in ship.squares:
            ship.on_hit()
            # Update a hit on the target board and let the attacker remember it
            target_board[coord[1]][coord[0]] = SquareState.HIT
            attacker_knowledge[coord[1]][coord[0]] = KnowledgeSquareState.HIT
            break
    else:
        attacker_knowledge[coord[1]][coord[0]] = KnowledgeSquareState.MISS
        target_board[coord[1]][coord[0]] = SquareState.MISS
    return True


def display_board(board: list[list[Any]]):
    print("│   0 1 2 3 4 5 6 7 8 9   │")
    for i in range(GRID_HEIGHT):
        print(f"│ {chr(i + 65)} ", end="")
        print(*[square.value for square in board[i]], sep=" ", end="   │\n")


def display():
    clear()
    print("┌" + "─" * 25 + "┐")
    display_board(player_knowledge)
    print("├" + "─" * 25 + "┤")
    display_board(player_board)
    print("└" + "─" * 25 + "┘")


def inverse_orientation(orientation: Orientation):
    match orientation:
        case Orientation.N:
            return Orientation.S
        case Orientation.S:
            return Orientation.N
        case Orientation.E:
            return Orientation.W
        case Orientation.W:
            return Orientation.E


def decode_notation(str):
    return (ord(str[0]) - 97, int(str[1]))


class RandomState:
    pass


class ScanState:
    def __init__(self, focus):
        self.focus = focus
        self.options = iter(
            [
                orientation
                for orientation in list(Orientation)
                if not (
                    vec_add(self.focus, orientation.value)[0] > GRID_WIDTH - 1
                    or vec_add(self.focus, orientation.value)[0] < 0
                    or vec_add(self.focus, orientation.value)[1] > GRID_HEIGHT - 1
                    or vec_add(self.focus, orientation.value)[1] < 0
                )
            ]
        )


class FollowState:
    def __init__(self, focus: tuple[int, int], orientation: Orientation):
        self.focus = focus
        self.orientation = orientation


def battleships():
    # AI ship placement
    for displacement in SHIP_LENGTHS:
        new_ship = False
        while new_ship == False:
            new_ship = Ship(
                ai_board,
                ai_ships,
                (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1)),
                choice(list(Orientation)).value,
                displacement,
            )
        ai_ships.append(new_ship)

    available_ship_lengths = SHIP_LENGTHS
    # available_ship_lengths = []
    # Player ship placement
    while len(available_ship_lengths) > 0:
        display()
        inp = input("Enter start/end points of a ship to place it (e.g. c0 c2): ")
        try:
            a, b = [i.lower() for i in inp.split()]
            a_row, a_column = decode_notation(a)
            b_row, b_column = decode_notation(b)
            # Determine orientation from a to b
            orientation = False
            if a_row == b_row:
                displacement = b_column - a_column
                if displacement > 0:
                    orientation = Orientation.E
                else:
                    orientation = Orientation.W
            elif a_column == b_column:
                displacement = b_row - a_row
                if displacement > 0:
                    orientation = Orientation.S
                else:
                    orientation = Orientation.N
            # print(f"fDEBUG {a_row} {a_column} {orientation.value} {abs(displacement) + 1}")
            length = abs(displacement) + 1
            if length in available_ship_lengths:
                new_ship = Ship(
                    player_board,
                    player_ships,
                    (a_column, a_row),
                    orientation.value,
                    length,
                )
                if new_ship != False:
                    player_ships.append(new_ship)
                else:
                    raise Exception
                available_ship_lengths.remove(length)
            else:
                display()
                print("Error: ship length not available.")
                sleep(2)
        except Exception:
            pass

    ai_state = RandomState()
    run = True
    # Main game loop
    while run:
        display()
        # Player turn
        inp = input("Enter square to fire missile (e.g. c4): ")
        if inp != "exit":
            a_row, a_column = decode_notation(inp)
            fire_missile((a_column, a_row), ai_board, player_knowledge, ai_ships)
            # AI turn
            if isinstance(ai_state, RandomState):
                # Fire at a random square
                coord = (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1))
                fire_missile(
                    coord,
                    player_board,
                    ai_knowledge,
                    player_ships,
                )
                # If it's a hit, scan
                if ai_knowledge[coord[1]][coord[0]] == KnowledgeSquareState.HIT:
                    ai_state = ScanState(coord)
            elif isinstance(ai_state, ScanState):
                try:
                    explore = next(ai_state.options)
                    coord = vec_add(ai_state.focus, explore.value)
                    fire_missile(
                        coord,
                        player_board,
                        ai_knowledge,
                        player_ships,
                    )
                    # If it's a hit
                    if ai_knowledge[coord[1]][coord[0]] == KnowledgeSquareState.HIT:
                        ai_state = FollowState(coord, explore)
                except StopIteration:
                    ai_state = RandomState()
            elif isinstance(ai_state, FollowState):
                coord = vec_add(ai_state.focus, ai_state.orientation.value)
                fire_missile(
                    coord,
                    player_board,
                    ai_knowledge,
                    player_ships,
                )
                # If it's a hit
                if ai_knowledge[coord[1]][coord[0]] == KnowledgeSquareState.HIT:
                    ai_state.focus = coord
                elif (
                    # If going further would take us off the grid
                    vec_add(ai_state.focus, ai_state.orientation.value)[0] > GRID_WIDTH - 1
                    or vec_add(ai_state.focus, ai_state.orientation.value)[0] < 0
                    or vec_add(ai_state.focus, ai_state.orientation.value)[1]
                    > GRID_HEIGHT - 1
                    or vec_add(ai_state.focus, ai_state.orientation.value)[1] < 0
                ):
                    ai_state = RandomState()
                else:
                    ai_state = RandomState()

            # Win condition
            if all([ship.sunk for ship in player_ships]):
                display()
                input("You LOST! Press enter...")
                run = False
            if all([ship.sunk for ship in ai_ships]):
                display()
                input("You WON! Clue: `AI`. Press enter...")
                run = False
        else:
            run = False


if __name__ == "__main__":
    battleships()
