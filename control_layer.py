import pygame as pg
bulletSize = 0.05
RedHealth = 10
YellowHealth = 10
ShipSpeed = 0
ShipSpeedSecond = 0.65
bulletSpeed = 0
bulletSpeedSecond = 0.7

keys = {
    "up": False,
    "down": False,
    "left": False,
    "right": False,
    "w": False,
    "s": False,
    "a": False,
    "d": False,
}
def handle_keys(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex):
    for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    keys["up"] = True
                elif event.key == pg.K_DOWN:
                    keys["down"] = True
                elif event.key == pg.K_LEFT:
                    keys["left"] = True
                elif event.key == pg.K_RIGHT:
                    keys["right"] = True
                elif event.key == pg.K_RCTRL:
                    ShootYellow(YellowBulletVertexList,YellowVertex)
                elif event.key == pg.K_w:
                    keys["w"] = True
                elif event.key == pg.K_s:
                    keys["s"] = True
                elif event.key == pg.K_a:
                    keys["a"] = True
                elif event.key == pg.K_d:
                    keys["d"] = True
                elif event.key == pg.K_e:
                    ShootRed(RedBulletVertexList,RedVertex)
            elif event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    keys["up"] = False
                elif event.key == pg.K_DOWN:
                    keys["down"] = False
                elif event.key == pg.K_LEFT:
                    keys["left"] = False
                elif event.key == pg.K_RIGHT:
                    keys["right"] = False
                
                
                elif event.key == pg.K_w:
                    keys["w"] = False
                elif event.key == pg.K_s:
                    keys["s"] = False
                elif event.key == pg.K_a:
                    keys["a"] = False
                elif event.key == pg.K_d:
                    keys["d"] = False


def move(RedVertex, YellowVertex, ShipSpeed):
    if keys["d"] and RedVertex[2][0] <=1:
            for i in RedVertex:
                i[0]+=ShipSpeed
    if keys['a'] and RedVertex[0][0] >=-1:
        for i in RedVertex:
            i[0]-=ShipSpeed
    if keys["w"] and RedVertex[2][1]<=0:
        for i in RedVertex:
            i[1]+=ShipSpeed
    if keys['s'] and RedVertex[0][1] >= -1:
        for i in RedVertex:
            i[1]-=ShipSpeed
    if keys["up"] and YellowVertex[2][1]<=1:
        for i in YellowVertex:
            i[1]+=ShipSpeed
    if keys["down"] and YellowVertex[0][1] >= 0:
        for i in YellowVertex:
            i[1]-=ShipSpeed
    if keys["left"] and YellowVertex[0][0] >=-1:
        for i in YellowVertex:
            i[0]-=ShipSpeed
    if keys["right"] and YellowVertex[2][0] <=1:
        for i in YellowVertex:
            i[0]+=ShipSpeed

def ShootRed(RedBulletVertexList,RedVertex):
    tip = [((RedVertex[1][0] - RedVertex[0][0])/2) + RedVertex[0][0],  RedVertex[2][1]]
    RedBulletVertexList.append([[tip[0] - bulletSize/2,  tip[1]],
                               [tip[0] + bulletSize/2,  tip[1]],
                               [tip[0] + bulletSize/2,  tip[1] + bulletSize],
                               [tip[0] - bulletSize/2, tip[1] + bulletSize]])
def ShootYellow(YellowBulletVertexList,YellowVertex):
    tip = [((YellowVertex[1][0] - YellowVertex[0][0])/2) + YellowVertex[0][0],  YellowVertex[0][1]]
    YellowBulletVertexList.append([[tip[0] - bulletSize/2,  tip[1]],
                               [tip[0] + bulletSize/2,  tip[1]],
                               [tip[0] + bulletSize/2,  tip[1] + bulletSize],
                               [tip[0] - bulletSize/2, tip[1] + bulletSize]])
def collide(bullet,Ship) -> bool:
    if (Ship[0][0] < bullet[0][0] < Ship[1][0]) and (Ship[0][1] < bullet[0][1] < Ship[2][1]):
        return True
    elif (Ship[0][0] < bullet[1][0] < Ship[1][0]) and (Ship[0][1] < bullet[1][1] < Ship[2][1]):
        return True
    elif (Ship[0][0] < bullet[2][0] < Ship[1][0]) and (Ship[0][1] < bullet[2][1] < Ship[2][1]):
        return True
    elif (Ship[0][0] < bullet[3][0] < Ship[1][0]) and (Ship[0][1] < bullet[3][1] < Ship[2][1]):
        return True
    else:
        return False
def bulletOutBounds(bullet) -> bool:
    if bullet[0][1] < -1:
        return True
    elif bullet[2][1] > 1:
        return True
    else:
        return False

def handleBullets(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex,bulletSpeed) :
    for bullet in RedBulletVertexList:
        if (collide(bullet,YellowVertex)):
            global YellowHealth
            YellowHealth -=1
            RedBulletVertexList.remove(bullet)
        elif (bulletOutBounds(bullet)):
            RedBulletVertexList.remove(bullet)
        else:
            
            bullet[0][1] += bulletSpeed
            bullet[1][1] += bulletSpeed
            bullet[2][1] += bulletSpeed
            bullet[3][1] += bulletSpeed
    for bullet in YellowBulletVertexList:
        if (collide(bullet,RedVertex)):
            global RedHealth
            RedHealth -=1
            YellowBulletVertexList.remove(bullet)
        elif (bulletOutBounds(bullet)):
            YellowBulletVertexList.remove(bullet)
        else:
            
            bullet[0][1] -= bulletSpeed
            bullet[1][1] -= bulletSpeed
            bullet[2][1] -= bulletSpeed
            bullet[3][1] -= bulletSpeed 
    return RedHealth, YellowHealth

    
def reset(RedBulletVertexList,RedVertex,YellowBulletVertexList,YellowVertex):
    global RedHealth
    global YellowHealth
    RedHealth = 10
    YellowHealth = 10
    RedBulletVertexList.clear()
    YellowBulletVertexList.clear()
    RedVertex.clear()
    RedVertex.append([-0.3, -0.3])
    RedVertex.append([0.0, -0.3])
    RedVertex.append([0.0, 0.0])
    RedVertex.append([-0.3, 0.0])

    YellowVertex.clear()
    YellowVertex.append([0.0,0.0])
    YellowVertex.append([0.3,0.0])
    YellowVertex.append([0.3,0.3])
    YellowVertex.append([0.0,0.3])

def calculateSpeeds(FPS):
    global ShipSpeed
    global bulletSpeed
    try:
            ShipSpeed = ShipSpeedSecond/FPS
            bulletSpeed = bulletSpeedSecond/FPS
    except:
        pass
    finally:
        return ShipSpeed, bulletSpeed

    