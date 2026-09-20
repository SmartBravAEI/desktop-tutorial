import random
import os

def terreno():
  yx = random.randint(7, 16) #asigna un numero random entre 7 y 16
  terreno=[] # se crea el terreno(lista vacia)
  for y in range(yx): #empieza 
    lista = [] # de aqui voy agarrar la lista por partes para que se vea la matriz visualmente
    for x in range(yx):
      lista.append(random.randint(1,6))
      if lista[x] == 1 or lista[x] == 4:
        lista[x] = "🧱"

      if lista[x] == 2:
        lista[x] = "🧰"
      if lista[x] == 3 or lista[x] == 5 or lista[x] == 6:
        lista[x] = "__"
    terreno.append(lista)
  
  return terreno, yx

terr, yx = terreno()

j = "😎"
terr[0][0] = j
pos_y = 0
pos_x = 0

while True:
  os.system('cls' if os.name == 'nt' else 'clear')
  for e in range(yx): #se imprime el terreno completo
    print(terr[e])

  mov = {'a':(0,-1), 'w':(-1,0), 'd':(0,1), 's':(1,0)}
  cont = input("a = izqierda, w = arriba, d = derecha, s = abajo    respuesta --->  ").lower()

  

  if cont in mov: 
    cordy, cordx = mov[cont]
    cord = {'s':yx-1 > pos_y, 'a':pos_x > 0, 'w':pos_y > 0,'d':yx-1 > pos_x}
    if cord[cont]:
      if terr[pos_y+cordy][pos_x+cordx] != "🧱":
        terr[pos_y][pos_x] = '__'
        pos_y += cordy
        pos_x += cordx
        terr[pos_y][pos_x] = j
      else:
        print("No se puede cruzar por las paredes")        
    else:
      print("No puedes cruzar, es el limite del mundo")

  
