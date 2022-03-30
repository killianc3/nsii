from random import randint

import nsii

nsii = nsii.Nsii()
nsii.fps_target = 'max'

nsii.font = ('Terminal', 6)
#nsii.font = ('Consolas', 16)

background = nsii.new_image('image/win10.ppm')
background.size = nsii.size
background.show()

tracker = nsii.new_image('image/winxp.ppm')
tracker.size = (6, 6)

while True:

	nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

	tracker.pos = nsii.m_pos
	tracker.show()

	nsii.draw()