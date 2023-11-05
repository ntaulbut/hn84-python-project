from typing import Self
from enum import Enum
from random import randint, choice

# Constants
GRID_WIDTH = 10
GRID_HEIGHT = 10
SHIP_LENGTHS = [5, 4, 3, 3, 2]


# TODO: set ship positions, ai turn, player turn,
class SquareState(Enum):
    EMPTY = " "
    SHIP = "#"
    HIT = "X"


class KnowledgeSquareState(Enum):
    UNKNOWN = " "
    MISS = "O"
    HIT = "X"


class Orientation(Enum):
    N = (0, 1)
    E = (1, 0)
    S = (0, -1)
    W = (-1, 0)


def new_board() -> list[list[str]]:
    return [[" " for _ in range(10)] for _ in range(10)]


player_board = new_board()
player_ships = []
player_knowledge = new_board()

ai_board = new_board()
ai_ships = []
ai_knowledge = new_board()


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
                coord[0] > GRID_WIDTH - 1 or coord[1] > GRID_HEIGHT - 1
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
            board[square[0]][square[1]] = SquareState.SHIP
        
        return obj

    def on_hit(self):
        self.hits += 1
        if self.hits == len(self.squares):
            self.sunk = True


def fire_missile(
    coord: tuple,
    target_board: list[list[SquareState]],
    attacker_knowledge: [list[list[KnowledgeSquareState]]],
    ships: list[Ship],
) -> bool:
    # If already fired at this square
    if attacker_knowledge[coord[0]][coord[1]] != SquareState.UNKNOWN:
        return False
    # Check if shot is a hit or a miss
    for ship in ships:
        if coord in ship.squares:
            ship.on_hit()
            # Update a hit on the target board and let the attacker remember it
            target_board[coord[0]][coord[1]] = SquareState.HIT
            attacker_knowledge[coord[0]][coord[1]] = KnowledgeSquareState.HIT
            break
    else:
        # Record a miss only in knowledge not on the main board
        attacker_knowledge[coord[0]][coord[1]] = KnowledgeSquareState.MISS


def ai_square_pick():
    pass


def battleships():
    # initialise ships
    for length in SHIP_LENGTHS:
        new_ship = False
        while new_ship == False:
            new_ship = Ship(
                ai_ships,
                (randint(0, GRID_WIDTH - 1), randint(0, GRID_HEIGHT - 1)),
                choice(list(Orientation)).value,
                length
            )
        ai_ships.append(new_ship)

    for ship in ai_ships:
        print(f"{ship.squares}")

    # begin game
    # winnerExists = False
    # while not winnerExists:
    #     pass


if __name__ == "__main__":
    battleships()
