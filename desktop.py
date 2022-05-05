from nsii import Nsii

import random
import time
import sys
import os
import pathlib

def main():

	script_location = pathlib.Path(__file__).absolute().parent

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

	icons = {'calc':[calc, 0], 'player':[player, 0], 'picture':[picture, 0], 'paint':[paint, 0], 'motus':[motus, 0]}

	nsii.name = 'loading'
	with open('log.log') as log:

		for i in range(160):

			sys.stdout.write(log.readline()[50:])
			sys.stdout.flush()
			time.sleep(0.00000000001)

	nsii.draw()
	time.sleep(0.6)
	nsii.name = 'Les fenêtres'

	while True:

		if nsii.m_click('left'):
			mx, my = nsii.m_pos

			for icon in icons:

				if mx >= icons[icon][0].pos[0] and mx < icons[icon][0].pos[0] + icons[icon][0].size[0] and my >= icons[icon][0].pos[1] and my < icons[icon][0].pos[1] + icons[icon][0].size[1]:

					if time.time() - icons[icon][1] < 0.4:

						if icon == 'calc': # calc
							os.system('start cmd /c Calc\\MainCalc.py')

						elif icon == 'player': # player
							os.system('start cmd /c Player\\PlayerInterface.py')

						elif icon == 'picture': # picture
							os.system('start cmd /k Picture\\main.py')

						elif icon == 'paint': # paint
							os.system('start cmd /c Paint\\Paint.py')

						elif icon == 'motus': # motus
							os.system('start cmd /c Motus\\motus.py')

					hover.pos = icons[icon][0].pos
					icons[icon][1] = time.time()
					of_x, of_y = mx - icons[icon][0].pos[0], my - icons[icon][0].pos[1]

					while nsii.m_click('left'):

						if abs(mx - nsii.m_pos[0]) > 2 or abs(my - nsii.m_pos[1]) > 2:

							while nsii.m_click('left'):

								icons[icon][0].pos = (nsii.m_pos[0] - of_x, nsii.m_pos[1] - of_y)
								hover.pos = icons[icon][0].pos

								routine(nsii, background, hover, icons)

		else:
			routine(nsii, background, hover, icons)


def routine(nsii, background, hover, icons):

	background.size = nsii.size
	background.show()

	hover.show(hide=(255, 0, 0))

	for icon in icons:
		icons[icon][0].show(hide=(255, 0, 0))

	nsii.draw()


def launch(path):

	names = ('py', 'py', 'python2', 'python3')
	for name in names:

		try:
			os.system(f'start cmd /k {name} {path}')
			return

		except:
			pass

	raise RuntimeError('enable to launch python')


if __name__ == '__main__':
	main()