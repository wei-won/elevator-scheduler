import config
import elevator
import passenger


class Scheduler:

	def __init__(self, n, m, x, y, z, l):
		self.n = n
		self.m = m
		self.z = z
		self.l = l
		self.elevators = [None]

		for e in range(1, self.m + 1):
			newElevator = elevator.Elevator(e, n, x, y, z)
			self.elevators.append(newElevator)
		print("Elevators Initialized.")

	def processUpOrder(self, psgr):
		# global elevators
		minDistance = 10000
		bestElevator = 0
		pStart = psgr.s
		pFloor = psgr.b
		pIdx = psgr.passengerIndex
		for eIdx in range(1, self.m+1):
			if (self.elevators[eIdx].status == 1 and self.elevators[eIdx].currentFloor <= pFloor):
				if self.elevators[eIdx].currentFloor < pFloor:
					distance = pFloor - self.elevators[eIdx].currentFloor
					if distance < minDistance:
						minDistance = distance
						bestElevator = eIdx
				if (self.elevators[eIdx].currentFloor == pFloor and self.elevators[eIdx].isTmpStay):
					minDistance = 0
					bestElevator = eIdx

		for eIdx in range(1, self.m+1):
			if self.elevators[eIdx].status == 0:
				distance = abs(pFloor - self.elevators[eIdx].currentFloor)
				if distance < minDistance:
					minDistance = distance
					bestElevator = eIdx
					self.elevators[bestElevator].updateT = pStart

		if bestElevator != 0:
			self.elevators[bestElevator].passengerOutList[pFloor].append(pIdx)
			if len(self.elevators[bestElevator].passengerOutList[pFloor]) > 1:
				self.elevators[bestElevator].passengerOutList[pFloor].sort()
			if pFloor >= self.elevators[bestElevator].currentFloor:
				self.elevators[bestElevator].upQueue.append(pFloor)
				if len(self.elevators[bestElevator].upQueue) > 1:
					self.elevators[bestElevator].upQueue.sort()
			else:
				self.elevators[bestElevator].downQueue.append(pFloor)
				if len(self.elevators[bestElevator].downQueue) > 1:
					self.elevators[bestElevator].downQueue.sort(reverse=True)

	def processDownOrder(self, psgr):
		# global elevators
		minDistance = 10000
		bestElevator = 0
		pStart = psgr.s
		pFloor = psgr.b
		pIdx = psgr.passengerIndex
		for eIdx in range(1, self.m+1):
			if (self.elevators[eIdx].status == -1 and self.elevators[eIdx].currentFloor >= pFloor):
				if self.elevators[eIdx].currentFloor > pFloor:
					distance = self.elevators[eIdx].currentFloor - pFloor
					if distance < minDistance:
						minDistance = distance
						bestElevator = eIdx
				if (self.elevators[eIdx].currentFloor == pFloor and self.elevators[eIdx].isTmpStay):
					minDistance = 0
					bestElevator = eIdx

		for eIdx in range(1, self.m+1):
			if self.elevators[eIdx].status == 0:
				distance = abs(pFloor - self.elevators[eIdx].currentFloor)
				if distance < minDistance:
					minDistance = distance
					bestElevator = eIdx
					self.elevators[bestElevator].updateT = pStart

		if bestElevator != 0:
			self.elevators[bestElevator].passengerOutList[pFloor].append(pIdx)
			if len(self.elevators[bestElevator].passengerOutList[pFloor]) > 1:
				self.elevators[bestElevator].passengerOutList[pFloor].sort()
			if pFloor <= self.elevators[bestElevator].currentFloor:
				self.elevators[bestElevator].downQueue.append(pFloor)
				if len(self.elevators[bestElevator].downQueue) > 1:
					self.elevators[bestElevator].downQueue.sort(reverse=True)
			else:
				self.elevators[bestElevator].upQueue.append(pFloor)
				if len(self.elevators[bestElevator].upQueue) > 1:
					self.elevators[bestElevator].upQueue.sort()

	def schedule(self, psgr):
		# global elevators
		# Ps, Pb, Pd = psgr.s, psgr.b, psgr.d
		# PIndex = psgr.passengerIndex

		# for elvtr in self.elevators:
		# 	elvtr.operateUpdate(Ps)

		if psgr.b < psgr.d:
			self.processUpOrder(psgr)

		if psgr.b > psgr.d:
			self.processDownOrder(psgr)

	def run(self, orders):
		# global passengers
		for o in range(1, self.l + 1):
			pOrder = orders[o - 1]
			newPassenger = passenger.Passenger(o, pOrder)
			config.passengers.append(newPassenger)
			print("Passenger " + str(o) + " called on Floor " + str(pOrder[1]) + " at time " + str(pOrder[0]))
			if o != 1:
				for elvt in self.elevators[1:]:
					elvt.operateUpdate(pOrder[0])

				self.schedule(newPassenger)
			else:
				self.schedule(newPassenger)

		for elvt in self.elevators[1:]:
			elvt.finish()


