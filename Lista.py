from tda_lista import Nodo_Lista ,Lista, lista_vacia, listacaracteres, listaint, listaneg, listastring, insertar, insertar_vec, eliminar,eliminar_vec, criterio,busqueda_lista,busqueda_lista_vec,tamanio_lista, barrido_lista,barrido_sublista
from random import randint, choice
from time import sleep
from datetime import date


#1. 

def cantidad_nodos(lista):
    c = 0
    aux = lista.inicio
    while aux is not None:
        aux = aux.sig
        c += 1
    print('La cantidad de nodos es: ', c)
#lista  = Lista()
#listaint(lista, 7)
#barrido_lista(lista)
#cantidad_nodos(lista)

#2.

#lista = Lista()
#listastring(lista, 7)
#barrido_lista(lista)

def eliminar_vocales(lista):
    aux = lista.inicio
    while aux is not None:
        if aux.info == 'a' or aux.info == 'e' or aux.info == 'i' or aux.info == 'o' or aux.info == 'u' or aux.info == 'A' or aux.info == 'I' or aux.info == 'E' or aux.info == 'O' or aux.info == 'U':
            eliminar(lista, aux.info)
        aux = aux.sig
    print('La lista sin vocales es : ')
    barrido_lista(lista)

#eliminar_vocales(lista)

#3. 

'''lista = Lista()
listaint(lista,6)
barrido_lista(lista)'''

def dividir_lista(lista):
    aux = lista.inicio
    lista_par = Lista()
    while aux is not None: 
        if aux.info % 2 == 0 :
            insertar(lista_par, aux.info)
            eliminar(lista,aux.info)
        aux = aux.sig
    print('Lista par es :')
    barrido_lista(lista_par)
    print('la lista de impares es: ')
    barrido_lista(lista)

#dividir_lista(lista)

#4
lista = Lista()

def pos_iesima(l, pos):
    nodo = Nodo_Lista()
    nodo.info = 1999
    aux = lista.inicio
    if pos >= 0 and pos <= lista.tamanio:
        if pos < l.tamanio:
            for i in range(1, pos):
                aux = aux.sig
            nodo.sig = aux.sig
            aux.sig = nodo
        else:
            while aux.sig is not None:
                aux = aux.sig
            aux.sig = nodo
    barrido_lista(lista)

#5. 

'''lista = Lista()
listaint(lista,6)
barrido_lista(lista)'''

def eliminar_primos(lista):
    aux = lista.inicio
    while aux is not None:
        cd= 0        
        for i in range (1, aux.info):
            if aux.info % i == 0:
                cd += 1
        if cd < 2:
            eliminar(lista, aux.info)
        aux = aux.sig
    print('Lista sin primos: ')
    barrido_lista(lista)

#eliminar_primos(lista)

#6

comic  =  Lista ()
nombre  = [ 'Linterna Verde' , 'Wolverine' , 'Dr. Strange' , 'Capitana Marvel' ,
'Mujer Maravilla' , 'Flash' , 'Star-Lord' , 'Joker' ]
año  = [ 1940 , 1974 , 1963 , 1968 , 1941 , 1940 , 1976 , 1940 ]
casacomic  = [ 'DC' , 'Marvel' , 'DC' , 'Marvel' , 'DC' , 'DC' , 'Marvel' , 'DC' ]
biografia  = [ 'traje: verde, arma: anillo de poder' , 'poderosa capacidad de regeneración' ,'hechicero supremo' , 'guerrera extraterrestre de la civilizacion Kree' , 'princesa guerrera de las amazonas' , 'capacidad de correr, moverse y pensar rápido' ,'policia interplanetario' , 'criminal mas notable de Gotham City' ]
maravilla , dc  =  0 , 0

for  i  in  range ( len(nombre)):
    insertar (comic, [ nombre [ i ], año [ i ], casacomic [ i ], biografia [ i ]])
#barrido_lista (comic)

#a. 

def eliminiar_nodo(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Linterna Verde':
            eliminar(comic, aux.info)
        aux = aux.sig
    print('Lista sin linterna verde: ' )
    barrido_lista(comic)
#eliminiar_nodo(comic)

#b.

def mostrar_anio(comic):
    aux= comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Wolverine':
            print ('El año de aparicion es:', dato[1])
        aux = aux.sig
#mostrar_anio(comic)

#c. 

def cambiar_casa(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Dr. Strange':
            dato[2]= 'Marvel'
        aux = aux.sig
    print(dato)
#cambiar_casa(comic)

#d.

def mostrar_superheroe(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[3].find('traje') >= 0 or dato[3].find('armadura') >= 0:
            print(dato[0])
        aux = aux.sig

#mostrar_superheroe(comic)

#e.

def anterior_anio(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[1] < 1963:
            print (dato[0], 'aperecio antes de 1963 y su casa es: ', dato[2])
        aux = aux.sig
#anterior_anio(comic)

#f.

def casa_s(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Capitana Marvel' or dato[0] == 'Mujer Maravilla':
            print('La casa de ' , dato[0], 'es: ', dato[2])
        aux = aux.sig
#casa_s(comic)

#g.

def informaciion(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        if dato[0] == 'Flash' or dato[0] == 'Star-Lord':
            print(dato)
        aux = aux.sig

#informaciion(comic)

#h.

def listas_s(comic):
    aux = comic.inicio
    while aux is not None:
        dato = aux.info
        cad = dato[0]
        if cad[0] == 'B' or cad[0] == 'M' or cad[0] == 'S':
            print(dato)
        aux = aux.sig
#listas_s(comic)

#i.

def cantidad_s(comic):
    aux = comic.inicio
    cdm= 0
    cdc= 0
    while aux is not None:
        dato = aux.info
        if dato[2] == 'Marvel':
            cdm += 1
        elif dato[2] == 'DC':
            cdc += 1
        aux = aux.sig
    print('La cantidad de supeerheroes de DC es: ', cdc)
    print('La cantidad de supeerheroes de Marvel es: ', cdm)

#cantidad_s(comic)

#7

#a. concatenar dos listas

# a. concatenar dos listas

def concatenarlistas(lista1, lista2):
    conc = Lista()
    conc = lista1
    aux = conc.inicio
    while aux.sig is not None:
        aux = aux.sig
        aux.sig = lista2.inicio
    print('Lista concantenada: ')
    barrido_lista(conc)

#b concatenar 2 listas omitiendo los datos repetidos y manteniendo su orden
#c interseccion

def lista_sin_repetidos(lista1, lista2):
        lista_sr = Lista()
        aux = lista1.inicio
        while aux is not None:
            if busqueda_lista(lista_sr, aux.info) is None:
                insertar(lista_sr, aux.info)
            aux = aux.sig
        aux = lista2.inicio
        while aux is not None:
            if busqueda_lista(lista_sr, aux.info) is None:
                insertar(lista_sr, aux.info)
            aux = aux.sig
        print('Lista concatenada sin repetidos:')
        barrido_lista(lista_sr)
        print('Interseccion de las listas: ', tamanio_lista(lista_sr))

#D

def eliminar_mostrar_nodos(lista):
        aux = lista.inicio
        while aux is not None:
            eliminar(lista, aux.info)
            print('Se elimino la siguiente información:', aux.info)
            aux = aux.sig


#9

alumnos = ['Milagros', 'Victtoria', 'Fernanda', 'Nahuel', 'Cristian', 'Rocio']
apellidos = ['Gimenez', 'Gonzales', 'Marks', ' Maiz', 'Caballier', 'Alcoba']
materias = ['Calculo', ' Matematica discreta','Algebra','Ecuaciones diferenciales']

class Alumno(object):
    def __init__(self,nombre,apellido,legajo):
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo

def __str__(self):
        return '<<<    ' + self.nombre + ' - ' + self.apellido + ' - ' + str(self.legajo) + '    >>>'

class Parcial(object):
    def __init__(self,materia,nota,fecha):
        self.materia = materia
        self.nota = nota
        self.fecha = fecha

    def __str__(self):
        return '' + self.materia + '|| Nota = '+ str(self.nota) + '|| fecha = ' + str(self.fecha)

def parciales(lista):
    print('Alumnos ordenados por apellido: ')
    for i in range(len(alumnos)):
        legajo = i+1
        dato = Alumno(alumnos[i],apellidos[i],legajo)
        insertar(lista, dato, 'apellido')
    barrido_lista(lista)
    for i in range(tamanio_lista(lista)):
        i += 1
        for j in range(3):
            pos = busqueda_lista(lista,i,'legajo')
            dato = Parcial(materias[j],randint(4,10),date(2020,randint(1,12),randint(1,30)))
            insertar(pos.sublista, dato, 'materia')
    barrido_sublista(lista)
    print(' ')
    aux = lista.inicio
    p = 0
    while aux != None:
        aprobado = True
        cont = 0
        prom = 0
        pos = aux.sublista.inicio
        while pos != None:
            cont += 1
            if pos.info.nota < 7:
                aprobado = False
            prom += pos.info.nota
            pos = pos.sig
        if aprobado == True:
            print(aux.info.nombre + ' ' + aux.info.apellido + ' aprobó todas las materias')
        if ((prom / cont) > 8.89):
            p += 1
            print(aux.info.nombre + ' ' + aux.info.apellido + ' Tiene promedio mayor a 8,89, su promedio es: ' + str(round(prom/cont,2)))
        aux = aux.sig
    if (p < 1):
        print('Ningun alumno tiene promedio mayor a 8,89.')
    print('')
    print('Alumnos con apellido que comienza con L')
    aux = lista.inicio
    while aux != None:
        if aux.info.apellido[0] == 'L':
            print(aux.info.nombre + ' ' + aux.info.apellido + ';  legajo ' + str(aux.info.legajo))
        aux = aux.sig
    print('')
    print('Promedio general:')
    aux = lista.inicio
    while aux != None:
        suma_notas = 0
        c = 0
        pos = aux.sublista.inicio
        while pos != None:
            suma_notas += pos.info.nota
            c += 1
            pos = pos.sig
        prom = (suma_notas / c)
        print('El promedio de el alumno ' + aux.info.nombre + ' ' + aux.info.apellido + ' es ' + str(round(prom,2)))
        aux = aux.sig


'''

#10

spotify = Lista()
nombre = ['Closer' , 'Creo en ti', 'Thinking Out Loud', 'Billie Eilish' , 'Sunflower', '7 Rings' , 'Old Town Road', 'Do I Wanna Know', 'R U Mine']
artista = ['The Chainsmokers', 'Reik','Ed Sheeran', 'Billie Eilish', 'Post Malone', 'Ariana Grande', 'Lil Nas X','Arctic Monkeys','Arctic Monkeys']
duracion = [ 3.10 , 3.30 , 3.25 , 4.15 , 2.55 , 3.00, 4.00 , 5.20, 2.52]
reproducciones = [1008 , 4078 , 1200 , 3500 , 6500 , 7890, 360, 2003, 2345]
 
for  i  in  range ( len(nombre)):
    insertar (spotify, [ nombre [ i ], artista [ i ], duracion [ i ], reproducciones [ i ]])
#barrido_lista (spotify)

#a.

def cancion_mas_larga(spotify):
    aux = spotify.inicio
    c_larga = 0
    while aux is not None:
        dato = aux.info
        if dato[2] > c_larga:
            c_larga = dato[2]
            info = dato
        aux = aux.sig
    print(info)  

cancion_mas_larga(spotify)   
            
#b. 

def top5(spotify):
    aux = spotify.inicio
    c_escuchada = 0
    while aux is not None:
        dato = aux.info
        if dato[3] > c_escuchada:

#c.

def canciones_banda(spotify):
    aux = spotify.inicio
    while aux is not None:
        dato = aux.info
        if dato[1] == 'Arctic Monkeys':
            print('Las canciones de Arctic Monkeys son: ', dato[0])
        aux = aux.sig

#canciones_banda(spotify)

#d.

def bandas_1palabra (spotify):
    aux = spotify.inicio
    while aux is not None:
        dato = aux.info
        if dato [1].find ' ':
            print'''

#Ej11

class Personaje(object):
    def __init__(self,nombre,altura,edad,genero,especie,planeta):
        self.nombre = nombre
        self.altura = altura
        self.edad = edad
        self.genero = genero
        self.especie = especie
        self.planeta = planeta

def __str__(self):
    return self.nombre+'  || Altura: ' +str(self.altura) +',    Edad: '+str(self.edad)+ ',    Genero: '+self.genero+ ',    Especie: '+self.especie+',    Planeta: '+self.planeta

class Episodios(object):
    def __init__(self,episodio):
        self.episodio = episodio
    def __str__(self):
        return 'Episodio: ' + str(self.episodio)


personajes = ['Luke Skywalker','Beru Lars', 'R2-D2', 'Han Solo', 'Maestro Yoda', 'Jar Jar Binks','Darth Vader','Chewbacca','Leia Organa']
alturas = [1.72 , 1.65 , 0.38 , 1.74 , 0.60 , 1.96 , 1.84 , 2.30 , 1.55]
edades = [47,37,853,54,917,1382,1059,987,90]
generos = ['M','F','Bot','M','M','M','M','M','F']
especies = ['Humano','Humano','Droide','Humano','Yoda','Gungan','Darth','Wookiee','Humano']
planetas = ['Tatooine','Tatooine','Naboo','Corellia','896 ABY','Naboo','Tatooine','Kashyyyk','Alderaan']
episodios = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for i in range(len(personajes)):
    dato = Personaje(personajes[i],alturas[i],edades[i],generos[i],especies[i],planetas[i])
    insertar(lista,dato,'planeta')
aux = lista.inicio
while not aux == None:
    cant = (randint(1,15))
    lista_epis = []
    for i in range(cant):
        epis = choice(episodios)
        if len(lista_epis) == 0:
            lista_epis.append(epis)
            insertar(aux.sublista,Episodios(epis),'episodio')
        if epis not in lista_epis:
            insertar(aux.sublista,Episodios(epis),'episodio')
            lista_epis.append(epis)
    aux = aux.sig
print('Lista de personajes ordenada segun Planetas Natales: ')
barrido_lista(lista)
print()
aux = lista.inicio
# A
print('Lista de personajes FEMENINOS')
while aux != None:
    if aux.info.genero == 'F':
        print(aux.info)
    aux = aux.sig
print()
# B
print('Lista de los personajes de especie Droide, que aparecieron en los primeros seis episodios de la saga:')
aux = lista.inicio
while not aux == None:
    pos = aux.sublista.inicio
    while not pos == None:
        if pos.info.episodio == 1:
            print(aux.info.nombre + ' aparecio en el capitulo 1.')
        elif pos.info.episodio == 2:
            print(aux.info.nombre + ' aparecio en el capitulo 2.')
        elif pos.info.episodio == 3:
            print(aux.info.nombre + ' aparecio en el capitulo 3.')
        elif pos.info.episodio == 4:
            print(aux.info.nombre + ' aparecio en el capitulo 4.')
        elif pos.info.episodio == 5:
            print(aux.info.nombre + ' aparecio en el capitulo 5.')
        elif pos.info.episodio == 6:
            print(aux.info.nombre + ' aparecio en el capitulo 6.')
        else:
            break
        pos = pos.sig
    aux = aux.sig
# C
print()
print('-información de Darth Vader y Han Solo')
aux = lista.inicio
while aux != None :
    if (aux.info.nombre == 'Darth Vader') or (aux.info.nombre == 'Han Solo'):
        print(aux.info)
    aux = aux.sig
# D
print()
print('Personajes que aparecen en el episodio VII y en los tres anteriores:')
aux = lista.inicio
p = 0
while aux != None:
    pos = aux.sublista.inicio
    c = 0
    while pos != None:
        if pos.info.episodio == 4:
            c += 1
        elif pos.info.episodio == 5:
            c += 1
        elif pos.info.episodio == 6:
            c +=1
        elif pos.info.episodio == 7:
            c += 1
            if c == 4:
                print(aux.info.nombre +', aparecio en los capitulos 4,5,6 y 7.')
                p += 1
        pos = pos.sig
    aux = aux.sig
if p == 0:
    print('__No hay personajes que mostrar en esta lista.')
# E
print()
print('Personajes con edad mayor a 850 años')
aux = lista.inicio
mayor = ''
ed = 0
while aux != None:
    if aux.info.edad > 850:
        print(aux.info.nombre + ': tiene ' + str(aux.info.edad) + ' años.')
    if ed < aux.info.edad:
        mayor = aux.info.nombre
        ed = aux.info.edad
    aux = aux.sig
print()
print('<<< El personaje de mayor EDAD es: '+ mayor+ ', con '+ str(ed) +' años >>>')
# F
print()
print('Se eliminaran los personajes que hayan aparecido solamente en los capitulos: 4,5 y 6')
aux = lista.inicio
p = 0
while aux != None:
    pos = aux.sublista.inicio
    c = 0
    n = 0
    while pos != None:
        if pos.info.episodio == 4:
            c += 1
        elif pos.info.episodio == 5:
            c += 1
        elif pos.info.episodio == 6:
            c += 1
        else:
            n += 1
            break
        pos = pos.sig
    if (c == 3) and (n == 0):
        eliminar(lista,aux.info.nombre,'nombre')
        print('Se ha eliminado al personaje '+ aux.info.nombre)
        p += 1
    aux = aux.sig
if p == 0:
    print('__No hay personajes que mostrar en esta lista.')
print()
# G
print('Personajes Humanos cuyo planeta de origen es Alderaan;')
aux = lista.inicio
while aux != None:
    if (aux.info.especie == 'Humano') and (aux.info.planeta == 'Alderaan'):
        print(aux.info.nombre +': es Humano y su planeta natal es: ' + aux.info.planeta) 
    aux = aux.sig
print()
# H
print('Personajes cuya altura es menor a 70 centímetros;')
aux = lista.inicio
while aux != None:
    if aux.info.altura < 0.70:
        print(aux.info)
    aux = aux.sig
print()
# I
aux = lista.inicio
while aux != None:
    if aux.info.nombre == 'Chewbacca':
        print('- Informacion de Chewbacca:')
        print(aux.info)
        print('>>> Episodios en los que aparece:')
        pos = aux.sublista.inicio
        while pos != None:
            print(pos.info.episodio)
            pos = pos.sig
    aux = aux.sig
print()

#12

def elim_el(lista):
    print('LISTA:')
    barrido_lista(lista)
    aux = lista.inicio
    i = 0
    while aux != None:
        if (i == tamanio_lista(lista)-1) :
            eliminar(lista,aux.info)
            print('')
        i+=1
        aux = aux.sig
    print('Lista sin anteultimo nodo:')
    barrido_lista(lista)


jugadores = ['Adrian',' Walter','Julio','Silvina','Marisa','Lourdes','Solange']
turnos = [1,2,3,4,5,6,7]
dados = [1,2,3,4,5,6]

class Jugador(object):
    def __init__(self, nombre,turno):
        self.nombre = nombre
        self.turno = turno
    def __str__(self):
        return self.nombre +' | turno numero: ' + str(self.turno)
    
def dados(lista):
    t = []
    for i in range(len(jugadores)):
        turno = None
        while turno == None:
            turno = randint(1,len(jugadores))
            if turno in t:
                turno = None
            else:
                t.append(turno)
        
        insertar(lista,Jugador(jugadores[i],turno),'turno')
        print(str(turno) + '.- sera la posicion de ' + jugadores[i])
    print('')
    print('--- Jugadores por turnos ---')
    barrido_lista(lista)
    print('')
    print('--- Comienza el juego ---')
    aux = lista.inicio
    while aux != ' ':
        dado = (choice(dados))
        sleep(1)
        print('Dado = ' + str(dado))
        if dado == 5:
            break
        else:
            print('El jugador ha sacado ' + str(dado))
            print('...Turno del siguiente jugador...')
        aux = aux.sig
        if aux == None:
            aux = lista.inicio
    print('El jugador ' + aux.info.nombre + ' ha ganado')

#Eej15

entrenadores = ['Rosario','Tamara','Josefina','Daniela','Norman','Mariano','Carmen','Sara']
pokemon = { 'Bulbasaur' : ['panta','veneno'] , 'Charmander' : ['fuego','None'] , 'Squirtle': ['Agua','None'],
            'Pelipper' : ['agua','volador'] , 'Wingull' : ['agua','volador'], 'Cyndaquil' : ['fuego','planta'],
            'Caterpie' : ['bicho','None'] , 'Pikachu' : ['electrico','None'] , 'Nidoran' : ['veneno','None'], 
            'Vulpix' : ['Fuego','None'] , 'Jigglypuff' : ['Normal','Hada'] , 'Psyduck' : ['agua','None'],
            'Abra' : ['psiquico','None'] , 'Machop' : ['lucha','None'] , 'Onix' : ['roca','tierra'], 
            'Terrakion' : ['roca','dragon'] , 'Hitmonlee' : ['lucha','None'] , 'Magikarp' : ['agua','None'] ,
            'Eevee' : ['normal','None'] ,'Snorlax' : ['normal','None'] , 'Mewtwo' : ['psiquico','None'] ,
            'Tyrantrum' : ['roca','dragon'] , 'Articuno' : ['hielo','volador']}
class Entrenador(object):
    def __init__(self,nombre,t_ganados,bat_ganadas,bat_perdidas,cant_pok):
        self.nombre = nombre
        self.t_ganados = t_ganados
        self.bat_ganadas = bat_ganadas
        self.bat_perdidas = bat_perdidas
        self.cant_pok = cant_pok
    
    def __str__(self):
        return self.nombre + ' | torneos: ' + str(self.t_ganados) + ' | gano ' + str(self.bat_ganadas) + ' batallas y perdio ' + str(self.bat_perdidas) + '| Tiene ' +str(self.cant_pok)+ ' Pokemones'
class Pokemon(object):
    def __init__(self, nombre,tipo,subtipo,nivel):
        self.nombrepok = nombre
        self.tipo = tipo
        self.subtipo = subtipo
        self.nivel = nivel
    def __str__(self):
        return self.nombrepok + ' tipo: ' + self.tipo + '/'+ self.subtipo + '. su nivel es ' + str(self.nivel)
def pokemones(lista):
    for i in range(len(entrenadores)):
        aux = Entrenador(entrenadores[i],randint(0,10),randint(0,100),randint(0,100),randint(1,10))
        insertar(lista,aux,'t_ganados')
    barrido_lista(lista)
    print('')
    aux = lista.inicio
    while not aux == None:
        print(aux.info)
        print('---- Pokemones')
        cant = aux.info.cant_pok
        for j in range (cant):
            pok = choice(list(pokemon.keys()))
            dato = Pokemon(pok, pokemon[pok][0], pokemon[pok][1], randint(1,50))
            print(dato)
            insertar(aux.sublista,dato,'nivel')
        aux = aux.sig
        print('')
    #b
    print('')
    print('<<<<< Entrenadores que han ganado MAS de 3 torneos Pokemon >>>>>')
    aux = lista.inicio
    c = 0
    while not aux == None:
        if aux.info.t_ganados > 3 :
            print(aux.info)
            c += 1
        aux = aux.sig
    print(' - Hay ' + str(c) + ' entrenadores que ganaron mas de 3 torneos Pokemon.')
    print('')
    # C
    torn = 0
    ent = None
    aux = lista.inicio
    nv = 0
    pok = None
    while not aux == None:
        if aux.info.t_ganados > torn:
            torn = aux.info.t_ganados
            max_torn = aux.info.nombre
            ent = aux.sublista.inicio
            while not ent == None:
                if nv < ent.info.nivel:
                    nv = ent.info.nivel
                    pok = ent.info.nombrepok
                ent = ent.sig
        aux = aux.sig
    print('- El entrenador que mas Torneos Pokemon ha ganado es: ' + max_torn + ', con ' + str(torn)+ ' Torneos ganados.')
    print('- Su pokemon de mayor nivel es: ' + pok + ' de nivel ' + str(nv))
    print('')
    nom = input('ingrese Entrenador a mostrar sus datos y pokemones: ')
    pos = busqueda_lista(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        print('_____Pokemones:')
        aux = pos.sublista.inicio
        while not aux == None:
            print(aux.info)
            aux = aux.sig
    print('')
    # e
    print('- ENTRENADORES CON PORCENTAJE DE VICTORIA MAYOR A 79% :')
    aux = lista.inicio
    x = False
    while aux is not None:
        bat_tot = aux.info.bat_ganadas + aux.info.bat_perdidas
        porcentaje = (aux.info.bat_ganadas * 100)/bat_tot
        if porcentaje > 79:
            x = True
            print(aux.info.nombre +' tiene un porcentaje de ' +str(round(porcentaje,2)) + '% batalladas ganadas.')
        aux = aux.sig
    if x == False:
        print('No hay Entrenadores con un porcentaje mayor a 79.')
    print()
    # f
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.tipo == 'fuego'):
                if (sub.info.subtipo == 'planta'):
                    print(aux.info.nombre, ': tiene un pokemon tipo fuego y subtipo planta, ' + sub.info.nombrepok)
            if (sub.info.tipo == 'agua'):
                if (sub.info.subtipo == 'volador'):
                    print(aux.info.nombre, ': tiene un pokemon tipo agua y subtipo volador, ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
        print('-')
    print('')
    # g
    nom = input('ingrese Entrenador a sacar promedio de nivel de sus Pokemones: ')
    pos = busqueda_lista(lista,nom,'nombre')
    if not pos == None:
        print(pos.info)
        niveles = 0
        cant = 0
        sub = pos.sublista.inicio
        while sub is not None:
            cant += 1
            print(sub.info)
            niveles += sub.info.nivel
            sub = sub.sig
        prom = niveles / cant
        print('--- El promedio de nivel de sus pokemones es: '+ str(round(prom, 2)))
    print('')
    # H
    aux = lista.inicio
    cont = 0
    pok = input(str('Ingrese el nombre del pokemon a buscar: '))
    while aux is not None:
        pos = busqueda_lista(aux.sublista, pok, 'nombrepok')
        if pos is not None:
            cont += 1
            print(aux.info.nombre +' tiene a ' + pok)
        aux = aux.sig
    print(str(cont) +' entrenadores tienen al pokemon '+ pok)
    print('')
    # J
    aux = lista.inicio
    while aux is not None:
        sub = aux.sublista.inicio
        while sub is not None:
            if (sub.info.nombrepok == 'Tyrantrum') or (sub.info.nombrepok == 'Terrakion') or (sub.info.nombrepok == 'Wingull'):
                print('El entrenador ' +aux.info.nombre + ', tiene al pokemon ' + sub.info.nombrepok)
            sub = sub.sig
        aux = aux.sig
    print('')
    # K
    pos = None
    n = None
    x = None
    while ent not in entrenadores:
        ent = input('Ingrese nombre del entrenador: ')
    pos = busqueda_lista(lista,ent,'nombre')
    while n not in pokemon:
        n = input('Ingrese nombre de pokemon a buscar: ')
    if (not pos == None) and (not n == None):
        print('')
        b = False
        nom = pos.sublista.inicio
        while not nom == None:
            if (nom.info.nombrepok == n):
                b = True
                break
            nom = nom.sig
        if b == False:
            print('El entrenador '+ pos.info.nombre + ' no tiene al pokemon buscado.')
        elif b == True:
            print('Entrenador y pokemon encontrados.')
            print('Mostrando sus datos...')
            sleep(1.5)
            print(pos.info)
            sleep(0.7)
            print(nom.info)

#EJ17

def proyecto_sW():
    proyecto = Lista()
    a_tiempo = Lista()
    fuera_de_tiempo = Lista()
    personal = ['Milagros', 'Fiamaa', 'Lujan', 'Raul', 'Pamela', '']
    actividades = ['Recopilar informacion','Estudio de factibilidad','Planificacion','Analisar la informacion','Codificar el sistema','Probar el sistema','Instalacion Sw']
    prom = 0
    costo_total = 0
    for i in range(len(personal)):
        costo = randint(0, 50000)
        tiempo_ejecucion = randint(1, 10)
        fecha_inicio = [ randint(1, 31), randint(1, 12),2020]
        fecha_estimada = [ randint(1, 31), randint(1, 12),2020]
        fechaF_efectiva = [ randint(1, 31), randint(1, 12),2020]
        persona_cargo = choice(personal)
        actividad = actividades[i]
        tareas = [costo,actividad, tiempo_ejecucion, fecha_inicio, fecha_estimada, fechaF_efectiva, persona_cargo]
        insertar(proyecto, tareas)
    print()
    print('Lista con actividades:')
    barrido_lista(proyecto)
    aux = proyecto.inicio
    print()
    while aux is not None:
        # A
        prom = prom + aux.info[2]
        # B
        costo_total = costo_total + aux.info[0]
        # C
        if aux.info[5]:
            print('Persona:',aux.info[6])
            print('Actividades que realiza:',aux.info[1])
            print('Costo de la actividad:',aux.info[0])
            print('Tiempo de ejecucion:',aux.info[2])
            print()
        if aux.info[2] < 7:
            insertar(a_tiempo,aux.info[1])
        else:
            insertar(fuera_de_tiempo,aux.info[1])
        aux = aux.sig
    # D
    fecha1 = [1,2,2020] 
    fecha2 = [25,4,2020]
    print()
    print('Actividades entre '+ str(fecha1) + ' y '+ str(fecha2))
    aux = proyecto.inicio
    while aux is not None:
        if fecha1 < aux.info[5] and fecha2 > aux.info[5]:
            print(aux.info[1])
        aux = aux.sig   
    print()
    print('Tareas que se realizaron a tiempo: ')
    barrido_lista(a_tiempo)
    print()
    print('Tareas que se realizaron fuera de tiempo: ')
    barrido_lista(fuera_de_tiempo)

#ej17

empresas = ['"British Airways"','"American Airlines"','"Lufthansa"','"Lion Air"']
destinos = ['Atenas','Miconos','Rodas','Argentina','China','Brasil','España','Francia','Tailandia']
asientos = [1,10,11,12,19,29]
km = [1000,2000,2500,5000,7000,10500]
clases = ['turista','primera clase']
tru = [False,True]


class Vuelo(object):
    def __init__(self,empresa,num_v,c_asientos,f_salida,destino,kms):
        self.empresa = empresa
        self.num_v = num_v
        self.c_asientos = c_asientos
        self.f_salida = f_salida
        self.destino = destino
        self.kms = kms
    def __str__(self):
        return 'datos: ' + self.empresa +': vuelo ' +str(self.num_v)+', asientos: ' + str(self.c_asientos)+'; Fecha: '+ str(self.f_salida)+ ', Destino: ' + self.destino+ ', kms: ' + str(self.kms) +'.'


class Asiento(object):
    def __init__(self,numero,ocupado,clase,precio):
        self.numero = numero
        self.ocupado = ocupado
        self.clase = clase
        self.precio = precio
    def __str__(self):
        return self.numero +'; Vendido = '+self.ocupado +', Clase: '+ self.clase +', Precio:'+ self.precio


def aeropuertos(lista):
    for i in range(len(destinos)):
        num_v = i+1
        d = randint(1,30)
        m = randint(1,12)
        a = randint(2020,2021)
        fecha = [d,m,a]
        kms = choice(km)
        cant = choice(asientos)
        dato = Vuelo(choice(empresas),num_v,cant,fecha,destinos[i],kms)
        insertar(lista,dato,'destino')
    aux = lista.inicio
    while aux != None:
        cant = aux.info.c_asientos
        p = cant//1.5
        precio = 0
        for i in range(cant):
            asiento = i+1
            ocupado = choice(tru)
            if asiento < p:
                clase = 'Turista'
                precio = (75*kms)
            else:
                clase = 'Primera'
                precio = (203*kms)
            dato = Asiento(asiento,ocupado,clase,precio)
            insertar(aux.sublista,dato,'numero')
        aux = aux.sig
    # A
    aux = lista.inicio
    while not aux == None:
        if aux.info.destino == 'Atenas':
            print('Destino a Atenas: ')
            print(aux.info)
        if aux.info.destino == 'Miconos':
            print('Destino a Miconos: ')
            print(aux.info)
        if aux.info.destino == 'Rodas':
            print('Destino a Rodas: ')
            print(aux.info)
        aux = aux.sig
    print('')
    # B
    aux = lista.inicio
    while not aux == None:
        print()
        s_n = input('Desea ver los asientos libres de la clase turista del destino '+ aux.info.destino + ': ')
        if (s_n == 'S') or (s_n == 's'):
            pos = aux.sublista.inicio
            while not pos == None:
                if pos.info.clase == 'Turista' and pos.info.ocupado == False:
                    print('El asiento '+ str(pos.info.numero) + ' esta desocupado')
                pos = pos.sig
        aux = aux.sig
    # C
    print()
    print('Total recaudado por cada vuelo')
    aux = lista.inicio
    while not aux == None:
        recaudado = 0
        pos = aux.sublista.inicio
        while pos != None:
            if pos.info.ocupado == True:
                recaudado += pos.info.precio
            pos = pos.sig
        print('El vuelo nro '+str(aux.info.num_v)+', a '+ aux.info.destino +' recaudo: '+ str(recaudado)+ ' dinero.')
        aux = aux.sig
    print()
    # E
    s_n = None
    while (s_n != 'n') and (s_n != 'N'):
        s_n = input('Quiere comprar un nuevo pasaje? S/N: ')
        if (s_n == 'S') or (s_n == 's'):
            destino = input('Indique su destino: ')
            bus = None
            bus = busqueda_lista(lista,destino,'destino')
            if bus != None:
                compra = False
                while compra == False:
                    pas = int(input('Elija numero de pasaje: (1/'+ str(bus.info.c_asientos) +') : '))
                    pos = bus.sublista.inicio
                    while pos != None:
                        if pos.info.numero == pas:
                            if pos.info.ocupado == False:
                                pos.info.ocupado = True
                                print('Compra de pasaje exitosa.')
                                print()
                                compra = True
                                break
                            else:
                                print('Lo siento, ese pasaje esta ocupado.')
                                print()
                                break
                        pos = pos.sig
    # F
    print()
    elim = None
    while (elim != 'n') and (elim != 'N'):
        elim = input('Desea eliminar algun vuelo? S/N: ')
        if (elim == 's') or (elim == 'S'):
            vuelo = int(input('Indique con numero, el Nro de vuelo a eliminar: '))
            bus = None
            bus = busqueda_lista(lista,vuelo,'num_v')
            if bus != None:
                b = input('- Seguro que desea eliminar el vuelo con destino a '+ bus.info.destino+' ? S/N: ')
                if (b == 's') or (b == 'S'):
                    eliminar(lista,bus.info.num_v,'num_v')
                    print('>>> Se ha eliminado el vuelo Nro: '+str(bus.info.num_v)+', con destino a '+ bus.info.destino )
                    pos= bus.sublista.inicio
                    recaudado = 0
                    while pos != None:
                        if pos.info.ocupado == True:
                            recaudado += pos.info.precio
                        pos = pos.sig
                    print('>>> La cantidad de dinero a devolver es igual a: ' + str(recaudado))
                    print()
    # G
    print()
    print('Empresas y kilómetros de vuelos con destino a Tailandia:')
    aux = lista.inicio
    while aux != None:
        if aux.info.destino == 'Tailandia':
            print('__ La empresa '+aux.info.empresa + ' tiene un viaje a Tailandia de '+str(aux.info.kms)+' KMs.')
        aux = aux.sig


#18

class Usuario():
    def __init__(self, nombre):
        self.nombre = nombre
    def __str__(self):
        return self.nombre

class Commit():
    def __init__(self, archivo, timestamp, mensaje, cant_lineas):
        self.archivo = archivo
        self.timestamp = timestamp
        self.mensaje = mensaje
        self.cant_lineas = cant_lineas
    def __str__(self):
        return 'Archivo: '+ self.archivo +'; Timestamp: '+ self.timestamp + ', Mensaje: ' + self.mensaje + ', Modificó: ' + str(self.cant_lineas)+ ' lineas'


def github(lista):
    lista = Lista()
    user = Usuario('Roman')
    insertar(lista, user, 'nombre')
    user = Usuario('Regina')
    insertar(lista, user, 'nombre')
    user = Usuario('Tania')
    insertar(lista, user, 'nombre')
    user = Usuario('Jesus')
    insertar(lista, user, 'nombre')
    commit = Commit('test.py', '11-11-20 19:00', 'testeo de la applicacion', 46)
    pos = busqueda_lista(lista, 'Roman', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('data.py', '11-11-20 19:00', 'correccion error', 12)
    pos = busqueda_lista(lista, 'Roman', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('object.java', '11-11-20 19:00', 'modelado del objeto', -37)
    pos = busqueda_lista(lista, 'Regina', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('app.py', '11-11-20 19:00', 'basta chicos', 34)
    pos = busqueda_lista(lista, 'Tania', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('front.html', '11-11-20 19:00', 'update', 47)
    pos = busqueda_lista(lista, 'Jesus', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    commit = Commit('vista.css', '11-11-20 19:00', 'update', -2)
    pos = busqueda_lista(lista, 'Jesus', 'nombre')
    insertar(pos.sublista, commit, 'archivo')
    print('Lista de colaboradores: ')
    barrido_lista(lista)
    print()
    # a
    aux = lista.inicio
    mayor = 0
    while aux is not None:
        if tamanio_lista(aux.sublista) > mayor:
            mayor = tamanio_lista(aux.sublista)
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if tamanio_lista(aux.sublista) == mayor:
            print('Colaborador con mayor cantidad de commits: ' + aux.info.nombre)
            print('Cantidad de commits: '+ str(mayor))
        aux = aux.sig
    print()
    # b
    mayor = 0
    usuario = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        mayor_aux = 0
        while pos is not None:
            mayor_aux += pos.info.cant_lineas
            pos = pos.sig
        if mayor_aux > mayor:
            mayor = mayor_aux
            usuario = aux.info.nombre
        aux = aux.sig
    print(usuario +', agrego la mayor cantidad de lineas: ' +str(mayor))
    menor = 0
    usuario_menor = ''
    aux = lista.inicio
    while aux is not None:
        pos = aux.sublista.inicio
        menor_aux = 0
        while pos is not None:
            menor_aux += pos.info.cant_lineas
            pos =pos.sig
        if menor_aux < menor:
            menor = menor_aux
            usuario_menor = aux.info.nombre
        aux = aux.sig
    print(usuario_menor+ ' elimino la mayor cantidad de lineas: '+ str(menor))
    print()
    # C
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,'test.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en test.py')
        aux = aux.sig
    # D
    print()
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,0,'cant_lineas')
        if pos is not None:
            print(aux.info.nombre + ' ha realizado un commit con 0 lineas')
        aux = aux.sig
    print()
    # E
    aux = lista.inicio
    while aux is not None:
        pos = busqueda_lista(aux.sublista,'app.py','archivo')
        if pos is not None:
            print(aux.info.nombre + ', ha realizado cambios en app.py')
            barrido_sublista(aux.sublista)
        aux = aux.sig

#19

def navesss():
    lista_ventas = Lista()
    clientes = Lista()
    sin_clientes = Lista()
    nombre_clientes = Lista()
    informe = Lista()
    #A
    archivo = open('naves')
    linea = archivo.readline()
    while linea:
        linea = linea.replace('\n', '')
        linea = linea.split(';')
        linea[0] = linea[0].upper()
        linea[1] = linea[1].upper()
        linea[2] = float(linea[2])
        linea[3] = linea[3].title()
        linea[4] = linea[4].title()
        insertar(lista_ventas, linea)
        linea = archivo.readline()      
    print('Lista de ventas de naves')
    barrido_lista(lista_ventas)
    print()
    aux = lista_ventas.inicio
    cont = 0
    ac = 0
    devolver = 0
    ingresoAT = 0
    while aux is not None:
        #B
        if aux.info[4] == 'Desconocido':
            insertar(sin_clientes, aux.info)
        else:
            insertar(clientes,aux.info)
            pos = busqueda_lista(nombre_clientes, aux.info[4],4)
            #E
            if pos == None:
                insertar(nombre_clientes,aux.info[4])
        #D
        cont += 1
        ac = ac + aux.info[2]
        #F
        if aux.info[4] == 'Darth Vader':
            insertar(informe, aux.info)
        #H
        if aux.info[1] == 'AT-AT' or aux.info == 'AT-ST' or aux.info == 'AT-TE':
            ingresoAT = ingresoAT + aux.info[2]
        aux = aux.sig

    print('Total de ingresos de creditos galacticos: ')
    print(ac)
    print()
    print('Total de naves vendidas:')
    print(cont)
    print()
    print('Listado de clientes')
    barrido_lista(nombre_clientes)
    print()
    print('Informe de compras de Darth Vader')
    barrido_lista(informe)
    print()
    print('Clientes que han comprado naves construidas con material reciclado y monto a devoler:')
    aux2 = lista_ventas.inicio
    while aux2 is not None:
        #G
        if aux2.info[3] == 'Si':
            devolver = (aux2.info[2] * 15) / 100
            print('Al cliente: '+ aux2.info[4] + ' se le devolvera, '+str(round(devolver,2)))
        aux2 = aux2.sig
    print()
    print('Ingreso genero la producción de naves cuyos modelos contengan la sigla “AT”.: '+str(round(ingresoAT,2)))

#20

paises = ['Argentina','Uruguay','Brasil','Chile','Paraguay','Mexico','Colombia','Venezuela']
estados_clima = ['soleado','nublado','lloviendo','nevando','tormenta eléctrica','vientos fuertes','huracanes']
estaciones = ['verano','otoño','invierno','primavera']
class Pais():
    def __init__(self,pais,latitud,longitud,altitud):
        self.pais = pais
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
    def __str__(self):
        return 'Pais: '+ self.pais +'|| Ubicacion: Latitud '+ str(self.latitud) + ', Longitud: '+ str(self.longitud) +', Altitud: '+str(self.altitud)
class Medicion():
    def __init__(self,fecha,temperatura,presion,humedad,clima):
        self.fecha = fecha
        self.temperatura = temperatura
        self.presion = presion
        self.humedad = humedad
        self.clima = clima
    def __str__(self):
        return '- Fecha: '+str(self.fecha)+'. Temperatura: '+str(self.temperatura)+ ' grados, Presion: '+str(self.presion)+ ', Humedad: '+str(self.humedad)+ ' % , Clima: '+self.clima
# A
for i in range(len(paises)):
    dato = Pais(paises[i],randint(0,100),randint(0,100),randint(0,100))
    insertar(lista,dato,'pais')
aux = lista.inicio
# B
while not aux == None:
    print(aux.info)
    for i in range(12):
        d = randint(1,30)
        m = i+1
        a = randint(2020,2021)
        fecha = [d,m,a]
        dato = Medicion(fecha,randint(-10,50),randint(0,20),randint(0,100),choice(estados_clima))
        print(dato)
        insertar(aux.sublista,dato,'fecha')
    print('')
    aux = aux.sig
# C
print('Promedios de Temperatura y Humedad:')
aux = lista.inicio
while not aux == None:
    pos = aux.sublista.inicio
    temp = 0
    hum = 0
    cont = 0
    while not pos == None:
        temp += pos.info.temperatura
        hum += pos.info.humedad
        cont += 1
        pos = pos.sig
    print(aux.info.pais + ': El promedio de Temperatura es: ' + str(round(temp/cont , 2)))
    print(aux.info.pais + ': El promedio de Humedad es: ' + str(round(hum/cont , 2)))
    aux = aux.sig
    print('')
# D
aux = lista.inicio
while aux is not None:
    pos = aux.sublista.inicio
    while not pos == None:
        if pos.info.clima == 'lloviendo':
            print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta lloviendo.')
        elif pos.info.clima == 'nevando':
            print('En la fecha '+str(pos.info.fecha)+', en el pais ' +aux.info.pais + ' esta nevando.')
        pos = pos.sig
    aux = aux.sig
print('')
# E
print('- Registros de estado del clima con tormenta eléctrica o huracanes:')
aux = lista.inicio
while aux != None:
    pos = aux.sublista.inicio
    while pos != None:
        if pos.info.clima == 'huracanes':
            print(aux.info.pais + ' registro clima de huracanes en la fecha ' + str(pos.info.fecha))
        elif pos.info.clima == 'tormenta eléctrica':
            print(aux.info.pais+ ' registro clima de Tormenta Electrica en la fecha ' + str(pos.info.fecha))
        pos = pos.sig
    aux = aux.sig


#21

class Pelicula():
    def __init__(self,nombre,valoracion,estreno,recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.estreno = estreno
        self.recaudacion = recaudacion
    def __str__(self):
        return '- Pelicula: ' + self.nombre + ' ||valoracion: ' + str(self.valoracion) + '. Año de estreno: ' + str(self.estreno) + '. Ha recaudado: ' + str(self.recaudacion)

peliculas = ['Tiburon','Francotirador','¿Donde estan las rubias?','La huerfana','Dark',
'Desde mi cielo','Titanic']

def lista_peliculas(lista):
    for i in range(len(peliculas)):
        dato = Pelicula(peliculas[i],randint(1,10),randint(1970,2020),randint(100000,10000000))
        insertar(lista,dato,'nombre')
    barrido_lista(lista)
    print('')
    # A
    pos = None
    while pos == None:
        pos = input('Ingrese un año de estreno: ')
        if pos not in '1234567890':
            pos = None
    aux = lista.inicio
    vacio = False
    while aux is not None:
        if pos == aux.info.estreno:
            print('- '+aux.info.nombre +' se estreno en el año: '+ str(aux.info.estreno))
            vacio = True
        aux = aux.sig
    if vacio == False:
        print('No se estreno pelicula en ese año.')
    print('')
    # B
    mas_rec = 0
    may_p = ''
    aux = lista.inicio
    while aux is not None:
        if aux.info.recaudacion > mas_rec:
            mas_rec = aux.info.recaudacion
            mayor_p = aux.info
        aux = aux.sig
    print('Datos de la pelicula que mas ha recaudado:')
    print(may_p)
    print('')
    # C
    print('Mayor valoracion:')
    aux = lista.inicio
    max_val = 0
    while aux is not None:
        if aux.info.valoracion > max_val:
            max_val = aux.info.valoracion
        aux = aux.sig
    aux = lista.inicio
    while aux is not None:
        if aux.info.valoracion == max_val:
            print('- ' +aux.info.nombre +' tiene la valoracion mas alt con un puntaje es de ' + str(max_val) + ' puntos.')
        aux = aux.sig
    print('')
    # D
    print('Peliculas mostradas por criterio:')
    criterio = None
    lista_aux = Lista()
    print('CRITERIOS: nombre - valoracion - estreno - recaudacion : ')
    while criterio == None:
        criterio = input('Ingrese criterio por el que quiere mostrar: ')
        if (criterio != 'nombre') and (criterio != 'recaudacion') and (criterio != 'estreno') and (criterio != 'valoracion'):
            criterio = None
            print('Se ha producido un error: el criterio ha sido mal ingresado, vuelva a ingresar...')
    # ordenado por criterio
    print('')
    aux = lista.inicio
    while aux is not None:
        insertar(lista_aux, aux.info, criterio)
        aux = aux.sig
    print('Peliculas por ' + criterio +'...')
    sleep(2)
    barrido_lista(lista_aux)

