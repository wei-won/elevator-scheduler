
class Passenger:

	def __init__(self, idx, order):
		self.passengerIndex = idx
		self.s = order[0]
		self.b = order[1]
		self.d = order[2]
		self.t = 0

	def setT(self, t):
		self.t = t
