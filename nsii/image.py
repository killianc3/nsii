class Image:

	def __init__(self, buffer, coords, path):

		self.size = (40, 20)
		self.pos = (0, 0)

		self._buffer = buffer
		self._coords = coords
		self._img = []
		self._img_size = None

		self._cache = [[None for a in range(400)] for b in range(400)]
		self._cache_size = None

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

		if self.size == self._cache_size:

			for y in range(self.size[1]):
				for x in range(self.size[0]):

					pixel = self._cache[y][x]

					if self._buffer[y + self.pos[1]][x + self.pos[0]] != pixel:

						self._buffer[y + self.pos[1]][x + self.pos[0]] = pixel

						self._coords.add((x + self.pos[0], y + self.pos[1]))

		else:

			of_x, of_y = self._img_size[0] / self.size[0], self._img_size[1] / self.size[1]
			po_x, po_y = 0, 0

			for y in range(self.size[1]):
				for x in range(self.size[0]):

					r, g, b = self._img[round(po_y)][round(po_x)]

					self._buffer[y + self.pos[1]][x + self.pos[0]] = ((r, g, b), '█')
					self._coords.add((x + self.pos[0], y + self.pos[1]))

					self._cache[y][x] = ((r, g, b), '█')

					po_x += of_x

				po_x = 0
				po_y += of_y


			self._cache_size = self.size

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