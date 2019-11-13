#Modulos
import pygame,sys
from pygame.locals import *
from Tkconstants import FALSE
from random import randint

#Inicializacion de pygame
pygame.init()

#Imagenes globales
menu = pygame.image.load("menu/iniciosinbotones.png")
icon_surf = pygame.image.load("icon.png")
botonjugar = pygame.image.load("menu/botonjugar.png")
botonjugar2 = pygame.image.load("menu/botonjugar2.png")
botonsalir = pygame.image.load("menu/botonsalir.png")
botonsalir2 = pygame.image.load("menu/botonsalir2.png")
botonajustes = pygame.image.load("menu/botonajustes.png")
botonajustes2 = pygame.image.load("menu/botonajustes2.png")
clic = pygame.mixer.Sound("sonidos/clic.ogg")
soundDisPlom= pygame.mixer.Sound("sonidos/disparo.ogg")
soundGameover = pygame.mixer.Sound("sonidos/gameover.ogg")
sonidofondo = pygame.mixer.music.load("sonidos/fondo.mp3")
bala = pygame.image.load("nivel1/arma.png")
balaenemigo = pygame.image.load("nivel1/proyectil.png")
reloj = pygame.time.Clock()

#Fuentes de letra
miFuente = pygame.font.Font(None,50)
miFuentepeque = pygame.font.Font(None,25)

#Sonidos y musica
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.25)

class Plomero(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('personajes/plomero/plomero.png')
        self.sheet.set_clip(pygame.Rect(215, 0, 50, 159))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.izquierda={}
        self.derecha={}
        self.i=1
        self.cont=4
        self.p=6

        self.direccion=True
        self.salto=False
        self.saltoPar=False
        self.bajadaPar=False
        self.bajada=False

        self.izquierda[0] = ( 40, 160, 90, 159)
        self.izquierda[1] = (200, 160, 90, 159)
        self.izquierda[2] = (360, 160, 90, 159)
        self.izquierda[3] = (200, 160, 90, 159)

        self.derecha[0] = (40,  0, 90, 159)
        self.derecha[1] = (200, 0, 90, 159)
        self.derecha[2] = (360, 0, 90, 159)
        self.derecha[3] = (200, 0, 90, 159)
    def eventos(self):
        teclado=pygame.key.get_pressed()
        if teclado[K_SPACE] and teclado[K_RIGHT] and self.saltoPar==False and self.salto==False:
            self.saltoPar=True
        elif teclado[K_SPACE] and teclado[K_LEFT] and self.saltoPar==False and self.salto==False:
            self.saltoPar=True
        elif teclado[K_RIGHT] and self.salto==False and self.saltoPar==False:
            self.direccion=True
            self.rect.x+=5
            self.cont+=0.5
            if self.cont==self.p:
                self.i=0
            if self.cont==self.p*2:
                self.i=1
            if self.cont==self.p*3:
                self.i=2
            if self.cont==self.p*4:
                self.i=3
                self.cont=0
        elif teclado[K_LEFT] and self.salto==False and self.saltoPar==False:
            self.direccion=False
            self.rect.x-=5
            self.cont+=0.5
            if self.cont==self.p:
                self.i=0
            if self.cont==self.p*2:
                self.i=1
            if self.cont==self.p*3:
                self.i=2
            if self.cont==self.p*4:
                self.i=3
                self.cont=0
        elif teclado[K_SPACE] and self.salto==False and self.saltoPar==False:
            self.salto=True

        else:
            self.i=1
        self.saltando()
        self.saltoparabolico()

    def saltando(self):
        if self.salto==True and self.saltoPar==False:
            self.i=0
            if self.bajada==False:
                self.rect.y-=15
            if self.bajada==True:
                self.rect.y+=15
            if self.rect.y==300:
                self.bajada=True
            if self.rect.y==450:
                self.bajada=False
                self.salto=False 
                self.i=1

    def saltoparabolico(self):
        if self.saltoPar==True and self.salto==False and self.direccion==True:
            self.i=0
            if self.bajadaPar==False:
                self.rect.y-=15
                self.rect.x+=10
            if self.bajadaPar==True:
                self.rect.y+=15
                self.rect.x+=10
            if self.rect.y==300:
                self.bajadaPar=True
            if self.rect.y==450:
                self.bajadaPar=False
                self.saltoPar=False
                self.i=1
        if self.saltoPar==True and self.salto==False and self.direccion==False:
            self.i=0
            if self.bajadaPar==False:
                self.rect.y-=15
                self.rect.x-=10
            if self.bajadaPar==True:
                self.rect.y+=15
                self.rect.x-=10
            if self.rect.y==300:
                self.bajadaPar=True
            if self.rect.y==450:
                self.bajadaPar=False
                self.saltoPar=False
                self.i=1
    def update(self,screen):
        if self.direccion==True:
            screen.blit(self.sheet, (self.rect.x, self.rect.y),(self.derecha[self.i]))
        if self.direccion==False:
            screen.blit(self.sheet, (self.rect.x, self.rect.y),(self.izquierda[self.i]))

class enemigo(pygame.sprite.Sprite):
	def __init__(self,posx,posy):
		pygame.sprite.Sprite.__init__(self)

		self.imagen = pygame.image.load('nivel1/Enemigo1.png')
		self.rect = self.imagen.get_rect()

		self.listaDisparo = []
		self.velocidad = 20
		self.rect.top = posy
		self.rect.left = posx

		self.arriba = True
		self.veloz = 3

	def dibujar (self,screen):
		if self.arriba == True:
			self.rect.top = self.rect.top - self.veloz
			if self.rect.top < 150:
				self.arriba = False
		else:
			self.rect.top = self.rect.top + self.veloz
			if self.rect.top > 450:
				self.arriba = True
		screen.blit(self.imagen, self.rect)

class Proyectil(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bala
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y


    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x += 10
        screen.blit(self.image,self.rect)

class Proyectilenemigo(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = balaenemigo
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y+100


    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x -=5
        self.rect.y +=2
        screen.blit(self.image,self.rect)

class Boton(pygame.sprite.Sprite):
    def __init__(self,botonjugar,botonjugar2,x=360,y=300):
        self.imagen_normal=botonjugar
        self.imagen_seleccion=botonjugar2
        self.imagen_actual=self.imagen_normal
        self.rect=self.imagen_actual.get_rect()
        self.rect.left,self.rect.top=(x,y)

    def update(self,screen,cursor):
        if cursor.colliderect(self.rect):
            self.imagen_actual=self.imagen_seleccion
        else: self.imagen_actual=self.imagen_normal

        screen.blit(self.imagen_actual,self.rect)

class cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left,self.top=pygame.mouse.get_pos()

def main():
    pygame.init()
    pygame.mixer.music.set_volume(.25)
    pygame.display.set_caption("Plumber Jumper")
    screen = pygame.display.set_mode((1080,720)) 
    pygame.display.set_icon(icon_surf)
    cursor1=cursor()

    boton1=Boton(botonjugar,botonjugar2,360,300)
    boton2=Boton(botonsalir,botonsalir2,360,450)
    boton3=Boton(botonajustes,botonajustes2,50,570)

    #LOOP PRINCIPAL
    while True:
        screen.blit(menu,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    Menujugar()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pygame.quit()
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    Ajustes()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        cursor1.update()
        #movement = pygame.mouse.get_pos()
        #print (movement)
        print (event)
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        pygame.display.update()
        reloj.tick(30)        

def Ajustes():
    pygame.init()

    fondo=pygame.image.load("menuopciones/menuopciones.png")
    botonregresar = pygame.image.load("menujugar/botonregresar.png")
    botonregresar2 = pygame.image.load("menujugar/botonregresar2.png")
    espanol=pygame.image.load("menuopciones/espanol.png")
    espanol2=pygame.image.load("menuopciones/espanol2.png")
    ingles=pygame.image.load("menuopciones/ingles.png")
    ingles2=pygame.image.load("menuopciones/ingles2.png")
    sonidosi=pygame.image.load("menuopciones/sonidosi.png")
    sonidosi2=pygame.image.load("menuopciones/sonidosi2.png")
    sonidono=pygame.image.load("menuopciones/sonidono.png")
    sonidono2=pygame.image.load("menuopciones/sonidono2.png")

    pygame.display.set_caption("Ajustes")
    screen = pygame.display.set_mode((1080,720))
    reloj=pygame.time.Clock()
    cursor1=cursor()
    
    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(espanol,espanol2,430,240)
    boton3=Boton(ingles,ingles2,600,240)
    boton4=Boton(sonidosi,sonidosi2,430,380)
    boton5=Boton(sonidono,sonidono2,600,380)
    boton6=Boton(sonidosi,sonidosi2,430,525)
    boton7=Boton(sonidono,sonidono2,600,525)

    while True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton5.rect):
                    clic.play()
                    clic.set_volume(0)
                    soundDisPlom.set_volume(0)
                if cursor1.colliderect(boton4.rect):
                    clic.play()
                    clic.set_volume(1)
                    soundDisPlom.set_volume(1)
                if cursor1.colliderect(boton6.rect):
                    clic.play()
                    pygame.mixer.music.set_volume(.25)
                if cursor1.colliderect(boton7.rect):
                    clic.play()
                    pygame.mixer.music.set_volume(0)
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
                
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)
        boton5.update(screen,cursor1)
        boton6.update(screen,cursor1)
        boton7.update(screen,cursor1)

        cursor1.update()
        print (event)
        reloj.tick(30)        
        pygame.display.update()

def Menujugar():
    
    menujugar = pygame.image.load("menujugar/menujugar.png")
    botonregresar = pygame.image.load("menujugar/botonregresar.png")
    botonregresar2 = pygame.image.load("menujugar/botonregresar2.png")
    miniaturalvl1 = pygame.image.load("menujugar/miniaturalvl1.png")
    miniaturalvl12 = pygame.image.load("menujugar/miniaturalvl1_2.png")
    miniaturalvl2 = pygame.image.load("menujugar/miniaturalvl2.png")
    miniaturalvl22 = pygame.image.load("menujugar/miniaturalvl2_2.png")
    miniaturalvl3 = pygame.image.load("menujugar/miniaturalvl3.png")
    miniaturalvl32 = pygame.image.load("menujugar/miniaturalvl3_2.png")

    cursor1=cursor()

    pygame.init()
    pygame.display.set_caption("Plumber Jumper")
    screen=pygame.display.set_mode((1080,720))

    boton1=Boton(botonregresar,botonregresar2,50,590)
    boton2=Boton(miniaturalvl1,miniaturalvl12,25,220)
    boton3=Boton(miniaturalvl2,miniaturalvl22,378,220)
    boton4=Boton(miniaturalvl3,miniaturalvl32,730,220)

    reloj=pygame.time.Clock()


    while True:
        screen.blit(menujugar,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    nivel1()

            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        boton4.update(screen,cursor1)

        print (event)
        reloj.tick(20)
        cursor1.update()
        pygame.display.update()

def pausa():
    pausado = True
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("nivel1/nivel1.png")
    
    fondopausa = pygame.image.load("pausa/fondopausa.png")
    botoninicio = pygame.image.load("pausa/botoninicio.png")
    botoninicio2 = pygame.image.load("pausa/botoninicio2.png")
    botonplay = pygame.image.load("pausa/botonplay.png")
    botonplay2 = pygame.image.load("pausa/botonplay2.png")
    botonsalir = pygame.image.load("pausa/botonsalir.png")
    botonsalir2 = pygame.image.load("pausa/botonsalir2.png")
    
    #BOTONES DE MENU PAUSA
    boton1=Boton(botoninicio,botoninicio2,350,290)
    boton2=Boton(botonplay,botonplay2,500,290)
    boton3=Boton(botonsalir,botonsalir2,650,290)

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    while pausado:
        screen.blit(fondo,(0,0))
        screen.blit(fondopausa,(300,250))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausado = False
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    main()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pausado = False
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    pygame.quit()
                    sys.exit(0)
       
        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        reloj1.tick(30)
        cursor1.update()
        pygame.display.update()

def perdiste(enjuego):
    enjuego=False
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("perdiste/perdistelvl1.png")

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    soundGameover.play()
    youlose=True
    while youlose==True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    nivel1()
                if event.key == pygame.K_ESCAPE:
                    main()

        reloj1.tick(30)
        cursor1.update()
        pygame.display.update()

def nivel1():

    pygame.init()

    fondo = pygame.image.load("nivel1/nivel1.png")
    barravidapersonaje = pygame.image.load("nivel1/barravidapersonaje.png")     
    barraagua = pygame.image.load("nivel1/barraporcentajeagua.png")
    barratubos = pygame.image.load("nivel1/barratubos.png")
    barraenemigo = pygame.image.load("nivel1/barravidaenemigo.png")
    llavedeagua = pygame.image.load("nivel1/llavedeagua.png") 
    botonpausa = pygame.image.load("pausa/botonpausa.png")
    botonpausa2 = pygame.image.load("pausa/botonpausa2.png")

    agua100=pygame.image.load("nivel1/agua100porciento.png")
    agua75= pygame.image.load("nivel1/agua75porciento.png")
    agua50= pygame.image.load("nivel1/agua50porciento.png")
    agua25= pygame.image.load("nivel1/agua25porciento.png")
    agua5= pygame.image.load("nivel1/agua5porciento.png")

    #Pantalla
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: Nivel 1")

    #Personaje 
    plomero=Plomero(20,450)

    #Enemigo
    enemigo1= enemigo(800, 400)


    reloj1=pygame.time.Clock()
    boton1=Boton(botonpausa,botonpausa2,980,10)
    cursor1=cursor()
    rangodisparo=1
    pygame.mixer.music.set_volume(0)

    x=0

    vidaenemigo=100
    vidaplomero=10

    lista_plomero=pygame.sprite.Group()
    lista_bloques=pygame.sprite.Group()
    lista_proyectiles=pygame.sprite.Group()
    lista_proyectilenemigo=pygame.sprite.Group()

    enjuego=False
    movimientobala=False

    #Variables del agua
    aux=1
    litrosagua=100
    crono2=pygame.time.get_ticks()/1000
    color=(0,255,0)

    while enjuego==False:

        crono=(pygame.time.get_ticks()/1000)-crono2
        if crono==aux:
            aux+=1
            litrosagua-=2

        if litrosagua==50:
            color=(255,128,0)
        elif litrosagua==20:
            color=(255,0,0)



        textovidaenemigo=miFuente.render(str(vidaenemigo),0,(255,255,255))
        textovidaplomero=miFuente.render(str(vidaplomero),0,(255,255,255))
        textolitroagua=miFuente.render(str(litrosagua),0,(color))
        textoaguadisp=miFuentepeque.render("LITROS DE",0,(255,255,255))
        textoaguadisp2=miFuentepeque.render("AGUA DISPONIBLE :",0,(255,255,255))

        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(10,20))
        screen.blit(barraagua,(10,100))
        screen.blit(barratubos,(10,185))
        screen.blit(barraenemigo,(832,80))
        screen.blit(llavedeagua,(950,510))
        screen.blit(textovidaenemigo,(960,94))
        screen.blit(textovidaplomero,(150,35))
        screen.blit(textolitroagua,(200,125))
        screen.blit(textoaguadisp,(100,125))
        screen.blit(textoaguadisp2,(28,140))

        if litrosagua<=100 and litrosagua>75:      
            screen.blit(agua100,(952,560))
        elif litrosagua<=75 and litrosagua>50:
            screen.blit(agua75,(785,560))
        elif litrosagua<=50 and litrosagua>25:
            screen.blit(agua50,(458,562))
        elif litrosagua<=25 and litrosagua>10:
            screen.blit(agua25,(240,562))
        else:
            screen.blit(agua5,(0,562))

        #Disparo enemigo
        lista_bloques.add(enemigo1)
        lista_plomero.add(plomero)

        if (randint(0,100)<rangodisparo):
            pryenemigo=Proyectilenemigo(enemigo1.rect.x,enemigo1.rect.y)
            lista_proyectilenemigo.add(pryenemigo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa()
                if event.key == pygame.K_x:
                    movimientobala=True
                    soundDisPlom.play()
                    proyectil = Proyectil(plomero.rect.x+50,plomero.rect.y+80)
                    x = proyectil.rect.x
                    lista_proyectiles.add(proyectil)

                if event.key == pygame.K_r:
                	plomero.rect.y=460
                	plomero.rect.x=20
                	enjuego=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    pausa()
        for proyectil in lista_proyectiles:
        	lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil,lista_bloques,True)
        	for enemigo1 in lista_bloques_alcanzados:
        		lista_proyectiles.remove(proyectil)
        		vidaenemigo-=2
        		movimientobala=False
        for pryenemigo in lista_proyectilenemigo:
            colisiondebalaenpersonaje = pygame.sprite.spritecollide(pryenemigo,lista_plomero,True)
            for plomero in colisiondebalaenpersonaje:
                lista_proyectilenemigo.remove(pryenemigo)
                vidaplomero-=1
                movimientobala=False
        if vidaplomero==0 or litrosagua==0:
            perdiste(enjuego)

        print event
        plomero.eventos()
        plomero.update(screen)
        enemigo1.dibujar(screen)
        lista_proyectilenemigo.update(screen)
        lista_proyectiles.update(screen)
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

main()



