
from queue import PriorityQueue
IDLE = 0
UP = 1
DOWN = -1


class Elevator():

	def __int__(self, n， x, y, z, elevatorIndex):
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
		self.upQueue = PriorityQueue()
		self.downQueue = PriorityQueue()
		self.passengerQueue = PriorityQueue()


	def stopFloor(self):
		if (self.upQueue.qsize()==0 and self.downQueue.qsize()==0):
			self.status = IDLE


	def move(self, ):
		if self.isAvailable == True:
			self.currentFloor = self.currentFloor + self.status
		else:
			Print("Elevator "+str(self.elevatorIndex)+" is not available.")


	def stepRun(self):
			if (self.upQueue.qsize() > 0):
				self.status = UP
				if self.upQueue.get() != self.currentFloor:
					moveOneFloor(self)

