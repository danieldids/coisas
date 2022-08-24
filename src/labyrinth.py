from PIL import Image
from src.labyrinthRoom import LabyrinthRoom
import random
import threading

lock = threading.Lock()

class Labyrinth:

    def __init__(self,width=25, height=25):

        if width < 3 or height < 3:
            raise Exception("O labirinto precisa ter no mínimo 3x3 de tamanho.")
            
        self.width = width
        self.height = height
        self.rooms = []

        self._createLabyrinth()




    def _createLabyrinth(self):
        """Wrapper com os métodos privados para criação de um labirinto        
        """
        self._createRooms()
        self._drawLabyrinth('labirinto_sem_resposta.png')
        self._connectRooms()
        self._drawLabyrinth('labirinto_com_resposta.png')

        print("Labirinto com",self.height,"de altura e",self.width,"de largura foi criado.")




    def _createRooms(self):
        for y in range(self.height):
            for x in range(self.width):
                room = LabyrinthRoom(x,y)
                roomId = str(x) + "," + str(y)
                self.rooms.append(room)
                    
        self.rooms[0].isStart = True
        self.rooms[-1].isEnd = True




    def getRoom(self, x, y):
        """Retorna um cômodo do labirinto

        Args:
            x (int): Posição X do cômodo
            y (int): Posição Y do cômodo

        Returns:
            LabyrinthRoom: Um cômodo do labirinto ou None caso não exista
        """
        for room in self.rooms:
            if room.posX == x and room.posY == y:
                return room



    def _connectRooms(self):
        """Conecta as salas do labirinto
        """

        # A sala inicial é sempre a (0,0)
        currentRoom = self.getRoom(0,0)
        
        # Enquanto a sala em análise não for a marcada como saída (ou fim)
        # do labirinto, método não se encerra.
        while currentRoom.isEnd == False:
            
            nextMove = random.choice(['n','e','s','w'])

            if nextMove == 'n':
                nextX = 0
                nextY = 1
            elif nextMove == 'e':
                nextX = 1
                nextY = 0
            elif nextMove == 's':
                nextX = 0
                nextY = -1
            else:
                nextX = -1
                nextY = 0

            nextRoom = self.getRoom(currentRoom.posX + nextX, currentRoom.posY + nextY)

            if nextRoom is None:
                continue

            # Condição criada para criar labirintos mais interessantes.
            # O valor 1 foi definido por tentativa e erro.
            if nextRoom.connectionCount > 1:
                currentRoom = nextRoom
                continue
            
            if nextMove == 'n':
                currentRoom.connectToRoom('north', nextRoom)
                
            elif nextMove == 'e':
                currentRoom.connectToRoom('east', nextRoom)
                
            elif nextMove == 's':
                currentRoom.connectToRoom('south', nextRoom)
                
            else:
                currentRoom.connectToRoom('west', nextRoom)

            currentRoom = nextRoom

        print('Conexão das salas finalizada.')

    
    
    def _drawLabyrinth(self, fileName='labyrinth.png'):
        """
        O método coleta toas as salas do labirinto e as combina
        numa imagem integral. Há um porém: na lista de salas 
        existente na instância da classe Labyrinth, as coordenadas
        se referem ao quadrante com X e Y positivos (em um plano cartesiano).
        Os cômodos do labirinto são construídos de baixo para cima.

        A biblioteca para manipulação de imagens (PIL) também tem como origem o ponto (0,0),
        mas constrói a imagem de cima para baixo - mesmo que a coordenada Y seja positiva.

        Dessa forma, são necessários alguns cálculos para criar a imagem de baixo para cima.
        """
        labyrinth = Image.new('RGB',(25*self.width,25*self.height), (255,255,255))
        lock.acquire()
        for room in self.rooms:
            roomMap = room.getRoomMap()
            roomX = room.posX * 25
            roomY = (self.height * 25) - (room.posY * 25) - 25
            labyrinth.paste(roomMap,(roomX,roomY))
        
        labyrinth.save(fileName,'PNG')
        lock.release()
