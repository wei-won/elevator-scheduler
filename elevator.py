import config
import passenger

"""
IDLE = 0
UP = 1
DOWN = -1
"""


class Elevator:

	def __init__(self, elevatorIndex, n, x, y, z):
		"""
		:param elevatorIndex: the index of this elevator
		:param n: number of floors
		:param x: seconds to move between the floors
		:param y: seconds to pick up or drop off a passenger
		:param z: total number of passengers
		"""
		self.n = n
		self.x = x
		self.y = y
		self.z = z
		self.elevatorIndex = elevatorIndex
		self.currentFloor = 1
		self.status = 0
		self.isAvailable = True
		self.isFull = False
		self.moveTime = 0
		self.stopTime = 0
		self.upQueue = []
		self.downQueue = []
		self.passengerInList = [[] for f in range(n + 1)]
		self.passengerOutList = [[] for f in range(n + 1)]
		self.updateT = 0
		self.isTmpStay = False
		self.passengerCount = 0

	def dropOff(self):
		for pIdx in self.passengerInList[self.currentFloor]:
			config.passengers[pIdx].setT(self.updateT)
			config.waitingList.remove(pIdx)
			self.passengerCount -= 1
			print("Passenger " + str(pIdx) + " dropped off by Elevator " + str(self.elevatorIndex) + " on Floor " + str(
				self.currentFloor) + " at time " + str(self.updateT))
		self.passengerInList[self.currentFloor].clear()
		self.isFull = False

	def pickUp(self):
		for passengerOut in self.passengerOutList[self.currentFloor]:
			if not self.isFull:
				self.passengerOutList[self.currentFloor].remove(passengerOut)
				destination = config.passengers[passengerOut].d
				if destination > self.currentFloor:
					self.upQueue.append(destination)
					self.passengerCount += 1
					if len(self.upQueue) > 1:
						self.upQueue.sort()
				if destination < self.currentFloor:
					self.downQueue.append(destination)
					self.passengerCount += 1
					if len(self.downQueue) > 1:
						self.downQueue.sort(reverse=True)
				self.passengerInList[destination].append(passengerOut)
				# self.passengerCount = sum([len(floorPassenger) for floorPassenger in self.passengerInList])
				if self.passengerCount == self.z:
					self.isFull = True
				print("Passenger " + str(passengerOut) + " picked up by Elevator " + str(self.elevatorIndex) +
					  " on Floor " + str(self.currentFloor) + " at time " + str(self.updateT))

	def stopFloor(self):
		if self.status == 1:
			self.upQueue.pop(0)
		elif self.status == -1:
			self.downQueue.pop(0)

		if len(self.upQueue) == 0 and len(self.downQueue) == 0:
			self.status = 0

		self.updateT += self.y

		if self.passengerInList[self.currentFloor]:
			self.dropOff()

		if self.passengerOutList[self.currentFloor]:
			# for passengerOut in self.passengerOutList[self.currentFloor]:	# put in pickUp
			# 	if not self.isFull:
			self.pickUp()

	def moveOneFloor(self):
		if self.isAvailable:
			self.updateT += self.x
			self.currentFloor += self.status
		else:
			print("Elevator " + str(self.elevatorIndex) + " is not available.")

	def operateUpdate(self, t):
		if t == 0:
			t += 0.1
		while (self.updateT < t):
			if self.status == 1:
				if len(self.upQueue) > 0:
					if self.upQueue[0] != self.currentFloor:
						if (self.updateT + self.x) <= t:
							self.moveOneFloor()
						else:
							break
					else:
						self.isTmpStay = True
						if (self.updateT + self.y) <= t:
							self.stopFloor()
							self.isTmpStay = False
						else:
							break
				elif len(self.downQueue) > 0:
					self.status = -1
				else:
					self.status = 0

			elif self.status == -1:
				if len(self.downQueue) > 0:
					if self.downQueue[0] != self.currentFloor:
						if (self.updateT + self.x) <= t:
							self.moveOneFloor()
						else:
							break
					else:
						self.isTmpStay = True
						if (self.updateT + self.y) <= t:
							self.stopFloor()
							self.isTmpStay = False
						else:
							break
				elif len(self.upQueue) > 0:
					self.status = 1
				else:
					self.status = 0

			else:
				if len(self.upQueue) > 0:
					self.status = 1
				elif len(self.downQueue) > 0:
					self.status = -1
				else:
					break

	def finish(self):
		while len(self.upQueue) > 0:
			self.status = 1
			if self.upQueue[0] != self.currentFloor:
				self.moveOneFloor()

			if self.upQueue[0] == self.currentFloor:
				self.isTmpStay = True
				self.stopFloor()
				self.isTmpStay = False

		while len(self.downQueue) > 0:
			self.status = -1
			if self.downQueue[0] != self.currentFloor:
				self.moveOneFloor()

			if self.downQueue[0] == self.currentFloor:
				self.isTmpStay = True
				self.stopFloor()
				self.isTmpStay = False

		self.status = 0
