import pygame
import random
import time
#width = 640
#height = 400
width = 1000
height = 700


# 3 formas de definir los colores
red = pygame.Color('Red')

cyan = pygame.Color('cyan')
blue = pygame.Color(0,0,255) # ¿alpha?
green = (0, 255, 0)
white = (255,255,255)
black = (0,0,0)
pygame.init() # Inicializa el entorno de pygame
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pelota y rectangulo David')
# tamaño del rectángulo
rect_width = 120
rect_height = 20

#Atrbibutos Para pelota
ballColor=(255,0,0)#color pelota
rad=10#radio pelota

#Coordenadas pelota
x1 = width/2
y1 = height/2
#Puntos
Point=0
#Randomizador de X e Y de pelota
randomX=random.randint(2,2)
randomY=random.randint(2,2)

#Color fondo
screenColor=(25,25,25)

# coordenadas del cuadrado
x = width/2-(rect_width/2)
y = height-rect_height

# velocidad de movimiento
vel = 5
running = True
inicio= True
while running:
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            
    screen.fill(screenColor)
    
    #Pelota cae
    if(y1 + rad > height+rad+rad ):
        #Reiniciamos coordenadas y puntos
        x = width/2-(rect_width/2)
        y = height-rect_height
        x1 = width/2
        y1 = height/2
        Point=0
        pygame.display.set_caption("! OH NO LA PELOTA HA CAIDO !")
        
        #Redibujamos todo a la posicion inicio
        #dibujamos pelota
        pygame.draw.circle(screen,ballColor,localizarPelota,rad)
        #dibujamos el rectángulo
        pygame.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
        
        #Actualizamos pantalla
        pygame.display.flip()
        
        #Espera 4 sec
        time.sleep(4)
        pygame.display.set_caption('Puntos consecutivos -> '+str(Point))
       
       
    #Esperar 1 sec al inicio  
    if (inicio):  
        time.sleep(1)
        inicio=False
    localizarPelota = (x1,y1)
    

    #dibujamos pelota
    pygame.draw.circle(screen,ballColor,localizarPelota,rad)
    #dibujamos el rectángulo
    pygame.draw.rect(screen, (255, 0, 0), (x, y, rect_width, rect_height))
    
    #Posiciones a mover de pelota
    x1 +=randomX
    y1 +=randomY
  
    #Colision con rectangulo
    if (x1+rad >=x and x1-rad <= x+rect_width and y1+rad == y-rad):
        Point+=1
        pygame.display.set_caption('Puntos consecutivos -> '+str(Point))
        ballColor=(0,255,255)
        randomY *=(-1) 
        #randomX *=(-1)
        
    #Colision con paredes X Pelota
    if (x1 + rad >= width or x1 - rad <= 0):
        ballColor=(255,0,0)
        randomX *=(-1)
        #randomY=random.randint(0,4)
 
    #Colision con paredes Y Pelota   
    if (y1 - rad <= 0):
        ballColor=(255,0,0)
        randomY *=(-1)
        #randomX=random.randint(0,4)
    
        
    
    keyPressed = pygame.key.get_pressed()
        
    if keyPressed[pygame.K_q]: # salimos con la tecla q

        running = False

    elif ((keyPressed[pygame.K_LEFT] or keyPressed[pygame.K_a]) and x>0):
        print('Flecha izquierda')
        x -= vel
        
    elif ((keyPressed[pygame.K_RIGHT] or keyPressed[pygame.K_d])and x<width-rect_width):
        print('Flecha derecha')
        x += vel
        
    #elif keyPressed[pygame.K_UP] or keyPressed[pygame.K_w]:
        #if not y<0:
            #print('Flecha arriba')
            #y -= vel

    #elif keyPressed[pygame.K_DOWN] or keyPressed[pygame.K_s]:
        #if not y>(height-rect_height):
            #print('Flecha abajo')
            #y += vel
   
  
    pygame.time.delay(5)
    pygame.display.flip() # actualizamos la pantalla
    
pygame.quit()
