import pygame
import time
import random
from pygame import mixer

#------------FUNCTIONS-START---------------
def randomMovementBallStartX(bally_Speed):
    randomizer = 1
    randomizer = random.randint(0, 1)
    bally_Speed=(-2)
    
    if (randomizer == 1):
        randomizer = (-2)
    else:
        randomizer = 2
    return randomizer,bally_Speed
    
    
def stickMovement(stick_x,stick_speed):
    #Funcion para detectar el movimiento del stick , retorna stick_x
    #Recibe todos los parametros de CFG necesarios.
    
    keyPressed = pygame.key.get_pressed()
    
    if ((keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]) and stick_x>0):
        print('Flecha izquierda')
        stick_x -= stick_speed
        
    elif ((keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d])and stick_x<screen_width-stick_width):
        print('Flecha derecha')
        stick_x += stick_speed
        
    return stick_x


def ballStickCollision(ballx_Speed,ball_y,ball_x,ball_radio,stick_x,stick_width,Point,bally_Speed,ball_color,stick_height):
    #Funcion para detectar colision de pelota contra la barra , retorna bally_Speed
    #Recibe todos los parametros de CFG necesarios.
    
    #if (ball_x+ball_radio >stick_x and ball_x-ball_radio < stick_x+stick_width and ball_y+ball_radio == stick_y):
        #Version navegador
    if (ball_x+ball_radio >stick_x and ball_x-ball_radio < stick_x+stick_width and ball_y+ball_radio >= stick_y and ball_y+ball_radio <= stick_y+stick_height ):
        Point+=1
        pygame.display.set_caption('Botes en barra consecutivos ->'+str(Point))
        ball_color=(0,255,255)
        bally_Speed *=(-1)
        
    if ((ball_x+ball_radio >= stick_x and ball_x-ball_radio <= stick_x+stick_width ) and ball_y+ball_radio <= stick_y+stick_height and ball_y-ball_radio >= stick_y):
        ballx_Speed *=(-1)
        ball_color=(0,255,0)
        
    return ball_color,ballx_Speed,bally_Speed,Point,ball_color


def wallBallCollision(ball_x,ball_radio,screen_width,ballx_Speed,ball_y,bally_Speed,ball_color):
    if (ball_x + ball_radio >= screen_width or ball_x - ball_radio <= 0):
        ballx_Speed *=(-1)
        ball_color=(255,255,0)
        
    if (ball_y - ball_radio <= 0):
        bally_Speed *=(-1)
        ball_color=(255,255,0)
        
    return ballx_Speed,bally_Speed,ball_color


def resetLocations(ball_x,ball_y,ball_radio,screen_height,stick_x,Point,ballx_Speed,bally_Speed):
    if(ball_y + ball_radio > screen_height+ball_radio+ball_radio ):
        #Reiniciamos coordenadas y puntos
        stick_x = screen_width/2-(stick_width/2)
        ball_x = screen_width/2
        ball_y = screen_height/2
        Point=0

        pygame.display.set_caption("! OH NO LA PELOTA HA CAIDO !")

        #aletoriedad del movimiento X de la pelota
        ballx_Speed,bally_Speed=randomMovementBallStartX(bally_Speed)
        #Redibujamos todo a la posicion inicio
        #dibujamos pelota
        pygame.draw.circle(screen,ball_color,ballCenter,ball_radio)
        #dibujamos el rectángulo
        pygame.draw.rect(screen, (255, 0, 0), (stick_x, stick_y, stick_width, stick_height))
        
        #Actualizamos pantalla
        pygame.display.flip()
        
        #Espera 1 sec
        #time.sleep(1)
        
    return stick_x,stick_y,ball_x,ball_y,Point,ballx_Speed,bally_Speed


def resetGame(score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_x,ball_y,ball_radio,lifes,winnerValue,arrayOfBlocks,arrayOfBlocksReset):
    lifes=3
    winnerValue=0
    arrayOfBlocks=arrayOfBlocksReset
    arrayOfBlocksReset=arrayOfBlocks.copy()
    ball_radio=8
    ball_x = (screen_width/2)
    ball_y = (screen_height/2)+150
    bally_Speed = -2
    ballx_Speed = 2
    stick_width = 120
    mulyiplier=25
    score=0
    #Espera 1 sec
    time.sleep(2)
    
    return score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_x,ball_y,ball_radio,lifes,winnerValue,arrayOfBlocks,arrayOfBlocksReset


def arrayOfBlocksFill(arrayOfBlocks,block_total,block_y,block_x):
    while (block_total>0):
        #arrayOfBlocks.append(pygame.draw.rect(screen, (255, 0, 0),(10+y, 10, 20, 5)))
        if (block_total<=40 and block_total%10==0):
            block_y+=40
            block_x=10
        arrayOfBlocks.append((block_x,block_y,block_width,block_height))
        block_total-=1
        block_x+=100
    arrayLongitud=len(arrayOfBlocks)
    i=0
    
    return arrayOfBlocks,arrayLongitud,block_x,block_y


def isLostLife(lifes):
    if(ball_y + ball_radio > screen_height+ball_radio+ball_radio ):
        lifes-=1
    if(lifes<=0):
        lifes=0
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS', 30)
    lifesText=font.render("Vidas: "+str(lifes),True,(255,255,255))
    lifesRect=lifesText.get_rect()
    lifesRect.center=(screen_width-100,screen_height-30)
    
    return lifes,lifesText,lifesRect

def playerScore(score):
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS', 30)
    scoreText=font.render("Score: "+str(score),True,(255,255,255))
    scoreRect=scoreText.get_rect()
    scoreRect.center=(100,screen_height-30)
    
    return score,scoreText,scoreRect

def scoreMultiplier(arrayOfBlocks):
    multiplier=25
    
    if (arrayOfBlocks[39][0]==999999):
        multiplier+=100
    if (arrayOfBlocks[30][0]==999999):
        multiplier+=80
    if (arrayOfBlocks[27][0]==999999):
        multiplier-=30
    if (arrayOfBlocks[22][0]==999999):
        multiplier+=45
        
    return multiplier
    
def isWinner(winner):
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS', 30)
    winnerText=font.render(winner,True,(255,255,255))
    winnerRect=winnerText.get_rect()
    winnerRect.center=(screen_width/2,screen_height/2)
    
    return winner,winnerText,winnerRect

def pressUKey(pressU):
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS', 30)
    pressUText=font.render(pressU,True,(255,255,255))
    pressURect=pressUText.get_rect()
    pressURect.center=(screen_width/2,screen_height/2+33)
    
    return pressU,pressUText,pressURect


def isLosser(losser):
    pygame.font.init()
    font=pygame.font.SysFont('Comic Sans MS', 30)
    losserText=font.render(losser,True,(255,255,255))
    losserRect=losserText.get_rect()
    losserRect.center=(screen_width/2,screen_height/2)
    
    return losser,losserText,losserRect


def isCollisionWithBlock(score,multiplier,stick_width,bally_Speed,ball_radio,i,lifes,winnerValue,arrayOfBlocks,localizarPelota,block_width,block_height,ballx_Speed,ball_color):
    if (lifes>0 and winnerValue==0 and(arrayOfBlocks[i][0] < localizarPelota[0] < arrayOfBlocks[i][0] + block_width) and (arrayOfBlocks[i][1] < localizarPelota[1] < arrayOfBlocks[i][1] + block_height)):
        print("Tocado un bloque en la coordena ",arrayOfBlocks[i]," bloque numero ",str(i))
        arrayOfBlocks[i]=(999999,999999,999999,999999)
        ballx_Speed *=(-1)
        ball_color=(0,0,255)
        score+=multiplier
        
        #Bloques especiales , pelota grande , pelota peque , barra peque , x2 velocidad pelota
        if(i==22):
            ball_radio=4#pelota peque
        if(i==27):
            ball_radio=16#pelota grande
        if(i==30):
            stick_width=70#barra peque
        if(i==39):
            bally_Speed*=2 #x2 velocidad pelota x
            ballx_Speed*=2 #x2 velocidad pelota y
        
    return score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_radio,i,lifes,winnerValue,arrayOfBlocks,localizarPelota,block_width,block_height,ballx_Speed,ball_color


def wonTheGame(arrayOfBlocks,cont,winner,winnerValue):
    if (arrayOfBlocks[i][0]==999999):
        cont+=1
        if(cont==50):
            winner,winnerText,winnerRect=isWinner(winner)
            winnerValue=1
            screen.blit(winnerText,winnerRect)
    return arrayOfBlocks,cont,winner,winnerValue


def printArrayOfBlocks(i,arrayOfBlocks,block_color,screen):
    block_ballSmall=22
    block_ballBig=27
    block_smallStick=30
    block_superSeepdBall=39
    
    if (i<20):
        block_color=(0, 120, 255)
    elif (i>39):
        block_color=(0, 255, 255)
    else:
        block_color=(0, 170, 185)
        
    #Imprime bloque especial pelota peque   
    if(i==block_ballSmall):
        block_color=(255,0,0)
        
    #Imprime bloque especial pelota grande 
    if(i==block_ballBig):
        block_color=(0,255,0)
        
    #Imprime bloque especial barra peque
    if(i==block_smallStick):
        block_color=(255,255,0)
        
    #Imprime bloque especial velocidad pelota x2
    if(i==block_superSeepdBall):
        block_color=(233,153,234)
        
    pygame.draw.rect(screen, block_color,(arrayOfBlocks[i]))
    
    return i,arrayOfBlocks,block_color,screen
        

#------------FUNCTIONS-END-----------------------------


#---------------CFG_VARIABLES--------------------------
#Sonido
#Instanciar mixer
mixer.init()

#Sonido de fondo
mixer.music.load('playing.mp3')
mixer.music.play(-1)


#OLD_screen_width = 640
#OLD_screen_height = 400
screen_width = 1000
screen_height = 700

#fondo imagen
bg_img = pygame.image.load('fondo4.jpg')
bg_img = pygame.transform.scale(bg_img,(screen_width,screen_height))

# 3 formas de definir los colores
#red = pygame.Color('Red')
#cyan = pygame.Color('cyan')
#blue = pygame.Color(0,0,255) # ¿alpha?
#green = (0, 255, 0)
#white = (255,255,255)
#black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('ARKADNOID POR DAVID')
# tamaño del rectángulo
stick_width = 120
stick_height = 20

#Atrbibutos Para pelota
ball_color=(255,255,0)#color pelota
ball_radio=8#radio de pelota 28 , super pelota , 4 mini pelota , 10 normal

#Coordenadas pelota
ball_x = screen_width/2
ball_y = screen_height/2

#Puntos / botes consecutivos
Point=0

#Velocidad y Centro de pelota
bally_Speed=-2
ballx_Speed,bally_Speed=randomMovementBallStartX(bally_Speed)
ballCenter=(screen_width/2,screen_height/2)

#textos
lifes=3
winner="!HAS GANADO LA PARTIDA!"
losser="!OH NO! HAS PERDIDO , NO TE QUEDAN VIDAS"
pressU="Presiona la tecla [U] para reiniciar la partida!"
score=0

#Gannador inicializado a 0
winnerValue=0

#Color fondo
screenColor=(25,25,25)

# coordenadas del cuadrado
stick_x = screen_width/2-(stick_width/2)
stick_y = screen_height-(stick_height*3)

#Velocidad de movimiento de barra
stick_speed = 4

#CFG-Bloques
block_color=(0, 240, 255)
block_total=50
block_x=10
block_y=10
block_width=70
block_height=20
arrayOfBlocks=[]

#Rellerar array de bloques
arrayOfBlocks,arrayLongitud,block_x,block_y=arrayOfBlocksFill(arrayOfBlocks,block_total,block_y,block_x)

#Crear copy adel array completo para restaurar al estado inicial
arrayOfBlocksReset=arrayOfBlocks.copy()

multiplier=scoreMultiplier(arrayOfBlocks)
    
#-----------END_OF---CFG_VARIABLES----------------------


#-----------GAME-WHILE-START----------------------------q
running = True

while running:
    multiplier=scoreMultiplier(arrayOfBlocks)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    localizarPelota = (ball_x,ball_y)
    screen.fill(screenColor)
    screen.blit(bg_img,(0,0))
    
    score,scoreText,scoreRect=playerScore(score)
    screen.blit(scoreText,scoreRect)
    #Control de pelota al caer , reseteamos todo
    stick_x,stick_y,ball_x,ball_y,Point,ballx_Speed,bally_Speed=resetLocations(ball_x,ball_y,ball_radio,screen_height,stick_x,Point,ballx_Speed,bally_Speed)
    #dibujamos pelota
    pygame.draw.circle(screen,ball_color,localizarPelota,ball_radio)
    #dibujamos el rectángulo
    pygame.draw.rect(screen, (255, 0, 0),(stick_x, stick_y, stick_width, stick_height))
    
    
    #---------BLOCKS-START-----------
    #Este while recorre el array de bloques
    i=0
    cont=0
    while i<len(arrayOfBlocks):
        #Imprime array de bloques
        i,arrayOfBlocks,block_color,screen=printArrayOfBlocks(i,arrayOfBlocks,block_color,screen)
        
        #Comprueba colision con bloque
        score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_radio,i,lifes,winnerValue,arrayOfBlocks,localizarPelota,block_width,block_height,ballx_Speed,ball_color=isCollisionWithBlock(score,multiplier,stick_width,bally_Speed,ball_radio,i,lifes,winnerValue,arrayOfBlocks,localizarPelota,block_width,block_height,ballx_Speed,ball_color)
        
        #Comprueba si ya no existen bloques para que el jugador gane
        arrayOfBlocks,cont,winner,winnerValue=wonTheGame(arrayOfBlocks,cont,winner,winnerValue)

        #Iterador i del bucle while
        i+=1
    #---------BLOCKS-END-------------   

    #TEST
    
    
    #Posiciones a mover de pelota
    ball_x +=ballx_Speed
    ball_y +=bally_Speed
  
    #Colision con rectangulo
    ball_color,ballx_Speed,bally_Speed,Point,ball_color=ballStickCollision(ballx_Speed,ball_y,ball_x,ball_radio,stick_x,stick_width,Point,bally_Speed,ball_color,stick_height) 
 
    #Colision con paredes de Pelota
    ballx_Speed,bally_Speed,ball_color=wallBallCollision(ball_x,ball_radio,screen_width,ballx_Speed,ball_y,bally_Speed,ball_color)
   
    #Controlamos teclas pulsadas
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_q]: # salimos con la tecla q
        running = False
    if keyPressed[pygame.K_u] and (lifes <=0 or winnerValue==1): # Reset Partida
        stick_x,stick_y,ball_x,ball_y,Point,ballx_Speed,bally_Speed=resetLocations(ball_x,ball_y,ball_radio,screen_height,stick_x,Point,ballx_Speed,bally_Speed)
        score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_x,ball_y,ball_radio,lifes,winnerValue,arrayOfBlocks,arrayOfBlocksReset=resetGame(score,multiplier,stick_width,bally_Speed,ballx_Speed,ball_x,ball_y,ball_radio,lifes,winnerValue,arrayOfBlocks,arrayOfBlocksReset)
        
       
    #Impresion de vidas
    if(winnerValue==0):
        lifes,lifesText,lifesRect=isLostLife(lifes)
        screen.blit(lifesText,lifesRect)
        
    #Impresion de perder
    if (lifes<=0 and winnerValue==0):
        losser,losserText,losserRect=isLosser(losser)
        screen.blit(losserText,losserRect)
        pressU,pressUText,pressURect=pressUKey(pressU)
        screen.blit(pressUText,pressURect)
        
    if(winnerValue==1):
        pressU,pressUText,pressURect=pressUKey(pressU)
        screen.blit(pressUText,pressURect)
        #winnerSound = mixer.Sound('victory.mp3')
        #winnerSound.play(-1)
    
    #Actualizamos la coordenada del stick ->stick_x con el resultado de la funcion stickMovement
    stick_x=stickMovement(stick_x,stick_speed)  
    
    pygame.time.delay(5)#Delay para fluidez en saltos
    pygame.display.flip() # actualizamos la pantalla

pygame.quit()
#-----------GAME-WHILE-END---------------------------