class Image:

	def __init__(self, buffer, coords, path):

		self.size = (40, 20)
		self.pos = (0, 0)

		self._buffer = buffer
		self._coords = coords
		self._img = []
		self._img_size = None

		self.ppmread(path)


	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, new_size):
		self._size = new_size


	@property
	def pos(self):
		return self._pos

	@pos.setter
	def pos(self, new_pos):
		self._pos = new_pos


	def show(self):

		of_x, of_y = self._img_size[0] / self.size[0], self._img_size[1] / self.size[1]
		po_x, po_y = 0, 0

		for y in range(self.size[1] - 1):
			for x in range(self.size[0] - 1):

				r, g, b = self._img[round(po_y)][round(po_x)]

				self._buffer[y + self.pos[1] + 1][x + self.pos[0] + 1] = ((r, g, b), '█')
				self._coords.add((1 + x + self.pos[0], 1 + y + self.pos[1]))
				#self._buffer.append((r, g, b, y + self.pos[1], x + self.pos[0], '█'))

				po_x += of_x

			po_x = 0
			po_y += of_y


	def ppmread(self, filename):
		with open(filename, 'rb') as f:

			line = f.readline().decode('ascii')

			if not line.startswith('P6'):

				print("ERROR: Expected PPM file to start with P6")
				return False

			line = f.readline().decode('ascii')
			dims = line.split()

			self._img_size = tuple(map(int, dims))

			line = f.readline().decode('ascii')
			if not line.startswith('255'):

				print("ERROR: Expected 8-bit PPM with MAXVAL=255")
				return False

			temp = f.read(self._img_size[0]*self._img_size[1]*3)

			cmpt = 0
			for y in range(self._img_size[1]):

				self._img.append([])				
				for x in range(self._img_size[0]):

					self._img[-1].append((temp[cmpt], temp[cmpt+1], temp[cmpt+2]))
					cmpt += 3