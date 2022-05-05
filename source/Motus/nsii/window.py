import sys
import time

from . import frame_rate
from . import cmd_input
from . import config
from . import tools

class Window:

	def __init__(self, widht=80, height=40, target_fps=60, rgb_mode=False):

		self.rgb_mode = rgb_mode
		self.target_fps = target_fps

		self.widht = widht
		self.height = height

		self.buffer = [[None for x in range(widht)] for y in range(height)]
		self.to_update = set()

		self.config = config.Config()
		self.frame_rate = frame_rate.Frame_rate(self, 1)
		self.cmd_input = cmd_input.Cmd_input()
		self.basics = tools.Basics(self)
		self.layer = tools.Layer(self)
		self.text = tools.Text(self)


		self.config.cmd_config(widht, height)

	def draw(self):

		while len(self.to_update) > 0:

			x, y = self.to_update.pop()
			car, f_color, b_color = self.buffer[y][x]

			if self.rgb_mode:
				sys.stdout.write(f'\x1b[38;2;{f_color[0]};{f_color[1]};{f_color[2]}m')
				sys.stdout.write(f'\x1b[48;2;{b_color[0]};{b_color[1]};{b_color[2]}m')

			sys.stdout.write(f'\x1b[{y + 1};{x + 1}H{car}')

		sys.stdout.flush()

		self.frame_rate.update_and_wait()

	def put_pixel(self, x, y, car, f_color, b_color):

		if (x >= 0 and x < self.widht) and (y >= 0 and y < self.height):

			self.buffer[y][x] = (car, f_color, b_color)
			self.to_update.add((x, y))

	def back_ground(self, color=(0, 0, 0), draw=False):

		sys.stdout.write(f'\x1b[48;2;{color[0]};{color[1]};{color[2]}m\x1b[2J')

		if draw:
			sys.stdout.flush()
			self.frame_rate.update()