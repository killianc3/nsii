from . import core
from . import terminal
from . import fps

from . import io

from . import image
from . import window

class Nsii:

	def __init__(self):

		self._core = core.Core()
		self._terminal = terminal.Terminal()
		self._fps_handler = fps.Fps_handler()


	@property
	def name(self):
		return self._terminal.name

	@name.setter
	def name(self, new_name):
		self._terminal.name = new_name


	@property
	def size(self):
		return self._terminal.size

	@size.setter
	def size(self, new_size):
		self._terminal.size = new_size 


	@property
	def client_size(self):
		return self._terminal.client_size

	@client_size.setter
	def client_size(self, new_size):
		self._terminal.client_size = new_size


	@property
	def pos(self):
		return self._terminal.pos

	@pos.setter
	def pos(self, new_pos):
		self._terminal.pos = new_pos


	@property
	def fps(self):
		return self._fps_handler.fps


	@property
	def fps_target(self):
		return self._fps_handler.fps_target

	@fps_target.setter
	def fps_target(self, new_target):
		self._fps_handler.fps_target = new_target


	@property
	def font(self):
		return self._terminal.font

	@font.setter
	def font(self, new_font):
		self._terminal.font = new_font


	@property
	def m_pos(self):
		return self._terminal.m_pos
	
	@m_pos.setter
	def m_pos(self, new_pos):
		self._terminal.m_pos = new_pos


	def draw(self, *args, **kwargs):
		self._core.draw(self._fps_handler.update, *self.size, *args, **kwargs)


	def new_window(self, *args, **kwargs):
		return window.Window(self._core.buffer, self._core.state, *args, **kwargs)


	def new_image(self, *args, **kwargs):
		return image.Image(self._core.buffer, self._core.state, *args, **kwargs)


	def m_click(self, *args, **kwargs):
		return self._terminal.m_click(*args, **kwargs)


	def input(self, *args, **kwargs):
		return io.input(self.draw, *args, **kwargs)

	def key_pressed(self, *args, **kwargs):
		return io.key_pressed(self._terminal.user32, *args, **kwargs)