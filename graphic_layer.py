from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from OpenGL.GLUT.fonts import *
from PIL import Image
import sys

RedVertex = [[-0.3, -0.3],
             [0.0, -0.3],
             [0.0, 0.0],
             [-0.3, 0.0]]

YellowVertex = [[0.0,0.0],
                [0.3,0.0],
                [0.3,0.3],
                [0.0,0.3]]

RedBulletVertexList = []
YellowBulletVertexList = []

glutInit(sys.argv)
def drawText(text, x, y):
    glRasterPos2f(x, y)
    for character in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(character))

def load_texture(filename):
    # Load image using Pillow
    image = Image.open(filename)

    # Flip image vertically (OpenGL expects image origin to be at lower-left corner)
    image = image.transpose(Image.FLIP_TOP_BOTTOM)

    # Convert image to RGB format
    image = image.convert('RGBA')

    # Generate texture object and bind it
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)

    # Set texture parameters
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

    # Load texture data
    tex_data = image.tobytes()
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image.width, image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_data)

    return texture


def display(space, redShip, yellowShip, RedHealth,YellowHealth):
    glClear(GL_COLOR_BUFFER_BIT)
    #Enable blending
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

    # Bind texture to a texture unit
    glActiveTexture(GL_TEXTURE0)
    

    # Enable texture mapping
    glEnable(GL_TEXTURE_2D)

    drawBackGround(space)


    drawShips(redShip,yellowShip)


    

    # Disable texture mapping
    glDisable(GL_TEXTURE_2D)

    drawBullets()

    drawText("Red Health: "+str(RedHealth), -0.9,0.9)
    drawText("Yellow Health: "+str(YellowHealth) ,0.6,0.9)
    drawWin(RedHealth, YellowHealth)
        
    
    
def drawBackGround(space):
    #Background
    glBindTexture(GL_TEXTURE_2D, space)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(-1.0, -1.0)
    glTexCoord2f(1.0, 0.0)
    glVertex2f(1.0, -1.0)
    glTexCoord2f(1.0, 1.0)
    glVertex2f(1.0, 1.0)
    glTexCoord2f(0.0, 1.0)
    glVertex2f(-1.0, 1.0)
    glEnd()

def drawShips(redShip,yellowShip):
    #Red Ship
    glBindTexture(GL_TEXTURE_2D, redShip)
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(RedVertex[0][0], RedVertex[0][1])
    glTexCoord2f(1.0, 0.0)
    glVertex2f(RedVertex[1][0], RedVertex[1][1])
    glTexCoord2f(1.0, 1.0)
    glVertex2f(RedVertex[2][0], RedVertex[2][1])
    glTexCoord2f(0.0, 1.0)
    glVertex2f(RedVertex[3][0], RedVertex[3][1])
    glEnd()


    #Yellow Ship
    glBindTexture(GL_TEXTURE_2D, yellowShip)

    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0)
    glVertex2f(YellowVertex[0][0], YellowVertex[0][1])
    glTexCoord2f(1.0, 0.0)
    glVertex2f(YellowVertex[1][0], YellowVertex[1][1])
    glTexCoord2f(1.0, 1.0)
    glVertex2f(YellowVertex[2][0], YellowVertex[2][1])
    glTexCoord2f(0.0, 1.0)
    glVertex2f(YellowVertex[3][0], YellowVertex[3][1])
    glEnd()


def drawBullets():
    #Red Bullets
    if(RedBulletVertexList):
        
        glColor3f(1.0,0.0,0.0)
        for bullet in RedBulletVertexList:
            
            glBegin(GL_QUADS)
            glVertex2f(bullet[0][0], bullet[0][1])
            glVertex2f(bullet[1][0], bullet[1][1])
            glVertex2f(bullet[2][0], bullet[2][1])
            glVertex2f(bullet[3][0], bullet[3][1])
            glEnd()
        glClearColor(1.0,1.0,1.0,1.0)
    #Yellow Bullets
    if(YellowBulletVertexList):
        glColor3f(1.0,1.0,0.0)
        for bullet in YellowBulletVertexList:
            glBegin(GL_QUADS)
            glVertex2f(bullet[0][0], bullet[0][1])
            glVertex2f(bullet[1][0], bullet[1][1])
            glVertex2f(bullet[2][0], bullet[2][1])
            glVertex2f(bullet[3][0], bullet[3][1])
            glEnd()
    glColor3f(1.0,1.0,1.0)

def drawWin(RedHealth, YellowHealth):
    if(RedHealth == 0):
        drawText("Yellow Wins", 0.0, 0.0)
    elif(YellowHealth == 0):
        drawText("Red Wins", 0.0, 0.0)