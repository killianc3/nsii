from .color import BLACK, WHITE

def dot(add_buffer, x, y, car, f_col=WHITE):

	add_buffer((*f_col, x, y, car))


def line(add_buffer, x0, y0, x1, y1, car, f_col=WHITE):

	if x0 == x1:

		for y in range(y0, y1 + 1):
			add_buffer((*f_col, x0, y, car))

	elif y0 == y1:

		for x in range(x0, x1 + 1):
			add_buffer((*f_col, x, y0, car))

	else:

		if abs(y1 - y0) < abs(x1 - x0):

			if x0 > x1:
				line_low(add_buffer, x1, y1, x0, y0, car, f_col)

			else:
				line_low(add_buffer, x0, y0, x1, y1, car, f_col)

		else:

			if y0 > y1:
				line_high(add_buffer, x1, y1, x0, y0, car, f_col)

			else:
				line_high(add_buffer, x0, y0, x1, y1, car, f_col)


def line_high(add_buffer, x0, y0, x1, y1, car, f_col):

	dx, dy, xi = x1 - x0, y1 - y0, 1

	if dx < 0:
		xi, dx = -1, -dx

	D, x = (2 * dx) - dy, x0

	for y in range(y0, y1 + 1):

		add_buffer((*f_col, x, y, car))

		if D > 0:
			x = x + xi
			D = D + (2 * (dx - dy))

		else:
			D = D + 2*dx


def line_low(add_buffer, x0, y0, x1, y1, car, f_col):

	dx, dy, yi = x1 - x0, y1 - y0, 1

	if dy < 0:
		yi, dy = -1, -dy

	D, y = (2 * dy) - dx, y0

	for x in range(x0, x1 + 1): 

		add_buffer((*f_col, x, y, car))

		if D > 0:
			y = y + yi
			D = D + (2 * (dy - dx))

		else:
			D = D + 2*dy


def rect(add_buffer, x, y, width, height, car, f_col=WHITE):

	for a in range(height):

		add_buffer((*f_col, x, y + a, car))
		add_buffer((*f_col, x + width - 1, y + a, car))

	for b in range(1, width - 1):

		add_buffer((*f_col, x + b, y, car))
		add_buffer((*f_col, x + b, y + height - 1, car))


def circle(add_buffer, cx, cy, rad, car, f_col=WHITE):
		
	x, y, m = 0, rad, 5 - 4 * rad

	while x <= y:

		circle_add(add_buffer, cx, cy, x, y, car, f_col)

		if m > 0:

			y -= 1
			m -= 8 * y

		x += 1
		m += 8 * x + 4


def circle_add(add_buffer, cx, cy, x, y, car, f_col):

	add_buffer((*f_col, cx + x, cy + y, car))
	add_buffer((*f_col, cx - x, cy + y, car))
	add_buffer((*f_col, cx + x, cy - y, car))
	add_buffer((*f_col, cx - x, cy - y, car))

	add_buffer((*f_col, cx + y, cy + x, car))
	add_buffer((*f_col, cx - y, cy + x, car))
	add_buffer((*f_col, cx + y, cy - x, car))
	add_buffer((*f_col, cx - y, cy - x, car))