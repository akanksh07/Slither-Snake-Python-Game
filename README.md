# Python-based-Slither-Snake-Game
# About:

<p align="justify"> I have tried recreating the classic Snakes-II game using Pygame where the player maneuvers the body which grows lengthwise on ingesting a target (let's say an egg) , with the body itself being the primary obstacle. The pace of the game increases after every fifth point scored and the body of the snake increases by three blocks.The leaderboards of the game are maintained locally using a  SQLite db. </p>

# Gameplay:

![slither](https://user-images.githubusercontent.com/36961513/131455927-2acfd416-398b-472b-96ca-a37a25d2ecd0.gif)

# Steps to generate an executable application.
1. ~/pip install  pyinstaller
2. ~/pyinstaller --onefile -w main.py
3. Place the application file (snakes.exe) from the dist folder along with the other dependancies.
4. Ready to go! 
