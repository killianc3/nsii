import sys

class Core:

	def __init__(self):

		self.buffer = [[None]*1920 for a in range(1080)]
		self.coords = set()


	def draw(self, update, wipe=False):

		if wipe: sys.stdout.write('\x1b[2J')

		while len(self.coords) > 0:

			x, y = self.coords.pop()
			color, car = self.buffer[y][x]

			sys.stdout.write('\x1b[38;2;{};{};{}m\x1b[{};{}H{}'.format(*color, y, x, car))

		update()
		sys.stdout.flush()