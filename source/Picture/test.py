from random import randint

import nsii

nsii = nsii.Nsii()
nsii.fps_target = 'max'
#nsii.font = ('Terminal', 6)
nsii.font = ('Consolas', (16, 8))

win = nsii.new_window()
win.size = nsii.size

background = nsii.new_image('image/win10.ppm')

pointer = nsii.new_image('image/pointer.ppm')
pointer.size = (5, 5)

tracker = nsii.new_image('image/winxp.ppm')
tracker.size = (6, 6)

while True:

	nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos}'

	background.size = nsii.size
	background.show()

	pointer.pos = tuple(map(lambda x: x-2, nsii.m_pos))
	pointer.show(hide=(255, 255, 255))

	ox, oy = nsii.m_pos
	while nsii.m_click('left'):

		x, y = nsii.m_pos
		background.show()

		if x < ox and y < oy:
			win.rect(x, y, ox-x, oy-y)

		elif x < ox:
			win.rect(x, oy, ox-x, y-oy)

		elif y < oy:
			win.rect(ox, y, x-ox, oy-y)

		else:
			win.rect(ox, oy, x-ox, y-oy)

		nsii.draw()

	nsii.draw()
