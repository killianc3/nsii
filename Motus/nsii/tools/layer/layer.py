from . import template

class Layer:

	def __init__(self, window):

		self.window = window

	def new_layer(self, x, y, pixel, color=tuple(), reference=dict(), color_mode=False, f_color=(255, 255, 255), b_color=(0, 0, 0), ban_car=' '):

		return template.Template(self.window, x, y, pixel, color, reference, color_mode, f_color, b_color, ban_car)