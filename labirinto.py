#!/usr/bin/python3
import random
from src.labyrinthRoom import LabyrinthRoom
from src.labyrinth import Labyrinth
from src.mouse import Mouse
import threading

tryCount = None
labyrinthHeight = None
labyrinthWidth = None
userInput = None


def spawnMouse(labyrinth):
    
    mouse = Mouse(labyrinth)
    
    try:
        mouse.searchCheese()
    
    except:
        for room in mouse.visitedRooms:
            r = labyrinth.getRoom(room.posX, room.posY)
            r.visited = True
        
        labyrinth._drawLabyrinth('caminho_do_rato.png')
        print('Um rato encontrou o queijo')



print('------------------------------------------------------')
print('LABIRINTO GENERATOR E SOLUCIONATOR')
print('Daniel Dutra')
print('------------------------------------------------------')

userInput = input('Informe a quantidade de tentativas (padrão 100000):')
try:
    tryCount = int(userInput)
except:
    tryCount = 100000
    print('Valor informado inválido, usando padrão.')

userInput = input('Informe a largura do labirinto (padrão 25) em número de salas/cômodos:')
try:
    labyrinthWidth = int(userInput)
except:
    labyrinthWidth = 25
    print('Valor informado inválido, usando padrão.')

userInput = input('Informe a altura do labirinto (padrão 25) em número de salas/cômodos:')
try:
    labyrinthHeight = int(userInput)
except:
    labyrinthHeight = 25
    print('Valor informado inválido, usando padrão.')

userInput = input('Deseja iniciar criação do labirinto? (S/N)')

if userInput.lower() == 's':
    labyrinth = Labyrinth(labyrinthWidth,labyrinthHeight)
    
    counter = 0
    
    for mouse in range(tryCount):
        
        counter += 1
        if counter % 100 == 0:
            print('Tentativa',counter)

        t1 = threading.Thread(target=spawnMouse, args=(labyrinth,))
        t2 = threading.Thread(target=spawnMouse, args=(labyrinth,))
        t3 = threading.Thread(target=spawnMouse, args=(labyrinth,))
        t4 = threading.Thread(target=spawnMouse, args=(labyrinth,))
        
        t1.start()
        t2.start()
        t3.start()
        t4.start()
else:
    print('Labirinto e resolução canceladas.')
