import pygame
import time

def stickMovement(stick_x,stick_speed):
    #Funcion para detectar el movimiento del stick , retorna stick_x
    
    keyPressed = pygame.key.get_pressed()
    
    if ((keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]) and stick_x>0):
        print('Flecha izquierda')
        stick_x -= stick_speed
        
    elif ((keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d])and stick_x<screen_width-stick_width):
        print('Flecha derecha')
        stick_x += stick_speed
    return stick_x

def ballStickCollision(ball_y,ball_x,ball_radio,stick_x,stick_width,Point,bally_Speed):
    #Funcion para detectar colision de pelota contra la barra , retorna bally_Speed
    
    if (ball_x+ball_radio >stick_x and ball_x-ball_radio < stick_x+stick_width and ball_y+ball_radio == stick_y-ball_radio):
        #Point+=1
        pygame.display.set_caption('Puntos consecutivos -> '+str(Point))
        #ball_color=(0,255,255)
        bally_Speed *=(-1)
    return bally_Speed

#---------------CFG_VARIABLES--------------
#OLD_screen_width = 640
#OLD_screen_height = 400
screen_width = 1000
screen_height = 700

# 3 formas de definir los colores
#red = pygame.Color('Red')
#cyan = pygame.Color('cyan')
#blue = pygame.Color(0,0,255) # ¿alpha?
#green = (0, 255, 0)
#white = (255,255,255)
#black = (0,0,0)

pygame.init() # Inicializa el entorno de pygame

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pelota y rectangulo David')
# tamaño del rectángulo
stick_width = 120
stick_screen_height = 20

#Atrbibutos Para pelota
ball_color=(255,0,0)#color pelota
ball_radio=10#ball_radioio pelota

#Coordenadas pelota
ball_x = screen_width/2
ball_y = screen_height/2
#Puntos
Point=0
#Velocidad y Centro de pelota
ballx_Speed=2
bally_Speed=2
ballCenter=(screen_width/2,screen_height/2)

#Color fondo
screenColor=(25,25,25)

# coordenadas del cuadrado
stick_x = screen_width/2-(stick_width/2)
stick_y = screen_height-stick_screen_height

# stick_speedocidad de movimient
stick_speed = 5
#-----------END_OF---CFG_VARIABLES--------------

running = True

while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
    localizarPelota = (ball_x,ball_y)      
    screen.fill(screenColor)
    
    #Pelota cae
    if(ball_y + ball_radio > screen_height+ball_radio+ball_radio ):
        #Reiniciamos coordenadas y puntos
        stick_x = screen_width/2-(stick_width/2)
        stick_y = screen_height-stick_screen_height
        ball_x = screen_width/2
        ball_y = screen_height/2
        Point=0
        pygame.display.set_caption("! OH NO LA PELOTA HA CAIDO !")
        
        #Redibujamos todo a la posicion inicio
        #dibujamos pelota
        pygame.draw.circle(screen,ball_color,ballCenter,ball_radio)
        #dibujamos el rectángulo
        pygame.draw.rect(screen, (255, 0, 0), (stick_x, stick_y, stick_width, stick_screen_height))
        
        #Actualizamos pantalla
        pygame.display.flip()
        
        #Espera 4 sec
        time.sleep(2)
        pygame.display.set_caption('Puntos consecutivos -> '+str(Point))

    #dibujamos pelota
    pygame.draw.circle(screen,ball_color,localizarPelota,ball_radio)
    #dibujamos el rectángulo
    pygame.draw.rect(screen, (255, 0, 0), (stick_x, stick_y, stick_width, stick_screen_height))
    
    #Posiciones a mover de pelota
    ball_x +=ballx_Speed
    ball_y +=bally_Speed
  
    #Colision con rectangulo
   
    bally_Speed=ballStickCollision(ball_y,ball_x,ball_radio,stick_x,stick_width,Point,bally_Speed) 
        
    #Colision con paredes X Pelota
    if (ball_x + ball_radio >= screen_width or ball_x - ball_radio <= 0):
        ball_color=(255,0,0)
        ballx_Speed *=(-1)
        
 
    #Colision con paredes Y Pelota   
    if (ball_y - ball_radio <= 0):
        ball_color=(255,0,0)
        bally_Speed *=(-1)
        
    
        
    #Controlamos teclas pulsadas
    keyPressed = pygame.key.get_pressed()
    if keyPressed[pygame.K_q]: # salimos con la tecla q
        running = False
    #Actualizamos la coordenada del stick ->stick_x con el resultado de la funcion stickMovement
    stick_x=stickMovement(stick_x,stick_speed)  
    
    pygame.time.delay(5)
    pygame.display.flip() # actualizamos la pantalla
    
pygame.quit()
