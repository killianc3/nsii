def dot(buffer, state, x, y, f_col=(255, 255, 0)):

	buffer[y][x] = '8;2;%d;%d;%dm' % f_col
	state[y][x] = True


def line(buffer, state, x0, y0, x1, y1, f_col=(255, 255, 255)):

	if x0 == x1:

		for y in range(y0, y1 + 1):

			buffer[y][x0] = '8;2;%d;%d;%dm' % f_col
			state[y][x0] = True

	elif y0 == y1:

		for x in range(x0, x1 + 1):

			buffer[y0][x] = '8;2;%d;%d;%dm' % f_col
			state[y0][x] = True

	else:

		if abs(y1 - y0) < abs(x1 - x0):

			if x0 > x1:
				line_low(buffer, state, x1, y1, x0, y0, f_col)

			else:
				line_low(buffer, state, x0, y0, x1, y1, f_col)

		else:

			if y0 > y1:
				line_high(buffer, state, x1, y1, x0, y0, f_col)

			else:
				line_high(buffer, state, x0, y0, x1, y1, f_col)


def line_high(buffer, state, x0, y0, x1, y1, f_col):

	dx, dy, xi = x1 - x0, y1 - y0, 1

	if dx < 0:
		xi, dx = -1, -dx

	D, x = (2 * dx) - dy, x0

	for y in range(y0, y1 + 1):

		buffer[y][x] = '8;2;%d;%d;%dm' % f_col
		state[y][x] = True

		if D > 0:
			x = x + xi
			D = D + (2 * (dx - dy))

		else:
			D = D + 2*dx


def line_low(buffer, state, x0, y0, x1, y1, f_col):

	dx, dy, yi = x1 - x0, y1 - y0, 1

	if dy < 0:
		yi, dy = -1, -dy

	D, y = (2 * dy) - dx, y0

	for x in range(x0, x1 + 1):

		buffer[y][x] = '8;2;%d;%d;%dm' % f_col
		state[y][x] = True 

		if D > 0:
			y = y + yi
			D = D + (2 * (dy - dx))

		else:
			D = D + 2*dy


def rect(buffer, state, x, y, width, height, f_col=(255, 255, 255)):

	for a in range(height):

		buffer[y + a][x] = '8;2;%d;%d;%dm' % f_col
		buffer[y + a][x + width - 1] = '8;2;%d;%d;%dm' % f_col

		state[y + a][x] = True
		state[y + a][x + width - 1] = True

	for b in range(1, width - 1):

		buffer[y][x + b] = '8;2;%d;%d;%dm' % f_col
		buffer[y + height - 1][x + b] = '8;2;%d;%d;%dm' % f_col

		state[y][x + b] = True
		state[y + height - 1][x + b] = True


def circle(buffer, state, cx, cy, rad, f_col=(255, 255, 255)):
		
	x, y, m = 0, rad, 5 - 4 * rad

	while x <= y:

		circle_add(buffer, state, cx, cy, x, y, f_col)

		if m > 0:

			y -= 1
			m -= 8 * y

		x += 1
		m += 8 * x + 4


def circle_add(buffer, state, cx, cy, x, y, f_col):

	buffer[cy + y][cx + x] = '8;2;%d;%d;%dm' % f_col
	buffer[cy + y][cx - x] = '8;2;%d;%d;%dm' % f_col
	buffer[cy - y][cx + x] = '8;2;%d;%d;%dm' % f_col
	buffer[cy - y][cx - x] = '8;2;%d;%d;%dm' % f_col

	buffer[cy + x][cx + y] = '8;2;%d;%d;%dm' % f_col
	buffer[cy + x][cx - y] = '8;2;%d;%d;%dm' % f_col
	buffer[cy - x][cx + y] = '8;2;%d;%d;%dm' % f_col
	buffer[cy - x][cx - y] = '8;2;%d;%d;%dm' % f_col

	state[cy + y][cx + x] = True
	state[cy + y][cx - x] = True
	state[cy - y][cx + x] = True
	state[cy - y][cx - x] = True

	state[cy + x][cx + y] = True
	state[cy + x][cx - y] = True
	state[cy - x][cx + y] = True
	state[cy - x][cx - y] = True