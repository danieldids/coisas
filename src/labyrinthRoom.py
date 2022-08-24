from PIL import Image

class LabyrinthRoom:
    """
    Representa uma sala (ou cômodo) do labirinto
    """

    def __init__(self, posX, posY):
        self.northDoor = None
        self.eastDoor = None
        self.southDoor = None
        self.westDoor = None
        self.connectionCount = 0
        self.visited = False
        self.roomImage = None
        self.visitor = None

        self.posX = posX
        self.posY = posY

        self.isStart = False
        self.isEnd = False




    def connectToRoom(self, toDoor, otherRoom):
        if toDoor == 'north':
            if self.northDoor == otherRoom:
                pass
            else:
                self.northDoor = otherRoom
                self.connectionCount = self.connectionCount + 1
                otherRoom.southDoor = self
                otherRoom.connectionCount = otherRoom.connectionCount + 1
        
        if toDoor == 'east':
            if self.eastDoor == otherRoom:
                pass
            else:
                self.eastDoor = otherRoom
                self.connectionCount = self.connectionCount + 1
                otherRoom.westDoor = self
                otherRoom.connectionCount = otherRoom.connectionCount + 1

        if toDoor == 'south':
            if self.southDoor == otherRoom:
                pass            
            else:
                self.southDoor = otherRoom
                self.connectionCount = self.connectionCount + 1
                otherRoom.northDoor = self
                otherRoom.connectionCount = otherRoom.connectionCount + 1
        
        if toDoor == 'west':
            if self.westDoor == otherRoom:
                pass
            else:
                self.westDoor = otherRoom
                self.connectionCount = self.connectionCount + 1
                otherRoom.eastDoor = self
                otherRoom.connectionCount = otherRoom.connectionCount + 1



    # Gera uma pequena imagem de uma sala do labirinto
    # Essa imagem depois é inserida num mosaico, formando a
    # visão geral do labirinto.
    def getRoomMap(self):
        
        self.roomImage = Image.open('images/room_notVisited.png')

        isStart = Image.open('images/roomVisited.png')
        isEnd = Image.open('images/isEnd_notVisited.png')
        
        if self.isStart:
            self.roomImage = Image.alpha_composite(self.roomImage, isStart)

        if self.isEnd:
            self.roomImage = Image.alpha_composite(self.roomImage, isEnd)

        # Imagens para salas não visitadas
        if self.visited == False:

            northDoor = Image.open('images/notVisited_northDoor.png')
            eastDoor = Image.open('images/notVisited_eastDoor.png')
            southDoor = Image.open('images/notVisited_southDoor.png')
            westDoor = Image.open('images/notVisited_westDoor.png')
        
        # Imagens para salas visitadas (usadas no rolê do ratinho, por exemplo)
        if self.visited == True:
            self.roomImage = Image.open('images/roomVisited.png')

            eastDoor = Image.open('images/visited_eastDoor.png')
            northDoor = Image.open('images/visited_northDoor.png')
            southDoor = Image.open('images/visited_southDoor.png')
            westDoor = Image.open('images/visited_westDoor.png')

        if self.northDoor is not None:
            self.roomImage = Image.alpha_composite(self.roomImage, northDoor)

        if self.eastDoor is not None:
            self.roomImage = Image.alpha_composite(self.roomImage, eastDoor)

        if self.southDoor is not None:
            self.roomImage = Image.alpha_composite(self.roomImage, southDoor)

        if self.westDoor is not None:
            self.roomImage = Image.alpha_composite(self.roomImage, westDoor)

        return self.roomImage