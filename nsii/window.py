from . import tools

class Window:

	def __init__(self, buffer, size=(10, 10), pos=(0, 0)):

		self.size = size
		self.pos = pos

		self._buffer = buffer


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


	def __add_buffer(self, pixel):

		if pixel[-3] >= 0 and pixel[-3] < self.size[0] and pixel[-2] >= 0 and pixel[-2] < self.size[1]:

			self._buffer.append((*pixel[:-3], pixel[-2] + 1 + self.pos[1], pixel[-3] + 1 + self.pos[0], pixel[-1]))


	def dot(self, *args, **kwargs):

		tools.dot(self.__add_buffer, *args, **kwargs)


	def line(self, *args, **kwargs):

		tools.line(self.__add_buffer, *args, **kwargs)


	def rect(self, *args, **kwargs):

		tools.rect(self.__add_buffer, *args, **kwargs)


	def circle(self, *args, **kwargs):

		tools.circle(self.__add_buffer, *args, **kwargs)