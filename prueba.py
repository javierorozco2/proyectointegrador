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
bala = pygame.image.load("nivel1/arma.png")
balaenemigo = pygame.image.load("nivel1/proyectil.png")
reloj = pygame.time.Clock()
tubo1=pygame.image.load("nivel1/tubo.png")
tubo2=pygame.image.load("nivel1/tubo2.png")
tubo3=pygame.image.load("nivel1/tubo3.png")

#Fuentes de letra
miFuente = pygame.font.Font(None,50)
miFuentepeque = pygame.font.Font(None,20)

#Sonidos y musica
clic = pygame.mixer.Sound("sonidos/clic.ogg")
soundDisPlom= pygame.mixer.Sound("sonidos/disparo.ogg")
soundGameover = pygame.mixer.Sound("sonidos/gameover.ogg")
sonidotubo = pygame.mixer.Sound("sonidos/tubo.ogg")
soundwin = pygame.mixer.Sound("sonidos/win.ogg")

sonidofondo = pygame.mixer.music.load("sonidos/fondo.mp3")
pygame.mixer.music.play(100)
pygame.mixer.music.set_volume(.25)
class Cartel(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("nivel2/cartelsi.png")
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y

        self.listaimag={}
        self.listaimag[0]=pygame.image.load("nivel2/cartelsi.png")
        self.listaimag[1]=pygame.image.load("nivel2/cartelno.png")

    def update(self,screen,i):
        screen.blit(self.listaimag[i],self.rect)

class personaventana(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("nivel2/personajetiraagua/persona14.png")
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y

        self.imgPersona={}
        self.i=0
        self.cont=2
        self.p=6
        self.actualizacion=True

        self.imgPersona[0]=pygame.image.load("nivel2/personajetiraagua/persona1.png")
        self.imgPersona[1]=pygame.image.load("nivel2/personajetiraagua/persona2.png")
        self.imgPersona[2]=pygame.image.load("nivel2/personajetiraagua/persona3.png")
        self.imgPersona[3]=pygame.image.load("nivel2/personajetiraagua/persona4.png")
        self.imgPersona[4]=pygame.image.load("nivel2/personajetiraagua/persona5.png")
        self.imgPersona[5]=pygame.image.load("nivel2/personajetiraagua/persona6.png")
        self.imgPersona[6]=pygame.image.load("nivel2/personajetiraagua/persona7.png")
        self.imgPersona[7]=pygame.image.load("nivel2/personajetiraagua/persona8.png")
        self.imgPersona[8]=pygame.image.load("nivel2/personajetiraagua/persona9.png")
        self.imgPersona[9]=pygame.image.load("nivel2/personajetiraagua/persona10.png") 
        self.imgPersona[10]=pygame.image.load("nivel2/personajetiraagua/persona11.png") 
        self.imgPersona[11]=pygame.image.load("nivel2/personajetiraagua/persona12.png") 
        self.imgPersona[12]=pygame.image.load("nivel2/personajetiraagua/persona13.png") 
        self.imgPersona[13]=pygame.image.load("nivel2/personajetiraagua/persona14.png") 
        self.imgPersona[14]=pygame.image.load("nivel2/personajetiraagua/persona15.png") 

        self.Magua={}
        self.i2=-1
        self.manguera=False
        self.Magua[0]=pygame.image.load("nivel2/personajetiraagua/agua1.png")
        self.Magua[1]=pygame.image.load("nivel2/personajetiraagua/agua2.png")
        self.Magua[2]=pygame.image.load("nivel2/personajetiraagua/agua3.png")
        self.Magua[3]=pygame.image.load("nivel2/personajetiraagua/agua4.png")
        self.Magua[4]=pygame.image.load("nivel2/personajetiraagua/agua5.png")

        self.Mcarreteragua={}
        self.i3=-1
        self.carretera=False
        self.Mcarreteragua[0]=pygame.image.load("nivel2/personajetiraagua/aguacalle1.png")
        self.Mcarreteragua[1]=pygame.image.load("nivel2/personajetiraagua/aguacalle2.png")
        self.Mcarreteragua[2]=pygame.image.load("nivel2/personajetiraagua/aguacalle3.png")

        self.soloagua=False
    def update(self,screen):
        if self.actualizacion==True:
            self.cont+=1
        if self.cont==self.p or self.cont==self.p*2 or self.cont==self.p*3 or self.cont==self.p*4 or self.cont==self.p*5 or self.cont==self.p*6 or self.cont==self.p*7 or self.cont==self.p*8 or self.cont==self.p*9 or self.cont==self.p*10 or self.cont==self.p*11 or self.cont==self.p*12 or self.cont==self.p*13 or self.cont==self.p*14:
            self.i+=1
        if self.cont==self.p*15:
            self.i=14
            self.manguera=True

        if self.cont==self.p*15 or self.cont==self.p*16 or self.cont==self.p*17 or self.cont==self.p*18:  
            self.i2+=1
        if self.cont==self.p*20:
            self.i2=4
            self.carretera=True

        if self.cont==self.p*20 or self.cont==self.p*21 or self.cont==self.p*22:
            self.i3+=1
        if self.cont==self.p*22:
            self.i3=2

        if self.cont==self.p*28:
            self.soloagua=True

        if self.soloagua==False:
            if self.carretera==True:
                screen.blit(self.Mcarreteragua[self.i3],(self.rect.x-70,self.rect.y+60))

            if self.manguera==True:
                screen.blit(self.Magua[self.i2],(self.rect.x-10,self.rect.y+23))
            screen.blit(self.imgPersona[self.i],self.rect)
        else:
            screen.blit(self.Mcarreteragua[2],(self.rect.x-70,self.rect.y+60))

class llavedeagua(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.imagen2=pygame.image.load("nivel1/llavedeaguaarreglada.png")
        self.imagen1=pygame.image.load("nivel1/llavedeaguajodida.png")
        self.rect= self.imagen1.get_rect()
        self.rect.x=x
        self.rect.y=y

        self.imagenes={}
        self.imagenes[0]=self.imagen1
        self.imagenes[1]=self.imagen2
    def update(self,screen,i):
        screen.blit(self.imagenes[i],self.rect)

class Plomero(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('personajes/plomero/plomero.png')
        self.sheet.set_clip(pygame.Rect(140, 0, 50, 130)) #215, - , -, 159
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.izquierda={}
        self.derecha={}
        self.i=1
        self.cont=0
        self.p=4

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
            if self.rect.x<=1020:
                self.rect.x+=5
            else:
                pass
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
            if self.rect.x>=0:
                self.rect.x-=5
            else:
                pass
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
                self.rect.y-=10
            if self.bajada==True:
                self.rect.y+=10
            if self.rect.y==250:
                self.bajada=True
            if self.rect.y==450:
                self.bajada=False
                self.salto=False 
                self.i=1

    def saltoparabolico(self):
        if self.saltoPar==True and self.salto==False and self.direccion==True:
            self.i=0
            if self.bajadaPar==False:
                if self.rect.x<=1020:
                    self.rect.y-=10
                    self.rect.x+=10
                else:
                    if self.rect.y<=450:
                        self.rect.y+=5
                    else:
                        self.bajadaPar=False
                        self.saltoPar=False
                        self.i=1

            if self.bajadaPar==True:
                if self.rect.x <=1020:
                    self.rect.y+=10
                    self.rect.x+=10
                else:
                    if self.rect.y<=450:
                        self.rect.y+=5
                    else:
                        self.bajadaPar=False
                        self.saltoPar=False
                        self.i=1
            if self.rect.y==300:
                self.bajadaPar=True
            if self.rect.y==450:
                self.bajadaPar=False
                self.saltoPar=False
                self.i=1
        if self.saltoPar==True and self.salto==False and self.direccion==False:
            self.i=0
            if self.bajadaPar==False:
                if self.rect.x>=0:
                    self.rect.y-=10
                    self.rect.x-=10
                else:
                    if self.rect.y<=450:
                        self.rect.y+=5
                    else:
                        self.bajadaPar=False
                        self.saltoPar=False
            if self.bajadaPar==True:
                if self.rect.x>=0:
                    self.rect.y+=10
                    self.rect.x-=10
                else:
                    if self.rect.y<=450:
                        self.rect.y+=5
                    else:
                        self.bajadaPar=False
                        self.saltoPar=False
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

class tubo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.image.load("nivel1/tubo.png")
        self.rect = self.image.get_rect()
        self.rect.x=randint(100,900)
        self.rect.y=550

        self.tubos={}
        self.crono=(pygame.time.get_ticks()/1000)
        self.i=0
        self.cont=1
        self.unlado=True

        self.tubos[0]=tubo1
        self.tubos[1]=tubo2
        self.tubos[2]=tubo3
    def update(self,screen):
        screen.blit(self.tubos[self.i],self.rect)
    def cambioimagen(self,crono,aux):
        if crono==self.cont and self.unlado==True:
            self.cont+=1
            self.i+=1 
            if self.i==2:
                self.unlado=False   
        if crono==self.cont and self.unlado==False:
            self.cont+=1
            self.i-=1 
            if self.i==0:
                self.unlado=True          

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
			if self.rect.top > 500:
				self.arriba = True
		screen.blit(self.imagen, self.rect)

class enemigo2(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load('nivel2/animacionenemigo/1.png')
        self.rect = self.imagen.get_rect()

        self.manguera1=pygame.image.load("nivel2/animacionenemigo/1.png")
        self.manguera2=pygame.image.load("nivel2/animacionenemigo/2.png")

        self.listaDisparo = []

        self.lstmangue={}
        self.lstmangue[0]=self.manguera1
        self.lstmangue[1]=self.manguera2
        self.i=0
        self.cont=1
        self.unlado=True

        self.velocidad = 20
        self.rect.y = posy #450
        self.rect.x = posx-50 #750

        self.arriba = True
        self.veloz = 2


        self.Mizq=True
        self.Marriba=False
        self.Mdere=False
        self.Mabajo=False

    def dibujar (self,screen):
        if self.Mizq==True:
            self.rect.x+=self.veloz
        if self.rect.x>=830 and self.Mizq==True:
            self.Mizq=False
            self.Marriba=True

        if self.Marriba==True:
            self.rect.x+=self.veloz-1
            self.rect.y-=self.veloz-1
        if self.rect.y==420 and self.Marriba==True:
            self.Marriba=False
            self.Mdere=True

        if self.Mdere==True:
            self.rect.x-=self.veloz
        if self.rect.x<=750 and self.Mdere==True:
            self.Mdere=False
            self.Mabajo=True

        if self.Mabajo==True:
            self.rect.x-=self.veloz-1
            self.rect.y+=self.veloz-1
        if self.rect.y>=450 and self.Mabajo==True:
            self.Mabajo=False
            self.Mizq=True

        screen.blit(self.lstmangue[self.i],self.rect)
    def cambioimagen(self,crono,aux):
        if crono==self.cont and self.unlado==True:
            self.cont+=1
            self.i+=1 
            if self.i==1:
                self.unlado=False   
        if crono==self.cont and self.unlado==False:
            self.cont+=1
            self.i-=1 
            if self.i==0:
                self.unlado=True      

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
    def __init__(self,x,y,nivel):
        pygame.sprite.Sprite.__init__(self)
        if nivel==1:
            self.image = balaenemigo
        if nivel==2:
            self.image = pygame.image.load("nivel2/proyectil2.png")
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y+100


    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x -=5
        self.rect.y +=2
        screen.blit(self.image,self.rect)

class Proyectilenemigo2(pygame.sprite.Sprite):
    """ Esta clase representa al proyectil . """
    def __init__(self,x,y,nivel):
        pygame.sprite.Sprite.__init__(self)
        if nivel==1:
            self.image = balaenemigo
        if nivel==2:
            self.image = pygame.image.load("nivel2/proyectil2.png")
        self.rect=self.image.get_rect()

        self.rect.x=x
        self.rect.y=y+100


    def update(self,screen):
        """ Desplaza al proyectil. """
        self.rect.x -=5
        self.rect.y +=1
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
    #pygame.mixer.music.set_volume(.25)
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
                    menu2()
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
                    sonidotubo.set_volume(0)
                    soundwin.set_volume(0)
                if cursor1.colliderect(boton4.rect):
                    clic.play()
                    clic.set_volume(1)
                    soundDisPlom.set_volume(1)
                    sonidotubo.set_volume(1)
                    soundwin.set_volume(1)
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
                    tutorial()
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    historia2()
                if cursor1.colliderect(boton4.rect):
                    clic.play()
                    nivel3()

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

def menu2():
    
    botonnuevo= pygame.image.load("menu2/botonnuevojuego.png")
    botonnuevo2= pygame.image.load("menu2/botonnuevojuego2.png")

    botoncargar= pygame.image.load("menu2/botoncargarnivel.png")
    botoncargar2= pygame.image.load("menu2/botoncargarnivel2.png")

    botonreturn = pygame.image.load("menujugar/botonregresar.png")
    botonreturn2 = pygame.image.load("menujugar/botonregresar2.png")

    fondo= pygame.image.load("menu2/fondo.png")
    fondo2= pygame.image.load("menu2/fondo2.png")

    cursor1=cursor()

    pygame.init()
    pygame.display.set_caption("Plumber Jumper")
    screen=pygame.display.set_mode((1080,720))

    reloj=pygame.time.Clock()

    boton1=Boton(botonnuevo,botonnuevo2,300,200)
    boton2=Boton(botoncargar,botoncargar2,300,400)
    boton3=Boton(botonreturn,botonreturn2,50,590)

    while True:
        screen.blit(fondo2,(0,0))
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    tutorial()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    Menujugar()
                if cursor1.colliderect(boton3.rect):
                    clic.play()
                    main()
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        boton1.update(screen,cursor1)
        boton2.update(screen,cursor1)
        boton3.update(screen,cursor1)
        reloj.tick(20)
        cursor1.update()
        pygame.display.update()

def pausa(nivel):
    pausado = True
    Nivel=nivel
    screen = pygame.display.set_mode((1080,720))
    if Nivel==1:
        fondo = pygame.image.load("nivel1/nivel1.png")
    if Nivel==2:
        fondo = pygame.image.load("nivel2/nivel2.png")
    if Nivel==3:
        fondo = pygame.image.load("nivel1/nivel3.png")
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
        reloj1.tick(60)
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

        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def perdiste2(enjuego):
    enjuego=False
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("perdiste/perdistelvl2.png")

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
                    nivel2()
                if event.key == pygame.K_ESCAPE:
                    main()

        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def ganaste1(enjuego):
    enjuego=False
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("nivel1/nivel1.png")
    letras = pygame.image.load("menuwin/lvlcompletado.png")

    boton1 = pygame.image.load("menuwin/nextlevel.png")
    boton2 = pygame.image.load("menuwin/nextlevel2.png")

    salir = pygame.image.load("pausa/botonsalir.png")
    salir2 = pygame.image.load("pausa/botonsalir2.png")

    cursor1=cursor()
    reloj1=pygame.time.Clock()

    boton=Boton(boton1,boton2,530,400)
    boton2=Boton(salir,salir2,400,400)

    soundwin.play()

    youlose=True
    while youlose==True:
        screen.blit(fondo,(0,0))
        screen.blit(letras,(0,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton.rect):
                    clic.play()
                    historia2()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pygame.quit()
                    sys.exit(0)

        #print event
        boton.update(screen,cursor1)
        boton2.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def ganaste2(enjuego):
    enjuego=False
    screen = pygame.display.set_mode((1080,720))
    fondo = pygame.image.load("nivel2/nivel2.png")
    letras = pygame.image.load("menuwin/lvlcompletado.png")

    boton1 = pygame.image.load("menuwin/nextlevel.png")
    boton2 = pygame.image.load("menuwin/nextlevel2.png")

    salir = pygame.image.load("pausa/botonsalir.png")
    salir2 = pygame.image.load("pausa/botonsalir2.png")

    cursor1=cursor()
    reloj1=pygame.time.Clock()

    boton=Boton(boton1,boton2,530,400)
    boton2=Boton(salir,salir2,400,400)

    soundwin.play()

    youlose=True
    while youlose==True:
        screen.blit(fondo,(0,0))
        screen.blit(letras,(0,100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton.rect):
                    clic.play()
                    nivel3()
                if cursor1.colliderect(boton2.rect):
                    clic.play()
                    pygame.quit()
                    sys.exit(0)

        #print event
        boton.update(screen,cursor1)
        boton2.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def tutorial():

    pygame.init()
    screen=pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: botones para jugar")

    fondo=pygame.image.load("historias/tutorial.png")
    botonnext = pygame.image.load("historias/botonnext.png")
    botonnext2 = pygame.image.load("historias/botonnext2.png")

    plomero=Plomero(20,450)

    boton1=Boton(botonnext,botonnext2,770,560)

    lista_proyectiles=pygame.sprite.Group()

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    enjuego=True
    while enjuego==True:
        screen.blit(fondo,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    historia1()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    movimientobala=True
                    soundDisPlom.play()
                    proyectil = Proyectil(plomero.rect.x+50,plomero.rect.y+80)
                    x = proyectil.rect.x
                    lista_proyectiles.add(proyectil)

        #print event
        lista_proyectiles.update(screen)
        plomero.eventos()
        plomero.update(screen)
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def historia1():

    pygame.init()
    screen=pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: botones para jugar")

    fondo=pygame.image.load("historias/historia1inicio.png")
    letras= pygame.image.load("historias/letrahistoria.png")

    botonnext = pygame.image.load("historias/botonplay.png")
    botonnext2 = pygame.image.load("historias/botonplay2.png")

    boton1=Boton(botonnext,botonnext2,930,590)

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    enjuego=True
    while enjuego==True:
        screen.blit(fondo,(0,0))
        screen.blit(letras,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    nivel1()

        #print event
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def historia2():

    pygame.init()
    screen=pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: botones para jugar")

    fondo=pygame.image.load("historias/historia2segundonivel.png")
    fondo2=pygame.image.load("historias/historia2segundonivel2.png")
    letras= pygame.image.load("historias/letrahistoria.png")

    botonnext = pygame.image.load("historias/botonplay.png")
    botonnext2 = pygame.image.load("historias/botonplay2.png")

    boton11 = pygame.image.load("historias/botonnext.png")
    boton22 = pygame.image.load("historias/botonnext2.png")

    boton1=Boton(botonnext,botonnext2,930,590)
    boton2=Boton(boton11,boton22,930,590)

    siguiente=False

    cursor1=cursor()
    reloj1=pygame.time.Clock()
    enjuego=True
    while enjuego==True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect) and siguiente==True:
                    clic.play()
                    nivel2()
                if cursor1.colliderect(boton2.rect) and siguiente==False:
                    clic.play()
                    siguiente=True
                    

        #print event
        if siguiente==False:
            screen.blit(fondo,(0,0))
        if siguiente==True:
            screen.blit(fondo2,(0,0))
        screen.blit(letras,(0,0))
        if siguiente==True:
            boton1.update(screen,cursor1)
        if siguiente==False:
            boton2.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def nivel1():

    pygame.init()

    fondo = pygame.image.load("nivel1/nivel1.png")
    barravidapersonaje = pygame.image.load("nivel1/barravidapersonaje.png")     
    barraagua = pygame.image.load("nivel1/barraporcentajeagua.png")
    barratubos = pygame.image.load("nivel1/barratubos.png")
    barraenemigo = pygame.image.load("nivel1/barravidaenemigo.png")
    botonpausa = pygame.image.load("pausa/botonpausa.png")
    botonpausa2 = pygame.image.load("pausa/botonpausa2.png")

    agua100=pygame.image.load("nivel1/agua100porciento.png")
    agua75= pygame.image.load("nivel1/agua75porciento.png")
    agua50= pygame.image.load("nivel1/agua50porciento.png")
    agua25= pygame.image.load("nivel1/agua25porciento.png")
    agua5= pygame.image.load("nivel1/agua5porciento.png")

    mensaje1= pygame.image.load("nivel1/cierrallave1.png")
    mensaje2= pygame.image.load("nivel1/cierrallave2.png")
    mensaje3= pygame.image.load("nivel1/cierrallave3.png")

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
    tubosrecog=0

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

    #Variables de tuberias
    tuberia1=tubo()
    tuberia2=tubo()
    tuberia3=tubo()
    random1=randint(5,95)
    random2=randint(5,95)
    random3=randint(5,95)

    llave=llavedeagua(950,510)
    llavecerrada=False

    while enjuego==False:

        crono=(pygame.time.get_ticks()/1000)-crono2
        if crono==aux:
            aux+=1
            if llavecerrada==False:
                litrosagua-=2

        if litrosagua==50:
            color=(255,128,0)
        elif litrosagua==20:
            color=(255,0,0)



        textovidaenemigo=miFuente.render(str(vidaenemigo),0,(255,255,255))
        textovidaplomero=miFuente.render(str(vidaplomero),0,(255,255,255))
        textolitroagua=miFuente.render(str(litrosagua),0,(color))
        textoaguadisp=miFuentepeque.render("LITROS DE",0,(255,155,0))
        textoaguadisp2=miFuentepeque.render("AGUA DISPONIBLE :",0,(255,155,0))
        textotubos=miFuente.render(str(tubosrecog),0,(255,255,255))
        textotubos2=miFuente.render("/ 3",0,(255,255,255))

        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(-30,20))
        screen.blit(barraagua,(-30,100))
        screen.blit(barratubos,(-30,185))
        screen.blit(barraenemigo,(832,80))
        screen.blit(textovidaenemigo,(960,94))
        screen.blit(textovidaplomero,(110,35))
        screen.blit(textolitroagua,(135,125))
        screen.blit(textoaguadisp,(25,125))
        screen.blit(textoaguadisp2,(0,140))
        screen.blit(textotubos,(110,203))
        screen.blit(textotubos2,(140,203))


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

        #TUBERIAS
        if litrosagua<=random1:
            tuberia1.update(screen)
            if plomero.rect.colliderect(tuberia1.rect):
                sonidotubo.play()
                tuberia1.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random2:
            tuberia2.update(screen)
            if plomero.rect.colliderect(tuberia2.rect):
                sonidotubo.play()
                tuberia2.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random3:
            tuberia3.update(screen)
            if plomero.rect.colliderect(tuberia3.rect):
                sonidotubo.play()
                tuberia3.rect.x=2000
                tubosrecog+=1

        if llavecerrada==True:
            tuberia1.update(screen)
            if plomero.rect.colliderect(tuberia1.rect):
                sonidotubo.play()
                tuberia1.rect.x=2000
                tubosrecog+=1
        if llavecerrada==True:
            tuberia2.update(screen)
            if plomero.rect.colliderect(tuberia2.rect):
                sonidotubo.play()
                tuberia2.rect.x=2000
                tubosrecog+=1
        if llavecerrada==True:
            tuberia3.update(screen)
            if plomero.rect.colliderect(tuberia3.rect):
                sonidotubo.play()
                tuberia3.rect.x=2000
                tubosrecog+=1

        #Disparo enemigo
        lista_bloques.add(enemigo1)
        lista_plomero.add(plomero)

        if (randint(0,50)<rangodisparo):
            pryenemigo=Proyectilenemigo(enemigo1.rect.x,enemigo1.rect.y,1)
            lista_proyectilenemigo.add(pryenemigo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa(1)
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
                    pausa(1)

        #COLISIONES DE BALAS
        if vidaenemigo>0:
            for proyectil in lista_proyectiles:
            	lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil,lista_bloques,True)
            	for enemigo1 in lista_bloques_alcanzados:
            		lista_proyectiles.remove(proyectil)
            		vidaenemigo-=2
            		movimientobala=False
        if vidaenemigo>0:
            for pryenemigo in lista_proyectilenemigo:
                colisiondebalaenpersonaje = pygame.sprite.spritecollide(pryenemigo,lista_plomero,True)
                for plomero in colisiondebalaenpersonaje:
                    lista_proyectilenemigo.remove(pryenemigo)
                    vidaplomero-=1
                    movimientobala=False
        #COLISION DE ENEMIGO CON PLOMERO
        if vidaenemigo>0:
            if plomero.rect.colliderect(enemigo1.rect):
                vidaplomero-=0.1
        #COLISION DE PLOMERO CON LA LLAVE
        if vidaenemigo<=0:
            if plomero.rect.colliderect(llave.rect):
                llavecerrada=True


        #GANAR O PERDER
        if vidaplomero<=0 or litrosagua==0:
            perdiste(enjuego)   
        if llavecerrada==True and tubosrecog==3:
            ganaste1(enjuego)

        #MENSAJES
        if vidaenemigo<=0 and tubosrecog<=2 and llavecerrada==False:
            #Mensaje: Cierra la llave y recoge tubos
            screen.blit(mensaje2,(plomero.rect.x+50, plomero.rect.y-50))

        if vidaenemigo<=0 and tubosrecog>=3 and llavecerrada==False:
            #Mensaje: Solo cierra la llave
            screen.blit(mensaje1,(plomero.rect.x+50, plomero.rect.y-50))

        if vidaenemigo<=0 and tubosrecog<=2 and llavecerrada==True:
            #Mensaje: Solo recoge tubos
            screen.blit(mensaje3,(plomero.rect.x+50, plomero.rect.y-50))

        #CERRAR LLAVE
        if vidaenemigo>0:
            llave.update(screen,0)
        else:
            llave.update(screen,1)

        #print event
        plomero.eventos()
        plomero.update(screen)
        tuberia1.cambioimagen(crono,aux)
        tuberia2.cambioimagen(crono,aux)
        tuberia3.cambioimagen(crono,aux)
        if vidaenemigo>0:
            enemigo1.dibujar(screen)
            lista_proyectilenemigo.update(screen)
        lista_proyectiles.update(screen)
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def nivel2():

    pygame.init()

    fondo = pygame.image.load("nivel2/nivel2.png")
    barravidapersonaje = pygame.image.load("nivel1/barravidapersonaje.png")     
    barraagua = pygame.image.load("nivel1/barraporcentajeagua.png")
    barratubos = pygame.image.load("nivel1/barratubos.png")
    barraenemigo = pygame.image.load("nivel1/barravidaenemigo.png")
    botonpausa = pygame.image.load("pausa/botonpausa.png")
    botonpausa2 = pygame.image.load("pausa/botonpausa2.png")

    mensaje1=pygame.image.load("nivel2/mensaje1.png")
    mensaje2=pygame.image.load("nivel2/mensaje2.png")
    mensaje3=pygame.image.load("nivel1/cierrallave3.png")

    #Pantalla
    screen = pygame.display.set_mode((1080,720))
    pygame.display.set_caption("Plumber Jumper: Nivel 1")

    #Personaje 
    plomero=Plomero(20,450)

    #Enemigo
    enemigo1= enemigo2(800, 450)

    #Persona en ventana
    #persona=personaventana(282,544)


    reloj1=pygame.time.Clock()
    boton1=Boton(botonpausa,botonpausa2,980,10)
    cursor1=cursor()
    rangodisparo=1
    pygame.mixer.music.set_volume(0)

    x=0

    vidaenemigo=100
    vidaplomero=10
    tubosrecog=0

    lista_plomero=pygame.sprite.Group()
    lista_bloques=pygame.sprite.Group()
    lista_proyectiles=pygame.sprite.Group()
    lista_proyectilenemigo=pygame.sprite.Group()

    lista_personas=pygame.sprite.Group()

    enjuego=False
    movimientobala=False

    #Variables del agua
    aux=1
    litrosagua=100
    crono2=pygame.time.get_ticks()/1000
    color=(0,255,0)

    #Variables de tuberias
    tuberia1=tubo()
    tuberia2=tubo()
    tuberia3=tubo()
    random1=randint(5,95)
    random2=randint(5,95)
    random3=randint(5,95)

    cartel=Cartel(800,400)
    quitlona=False
    ponlona=False
    while enjuego==False:

        crono=(pygame.time.get_ticks()/1000)-crono2
        if crono==aux:
            aux+=1
            #litrosagua-=2

        if litrosagua==50:
            color=(255,128,0)
        elif litrosagua==20:
            color=(255,0,0)

        #PERSONA TIRANDO AGUA:
        if ponlona==False:
            if aux==5:
                persona=personaventana(282,544)
                lista_personas.add(persona)
            if litrosagua>80 and aux>=8:
                litrosagua-=0.2

            if aux==20:
                persona=personaventana(82,544)
                lista_personas.add(persona)
            if litrosagua>60 and aux>=23:
                litrosagua-=0.2

            if aux==40:
                persona=personaventana(685,544)
                lista_personas.add(persona)
            if litrosagua>40 and aux>=43:
                litrosagua-=0.2

            if aux==60:
                persona=personaventana(164,544)
                lista_personas.add(persona)
            if litrosagua>20 and aux>=63:
                litrosagua-=0.2

            if aux==80:
                persona=personaventana(767,544)
                lista_personas.add(persona)
            if litrosagua>0 and aux>=83:
                litrosagua-=0.2
                if litrosagua<=0:
                    litrosagua=0


        textovidaenemigo=miFuente.render(str(vidaenemigo),0,(255,255,255))
        textovidaplomero=miFuente.render(str(vidaplomero),0,(255,255,255))
        textolitroagua=miFuente.render(str(litrosagua),0,(color))
        textoaguadisp=miFuentepeque.render("LITROS DE",0,(255,155,0))
        textoaguadisp2=miFuentepeque.render("AGUA DISPONIBLE :",0,(255,155,0))
        textotubos=miFuente.render(str(tubosrecog),0,(255,255,255))
        textotubos2=miFuente.render("/ 3",0,(255,255,255))

        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(-30,20))
        screen.blit(barraagua,(-30,100))
        screen.blit(barratubos,(-30,185))
        screen.blit(barraenemigo,(832,80))
        screen.blit(textovidaenemigo,(960,94))
        screen.blit(textovidaplomero,(110,35))
        screen.blit(textolitroagua,(135,125))
        screen.blit(textoaguadisp,(25,125))
        screen.blit(textoaguadisp2,(0,140))
        screen.blit(textotubos,(110,203))
        screen.blit(textotubos2,(140,203))

        #TUBERIAS
        if litrosagua<=random1:
            tuberia1.update(screen)
            if plomero.rect.colliderect(tuberia1.rect):
                sonidotubo.play()
                tuberia1.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random2:
            tuberia2.update(screen)
            if plomero.rect.colliderect(tuberia2.rect):
                sonidotubo.play()
                tuberia2.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random3:
            tuberia3.update(screen)
            if plomero.rect.colliderect(tuberia3.rect):
                sonidotubo.play()
                tuberia3.rect.x=2000
                tubosrecog+=1

        if ponlona==True:
            tuberia1.update(screen)
            if plomero.rect.colliderect(tuberia1.rect):
                sonidotubo.play()
                tuberia1.rect.x=2000
                tubosrecog+=1
        if ponlona==True:
            tuberia2.update(screen)
            if plomero.rect.colliderect(tuberia2.rect):
                sonidotubo.play()
                tuberia2.rect.x=2000
                tubosrecog+=1
        if ponlona==True:
            tuberia3.update(screen)
            if plomero.rect.colliderect(tuberia3.rect):
                sonidotubo.play()
                tuberia3.rect.x=2000
                tubosrecog+=1



        #Disparo enemigo
        lista_bloques.add(enemigo1)
        lista_plomero.add(plomero)

        if (randint(0,50)<rangodisparo):
            pryenemigo=Proyectilenemigo2(enemigo1.rect.x,enemigo1.rect.y-90,2)
            lista_proyectilenemigo.add(pryenemigo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa(2)
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

                if event.key == pygame.K_c and vidaenemigo<=0:
                    quitlona=True

                if event.key == pygame.K_n and vidaenemigo<=0:
                    ponlona=True

            if event.type==pygame.MOUSEBUTTONDOWN:
                if cursor1.colliderect(boton1.rect):
                    clic.play()
                    pausa(2)

        #COLISIONES DE BALAS
        if vidaenemigo>0:
            for proyectil in lista_proyectiles:
                lista_bloques_alcanzados = pygame.sprite.spritecollide(proyectil,lista_bloques,True)
                for enemigo1 in lista_bloques_alcanzados:
                    lista_proyectiles.remove(proyectil)
                    vidaenemigo-=2
                    movimientobala=False
        if vidaenemigo>0:
            for pryenemigo in lista_proyectilenemigo:
                colisiondebalaenpersonaje = pygame.sprite.spritecollide(pryenemigo,lista_plomero,True)
                for plomero in colisiondebalaenpersonaje:
                    lista_proyectilenemigo.remove(pryenemigo)
                    vidaplomero-=1
                    movimientobala=False
        if vidaenemigo>0:
            if plomero.rect.colliderect(enemigo1.rect):
                vidaplomero-=0.1

        #GANAR O PERDER
        if vidaplomero<=0 or litrosagua==0:
            perdiste2(enjuego)
        if vidaenemigo<=0 and ponlona==True and tubosrecog>=3:
            ganaste2(enjuego)

        #Mensajes
        if vidaenemigo<=0 and quitlona==False:
            screen.blit(mensaje1,(plomero.rect.x+50,plomero.rect.y-50))
        if vidaenemigo<=0 and quitlona==True and ponlona==False:
            screen.blit(mensaje2,(plomero.rect.x+50,plomero.rect.y-50))
        if vidaenemigo<=0 and quitlona==True and ponlona==True:
            screen.blit(mensaje3,(plomero.rect.x+50,plomero.rect.y-50))


        #print event
        if quitlona==False:
            cartel.update(screen,0)
        if ponlona==True:
            cartel.update(screen,1)
        lista_personas.update(screen)
        plomero.eventos()
        plomero.update(screen)
        tuberia1.cambioimagen(crono,aux)
        if vidaenemigo>0:
            enemigo1.dibujar(screen)
            enemigo1.cambioimagen(crono,aux)
            lista_proyectilenemigo.update(screen)
        lista_proyectiles.update(screen)
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

def nivel3():

    pygame.init()

    fondo = pygame.image.load("nivel1/nivel3.png")
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
    tubosrecog=0

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

    #Variables de tuberias
    tuberia1=tubo()
    tuberia2=tubo()
    tuberia3=tubo()
    random1=randint(5,95)
    random2=randint(5,95)
    random3=randint(5,95)

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
        textoaguadisp=miFuentepeque.render("LITROS DE",0,(255,155,0))
        textoaguadisp2=miFuentepeque.render("AGUA DISPONIBLE :",0,(255,155,0))
        textotubos=miFuente.render(str(tubosrecog),0,(255,255,255))
        textotubos2=miFuente.render("/ 3",0,(255,255,255))

        screen.blit(fondo,(0,0))
        screen.blit(barravidapersonaje,(-30,20))
        screen.blit(barraagua,(-30,100))
        screen.blit(barratubos,(-30,185))
        screen.blit(barraenemigo,(832,80))
        screen.blit(llavedeagua,(950,510))
        screen.blit(textovidaenemigo,(960,94))
        screen.blit(textovidaplomero,(110,35))
        screen.blit(textolitroagua,(135,125))
        screen.blit(textoaguadisp,(25,125))
        screen.blit(textoaguadisp2,(0,140))
        screen.blit(textotubos,(110,203))
        screen.blit(textotubos2,(140,203))


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

        #TUBERIAS
        if litrosagua<=random1:
            tuberia1.update(screen)
            if plomero.rect.colliderect(tuberia1.rect):
                sonidotubo.play()
                tuberia1.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random2:
            tuberia2.update(screen)
            if plomero.rect.colliderect(tuberia2.rect):
                sonidotubo.play()
                tuberia2.rect.x=2000
                tubosrecog+=1
        if litrosagua<=random3:
            tuberia3.update(screen)
            if plomero.rect.colliderect(tuberia3.rect):
                sonidotubo.play()
                tuberia3.rect.x=2000
                tubosrecog+=1



        #Disparo enemigo
        lista_bloques.add(enemigo1)
        lista_plomero.add(plomero)

        if (randint(0,50)<rangodisparo):
            pryenemigo=Proyectilenemigo(enemigo1.rect.x,enemigo1.rect.y,2)
            lista_proyectilenemigo.add(pryenemigo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pausa(3)
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
                    pausa(3)

        #COLISIONES DE BALAS
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

        if plomero.rect.colliderect(enemigo1.rect):
            vidaplomero-=0.1

        #GANAR O PERDER
        if vidaplomero<=0 or litrosagua==0:
            perdiste(enjuego)

        

        #print event
        plomero.eventos()
        plomero.update(screen)
        tuberia1.cambioimagen(crono,aux)
        tuberia2.cambioimagen(crono,aux)
        tuberia3.cambioimagen(crono,aux)
        enemigo1.dibujar(screen)
        lista_proyectilenemigo.update(screen)
        lista_proyectiles.update(screen)
        boton1.update(screen,cursor1)
        reloj1.tick(60)
        cursor1.update()
        pygame.display.update()

main()



