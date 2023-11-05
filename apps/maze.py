import keyboard
from utils import *
from time import sleep
from itertools import *

global playerPos
playerPos = [0,0,0]

def printMaze(maze, solved):
    clear()
    for i in range(16):
            for l in range(31):
                #prints maze
                print(maze[i][l], end="")
                #stores player position when found
                if (maze[i][l] == "■ "):
                    playerPos[0] = i
                    playerPos[1] = l
                    playerPos[2] = 0
                if (maze[i][l] == "■."):
                    playerPos[0] = i
                    playerPos[1] = l
                    playerPos[2] = 1
                if (maze[i][l] == "■x"):
                    playerPos[0] = i
                    playerPos[1] = l
                    playerPos[2] = 2

            #prints coke can
            if(solved):
                if (i == 10):
                    print("   /─────\\")
                elif (i == 11):
                    print("   │  C  │")
                elif(i == 12):
                    print("   │  O  │")
                elif (i == 13):
                    print("   │  K  │")
                elif(i == 14):
                    print("■  │  E  │")
                elif(i == 15):
                    print("   \\─────/")
                else:
                    print("")
            else:
                if (i == 10):
                    print("   /─────\\")
                elif (i == 11):
                    print("   │  C  │")
                elif(i == 12):
                    print("   │  O  │")
                elif (i == 13):
                    print("   │  K  │")
                elif(i == 14):
                    print("   │  E  │")
                elif(i == 15):
                    print("   \\─────/")
                else:
                    print("")

                # ┌────────┐
                # │ t -> T │
                # └────────┘

                #/─────\
                #│  C  │
                #│  O  │
                #│  K  │
                #│  E  │
                #\─────/

            


# print("""
#┌────────┬─────┬─────┬xx─────────┬─────┬──┬──┐ 
# ■       │     │     │ .  .  .  4│     │  │  │ 
#├─────┐     │     ┌──┤  │  ┌──┐  └───     │  │ 
#│     │  │  └──┐  │  │  ├──┘  │        │     │ 
#│  └──┘  │     │ 2│  │  │ .  .  5│  ┌──┘  │  │ 
#│        ├──┐  │ .   │  │ .│  │  │  │     └──┤ 
#├──┐  │  │  ├──┘ .│  │     ├──┤  │     │     │ 
#x  │  ├──┘  │    .│  │XX│  │  │  ├───  ├───  x 
#│  │  │     ├──┬──┤     │  │  │  │ .   │     │ 
#│     │  │  │  │  ├───  │     ├──┘ .│     ┌──┤ 
#│  ┌──┤  │     │  │     │  │  │    .└──┐  │  │   /─────\
#│ .│  ├──┘  ┌──┤  │ 3│  ├──┤  ├──┐ 6   │  │  │   │  C  │
#│ .   │     │  │    .│  │  │  │  ├──┐  │     │   │  O  │
#│ .│  └───     │  │ .│  │  │     │  │     │  │   │  K  │
#│ 1│        │     │ .│     │  │  │     │  │      │  E  │
#└──┴────────┴─────┴──┴xx───┴──┴──┴─────┴──┴──┘   \─────/

#┌────────┬─────┬─────┬xx─────────┬─────┬──┬──┐ 
# ■       │     │     │ .  .  4  .│     │  │ x│ 
#├─────┐     │     ┌──┤  │  ┌──┐  └───     │  │ 
#│     │  │  └──┐  │  │  ├──┘  │        │     │ 
#│  └──┘  │     │ .│  │  │ .  .  5│  ┌──┘  │  │ 
#│        ├──┐  │ 2   │  │ .│  │  │  │     └──┤ 
#├──┐  │  │  ├──┘ ┌───────────┐┤  │     │     │ 
#x  │  ├──┘  │    │ !! WIN !! ││  ├───  ├───  x 
#│  │  │     ├──┬─└───────────┘│  │ .   │     │ 
#│     │  │  │  │  ├───  │     ├──┘ .│     ┌──┤ 
#│  ┌──┤  │     │  │     │  │  │    6└──┐  │  │ 
#│ .│  ├──┘  ┌──┤  │ .│  ├──┤  ├──┐ .   │  │  │ 
#│ .   │     │  │    3│  │  │  │  ├──┐  │     │ 
#│ .│  └───     │  │ .│  │  │     │  │     │  │ 
#│ 1│        │     │ .│     │  │  │     │  │    
#└──┴────────┴─────┴──┴xx───┴──┴──┴─────┴──┴──┘ 

#┌───────────┐
#│ GAME OVER │11 across
#└───────────┘6 down

#""")

# ├
# ┬ 
# ┴
# ┤
# ┼
# │
# ──

# https://en.wikipedia.org/wiki/Box-drawing_character

# player: :) ■ 
# bad guy: <> □
# X

def maze():

    maze = []

    solved = False
    
    #cycle_iter = cycle(chain(range(3), range(3, 0, -1)))
    
    #arrays of all enemy paths
    enemy = [[[14, 1], [13, 1], [12, 1], [11, 1]], [[4, 11], [5, 11], [6, 11], [7, 11]], \
        [[11, 13], [12, 13], [13, 13], [14, 13]], [[1, 21], [1, 19], [1, 17], [1, 15]], \
        [[4, 21], [4, 19], [4, 17], [5, 17]], [[11, 23], [10, 23], [9, 23], [8, 23]]]
    

    while(not solved):

        enemyCycle = 0
        cycleFlip = 0
        panic = 0
        dead = False
        x = False
        #HARD CODE MAZE HERE
        maze = [
            ["┌", "──", "─", "──", "─", "──", "┬", "──", "─", "──", "┬", "──", \
            "─", "──", "┬", "──", "─", "──", "─", "──", "─", "──", "┬", "──", \
            "─", "──", "┬", "──", "┬", "──", "┐"], \

            [" ", "■ ", " ", "  ", " ", "  ", "│", "  ", " ", "  ", "│", "  ", \
            " ", "  ", "│", " .", " ", " .", " ", " .", " ", " □", "│", "  ", \
            " ", "  ", "│", "  ", "│", " x", "│"], \

            ["├", "──", "─", "──", "┐", "  ", " ", "  ", "│", "  ", " ", "  ", \
            "┌", "──", "┤", "  ", "│", "  ", "┌", "──", "┐", "  ", "└", "──", \
            "─", "  ", " ", "  ", "│", "  ", "│"], \

            ["│", "  ", " ", "  ", "│", "  ", "│", "  ", "└", "──", "┐", "  ", \
            "│", "  ", "│", "  ", "├", "──", "┘", "  ", "│", "  ", " ", "  ", \
            " ", "  ", "│", "  ", " ","  ", "│"], \

            ["│","  ","└","──","┘","  ","│","  "," ","  ","│"," □","│","  ","│","  ","│"," ."," ", \
            " ."," "," □","│","  ","┌","──","┘","  ","│","  ","│", "  "], \

            ["│","  "," ","  "," ","  ","├","──","┐","  ","│"," ."," ","  ","│","  ",\
            "│"," .","│","  ","│","  ","│","  ","│","  "," ","  ","└","──","┤"] ,\

            ["├","──","┐","  ","│","  ","│","  ","├","──","┘"," .","│","  ","│","  "," ","  ","├",\
            "──","┤","  ","│","  "," ","  ","│","  "," ","  ","│"], \

            ["│", "  ", "│", "  ", "├", "──", "┘", "  ", "│", "  "," ", " .", "│", "  ", "│", "  ", "│", \
            "  ", "│", "  ", "│", "  ", "├", "──", "─", "  ", "├", "──", "─", "  ", "│"], \

            ["│","  ","│","  ","│","  "," ","  ","├","──","┬","──","┤","  "," ","  ","│", "  ","│", \
            "  ","│","  ","│"," ."," ","  ","│","  "," ","  ","│"], \

            ["│", "  "," ", "  ", "│", "  ", "│", "  ", "│", "  ", "│", "  ", "├", "──", "─", "  ", "│", \
            "  ", " ", "  ", "├", "──", "┘", " .", "│", "  ", " ", "  ", "┌", "──", "┤"], \

            ["│","  ","┌","──","┤","  ","│","  "," ","  ","│","  ","│","  "," ","  ", \
            "│","  ","│","  ","│","  "," "," .","└","──","┐","  ","│","  ","│"], \

            ["│", " .", "│", "  ", "├", "──", "┘", "  ", "┌", "──", "┤", "  ", "│", " □", "│", "  ", "├", "──", \
            "┤", "  ", "├", "──", "┐", " □", " ",  "  ", "│", "  ", "│", "  ", "│"], \

            ["│"," ."," ","  ","│","  "," ","  ","│","  ","│","  "," "," .","│","  ", \
            "│","  ","│","  ","│","  ","├","──","┐","  ","│","  "," ","  ","│"], \

            ["│", " .", "│", "  ", "└", "──", "─", "  ", " ", "  ", "│", "  ", "│", " .", "│", "  ", "│", "  ", \
            "│", "  ", " ", "  ", "│", "  ", "│", "  ", " ", "  ", "│", "  ", "│"], \

            ["│"," □","│","  "," ","  "," ","  ","│","  "," ","  ","│"," .","│","  ", \
            " ","  ","│","  ","│","  ","│","  "," ","  ","│","  ","│","  "," "], \
                
            ["└","──","┴","──","─","──","─","──","┴","──","─","──","┴","──","┴","──", \
            "─","──","┴","──","┴","──","┴","──","─","──","┴","──","┴","──","┘"]
            ]
            
            #This took way too long

        while (not dead):
            #prints out entire maze
            
            printMaze(maze, solved)
            if(x == True):
                print("clue: V-E-S")
                x = False
            
            sleep(0.2)

            prevSpace = [0,0]
            #MOVE ENEMIES HERE
            if(cycleFlip == 0):
                enemyCycle += 1
                for i in range(6):
                    #swaps amonug with dot
                    if(maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] == maze[playerPos[0]][playerPos[1]]):
                        maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] = "■□"
                        maze[enemy[i][enemyCycle-1][0]][enemy[i][enemyCycle-1][1]] = " ."
                        panic = 1
                        prevSpace = [enemy[i][enemyCycle-1][0],enemy[i][enemyCycle-1][1]]
                    else:
                        # (this is necessary, but only because the programmer is dumb)
                        # the programmer thinks the above comment is valid
                        temp = maze[enemy[i][enemyCycle-1][0]][enemy[i][enemyCycle-1][1]]
                        maze[enemy[i][enemyCycle-1][0]][enemy[i][enemyCycle-1][1]] = maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]]
                        maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] = temp
                        
                #flips cycle at end
                if(enemyCycle == 3):
                    cycleFlip = 1
            elif(cycleFlip == 1):
                enemyCycle -= 1
                for i in range(6):
                    #swaps amonug with dot
                    if(maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] == maze[playerPos[0]][playerPos[1]]):
                        maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] = "■□"
                        maze[enemy[i][enemyCycle+1][0]][enemy[i][enemyCycle+1][1]] = " ."
                        panic = 1
                        prevSpace = [enemy[i][enemyCycle+1][0],enemy[i][enemyCycle+1][1]]
                    else:
                        temp = maze[enemy[i][enemyCycle+1][0]][enemy[i][enemyCycle+1][1]]
                        maze[enemy[i][enemyCycle+1][0]][enemy[i][enemyCycle+1][1]] = maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]]
                        maze[enemy[i][enemyCycle][0]][enemy[i][enemyCycle][1]] = temp
                #flips cycle if at end
                if(enemyCycle == 0):
                    cycleFlip = 0
                
            # (Example alternative)
            # prev_step = step
            # step = next(cycle_iter)
            # for i in range(len(enemies)):
            #   enemy = enemies[i]
            #   prev_step_coord = enemy[prev_step]
            #   next_step_coord = enemy[step]
            #   temp = maze[next_step_coord[0]][next_step_coord[1]]
            #   maze[next_step_coord[0]][next_step_coord[1]] = "A"
            #   maze[prev_step_coord[1]][prev_step_coord[1]] = temp
            #
            # show off
            
            event = keyboard.read_event()

            if event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "down":
                        if(playerPos[2]==0):
                            #player moves onto enemy tile
                            if(maze[playerPos[0]+1][playerPos[1]] == " □"):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]+1][playerPos[1]] = "■□"
                                dead = True
                            #player moves onto empty tile
                            if(maze[playerPos[0]+1][playerPos[1]] == "  "):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]+1][playerPos[1]] = "■ "
                            #player moves onto enemy path
                            if(maze[playerPos[0]+1][playerPos[1]] == " ."):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]+1][playerPos[1]] = "■."
                            pass
                        if(playerPos[2]==1):
                            if(panic == 0):
                                #player moves onto enemy tile
                                if(maze[playerPos[0]+1][playerPos[1]] == " □"):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]+1][playerPos[1]] = "■□"
                                    dead = True
                                #player moves onto empty tile
                                if(maze[playerPos[0]+1][playerPos[1]] == "  "):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]+1][playerPos[1]] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]+1][playerPos[1]] == " ."):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]+1][playerPos[1]] = "■."
                                pass
                            if(panic == 1):
                                #player moves onto empty tile
                                if(maze[playerPos[0]+1][playerPos[1]] == "  "):
                                    maze[playerPos[0]][playerPos[1]] = " □"
                                    maze[playerPos[0]+1][playerPos[1]] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]+1][playerPos[1]] == " ."):
                                    if(maze[playerPos[0]+1][playerPos[1]] != maze[prevSpace[0]][prevSpace[1]]):
                                        maze[playerPos[0]][playerPos[1]] = " □"
                                        maze[playerPos[0]+1][playerPos[1]] = "■."
                                    else:
                                        dead = True
                                panic = 0
                                pass
                        if(playerPos[2] == 2):
                                #player move off x tile
                                maze[playerPos[0]][playerPos[1]] = " x"
                                maze[playerPos[0]+1][playerPos[1]] = "■ "
                    case "up":
                        if(playerPos[2]==0):
                            #player moves onto enemy tile
                            if(maze[playerPos[0]-1][playerPos[1]] == " □"):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]-1][playerPos[1]] = "■□"
                                dead = True
                            #player moves onto empty tile
                            if(maze[playerPos[0]-1][playerPos[1]] == "  "):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]-1][playerPos[1]] = "■ "
                            #player moves onto enemy path
                            if(maze[playerPos[0]-1][playerPos[1]] == " ."):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]-1][playerPos[1]] = "■."
                            #player moves onto x tile
                            if(maze[playerPos[0]-1][playerPos[1]] == " x"):
                                maze[playerPos[0]][playerPos[1]] = "  "
                                maze[playerPos[0]-1][playerPos[1]] = "■x"
                                x = True
                            pass
                        if(playerPos[2]==1):
                            if(panic == 0):
                                #player moves onto enemy tile
                                if(maze[playerPos[0]-1][playerPos[1]] == " □"):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]-1][playerPos[1]] = "■□"
                                    dead = True
                                #player moves onto empty tile
                                if(maze[playerPos[0]-1][playerPos[1]] == "  "):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]-1][playerPos[1]] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]-1][playerPos[1]] == " ."):
                                    maze[playerPos[0]][playerPos[1]] = " ."
                                    maze[playerPos[0]-1][playerPos[1]] = "■."
                            if(panic == 1):
                                #player moves onto empty tile
                                if(maze[playerPos[0]-1][playerPos[1]] == "  "):
                                    maze[playerPos[0]][playerPos[1]] = " □"
                                    maze[playerPos[0]-1][playerPos[1]] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]-1][playerPos[1]] == " ."):
                                    if(maze[playerPos[0]-1][playerPos[1]] != maze[prevSpace[0]][prevSpace[1]]):
                                        maze[playerPos[0]][playerPos[1]] = " □"
                                        maze[playerPos[0]-1][playerPos[1]] = "■."
                                    else:
                                        dead = True
                                panic = 0
                            pass
                    case "left":
                        if(playerPos[1] != 1):
                            if(playerPos[2]==0):
                                #player moves onto enemy tile
                                if(maze[playerPos[0]][playerPos[1]-2] == " □" and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]-2] = "■□"
                                    dead = True
                                #player moves onto empty tile
                                if(maze[playerPos[0]][playerPos[1]-2] == "  " and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]-2] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]][playerPos[1]-2] == " ." and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]-2] = "■."
                            if(playerPos[2]==1):
                                if(panic == 0):
                                    #player moves onto enemy tile
                                    if(maze[playerPos[0]][playerPos[1]-2] == " □" and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]-2] = "■□"
                                        dead = True
                                    #player moves onto empty tile
                                    if(maze[playerPos[0]][playerPos[1]-2] == "  " and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]-2] = "■ "
                                    #player moves onto enemy path
                                    if(maze[playerPos[0]][playerPos[1]-2] == " ." and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]-2] = "■."
                                if(panic == 1):
                                    #player moves onto empty tile
                                    if(maze[playerPos[0]][playerPos[1]-2] == "  " and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " □"
                                        maze[playerPos[0]][playerPos[1]-2] = "■ "
                                    #player moves onto enemy path
                                    if(maze[playerPos[0]][playerPos[1]-2] == " ." and maze[playerPos[0]][playerPos[1]-1] != "│"):
                                        if(maze[playerPos[0]][playerPos[1]-2] != maze[prevSpace[0]][prevSpace[1]]):
                                            maze[playerPos[0]][playerPos[1]] = " □"
                                            maze[playerPos[0]][playerPos[1]-2] = "■."
                                        else:
                                            dead = True
                                    panic = 0
                                
                        pass
                    case "right":
                        if(playerPos[1] != 29):
                            if(playerPos[2] == 0):
                                #player moves onto enemy tile
                                if(maze[playerPos[0]][playerPos[1]+2] == " □" and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]+2] = "■□"
                                    dead = True
                                #player moves onto empty tile
                                if(maze[playerPos[0]][playerPos[1]+2] == "  " and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]+2] = "■ "
                                #player moves onto enemy path
                                if(maze[playerPos[0]][playerPos[1]+2] == " ." and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                    maze[playerPos[0]][playerPos[1]] = "  "
                                    maze[playerPos[0]][playerPos[1]+2] = "■."
                            if(playerPos[2] == 1):
                                if(panic == 0):
                                    #player moves onto enemy tile
                                    if(maze[playerPos[0]][playerPos[1]+2] == " □" and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]+2] = "■□"
                                        dead = True
                                    #player moves onto empty tile
                                    if(maze[playerPos[0]][playerPos[1]+2] == "  " and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]+2] = "■ "
                                    #player moves onto enemy path
                                    if(maze[playerPos[0]][playerPos[1]+2] == " ." and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " ."
                                        maze[playerPos[0]][playerPos[1]+2] = "■."
                                if(panic == 1):
                                    #player moves onto empty tile
                                    if(maze[playerPos[0]][playerPos[1]+2] == "  " and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                        maze[playerPos[0]][playerPos[1]] = " □"
                                        maze[playerPos[0]][playerPos[1]+2] = "■ "
                                    #player moves onto enemy path
                                    if(maze[playerPos[0]][playerPos[1]+2] == " ." and maze[playerPos[0]][playerPos[1]+1] != "│"):
                                        if(maze[playerPos[0]][playerPos[1]+2] != maze[prevSpace[0]][prevSpace[1]]):
                                            maze[playerPos[0]][playerPos[1]] = " □"
                                            maze[playerPos[0]][playerPos[1]+2] = "■."
                                        else:
                                            dead = True
                                    panic = 0
                        elif(playerPos[0] == 14):
                            maze[playerPos[0]][playerPos[1]] = "  "
                            #print("WIN")
                            solved = True
                            dead = True

                            #prints out WIN box
                            maze[6][11] = " ┌"
                            maze[6][12] = "─"
                            maze[6][13] = "──"
                            maze[6][14] = "─"
                            maze[6][15] = "──"
                            maze[6][16] = "─"
                            maze[6][17] = "──"
                            maze[6][18] = "─"
                            maze[6][19] = "─┐"

                            maze[7][11] = " │"
                            maze[7][12] = " "
                            maze[7][13] = "!!"
                            maze[7][14] = " "
                            maze[7][15] = "WI"
                            maze[7][16] = "N"
                            maze[7][17] = " !"
                            maze[7][18] = "!"
                            maze[7][19] = " │"

                            maze[8][11] = " └"
                            maze[8][12] = "─"
                            maze[8][13] = "──"
                            maze[8][14] = "─"
                            maze[8][15] = "──"
                            maze[8][16] = "─"
                            maze[8][17] = "──"
                            maze[8][18] = "─"
                            maze[8][19] = "─┘"

                            printMaze(maze, solved)
                        pass
                    case "qesc":
                        dead = True
                        solved = True
            if(maze[playerPos[0]][playerPos[1]] == "■□"):
                dead = True
        
        if(solved):
            # print("WIN")
            clear()
            break

        #ASSIGN GAME OVER ART HERE
        #┌───────────┐
        #│ GAME OVER │11 across
        #└───────────┘6 down

        maze[6][11] = " ┌"
        maze[6][12] = "─"
        maze[6][13] = "──"
        maze[6][14] = "─"
        maze[6][15] = "──"
        maze[6][16] = "─"
        maze[6][17] = "──"
        maze[6][18] = "─"
        maze[6][19] = "┐ "

        maze[7][11] = " │"
        maze[7][12] = "G"
        maze[7][13] = "AM"
        maze[7][14] = "E"
        maze[7][15] = " O"
        maze[7][16] = "V"
        maze[7][17] = "ER"
        maze[7][18] = " "
        maze[7][19] = "│─"

        maze[8][11] = " └"
        maze[8][12] = "─"
        maze[8][13] = "──"
        maze[8][14] = "─"
        maze[8][15] = "──"
        maze[8][16] = "─"
        maze[8][17] = "──"
        maze[8][18] = "─"
        maze[8][19] = "┘ "

        printMaze(maze, solved)
        sleep(2.5)

