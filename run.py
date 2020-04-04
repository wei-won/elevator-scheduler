import elevator
import scheduler
import passenger


def run():
	"""
	Take inputs and initialize objects
	"""

	IDLE = 0
	UP = 1
	DOWN = -1

	n, m, x, y, z, l = (3, 2, 1, 2, 1, 2)
	orders = [[0,1,3], [3,2,1]]

	elevators = []
	passengers = []
	waitingLst = [i for i in range(1, l+1)]


	scheduler = scheduler.Scheduler(n, m, x, y, z, l)

	for e in range(1, m+1):
		newElevator = elevator.Elevator(e, n, x, y, z)
		elevators.append(newElevator)

	for o in range(1, l+1):
		pOrder = orders[o-1]
		newPassenger = passenger.Passenger(o, pOrder)
		passengers.append(newPassenger)
		
		for elvt in elevators:
			elvt.operateTill(s)

		scheduler.schedule(elevators, newPassenger)


if __name__ == '__main__':
	run()