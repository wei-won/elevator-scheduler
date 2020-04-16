import config
import scheduler
import argparse
from generatePassengerRequest import generateRequests

def run():
	"""
	Take inputs and run scheduler
	"""
	parser = argparse.ArgumentParser(description='Take in input values.')

	parser.add_argument('n', type=int, nargs='?', default=config.params[0],
						help='number of floors')
	parser.add_argument('m', type=int, nargs='?', default=config.params[1],
						help='number of elevators installed')
	parser.add_argument('x', type=int, nargs='?', default=config.params[2],
						help='time (seconds) taken to move between the floors')
	parser.add_argument('y', type=int, nargs='?', default=config.params[3],
						help='time (seconds) taken to pick up or drop off a passenger')
	parser.add_argument('z', type=int, nargs='?', default=config.params[4],
						help='elevator car capacity: number of passengers can be boarded at a time')
	parser.add_argument('l', type=int, nargs='?', default=config.params[5],
						help='total number of passengers')
	args = parser.parse_args()

	# n, m, x, y, z, l = config.params
	if (args.n, args.m, args.x, args.y, args.z, args.l) == config.params:
		orders = config.orders
	else:
		orders = generateRequests(args.n, args.m, args.x, args.y, args.z, args.l)

	elevatorScheduler = scheduler.Scheduler(args.n, args.m, args.x, args.y, args.z, args.l)

	elevatorScheduler.run(orders)

	T = [psg.t for psg in config.passengers[1:]]
	print(T)


if __name__ == '__main__':
	run()