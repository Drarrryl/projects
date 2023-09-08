import time
from PIL import Image, ImageShow
im = Image.open(r"/workspace/Experiments/Pictures/white.png")
print("What would you like to play?")

games = ["Tic Tac Toe"]
gameList = "Choose a game!\n"
for i in range(len(games)):
    gameList += games[i]
    gameList += "\n"
gameChoice = input(gameList)

if gameChoice == "Tic Tac Toe":
    print("Loading Tic Tac Toe...")
    time.sleep(2)
    ImageShow.show(im)
