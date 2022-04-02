class Image:

	def __init__(self, buffer, state, path):

		self.size = (40, 20)
		self.pos = (0, 0)

		self._buffer = buffer
		self._state = state

		self._img = []
		self._img_size = None

		self._cache = []
		self._cache_size = None

		self.build_img(path)


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


	def show(self, hide=None):

		if self.size == self._cache_size:

			p_id = 0
			for y in range(self.pos[1], self.pos[1] + self.size[1]):
				for x in range(self.pos[0], self.pos[0] + self.size[0]):

					if self._buffer[y][x] != self._cache[p_id] and self._cache[p_id] != None:

						self._buffer[y][x] = self._cache[p_id]
						self._state[y][x] = True

					p_id += 1

		else:

			of_x, of_y = self._img_size[0] / self.size[0], self._img_size[1] / self.size[1]
			po_x, po_y = 0, 0

			self._cache.clear()

			for y in range(self.pos[1], self.pos[1] + self.size[1]):
				for x in range(self.pos[0], self.pos[0] + self.size[0]):

					color = self._img[round(po_y)][round(po_x)]

					if color != hide:

						pixel = '\x1b[38;2;%d;%d;%dm█'%(color)

						self._buffer[y][x] = pixel
						self._cache.append(pixel)

						self._state[y][x] = True

					else:
						self._cache.append(None)


					po_x += of_x

				po_x = 0
				po_y += of_y


			self._cache_size = self.size

	def build_img(self, filename):
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