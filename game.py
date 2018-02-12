import pygame
from pygame.locals import *
import random

pygame.init()

class mouse(pygame.Rect): #Clase para obtener posicion x y y del mouse
    def __init__(self):
        pygame.Rect.__init__(self,0,0,1,1)
    def update(self):
        self.left, self.top = pygame.mouse.get_pos() 

class boton(pygame.sprite.Sprite): #Clase en la que se definen los botones y sus posiciones
    def __init__(self,imagen1, imagen2, imagen3, x, y):
        self.boton_normal = imagen1
        self.boton_claro = imagen2
        self.boton_oscuro = imagen3
        self.boton_actual = self.boton_normal
        self.rect = self.boton_actual.get_rect() #Se crea un rectángulo en el boton para colicionar con el mouse
        self.rect.left, self.rect.top = (x,y)

    def update(self,display_game,mouse, x, y): #Pega la imagen del boton en la pantalla
        if mouse.colliderect(self.rect): # Condición si pasa el mouse encima del boton, este se ilumina(carga otra imagen)
            self.boton_actual = self.boton_claro 
        else:
            self.boton_actual = self.boton_normal
        display_game.blit(self.boton_actual,(x,y))
    def update2(self,display_game, mouse, name, x, y): #Permite que el boton de start se active o no
        if name != "": #Condición que permite que el boton de start se active y se ponga normal
            if mouse.colliderect(self.rect): # Condición si pasa el mouse encima del boton, este se ilumina(carga otra imagen)
                self.boton_actual = self.boton_claro
            else:
                self.boton_actual = self.boton_normal
        else:
            self.boton_actual = self.boton_oscuro
        display_game.blit(self.boton_actual,(x,y))

class confite(): #Clase en la que se definen los confites
    def __init__(self, color,color2, tipo, tipo_color):
        self.confite_c = color #Imagen
        self.confite_t = tipo #Tipo 0 = disco y vacio, 1 = normales, 2 = fusion horizontal, 3 = fusion vertical
        self.confite_c2 = color2 #Imagen del confite oscuro, cuando es presionado
        self.confite_t2 = tipo_color #Tipo 1 = rojo, 2 = amarillo, 3 = azul, 4 = verde, 5 = morado
    def update(self, display_game, x, y): #Pega los confites a la pantalla
        display_game.blit(self.confite_c, (x,y))
    def update2(self, display_game, x, y): #Pega los confites oscuros, cuando es presionado 1
        display_game.blit(self.confite_c2, (x,y))
    def update_tipo(self, new_tipo): #Actualiza el tipo de confite, usado para diferenciar entre fusion vertical y horizontal
        self.confite_t = new_tipo

def fin(name,puntos):
    pygame.init()
    display_width = 320 #Largo de la pantalla
    display_height = 240 #Ancho de la pantalla
    display_game = pygame.display.set_mode((display_width,display_height)) #Establece la ventana del juego con 800x600

    reloj3 = pygame.time.Clock() #Establece el reloj

    mouse3 = mouse()# Establece el mouse
    pygame.mixer.music.load("Alan Walker - Faded.mp3") #Carga la canción que será ejecutada durante el juego
    pygame.mixer.music.play(5) #Establece la cantidad de veces que la canción será repetida

    imagen_f = pygame.image.load("fin.jpeg") #Carga la imagen de fondo
    display_game.blit(imagen_f,(0,0)) #Pega la imagen de fondo

    fuente = pygame.font.Font(None, 30)

    text = ("Puntaje")
    mensaje = fuente.render(text, 1, (255, 255, 255))
    display_game.blit(mensaje, (235,185))
    pygame.display.flip()

    text = str(puntos[0])
    mensaje = fuente.render(text, 1, (255, 255, 255))
    display_game.blit(mensaje, (245,210))
    pygame.display.flip()

    archi = open("high_score.txt","a")
    archi.write(str(puntos[0]))
    archi.write(".")
    archi.write(name)
    archi.write("\n")
    archi.close

    fail = False
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        reloj3.tick(60)
        mouse3.update()
        pygame.display.update()


def juego(name): #Función juego, se encuentra todo el juego, despues del menú
    pygame.init() #Inicializa pygame

    display_width = 800 #Largo de la pantalla
    display_height = 600 #Ancho de la pantalla
    display_game = pygame.display.set_mode((display_width,display_height)) #Establece la ventana del juego con 800x600

    reloj2 = pygame.time.Clock() #Establece el reloj

    mouse2 = mouse()# Establece el mouse

    pygame.mixer.music.load("bleach ost 1 battle ignition 18.mp3") #Carga la canción que será ejecutada durante el juego
    pygame.mixer.music.play(5) #Establece la cantidad de veces que la canción será repetida

    sonido1 = pygame.mixer.Sound("Clap.wav")
    sonidof = pygame.mixer.Sound("Snare (Raw Cut).wav")
    sonido2 = pygame.mixer.Sound("Snare 2.wav")
    sonido3 = pygame.mixer.Sound("Snare.wav")

    imagen_f = pygame.image.load("bleach_py2.jpg") #Carga la imagen de fondo
    display_game.blit(imagen_f,(0,0)) #Pega la imagen de fondo

    #Aquí se empieza a cargar los datos de los confite en el siguiente orden:
    #Imagen del confite
    #Imagen del confite oscuro
    #Tipo de confite
    #Tipo de color del confite
    #Establece el objeto

    img_rojo = pygame.image.load("rojo.png")
    img_rojo2 = pygame.image.load("rojo2.png")
    t_rojo = 1
    t2_rojo = 1
    r = confite(img_rojo, img_rojo2, t_rojo, t2_rojo)

    img_amarillo = pygame.image.load("amarillo.png")
    img_amarillo2 = pygame.image.load("amarillo2.png")
    t_amarillo = 1
    t2_amarillo = 2
    am = confite(img_amarillo, img_amarillo2, t_amarillo, t2_amarillo)

    img_azul = pygame.image.load("azul.png")
    img_azul2 = pygame.image.load("azul2.png")
    t_azul = 1
    t2_azul = 3
    az = confite(img_azul, img_azul2, t_azul, t2_azul)

    img_verde = pygame.image.load("verde.png")
    img_verde2 = pygame.image.load("verde2.png")
    t_verde = 1
    t2_verde = 4
    v = confite(img_verde, img_verde2, t_verde, t2_verde)

    img_morado = pygame.image.load("morado.png")
    img_morado2 = pygame.image.load("morado2.png")
    t_morado = 1
    t2_morado = 5
    m = confite(img_morado, img_morado2, t_morado, t2_morado)

    img_fusion_rojo = pygame.image.load("fusion_rojo.png")
    img_fusion_rojo2 = pygame.image.load("fusion_rojo2.png")
    t_fusion_rojo = 2
    t2_fusion_rojo = 1
    fr = confite(img_fusion_rojo, img_fusion_rojo2, t_fusion_rojo, t2_fusion_rojo)

    img_fusion_amarillo = pygame.image.load("fusion_amarillo.png")
    img_fusion_amarillo2 = pygame.image.load("fusion_amarillo2.png")
    t_fusion_amarillo = 2
    t2_fusion_amarillo = 2
    fam = confite(img_fusion_amarillo, img_fusion_amarillo2, t_fusion_amarillo, t2_fusion_amarillo)

    img_fusion_azul = pygame.image.load("fusion_azul.png")
    img_fusion_azul2 = pygame.image.load("fusion_azul2.png")
    t_fusion_azul = 2
    t2_fusion_azul = 3
    faz = confite(img_fusion_azul, img_fusion_azul2, t_fusion_azul, t2_fusion_azul)

    img_fusion_verde = pygame.image.load("fusion_verde.png")
    img_fusion_verde2 = pygame.image.load("fusion_verde2.png")
    t_fusion_verde = 2
    t2_fusion_verde = 4
    fv = confite(img_fusion_verde, img_fusion_verde2, t_fusion_verde, t2_fusion_verde)

    img_fusion_morado = pygame.image.load("fusion_morado.png")
    img_fusion_morado2 = pygame.image.load("fusion_morado2.png")
    t_fusion_morado = 2
    t2_fusion_morado = 5
    fm = confite(img_fusion_morado, img_fusion_morado2, t_fusion_morado, t2_fusion_morado)

    vacio = pygame.image.load("fondo_vacio.png")
    va = confite(vacio, vacio, 0, 0)

    full = pygame.image.load("full.png")
    full2 = pygame.image.load("full2.png")
    fl = confite(full, full2, 4, 0) 
    #Aquí termina de establecer los datos de los confites

    #Se crea una lista la cual va a contener la matriz, ademas de la matriz logica, sus filas y sus columnas
    matriz = []
    filas = 9
    columnas = 9
    
    def crea_matrices(): #Función para crear la matriz
        for f in range(filas): #For en el crea los espacios de la matriz
            matriz.append([0]*columnas)
        ini = -50
        for q in range(filas): #For que recorre las filas
            ini = ini+60
            fin = -50
            for w in range(columnas): #For que recorre las columnas
                fin = fin + 60
                colores = [r, v, am, az, m] #Crea una lista con los clores, en un orden que mas adelante será de utilidad
                a = random.choice(colores) #Escoge un color random
                if q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8: #Se posiciona en la posición 2 de la matriz en la fila respectiva, reviza las 2 anteriores y si son iguales quita ese color, encoge otro, y vuelve a añadir el color
                    if matriz[w][q-1] == a and matriz[w][q-2] == a:
                        b = a
                        colores.remove(a)
                        a = random.choice(colores)
                        colores.append(b)
                if w == 2 or w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8: #Se posiciona en la posición 2 de la matriz en columna respectiva, reviza las 2 anteriores y si son iguales quita ese color, encoge otro, y vuelve a añadir el color
                    if matriz[w-1][q] == a and matriz[w-2][q] == a:
                        b = a
                        colores.remove(a)
                        a = random.choice(colores)
                        colores.append(b)
                matriz[w][q] = a
                a.update(display_game, ini, fin)

    crea_matrices()
    def moves(datos):
            mas_x = 10
            mas_y = 10
            pos_x = -1
            pos_y = -1
            def datos_obj(mas_x, mas_y, pos_x, pos_y, datos):
                if x > 9 and x < 551 and y > 9 and y < 551:
                    if x > 9 and y < mas_x:
                        if y > 9 and x < mas_y:
                            matriz[pos_x][pos_y].update2(display_game, mas_y-60, mas_x-60)
                            coordenadas = (mas_x-60, mas_y-60)
                            posicion = (pos_x, pos_y)
                            datos.append(coordenadas)
                            datos.append(posicion)
                        else:
                            datos_obj(mas_x, mas_y+60, pos_x, pos_y+1, datos)
                    else:
                        datos_obj(mas_x+60, mas_y, pos_x+1, pos_y, datos)
            datos_obj(mas_x, mas_y, pos_x, pos_y, datos)
    def cambia_posicion(datos):
        cx1, cy1 = datos[0]
        px1, py1 = datos[1]
        cx2, cy2 = datos[2]
        px2, py2 = datos[3]
        if px2 == px1+1 and py2 == py1 or px2 == px1-1 and py2 == py1 or py2 == py1+1 and px2 == px1 or py2 == py1-1 and px2 == px1:
            cambio(datos)
        else:
            matriz[px1][py1].update(display_game, cy1, cx1)
            matriz[px2][py2].update(display_game, cy2, cx2)
            del datos[0]
            del datos[0]
            del datos[0]
            del datos[0]
    def cambio(datos):
        cx1, cy1 = datos[0]
        px1, py1 = datos[1]
        cx2, cy2 = datos[2]
        px2, py2 = datos[3]
        g = matriz[px1][py1]
        matriz[px1][py1] = matriz[px2][py2]
        refresca_matriz()
        pygame.display.update()
        matriz[px2][py2] = g
        refresca_matriz()
        pygame.display.update()
        verificacion_fusion()


    def verificacion_fusion():
        cont = 0
        for w in range(9):
            for q in range(9):
                if q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q-2] and matriz[w][q].confite_t == 2 and matriz[w][q].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1] == matriz[w][q] and matriz[w][q-2].confite_t == 2 and matriz[w][q-2].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1].confite_t == 2 and matriz[w][q-2] == matriz[w][q] and matriz[w][q-1].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    elif matriz[w][q-1] == matriz[w][q-2] and matriz[w][q].confite_t == 3 and matriz[w][q].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1] == matriz[w][q] and matriz[w][q-2].confite_t == 3 and matriz[w][q-2].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1].confite_t == 3 and matriz[w][q-2] == matriz[w][q] and matriz[w][q-1].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                if w == 2 or w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w-2][q] and matriz[w][q].confite_t == 2 and matriz[w][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q] == matriz[w][q] and matriz[w-2][q].confite_t == 2 and matriz[w-2][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q].confite_t == 2 and matriz[w-2][q] == matriz[w][q] and matriz[w-1][q].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q] == matriz[w-2][q] and matriz[w][q].confite_t == 3 and matriz[w][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q] == matriz[w][q] and matriz[w-2][q].confite_t == 3 and matriz[w-2][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q].confite_t == 3 and matriz[w-2][q] == matriz[w][q] and matriz[w-1][q].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
        if cont == 0:
            refresca_matriz()
            verificacion_comb5()
        else:
            print("bien, reconoce la fusion rara")
            rompe_fusion(puntos)
            #ojo, aqui es rompe4, pero tiene el bug de que siempre hay convinacion, entonces deja mover, entonces, mientras puse verificacion, para que valla al del
    
    def verificacion_comb5():
        cont = 0
        for w in range(9):
            for q in range(9):
                if q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q] and matriz[w][q-3] == matriz[w][q] and matriz[w][q-4] == matriz[w][q]:
                        cont += 1
                if w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q] and matriz[w-3][q] == matriz[w][q] and matriz[w-4][q] == matriz[w][q]:
                        cont += 1
        if cont == 0:
            print("bien, el programa ve que no hay convinaciones")
            verificacion_comb4()
        else:
            print("el programa cuenta",cont,"combinacion")
            print("reconoce bien la de 5")
            rompe5(puntos)

            
    def verificacion_comb4():
        cont = 0
        for w in range(9):
            for q in range(9):
                if q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q] and matriz[w][q-3] == matriz[w][q]:
                        cont += 1
                if w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q] and matriz[w-3][q] == matriz[w][q]:
                        cont += 1
        if cont == 0:
            print("bien, el programa ve que no hay convinaciones")
            verificacion_comb3()
        else:
            print("el programa cuenta",cont,"combinacion")
            rompe4(puntos)
            
    def verificacion_comb3():
        cont = 0
        for w in range(9):
            for q in range(9):
                if q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q]:
                        cont += 1
                if w == 2 or w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q]:
                        cont += 1
        if cont == 0:
            print("bien, el programa ve que no hay convinaciones")
            rev_cambio(datos)
        else:
            print("el programa cuenta",cont,"combinacion")
            rompe3(cantidad_moves, puntos)

    def rompe_fusion(puntos):
        cont = 0
        cont_cambio = 0
        cont_q = -1
        cont_w = -1
        arriba = []
        derecha = []
        colores = [r, v, am, az, m]
        lista = [0,1,2,3,4,5,6,7,8]
                ############################################      
        def rompe_h(cont_q,cont_w,q,w):
            bandera = False
            for y in lista:
                sonidof.play()
                matriz[cont_q][y] = va
            refresca_matriz()
            pygame.display.update()
            pygame.time.wait(500)
            for l in lista:
                if matriz[cont_q][l].confite_t == 3:
                    lista.remove(l)
                    rompe_v(cont_q,cont_w,l,w)
                    bandera = True
                    print("sirve bien XD")
                    
            while cont_q > 0:
                for x in lista:
                    matriz[cont_q][x] = matriz[cont_q-1][x]
                    matriz[cont_q-1][x] = va
                    refresca_matriz()
                    pygame.display.update()
                cont_q -= 1
            if cont_q == 0:
                for x in lista:
                    a = random.choice(colores)
                    matriz[cont_q][x] = a
                    if x > 2:
                        if matriz[cont_q][x-1] == a and matriz[cont_q][x-2] == a:
                            colores.remove(a)
                            b = random.choice(colores)
                            matriz[cont_q][x] = b
                            colores.append(a)
                    else:
                        matriz[cont_q][x] = a
                refresca_matriz()
                pygame.display.update()
                if bandera == True:
                    lista.insert(l,l)
                ##############################################
        def rompe_v(cont_q,cont_w,q,w):
            for y in lista:
                matriz[y][q] = va
            refresca_matriz()
            pygame.display.update()
            pygame.time.wait(500)
            for l in lista:
                if matriz[l][q].confite_t == 3:
                    rompe_h(cont_q,cont_w,l,w)
                    print("sirve bien2 XD")
                    
            for x in lista:
                a = random.choice(colores)
                matriz[x][q] = a
                if x > 2:
                    if matriz[x-1][q] == a and matriz[x-2][q] == a:
                        colores.remove(a)
                        b = random.choice(colores)
                        matriz[x][q] = b
                        colores.append(a)
                else:
                    matriz[x][q] = a
            refresca_matriz()
            pygame.display.update()
                

      #####################################ROMPE HORIZONTAL CUANDO SE ENCUENTRAN 3 EN LA MISMA FILA##################################
        for w in range(9):
            cont_q += 1
            cont_w += 1
            for q in range(9):
                if q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q-2] and matriz[w][q].confite_t == 2 and matriz[w][q].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1] == matriz[w][q] and matriz[w][q-2].confite_t == 2 and matriz[w][q-2].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1].confite_t == 2 and matriz[w][q-2] == matriz[w][q] and matriz[w][q-1].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    if cont != 0:
                        cont = 0
                        print("Es romper horizontal, la 1")
                        cont_cambio += 1
                        puntos[0] += 400
                        print(puntos[0], "puntos")
                        rompe_h(cont_q,cont_w,q,w)
        #####################################ROMPE VERTICAL CUANDO SE ENCUENTRAN 3 EN LA MISMA FILA##################################
                    if matriz[w][q-1] == matriz[w][q-2] and matriz[w][q].confite_t == 3 and matriz[w][q].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1] == matriz[w][q] and matriz[w][q-2].confite_t == 3 and matriz[w][q-2].confite_t2 == matriz[w][q-1].confite_t2:
                        cont += 1
                    elif matriz[w][q-1].confite_t == 3 and matriz[w][q-2] == matriz[w][q] and matriz[w][q-1].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    if cont != 0:
                        cont = 0
                        print("Es romper vertical, la 1")
                        cont_cambio += 1
                        puntos[0] += 400
                        print(puntos[0], "puntos")
                        if  matriz[w][q-2].confite_t == 3:
                            q = q-2
                            cont_cambio += 1
                            rompe_v(cont_q,cont_w,q,w)
                        elif  matriz[w][q-1].confite_t == 3:
                            q = q-1
                            cont_cambio += 1
                            rompe_v(cont_q,cont_w,q,w)
                        elif  matriz[w][q].confite_t == 3:
                            q = q
                            cont_cambio += 1
                            rompe_v(cont_q,cont_w,q,w)
        #####################################ROMPE HORIZONTAL CUANDO SE ENCUENTRAN 3 EN LA MISMA COLUMNA##################################         
                if w == 2 or w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w-2][q] and matriz[w][q].confite_t == 2 and matriz[w][q].confite_t2 == matriz[w-1][q].confite_t2:
                           cont += 1
                    elif matriz[w-1][q] == matriz[w][q] and matriz[w-2][q].confite_t == 2 and matriz[w-2][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q].confite_t == 2 and matriz[w-2][q] == matriz[w][q] and matriz[w-1][q].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    if cont != 0:
                        cont = 0
                        cont_cambio += 1
                        puntos[0] += 400
                        print(puntos[0], "puntos")
                        print("Es romper horizontal, la 2")
                        if  matriz[w-2][q].confite_t == 2:
                            cont_q = w-2
                            cont_cambio += 1
                            rompe_h(cont_q,cont_w,q,w)
                        elif  matriz[w-1][q].confite_t == 2:
                            cont_q = w-1
                            cont_cambio += 1
                            rompe_h(cont_q,cont_w,q,w)
                        elif  matriz[w][q].confite_t == 2:
                            cont_q = w
                            cont_cambio += 1
                            rompe_h(cont_q,cont_w,q,w)
        #####################################ROMPE VERTICAL CUANDO SE ENCUENTRAN 3 EN LA MISMA COLUMNA##################################
                    if matriz[w-1][q] == matriz[w-2][q] and matriz[w][q].confite_t == 3 and matriz[w][q].confite_t2 == matriz[w-1][q].confite_t2:
                           cont += 1
                    elif matriz[w-1][q] == matriz[w][q] and matriz[w-2][q].confite_t == 3 and matriz[w-2][q].confite_t2 == matriz[w-1][q].confite_t2:
                        cont += 1
                    elif matriz[w-1][q].confite_t == 3 and matriz[w-2][q] == matriz[w][q] and matriz[w-1][q].confite_t2 == matriz[w][q].confite_t2:
                        cont += 1
                    if cont != 0:
                        cont = 0
                        print("Es romper vertical, la 2")
                        cont_cambio += 1
                        puntos[0] += 400
                        print(puntos[0], "puntos")
                        rompe_v(cont_q,cont_w,q,w)                                
                
        refresca_matriz()
        if cont_cambio == 0:
            rompe5(puntos)
        else:
            rompe_fusion(puntos)

    def rompe5(puntos):
        colores = [r, v, am, az, m]
        cont_cambio = 0
        cont_q = -1
        cont_w = -1
        for w in range(9):
            cont_q += 1
            cont_w += 1
            for q in range(9):
                if q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q] and matriz[w][q-3] == matriz[w][q] and matriz[w][q-4] == matriz[w][q]:
                        sonido3.play()
                        puntos[0] += 250
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        matriz[cont_q][q-4] = va
                        matriz[cont_q][q-3] = va
                        matriz[cont_q][q-2] = va
                        matriz[cont_q][q-1] = va
                        matriz[cont_q][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        matriz[cont_q][q] = fl
                        matriz[cont_q][q].update_tipo(4)
                        refresca_matriz()
                        pygame.display.update()
                        while cont_q > 0:
                            matriz[cont_q][q-4] = matriz[cont_q-1][q-4]
                            matriz[cont_q-1][q-4] = va
                            refresca_matriz()
                            matriz[cont_q][q-3] = matriz[cont_q-1][q-3]
                            matriz[cont_q-1][q-3] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q-2] = matriz[cont_q-1][q-2]
                            matriz[cont_q-1][q-2] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q-1] = matriz[cont_q-1][q-1]
                            matriz[cont_q-1][q-1] = va
                            refresca_matriz()
                            pygame.display.update()
                            cont_q -= 1
                        if cont_q == 0:
                            a = random.choice(colores)
                            matriz[cont_q][q-4] = a
                            refresca_matriz()
                            pygame.display.update()
                            b = random.choice(colores) 
                            matriz[cont_q][q-3] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_q][q-2] = c
                                refresca_matriz()
                                pygame.display.update()
                                d = random.choice(colores) 
                                matriz[cont_q][q-1] = d
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_q][q-2] = c
                                refresca_matriz()
                                pygame.display.update()
                                d = random.choice(colores) 
                                matriz[cont_q][q-1] = d
                                refresca_matriz()
                                pygame.display.update()
                            rompe_fusion(puntos)
                            return
                if w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q] and matriz[w-3][q] == matriz[w][q] and matriz[w-4][q] == matriz[w][q]:
                        sonido3.play()
                        puntos[0] += 250
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        matriz[cont_w-4][q] = va
                        matriz[cont_w-3][q] = va
                        matriz[cont_w-2][q] = va
                        matriz[cont_w-1][q] = va
                        matriz[cont_w][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        matriz[cont_w][q] = fl
                        matriz[cont_w][q].update_tipo(4)
                        refresca_matriz()
                        pygame.display.update()
                        while cont_w > 4:
                            matriz[cont_w-4][q] = matriz[cont_w-5][q]
                            matriz[cont_w-5][q] = va
                            refresca_matriz()
                            pygame.display.update()                            
                            matriz[cont_w-3][q] = matriz[cont_w-4][q]
                            matriz[cont_w-4][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w-2][q] = matriz[cont_w-3][q]
                            matriz[cont_w-3][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w-1][q] = matriz[cont_w-2][q]
                            matriz[cont_w-2][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            cont_w -= 1
                        if cont_w == 4:
                            a = random.choice(colores)
                            matriz[cont_w-1][q] = a
                            refresca_matriz()
                            pygame.display.update()
                            b = random.choice(colores) 
                            matriz[cont_w-2][q] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_w-3][q] = c
                                refresca_matriz()
                                pygame.display.update()
                                d = random.choice(colores) 
                                matriz[cont_w-4][q] = d
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_w-3][q] = c
                                refresca_matriz()
                                pygame.display.update()
                                d = random.choice(colores) 
                                matriz[cont_w-4][q] = d
                                refresca_matriz()
                                pygame.display.update()
                    
        refresca_matriz()
        if cont_cambio == 0:
            rompe4(puntos)
        else:
            rompe_fusion(puntos)
        
    def rompe4(puntos):
        colores = [r, v, am, az, m]
        colores2 = [fr, fv, fam, faz, fm]
        cont_cambio = 0
        cont_q = -1
        cont_w = -1
        for w in range(9):
            cont_q += 1
            cont_w += 1
            for q in range(9):
                if q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    lista_iguales = [matriz[w][q], matriz[w][q-1], matriz[w][q-2], matriz[w][q-3]]
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q] and matriz[w][q-3] == matriz[w][q]:
                        sonido2.play()
                        puntos[0] += 200
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        h = matriz[cont_q][q]
                        matriz[cont_q][q-3] = va
                        matriz[cont_q][q-2] = va
                        matriz[cont_q][q-1] = va
                        matriz[cont_q][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        matriz[cont_q][q] = h
                        for x in colores:
                            if matriz[cont_q][q] == x:
                                i = colores.index(x)
                                matriz[cont_q][q] = colores2[i]
                                matriz[cont_q][q].update_tipo(2)
                                refresca_matriz()
                                pygame.display.update()
                        while cont_q > 0:
                            matriz[cont_q][q-3] = matriz[cont_q-1][q-3]
                            matriz[cont_q-1][q-3] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q-2] = matriz[cont_q-1][q-2]
                            matriz[cont_q-1][q-2] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q-1] = matriz[cont_q-1][q-1]
                            matriz[cont_q-1][q-1] = va
                            refresca_matriz()
                            pygame.display.update()
                            cont_q -= 1
                        if cont_q == 0:
                            a = random.choice(colores)
                            matriz[cont_q][q-3] = a
                            refresca_matriz()
                            pygame.display.update()
                            b = random.choice(colores) 
                            matriz[cont_q][q-2] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_q][q-1] = c
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_q][q-1] = c
                                refresca_matriz()
                                pygame.display.update()
                            rompe_fusion(puntos)
                            return
                if w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q] and matriz[w-3][q] == matriz[w][q]:
                        sonido2.play()
                        puntos[0] += 200
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        h = matriz[cont_w][q]
                        matriz[cont_w-3][q] = va
                        matriz[cont_w-2][q] = va
                        matriz[cont_w-1][q] = va
                        matriz[cont_w][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        matriz[cont_w][q] = h
                        for x in colores:
                            if matriz[cont_w][q] == x:
                                i = colores.index(x)
                                matriz[cont_w][q] = colores2[i]
                                matriz[cont_w][q].update_tipo(3)
                                refresca_matriz()
                                pygame.display.update()
                        while cont_w > 3:
                            matriz[cont_w-3][q] = matriz[cont_w-4][q]
                            matriz[cont_w-4][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w-2][q] = matriz[cont_w-3][q]
                            matriz[cont_w-3][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w-1][q] = matriz[cont_w-2][q]
                            matriz[cont_w-2][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            cont_w -= 1
                        if cont_w == 3:
                            a = random.choice(colores)
                            matriz[cont_w-1][q] = a
                            refresca_matriz()
                            pygame.display.update()
                            b = random.choice(colores) 
                            matriz[cont_w-2][q] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_w-3][q] = c
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_w-3][q] = c
                                refresca_matriz()
                                pygame.display.update()
        refresca_matriz()
        if cont_cambio == 0:
            rompe3(cantidad_moves, puntos)
        else:
            rompe_fusion(puntos)
    def rompe3(cantidad_moves, puntos):
        colores = [r, v, am, az, m]
        cont_cambio = 0
        cont_q = -1
        cont_w = -1
        for w in range(9):
            cont_q += 1
            cont_w += 1
            for q in range(9):
                if q == 2 or q == 3 or q == 4 or q == 5 or q == 6 or q == 7 or q == 8:
                    if matriz[w][q-1] == matriz[w][q] and matriz[w][q-2] == matriz[w][q]:
                        sonido1.play()
                        puntos[0] += 150
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        matriz[cont_q][q-2] = va
                        matriz[cont_q][q-1] = va
                        matriz[cont_q][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        while cont_q > 0:
                            matriz[cont_q][q-2] = matriz[cont_q-1][q-2]
                            matriz[cont_q-1][q-2] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q-1] = matriz[cont_q-1][q-1]
                            matriz[cont_q-1][q-1] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_q][q] = matriz[cont_q-1][q]
                            matriz[cont_q-1][q] = va
                            cont_q -= 1
                            refresca_matriz()
                            pygame.display.update()
                        if cont_q == 0:
                            a = random.choice(colores)
                            matriz[cont_q][q-2] = a
                            refresca_matriz()
                            b = random.choice(colores)
                            matriz[cont_q][q-1] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_q][q] = c
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_q][q] = c
                                refresca_matriz()
                                pygame.display.update()
                            rompe_fusion(puntos)
                            return
                if w == 2 or w == 3 or w == 4 or w == 5 or w == 6 or w == 7 or w == 8:
                    if matriz[w-1][q] == matriz[w][q] and matriz[w-2][q] == matriz[w][q]:
                        sonido1.play()
                        puntos[0] += 150
                        print(puntos[0], "puntos")
                        cont_cambio += 1
                        matriz[cont_w-2][q] = va
                        matriz[cont_w-1][q] = va
                        matriz[cont_w][q] = va
                        refresca_matriz()
                        pygame.display.update()
                        pygame.time.wait(500)
                        while cont_w > 2:
                            matriz[cont_w-2][q] = matriz[cont_w-3][q]
                            matriz[cont_w-3][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w-1][q] = matriz[cont_w-2][q]
                            matriz[cont_w-2][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            matriz[cont_w][q] = matriz[cont_w-1][q]
                            matriz[cont_w-1][q] = va
                            refresca_matriz()
                            pygame.display.update()
                            cont_w -= 1
                        if cont_w == 2:
                            a = random.choice(colores)
                            matriz[cont_w][q] = a
                            refresca_matriz()
                            pygame.display.update()
                            b = random.choice(colores) 
                            matriz[cont_w-1][q] = b
                            refresca_matriz()
                            pygame.display.update()
                            if a == b:
                                colores.remove(b)
                                c = random.choice(colores)
                                colores.append(b)
                                matriz[cont_w-2][q] = c
                                refresca_matriz()
                                pygame.display.update()
                            else:
                                c = random.choice(colores)
                                matriz[cont_w-2][q] = c
                                refresca_matriz()
                                pygame.display.update()
        refresca_matriz()
        pygame.display.update()
        if cont_cambio == 0:
            print("bien, el programa ve que no hay convinaciones")
            del datos[0]
            del datos[0]
            del datos[0]
            del datos[0]
            cantidad_moves.remove(cantidad_moves[-1])
            print(cantidad_moves[-1])
            if len(cantidad_moves) == 1:
                pygame.mixer.quit()
                fin(name,puntos)
            refresca_matriz()
        else: 
            rompe_fusion(puntos)

    def rev_cambio(datos):
        cx1, cy1 = datos[0]
        px1, py1 = datos[1]
        cx2, cy2 = datos[2]
        px2, py2 = datos[3]
        g = matriz[px1][py1]
        matriz[px1][py1] = matriz[px2][py2]
        matriz[px2][py2] = g
        matriz[px1][py1].update(display_game, cy1, cx1)
        matriz[px2][py2].update(display_game, cy2, cx2)
        refresca_matriz()
        del datos[0]
        del datos[0]
        del datos[0]
        del datos[0]
    def refresca_puntaje():
        fuente = pygame.font.Font(None, 45)
        
        text = str(puntos[0])
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (670,60))

        text = "Puntos"
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (605,90))

        text = str(cantidad_moves[-1])
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (670,500))

        text = "Movimientos"
        mensaje = fuente.render(text, 1, (255, 255, 255))
        display_game.blit(mensaje, (605,530))
        
    def refresca_matriz():
        imagen_f = pygame.image.load("bleach_py2.jpg")
        display_game.blit(imagen_f,(0,0))
        refresca_puntaje()
        pygame.display.update
        pygame.draw.lines(display_game, (255,255,255), False, [(10,10), (10,550), (70,550), (70,10), (130,10), (130,550), (190,550),(190, 10), (250,10), (250,550), (310,550), (310,10), (370,10), (370,550), (430,550), (430,10), (490,10), (490,550), (550,550), (550,10), (10,10), (10,70), (550,70), (550,130), (10,130), (10,190), (550,190), (550,250), (10,250), (10,310), (550,310), (550,370), (10,370), (10,430), (550, 430), (550,490), (10,490), (10,550), (550,550)], 3)
        ini = -50
        for q in range(9):
            ini = ini+60
            fin = -50
            for w in range(9):
                fin = fin + 60            
                matriz[w][q].update(display_game, ini, fin)
                
    fail = False
    datos = []

    cantidad_moves = []
    puntos = [0]
    for x in range(51):######################################################################################################
        cantidad_moves.append(x)

    refresca_puntaje()
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = pygame.mouse.get_pos()
                if x > 9 and x < 551 and y > 9 and y < 551:
                    moves(datos)
                    if len(datos) == 4:
                        cambia_posicion(datos)


        mouse2.update()
        reloj2.tick(60)
        pygame.draw.lines(display_game, (255,255,255), False, [(10,10), (10,550), (70,550), (70,10), (130,10), (130,550), (190,550),(190, 10), (250,10), (250,550), (310,550), (310,10), (370,10), (370,550), (430,550), (430,10), (490,10), (490,550), (550,550), (550,10), (10,10), (10,70), (550,70), (550,130), (10,130), (10,190), (550,190), (550,250), (10,250), (10,310), (550,310), (550,370), (10,370), (10,430), (550, 430), (550,490), (10,490), (10,550), (550,550)], 3)
        pygame.display.update()

def menu():
    pygame.init()
    
    pygame.mixer.music.load("Bleach.D-tecnoLife.mp3")
    pygame.mixer.music.play(5)

    display_width = 800
    display_height = 600

    display_game = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption("Bleach Souls Sagas")

    reloj1 = pygame.time.Clock()
    mouse1 = mouse()
        
    img_ng = pygame.image.load("new_game.png")
    img_ng2 = pygame.image.load("new_game2.png")
    boton_ng = boton(img_ng, img_ng2, img_ng, 315, 485)
    
    img_h = pygame.image.load("high_score.png")
    img_h2 = pygame.image.load("high_score2.png")
    boton_h = boton(img_h, img_h2, img_h, 5, 20)

    img_opt = pygame.image.load("options.png")
    img_opt2 = pygame.image.load("options2.png")
    boton_opt = boton(img_opt, img_opt2, img_opt, 620, 545)

    img_ex = pygame.image.load("exit.png")
    img_ex2 = pygame.image.load("exit2.png")
    boton_ex = boton(img_ex, img_ex2, img_ex, 315, 545)

    img_eyn = pygame.image.load("enter_your_name.png")
    boton_eyn = boton(img_eyn, img_eyn, img_eyn, 300, 100)

    img_st = pygame.image.load("start.png")
    img_st2 = pygame.image.load("start2.png")
    img_st3 = pygame.image.load("start3.png")
    boton_st = boton(img_st, img_st2, img_st3, 315, 485)
    name = ""
    b_cambio = 0

    img_b = pygame.image.load("back.png")
    img_b2 = pygame.image.load("back2.png")
    boton_b = boton(img_b, img_b2, img_b, 315, 545)  
        
    imagen_f = pygame.image.load("bleach_py.jpg")
    display_game.blit(imagen_f,(0,0))

    def high_score():
        lista_puntos = []
        lista_nombres = []
        archi=open('high_score.txt','r')
        lineas=archi.readlines()
        for a in lineas:
            b = a.split(".")
            lista_puntos.append(b[0])
            lista_nombres.append(b[1])
        archi.close()

        indice = len(lista_puntos)
        i= 0
        while (i < indice):
            j = i
            while (j < indice):
                if(lista_puntos[i] < lista_puntos[j]):
                    temp = lista_puntos[i]
                    temp2 = lista_nombres[i]
                    lista_puntos[i] = lista_puntos[j]
                    lista_nombres[i] = lista_nombres[j]
                    lista_puntos[j] = temp
                    lista_nombres[j] = temp2
                j= j+1
            i=i+1

        fuente = pygame.font.Font(None, 35)
        x = 20
        y = 30
        i = 0
        for n in range(1,4):
            text = str(n)
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x,y))
            lista_nombres[i] = lista_nombres[i][:-1]
            text = lista_nombres[i]
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x+50,y))
            text = str(lista_puntos[i])
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x+165,y))
            
            y += 30
            i += 1
        x = 20
        y = 218
        for m in range(4,11):
            text = str(m)
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x,y))
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x,y))
            lista_nombres[i] = lista_nombres[i][:-1]
            text = lista_nombres[i]
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x+50,y))
            text = str(lista_puntos[i])
            mensaje = fuente.render(text, 1, (255, 255, 255))
            display_game.blit(mensaje, (x+165,y))
            
            y += 30
            i += 1
            if i == 11:
                return

    fuente = pygame.font.Font(None, 47)
    

    fail = False
    botones_menu1 = True
    eventos_menu1 = True
    botones_high_score = False
    eventos_high_score = False
    botones_menu2 = False
    eventos_menu2 = False
    evento_escritura = False
    while not fail:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if eventos_menu1 == True:
                    if mouse1.colliderect(boton_ex.rect):
                        pygame.quit()
                        quit()
                    if mouse1.colliderect(boton_ng.rect):
                        botones_menu1 = False
                        eventos_menu1 = False
                        botones_menu2 = True
                        eventos_menu2 = True
                        evento_escritura = True
                    if mouse1.colliderect(boton_h.rect):
                        botones_menu1 = False
                        eventos_menu1 = False
                        botones_high_score = True
                        eventos_high_score = True
                if eventos_high_score == True:
                    if mouse1.colliderect(boton_b.rect):
                        botones_menu1 = True
                        eventos_menu1 = True
                        botones_high_score = False
                        eventos_high_score = False
                if eventos_menu2 == True:
                    if mouse1.colliderect(boton_b.rect):
                        botones_menu1 = True
                        eventos_menu1 = True
                        botones_menu2 = False
                        eventos_menu2 = False
                        evento_escritura = False
                        name = ""
                        display_game.blit(imagen_f,(0,0))
                        b_cambio = 0
                    if mouse1.colliderect(boton_st.rect):
                        if b_cambio == 1:
                            botones_menu2 = False
                            eventos_menu2 = False
                            evento_escritura = False
                            pygame.mixer.quit()
                            imagen_f = pygame.image.load("cambio.jpeg")
                            display_game.blit(imagen_f,(0,0))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            juego(name)
            if event.type == pygame.KEYDOWN:
                if evento_escritura == True:
                    if event.unicode.isalpha():
                        if len(name) < 8:
                            name += event.unicode
                    if event.key == K_BACKSPACE:
                        name = name[:-1]
                    if event.key == K_RETURN:
                        if b_cambio == 1:
                            botones_menu2 = False
                            eventos_menu2 = False
                            evento_escritura = False
                            pygame.mixer.quit()
                            imagen_f = pygame.image.load("cambio.jpeg")
                            display_game.blit(imagen_f,(0,0))
                            pygame.display.update()
                            pygame.time.wait(3000)
                            juego(name)
                    if event.key == K_ESCAPE:
                        name = ""
                    if name == "":
                        b_cambio = 0
                    else:
                        b_cambio = 1
                print(name)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        mensaje = fuente.render(name, True, (255, 255, 255))
        a = mensaje.get_rect()
        a.center = display_game.get_rect().center 
        display_game.blit(mensaje, a)
        display_game.blit(imagen_f,(0,0))
        display_game.blit(mensaje, a)
        
        if botones_menu1 == True:
            boton_ng.update(display_game, mouse1, 315, 485)
            boton_ex.update(display_game, mouse1, 315, 545)
            boton_h.update(display_game, mouse1, 5, 20)
            boton_opt.update(display_game, mouse1, 620, 545)
        if botones_menu2 == True:
            boton_b.update(display_game, mouse1, 315, 545)
            boton_st.update2(display_game, mouse1, name, 315, 485)
            boton_eyn.update(display_game, mouse1, 300, 100)
        if botones_high_score == True:
            high_score()
            boton_b.update(display_game, mouse1, 315, 545)

        reloj1.tick(60)
        mouse1.update()
        pygame.display.update()

menu()
