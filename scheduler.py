import elevator
import passenger


class Scheduler:

	def __init__(self, n, m, z, l):
		self.n = n
		self.m = m
		self.z = z
		self.l = l


	def processUpOrder(self):
		global elevators
		minDistance = 10000
		bestElevator = 0
		for eIdx in range(1, m+1):
			if (elevators[eIdx].status == 1 and elevators[eIdx].currentFloor <= Pb)
				if elevators[eIdx].currentFloor < Pb:
					distance = Pb - elevators[eIdx].currentFloor
					if distance < minDistance:
						minDistance = distance
						bestElevator = eIdx
				if (elevators[eIdx].currentFloor == Pb and elevators[eIdx].isTmpStay):
					minDistance = 0
					bestElevator = eIdx

		for eIdx in range(1, m+1):
			if elevators[eIdx].status == 0:
				distance = abs(Pb - elevators[eIdx].currentFloor)
				if distance < minDistance:
					minDistance = distance
					bestElevator = eIdx

		if bestElevator != 0:
			elevators[bestElevator].passengerOutList[Pb].append()
			if Pb >= elevators[bestElevator].currentFloor:
				elevators[bestElevator].upQueue.append(Pb)
				elevators[bestElevator].upQueue.sort()
			else:
				elevators[bestElevator].downQueue.append(Pb)
				elevators[bestElevator].downQueue.sort(reverse=True)


				

	def processDownOrder(self):
		global elevators
		minDistance = 10000
		bestElevator = 0
		for eIdx in range(1, m+1):
			if (elevators[eIdx].status == -1 and elevators[eIdx].currentFloor >= Pb)
				if elevators[eIdx].currentFloor > Pb:
					distance = elevators[eIdx].currentFloor - Pb
					if distance < minDistance:
						minDistance = distance
						bestElevator = eIdx
				if (elevators[eIdx].currentFloor == Pb and elevators[eIdx].isTmpStay):
					minDistance = 0
					bestElevator = eIdx

		for eIdx in range(1, m+1):
			if elevators[eIdx].status == 0:
				distance = abs(Pb - elevators[eIdx].currentFloor)
				if distance < minDistance:
					minDistance = distance
					bestElevator = eIdx

		if bestElevator != 0:
			elevators[bestElevator].passengerOutList[Pb].append()
			if Pb <= elevators[bestElevator].currentFloor:
				elevators[bestElevator].downQueue.append(Pb)
				elevators[bestElevator].downQueue.sort(reverse=True)
			else:
				elevators[bestElevator].upQueue.append(Pb)
				elevators[bestElevator].upQueue.sort()
				


	def schedule(self, psgr):
		global elevators
		Ps, Pb, Pd = psgr.s, psgr.b, psgr.d
		PIndex = psgr.passengerIndex

		for elvtr in elevators:
			elvtr.operateUpdate(Ps)

		if psgr.b < psgr.d:
			processUpOrder()

		if psgr.b > psgr.d:
			processDownOrder()


