import config
import elevator
import scheduler
import passenger


def run():
	"""
	Take inputs and initialize objects
	IDLE = 0
	UP = 1
	DOWN = -1
	"""

	n, m, x, y, z, l = config.params
	orders = config.orders


	elevatorScheduler = scheduler.Scheduler(n, m, x, y, z, l)

	elevatorScheduler.run(orders)

	T = [psg.t for psg in config.passengers[1:]]
	print(T)


if __name__ == '__main__':
	run()