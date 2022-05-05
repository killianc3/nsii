import sys

class Core:

	def __init__(self):

		self.buffer = [['8;2;0;0;0m' for a in range(2000)] for b in range(2000)]
		self.state = [[True for a in range(2000)] for b in range(2000)]


	def draw(self, update, width, height, force=False):

		x, y = 0, 0
		serie = False

		for y in range(0, height, 2):
			for x in range(width):

				if self.state[y][x] or self.state[y+1][x] or force:

					if not(serie):
						sys.stdout.write('\x1b[%d;%dH'%(y//2+1, x+1))
						serie = True

					if self.buffer[y][x][0] == '8':
						sys.stdout.write(f'\x1b[4{self.buffer[y][x]}\x1b[3{self.buffer[y+1][x]}▄')

					elif self.buffer[y][x][0] != 'None':
						sys.stdout.write(self.buffer[y][x])

					self.state[y][x] = False
					self.state[y+1][x] = False

				else:
					if serie: serie = False

		update()
		sys.stdout.flush()