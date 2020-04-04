
from queue import PriorityQueue
IDLE = 0
UP = 1
DOWN = -1


class Elevator:

	def __int__(self, elevatorIndex, n， x, y, z):
		"""
		n: number of floors
		x: seconds to move between the floors
		y: seconds to pick up or drop off a passenger
		z: total number of passengers
		elevatorIndex: the index of this elevator
		"""
		self.n = n
		self.x = x
		self.y = y
		self.z = z
		self.elevatorIndex = elevatorIndex
		self.currentFloor = 1
		self.status = IDLE
		self.isAvailable = True
		self.isFull = False
		self.moveTime = 0
		self.stopTime = 0
		self.upQueue = PriorityQueue()
		self.downQueue = PriorityQueue()
		self.passengerQueue = PriorityQueue()
		self.updateT = 0


	def stopFloor(self):
		if (self.upQueue.qsize()==0 and self.downQueue.qsize()==0):
			self.status = IDLE


	def moveOneFloor(self):
		if self.isAvailable == True:
			self.currentFloor = self.currentFloor + self.status
		else:
			Print("Elevator "+str(self.elevatorIndex)+" is not available.")


	def openDoor(self, t):


	def operateTill(self, t):
		while(self.updateT < t):
			if self.status = UP:
				if self.upQueue.qsize() > 0:
					if self.upQueue.queue[0] != self.currentFloor:
						if (self.updateT+self.x <= t):
							moveOneFloor(self)




				else:
				
				if self.upQueue.get() != self.currentFloor:
					

