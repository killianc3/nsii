class Basics:

	def __init__(self, window):
		
		self.put_pixel = window.put_pixel
		self.draw = window.draw

	def check_for_int(self, number):

		if isinstance(number, int):
			return number

		else:
			return round(number)

	def dot(self, x, y, car, draw=True, f_color=(255, 255, 255), b_color=(0, 0, 0)):

		x = self.check_for_int(x)
		y = self.check_for_int(y)

		self.put_pixel(x, y, car, f_color, b_color)

		if draw:
			self.draw()


	def line(self, x0, y0, x1, y1, car, draw=True, f_color=(255, 255, 255), b_color=(0, 0, 0)):

		x0 = self.check_for_int(x0)
		y0 = self.check_for_int(y0)
		x1 = self.check_for_int(x1)
		y1 = self.check_for_int(y1)

		if x0 == x1:

			for y in range(y0, y1 + 1):
				self.put_pixel(x0, y, car, f_color, b_color)

		elif y0 == y1:

			for x in range(x0, x1 + 1):
				self.put_pixel(x, y0, car, f_color, b_color)

		else:
			if abs(y1 - y0) < abs(x1 - x0):

				if x0 > x1:
					self.low_line(x1, y1, x0, y0, car, f_color, b_color)

				else:
					self.low_line(x0, y0, x1, y1, car, f_color, b_color)

			else:

				if y0 > y1:
					self.high_line(x1, y1, x0, y0, car, f_color, b_color)

				else:
					self.high_line(x0, y0, x1, y1, car, f_color, b_color)

		if draw:
			self.draw()


	def high_line(self, x0, y0, x1, y1, car, f_color, b_color):

		dx, dy, xi = x1 - x0, y1 - y0, 1

		if dx < 0:
			xi, dx = -1, -dx

		D, x = (2 * dx) - dy, x0

		for y in range(y0, y1 + 1):

			self.put_pixel(x, y, car, f_color, b_color)

			if D > 0:
				x = x + xi
				D = D + (2 * (dx - dy))

			else:
				D = D + 2*dx


	def low_line(self, x0, y0, x1, y1, car, f_color, b_color):

		dx, dy, yi = x1 - x0, y1 - y0, 1

		if dy < 0:
			yi, dy = -1, -dy

		D, y = (2 * dy) - dx, y0

		for x in range(x0, x1 + 1): 

			self.put_pixel(x, y, car, f_color, b_color)

			if D > 0:
				y = y + yi
				D = D + (2 * (dy - dx))

			else:
				D = D + 2*dy


	def circle(self, centerx, centery, rad, car, fill=False, draw=True, f_color=(255, 255, 255), b_color=(0, 0, 0)):

		centerx = self.check_for_int(centerx)
		centery = self.check_for_int(centery)
		rad = self.check_for_int(rad)
		
		if fill:
			self.fillCircle(centerx, centery, rad, car, f_color, b_color)

		else:

			x, y, m = 0, rad, 5 - 4 * rad

			while x <= y:
				self.pixel_circle(centerx, centery, x, y, car, f_color, b_color)

				if m > 0:

					y -= 1
					m -= 8 * y

				x += 1
				m += 8 * x + 4

		if draw:
			self.draw()


	def fillCircle(self, centerx, centery, rad, car, f_color, b_color):

		x, y, m = 0, rad, 5 - 4 * rad

		while x <= y:

			for tempx in range(centerx - y, centerx + y + 1):

				self.put_pixel(tempx, centery - x, car, f_color, b_color)
				self.put_pixel(tempx, centery + x, car, f_color, b_color)

			if m > 0:

				for tempx in range(centerx - x, centerx + x + 1):

					self.put_pixel(tempx, centery - y, car, f_color, b_color)
					self.put_pixel(tempx, centery + y, car, f_color, b_color)

				y -= 1
				m -= 8 * y

			x += 1
			m += 8 * x + 4


	def pixel_circle(self, cx, cy, x, y, car, f_color, b_color):

		self.put_pixel(cx + x, cy + y, car, f_color, b_color)
		self.put_pixel(cx - x, cy + y, car, f_color, b_color)
		self.put_pixel(cx + x, cy - y, car, f_color, b_color)
		self.put_pixel(cx - x, cy - y, car, f_color, b_color)

		self.put_pixel(cx + y, cy + x, car, f_color, b_color)
		self.put_pixel(cx - y, cy + x, car, f_color, b_color)
		self.put_pixel(cx + y, cy - x, car, f_color, b_color)
		self.put_pixel(cx - y, cy - x, car, f_color, b_color)


	def rect(self, ox, oy, widht, height, car, fill=False, draw=True, f_color=(255, 255, 255), b_color=(0, 0, 0)):

		ox = self.check_for_int(ox)
		oy = self.check_for_int(oy)
		widht = self.check_for_int(widht)
		height = self.check_for_int(height)

		if fill:

			for y in range(oy, oy + height):

				self.line(ox, y, ox + widht, y, car, False, f_color, b_color)

		else:

			self.line(ox, oy, ox + widht, oy, car, False, f_color, b_color)
			self.line(ox, oy + height, ox + widht, oy + height, car, False, f_color, b_color)

			for y in range(oy + 1, oy + height):

				self.put_pixel(ox, y, car, f_color, b_color)
				self.put_pixel(ox + widht, y, car, f_color, b_color)

		if draw:
			self.draw()