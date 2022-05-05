class Template:

	def __init__(self, window, x, y, pixel, color, reference, color_mode, f_color, b_color, ban_car):

		self.put_pixel = window.put_pixel
		self.draw = window.draw

		self.pos_x = x
		self.pos_y= y

		self.pixel = pixel
		self.color = color
		self.reference = reference

		self.widht = len(self.pixel[0])
		self.height = len(self.pixel)

		self.pixel_list = []
		self.color_mode = color_mode

		self.build(ban_car, f_color, b_color)

	def build(self, ban_car, f_color, b_color):

		for x in range(self.widht):

			for y in range(self.height):

				if self.pixel[y][x] != ban_car:

					if self.color_mode:
						f_color, b_color = self.reference[self.color[y][x]]

					self.pixel_list.append((x, y, self.pixel[y][x], f_color, b_color))

	def show(self, draw=True, force_color=None):

		for pixel in self.pixel_list:

			if force_color != None:

				x, y, car, *trash = pixel
				f_color, b_color = force_color

			else:
				x, y, car, f_color, b_color = pixel

			self.put_pixel(self.pos_x + x, self.pos_y + y, car, f_color, b_color)

		if draw:
			self.draw()

	def change_pos(self, new_x, new_y):

		self.pos_x = new_x
		self.pos_y = new_y