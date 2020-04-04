
from queue import PriorityQueue
import passenger

"""
Global Var:
IDLE = 0
UP = 1
DOWN = -1
waitingList
passengers
"""
class Elevator:
	
	def __init__(self, elevatorIndex, n， x, y, z):
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
		self.upQueue = []
		self.downQueue = []
		self.passengerInList = [[] for f in range(n+1)]
		self.passengerOutList = [[] for f in range(n+1)]
		self.updateT = 0
		self.isTmpStay = False


	def dropOff(self):
		for pIdx in passengerInList[self.currentFloor]:
			passengers[pIdx].setT(self.updateT)
			waitingList.remove(pIdx)
		passengerInList[self.currentFloor].clear()


	def pickUp(self, psgr):
		passengerOutList[self.currentFloor].remove(psgr)
		destination = passengers[psgr].d
		if destination > self.currentFloor:
			self.upQueue.append(destination)
			self.upQueue.sort()
		if destination < self.currentFloor:
			self.downQueue.append(destination)
			self.upQueue.sort(reverse=True)
		passengerInList[destination].append(psgr)


	def stopFloor(self):
		if self.status == UP:
			self.upQueue.pop(0)
		elif self.status == DOWN:
			self.downQueue.pop(0)

		if (len(self.upQueue)==0 and len(self.downQueue)==0):
			self.status = IDLE

		self.updateT += self.y

		if self.passengerInList[self.currentFloor]:
			dropOff()

		if self.passengerOutList[self.currentFloor]:
			for passengerOut in passengerOutList[self.currentFloor].sort():
				if self.isFull = False:
					pickUp(passengerOut)


	def moveOneFloor(self):
		if self.isAvailable == True:
			self.updateT += self.x
			self.currentFloor += self.status
		else:
			Print("Elevator "+str(self.elevatorIndex)+" is not available.")


	def operateUpdate(self, t):
		while(self.updateT < t):
			if self.status = UP:
				if len(self.upQueue) > 0:
					if self.upQueue[0] != self.currentFloor:
						if (self.updateT+self.x <= t):
							moveOneFloor()
						else:
							break
					else:
						if (self.updateT+self.y <= t):
							stopFloor()
						else:
							break
				elif len(self.downQueue) > 0:
					self.status = DOWN
				else:
					self.status = IDLE
			
			if self.status = DOWN:
				if len(self.downQueue) > 0:
					if self.downQueue[0] != self.currentFloor:
						if (self.updateT+self.x <= t):
							moveOneFloor()
						else:
							break
					else:
						if (self.updateT+self.y <= t):
							stopFloor()
						else:
							break
				elif len(self.upQueue) > 0:
					self.status = UP
				else:
					self.status = IDLE

					
					

