import random
import threading

globalLock = threading.Lock()

class Mouse:

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.visitedRooms = []
        self.isAlive = True
        self.currentRoom = None
        self.cheeseFound = False
        
        self._enterLabyrinth()
    


    def _enterLabyrinth(self):
        for room in self.labyrinth.rooms:
            if room.isStart == True:
                self.currentRoom = room
                    

    def searchCheese(self):
        while self.isAlive and self.cheeseFound == False:
            movementsPlan = self._planMoves()
            self._walk(movementsPlan)

        if self.cheeseFound == True:
            print('O rato encontrou o queijo!')
        
    
    def _walk(self, movementsPlan: list):
        
        while len(movementsPlan) > 0:
            
            nextMove =  movementsPlan.pop()
            
            if nextMove in self.visitedRooms:
                continue

            if nextMove.isEnd:
                self.cheeseFound = True
                self.visitedRooms.append(self.currentRoom)
                globalLock.acquire()
                self.currentRoom = nextMove
                self.visitedRooms.append(self.currentRoom)
                globalLock.release()
                raise Exception('Queijo encontrado')
            
            self.visitedRooms.append(self.currentRoom)
            globalLock.acquire()
            self.currentRoom = nextMove
            globalLock.release()
            return
        
        self.visitedRooms.append(self.currentRoom)
        self.isAlive = False

        

    def _planMoves(self):

        moves = []
        
        if self.currentRoom.northDoor is not None:
            moves.append(self.currentRoom.northDoor)
        if self.currentRoom.eastDoor is not None:
            moves.append(self.currentRoom.eastDoor)
        if self.currentRoom.southDoor is not None:
            moves.append(self.currentRoom.southDoor)
        if self.currentRoom.westDoor is not None:
            moves.append(self.currentRoom.westDoor)


        movementsPlan = []

        while len(moves) > 0:
            movementsPlan.append(random.choice(moves))
            moves.remove(movementsPlan[-1])
        
        return movementsPlan