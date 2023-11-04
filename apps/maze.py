import keyboard
from utils import *
from time import sleep

global playerPos
playerPos = [0,0]

def printMaze(maze):
    clear()
    for i in range(15):
            for l in range(30):
                print(maze[i][l], end="")
                if (maze[i][l] == "■ "):
                    playerPos[0] = i
                    playerPos[1] = l
            print("")


print("""
┌────────┬─────┬─────┬───────────┬─────┬──┬──┐ 
 ■       │     │     │ .  .  ඞ  .│     │  │  │ 
├─────┐     │    .┌──┤  │  ┌──┐  └───     │  │ 
│     │  │  └──┐ .│  │  ├──┘  │        │     │ 
│  └──┘  │     │ .│  │  │ .  .  ඞ│  ┌──┘  │  │ 
│        ├──┐  │ ඞ   │  │  │  │  │  │     └──┤ 
├──┐  │  │  ├──┘ .│  │     ├──┤  │     │     │ 
│  │  ├──┘  │    .│  │  │  │  │  ├───  ├───  │ 
│  │  │     ├──┬──┤     │  │  │  │ .   │     │ 
│     │  │  │  │  ├───  │     ├──┘ .│     ┌──┤ 
│  ┌──┤  │     │  │ .   │  │  │    ඞ└──┐  │  │ 
│ .│  ├──┘  ┌──┤  │ .│  ├──┤  ├──┐ .   │  │  │ 
│ .   │     │  │    ඞ│  │  │  │  ├──┐  │     │ 
│ .│  └───     │  │ .│  │  │     │  │     │  │ 
│ ඞ│        │     │ .│     │  │  │     │  │    
└──┴────────┴─────┴──┴─────┴──┴──┴─────┴──┴──┘ 

┌───────────┐
│ GAME OVER │
└───────────┘

""")

# ├
# ┬ 
# ┴
# ┤
# ┼
# │
# ──

# https://en.wikipedia.org/wiki/Box-drawing_character

# player: :) ■ 
# bad guy: <> ඞ

maze = []
solved = False
dead = False
enemies = []

while(not solved):

    #HARD CODE MAZE HERE
    maze = [
        ["┌", "──", "─", "──", "─", "──", "┬", "──", "─", "──", "┬", "──", \
        "─", "──", "┬", "──", "─", "──", "─", "──", "─", "──", "┬", "──", "─", "──", \
        "┬", "──", "┬", "──", "┐"],\

        [" ", "■ ", " ", "  ", " ", "  ", "│", "  ", \
        " ", "  ", "│", "  ", " ", "  ", "│", " .", " ", " .", " ", " ඞ", " ", " .", \
        "│", "  ", " ", "  ", "│", "  ", "│", "  ", "│" ] ,\

        ["├", "──", "─", "──", "┐", \
        "  ", " ", "  ", "│", "  ", " ", " .", "┌", "──", "┤", "  ", "│", "  ", \
        "┌", "──", "┐", "  ", "└", "──", "─", "  ", " ", "  ", "│", "  ", "│"], \

        ["│", "  ", " ", "  ", "│", "  ", "│", "  ", "└", "──", "┐", " .", "│", "  ", "│",\
        "  ", "├", "──", "┘", "  ", "│", "  ", " ", "  ", " ", "  ", "│", "  ", " ","  ", "│"], \

        ["│","  ","└","──","┘","  ","│","  ","  ","│"," .","│","  ","│","  ","│"," ."," "," .",\
        " "," ඞ","│","  ","┌","──","┘","  ","│","  ","│"], \

        ["│", "  ", " ", "  ", " ", "  ", "├", "──", "┐", "  ", "│", " ඞ", " ", "  ", "│", "  ",\
         "│", "  ", "│", "  ", "│", "  ", "│", "  ", "│", "  ", " ", "  ", "└", "──", "┤"] ,\

        ["├","──","┐","  ","│","  ","│","  ","├","──","┘"," .","│","  ","│","  "," ","  ","├",\
        "──","┤","  ","│","  "," ","  ","│","  "," ","  ","│"], \

        ["│", "  ", "│", "  ", "├", "──", "┘", "  ", "│", "  ", " .", "│", "  ", "│", "  ", "│", \
         "  ", "│", "  ", "│", "  ", "├", "──", "─", "  ", "├", "──", "─", "  ", "│"], \

        ["│","  ","│","  ","│","  "," ","  ","├","──","┬","──","┤","  "," ","  ","│", \
        "  ","│","  ","│","  ","│"," ."," ","  ","│","  "," ","  ","│"], \

        ["│", "  ", " ", "  ", "│", "  ", "│", "  ", "│", "  ", "│", "  ", "├", "──", "─", "  ", "│", \
        "  ", " ", "  ", "├", "──", "┘", " .", "│", "  ", " ", "  ", "┌", "──", "┤"], \

        ["│","  ","┌","──","┤","  ","│","  "," ","  ","│","  ","│"," ."," ","  ", \
        "│","  ","│","  ","│","  "," "," ඞ","└","──","┐","  ","│","  ","│"], \

        ["│", " .│", "  ", "├", "──", "┘", "  ", "┌", "──", "┤", "  ", "│", " .", "│", "  ", "├", "──", \
        "┤", "  ", "├", "──", "┐", " .", "  ", " │", "  ", "│", "  ", "│"], \

        ["│"," ."," ","  ","│","  "," ","  ","│","  ","│","  "," "," ඞ","│","  ", \
        "│","  ","│","  ","│","  ","├","──","┐","  ","│","  "," ","  ","│"], \

        ["│", " .", "│", "  ", "└", "──", "─", "  ", " ", "  ", "│", "  ", "│", " .", "│", "  ", "│", "  ", \
        "│", "  ", " ", "  ", "│", "  ", "│", "  ", " ", "  ", "│", "  ", "│"], \

        ["│"," ඞ","│","  "," ","  "," ","  ","│","  "," ","  ","│"," .","│","  ", \
        " ","  ","│","  ","│","  ","│","  "," ","  ","│","  ","│","  "," "], \
            
        ["└","──","┴","──","─","──","─","──","┴","──","─","──","┴","──","┴","──", \
        "─","──","┴","──","┴","──","┴","──","─","──","┴","──","┴","──","┘"]
        ]
        

    while (not dead):
        #prints out entire maze
        
        printMaze(maze)
        
        #MOVE ENEMIES HERE


        event = keyboard.read_event()
        if event.event_type == keyboard.KEY_DOWN:
            match event.name:
                case "down":
                    #player moves onto enemy tile
                    if(maze[playerPos[0]+1, playerPos[1]] == " ඞ"):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]+1, playerPos[1]] == "■ඞ"
                        dead = True
                    #player moves onto empty tile
                    if(maze[playerPos[0]+1, playerPos[1]] == "  "):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]+1, playerPos[1]] == "■ "
                    #player moves onto enemy path
                    if(maze[playerPos[0]+1, playerPos[1]] == " ."):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]+1, playerPos[1]] == "■."
                    pass
                case "up":
                    #player moves onto enemy tile
                    if(maze[playerPos[0]-1, playerPos[1]] == " ඞ"):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]-1, playerPos[1]] == "■ඞ"
                        dead = True
                    #player moves onto empty tile
                    if(maze[playerPos[0]-1, playerPos[1]] == "  "):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]-1, playerPos[1]] == "■ "
                    #player moves onto enemy path
                    if(maze[playerPos[0]-1, playerPos[1]] == " ."):
                        maze[playerPos[0], playerPos[1]] == "  "
                        maze[playerPos[0]-1, playerPos[1]] == "■."
                    pass
                case "left":
                    if(playerPos[1] != 1):
                        #player moves onto enemy tile
                        if(maze[playerPos[0], playerPos[1]-2] == " ඞ" and maze[playerPos[0], playerPos[1]-1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]-2] == "■ඞ"
                            dead = True
                        #player moves onto empty tile
                        if(maze[playerPos[0], playerPos[1]-2] == "  " and maze[playerPos[0], playerPos[1]-1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]-2] == "■ "
                        #player moves onto enemy path
                        if(maze[playerPos[0], playerPos[1]-2] == " ." and maze[playerPos[0], playerPos[1]-1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]-2] == "■."
                    pass
                case "right":
                    if(playerPos[1] != 14):
                        #player moves onto enemy tile
                        if(maze[playerPos[0], playerPos[1]+2] == " ඞ" and maze[playerPos[0], playerPos[1]+1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]+2] == "■ඞ"
                            dead = True
                        #player moves onto empty tile
                        if(maze[playerPos[0], playerPos[1]+2] == "  " and maze[playerPos[0], playerPos[1]+1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]+2] == "■ "
                        #player moves onto enemy path
                        if(maze[playerPos[0], playerPos[1]+2] == " ." and maze[playerPos[0], playerPos[1]+1] != "│"):
                            maze[playerPos[0], playerPos[1]] == "  "
                            maze[playerPos[0], playerPos[1]+2] == "■."
                    pass
        
        if(dead):
            sleep(1)
            #ASSIGN GAME OVER ART HERE
            dead = False
            input()
            break
            

