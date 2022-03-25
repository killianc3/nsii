import PIL.Image

class Image:

	def __init__(self, buffer, path):

		self.size = (10, 10)
		self.pos = (0, 0)

		self._buffer = buffer
		self._img = PIL.Image.open(path)


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

		img_temp = self._img.resize(self.size, PIL.Image.ANTIALIAS)

		for x in range(self.size[0]):
			for y in range(self.size[1]):

				pixel = img_temp.getpixel((x, y))
				r, g, b = pixel

				self._buffer.append((0, 0, 0, r, g, b, y, x, ' '))


	def __import(self, path):

		img = PIL.Image.open(path)
		print(img.size)
		img = img.resize((400, 400), PIL.Image.ANTIALIAS)
		#img.thumbnail(size)
		print(img.size)
		img.show()