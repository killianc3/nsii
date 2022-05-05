from nsii import Nsii

import random
import time
import sys
import os

def main():

	nsii = Nsii()

	nsii.p_size = 6
	nsii.size = (140, 40)
	nsii.fps_target = 120

	background = nsii.new_image('image/wallpaper.ppm')

	hover = nsii.new_image('image/hover.ppm')
	hover.pos = (4, 4)
	hover.size = (16, 16)

	paint = nsii.new_image('image/paint.ppm')
	paint.pos = (4, 4)
	paint.size = (16, 16)

	player = nsii.new_image('image/player.ppm')
	player.pos = (24, 4)
	player.size = (16, 16)

	picture = nsii.new_image('image/picture.ppm')
	picture.pos = (44, 4)
	picture.size = (16, 16)

	motus = nsii.new_image('image/motus.ppm')
	motus.pos = (64, 4)
	motus.size = (16, 16)

	calc = nsii.new_image('image/calc.ppm')
	calc.pos = (84, 4)
	calc.size = (16, 16)

	icons = [calc, player, picture, paint, motus]
	lastc = [0 for i in range(len(icons))]

	init(nsii)
	loop(nsii, background, hover, icons, lastc)

def loop(nsii, background, hover, icons, lastc):

	while True:

		if nsii.m_click('left'):
			on_click(nsii, background, hover, icons, lastc)

		else:
			routine(nsii, background, hover, icons)

def init(nsii):

	nsii.name = 'loading'

	with open('log.log') as log:

		for i in range(160):

			sys.stdout.write(log.readline()[50:])
			sys.stdout.flush()
			time.sleep(0.00000000001)

	nsii.draw()
	time.sleep(0.6)
	nsii.name = 'Les fenêtres'

def routine(nsii, background, hover, icons):

	background.size = nsii.size
	background.show()

	hover.show(hide=(255, 0, 0))

	for icon in icons:
		icon.show(hide=(255, 0, 0))

	nsii.draw()

def on_click(nsii, background, hover, icons, lastc):

	mx, my = nsii.m_pos

	for indice, icon in enumerate(icons):

		if mx >= icon.pos[0] and mx < icon.pos[0] + icon.size[0] and my >= icon.pos[1] and my < icon.pos[1] + icon.size[1]:

			if time.time() - lastc[indice] < 0.4:

				if indice == 0:
					pass

				elif indice == 1:
					pass

				elif indice == 2:
					pass

				elif indice == 3:
					pass

				else:
					pass

			hover.pos = icon.pos
			lastc[indice] = time.time()
			of_x, of_y = mx - icon.pos[0], my - icon.pos[1]

			while nsii.m_click('left'):

				if abs(mx - nsii.m_pos[0]) > 2 or abs(my - nsii.m_pos[1]) > 2:

					while nsii.m_click('left'):

						icon.pos = (nsii.m_pos[0] - of_x, nsii.m_pos[1] - of_y)
						hover.pos = icon.pos
						routine(nsii, background, hover, icons)

if __name__ == '__main__':
	main()