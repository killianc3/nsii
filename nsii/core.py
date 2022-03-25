import sys

class Core:

	def __init__(self):

		self.buffer = []


	def draw(self, update, wipe=False):

		if wipe: sys.stdout.write('\x1b[2J')

		for pixel in self.buffer:

			sys.stdout.write('\x1b[38;2;{};{};{}m\x1b[48;2;{};{};{}m\x1b[{};{}H{}'.format(*pixel))

		self.buffer.clear()
		update()

		sys.stdout.flush()