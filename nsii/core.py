import sys
import io

class Core:

	def __init__(self):

		self.buffer = [[None for a in range(400)] for b in range(400)]
		self.state = [[None for a in range(400)] for b in range(400)]


	def draw(self, update, width, height):

		x, y = 0, 0
		serie = False

		while y < height:
			while x < width:

				if self.state[y][x]:

					if not(serie):
						sys.stdout.write('\x1b[%d;%dH'%(y+1, x+1))
						serie = True

					sys.stdout.write(self.buffer[y][x])
					self.state[y][x] = False

				else:
					if serie: serie = False

				x += 1

			y += 1
			x = 0

		update()
		sys.stdout.flush()