import pygame as pg
from pygame.locals import *
from graphic_layer import *
from control_layer import *



    
if __name__ == "__main__":

    pg.init()
    pg.display.set_mode((900,600), DOUBLEBUF | OPENGL)
    clock = pg.time.Clock() 
    redShip = load_texture('spaceship_red.png')
    yellowShip = load_texture('spaceship_yellow.png')
    space = load_texture('space.png')
    
    while True:
        RedHealth,YellowHealth = handleBullets(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex,bulletSpeed)
        ShipSpeed, bulletSpeed = calculateSpeeds(clock.get_fps())
        handle_keys(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex)
        
        move(RedVertex, YellowVertex, ShipSpeed)
        
        display(space, redShip, yellowShip,RedHealth,YellowHealth)
        if RedHealth == -1 or YellowHealth == -1:
            pg.time.delay(2000)
            reset(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex)

        pg.display.flip()
        clock.tick()
        
        
        
        