import sys
import io

class Core:

	def __init__(self):

		sys.stdout = io.TextIOWrapper(io.BufferedWriter(sys.stdout.buffer, 1000000), encoding='utf-8')

		self.buffer = [[None for a in range(400)] for b in range(400)]
		self.coords = set()


	def draw(self, update, wipe=False):

		if wipe: sys.stdout.write('\x1b[2J')

		for coord in self.coords:

			x, y = coord
			color, car = self.buffer[y][x]

			#sys.stdout.write('\x1b[38;2;{};{};{}m\x1b[{};{}H{}'.format(*color, y + 1, x + 1, car))
			sys.stdout.write('\x1b[38;2;%d;%d;%dm\x1b[%d;%dH%1s' % (*color, y + 1, x + 1, car))
			#sys.stdout.write('\x1b[38;2;' + str(color[0])  + ';' + str(color[1]) + ';' + str(color[2]) + 'm\x1b[' + str(y + 1) + ';' + str(x +1) + 'H' + car)

		self.coords.clear()

		update()
		sys.stdout.flush()