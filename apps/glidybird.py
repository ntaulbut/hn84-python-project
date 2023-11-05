import random
from utils import *
from time import sleep
import keyboard

def getObstacleLine():
    rand_num = (random.randrange(0, (MAX - 2))) # WOAH THATS ME!  NO WAY!!
    return ['█' for _ in range(rand_num)] + [' ', ' '] + ['█' for _ in range(MAX - (rand_num + 2))]

def getBlankLine():
    return [' ' for _ in range(MAX)]

WIDTH = 80
MAX = 10
OBSTACLE_CHAR = '█'
PLAYER_CHAR = '□'

def bird():
    player_height = 4
    counter = 0
    run_count = 0

    # Lines go here
    pipes = [getBlankLine() for _ in range(WIDTH)]
    pipes[10][4] = PLAYER_CHAR

    x = WIDTH // 8
    y = player_height
    

    while True:
        clear()

        # 2. Write player character unless they have crashed
        pipes[x][player_height] = PLAYER_CHAR

        # 1. Shuffle lines
        for i in range(1, WIDTH):
            pipes[i-1] = pipes[i]
          

        if pipes[x][y] == OBSTACLE_CHAR:
            print("DEAD!!")
            print("> Press any key to return")

            keyboard.read_event()
            break
        else:
            if keyboard.is_pressed("down"):
                if (y != 0):
                    player_height += 1
                    pipes[x][player_height] = PLAYER_CHAR
                    pipes[x][player_height - 1] = ' '
                    y += 1
                    continue
            elif keyboard.is_pressed("up"):
                if (y != 9):
                    player_height -= 1
                    pipes[x][player_height] = PLAYER_CHAR
                    pipes[x][player_height + 1] = ' '
                    y -= 1
                    continue

                    

        # 3. Append new line (obstacle every 5 or so)
        if (counter == 8): 
            pipes[i] = getObstacleLine()
            counter = 0
        else:
            pipes[i] = getBlankLine()
            counter+=1
        
        # Probably don't change this bit (please) (prints out map)
        for i in range(MAX - 1):
            print(*[m[i] for m in pipes], sep="")

        if (run_count == 150):
            print("!!  WIN  !!   m-s")
            print("> Press any key to return")

            keyboard.read_event()

            break

        run_count+=1
        sleep(0.35)

if __name__ == "__main__":
    bird()
