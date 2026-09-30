import random
import pgzrun
import time
import turtle

WIDTH = 400
HEIGHT = 400
TITLE = "YOU HAVE A GUN KILL"
message = "Game shan't be started "
score = 0

alien = Actor("alien")
alien.pos = 50,50
def draw():
    screen.clear()
    screen.fill("midnightblue")
    alien.draw()
    screen.draw.text(message, center = (200,20), fontsize = 30, color = "black")
    

def die():
    alien.x = random.randint(50,300)
    alien.y = random.randint(50,300)

def on_mouse_down(pos):
    global message
    if alien.collidepoint(pos):
        message = "Ok nvm WAR WITHOUT REASON!!!"
        die()
    else:
        
        message = "Well mad skill issue lolol"


pgzrun.go()