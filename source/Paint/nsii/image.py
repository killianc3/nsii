class Image:

	def __init__(self, buffer, state, path):

		self.pos = (0, 0)
		self.size = (8, 8)

		self._buffer = buffer
		self._state = state

		self._img = []
		self._img_size = None

		self._cache = []
		self._cache_size = None

		self.__decode_ppm(path)


	@property
	def pos(self):
		return self._pos

	@pos.setter
	def pos(self, new_pos):
		self._pos = new_pos

	@property
	def size(self):
		return self._size

	@size.setter
	def size(self, new_size):
		self._size = new_size


	def __decode_ppm(self, path):

		with open(path, 'rb') as file:

			if not file.readline().decode('ascii').startswith('P6'):
				raise RuntimeError('Failed to open ', path)

			self._img_size = tuple(map(int, file.readline().decode('ascii').split()))

			if not file.readline().decode('ascii').startswith('255'):
				raise RuntimeError('Failed to open ', path)

			content = file.read(3 * self._img_size[0] * self._img_size[1])
			indice = 0

			for a in range(self._img_size[1]):
				self._img.append([])

				for b in range(self._img_size[0]):

					self._img[-1].append((content[indice], content[indice+1], content[indice+2]))
					indice += 3


	def __resize(self, hide):

		self._cache.clear()
		self._cache_size = self.size

		of_x = self._img_size[0] / self._cache_size[0]
		of_y = self._img_size[1] / self._cache_size[1]

		x, y = 0, 0

		for a in range(self._cache_size[1]):
			for b in range(self._cache_size[0]):

				if self._img[round(y)][round(x)] != hide:
					self._cache.append('8;2;%d;%d;%dm' % self._img[round(y)][round(x)])

				else:
					self._cache.append(None)

				x += of_x

			x = 0
			y += of_y


	def show(self, hide=None):

		force = False
		if self.size != self._cache_size:
			self.__resize(hide)
			force = True

		indice = 0
		for y in range(self.pos[1], self._cache_size[1] + self.pos[1]):
			for x in range(self.pos[0], self._cache_size[0] + self.pos[0]):

				if (self._buffer[y][x] != self._cache[indice] or force) and self._cache[indice] != None:

					self._buffer[y][x] = self._cache[indice]
					self._state[y][x] = True

				indice += 1