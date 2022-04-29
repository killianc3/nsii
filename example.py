from random import randint

import nsii

nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.p_size = 8

background = nsii.new_image('image/win11.ppm')

pointer = nsii.new_image('image/pointer.ppm')
pointer.size = (5, 5)

while True:

	#nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

	background.size = nsii.size  # taille de l'arrière-plan
	background.show()            # affichage de l'arrière-plan

	ox, oy = nsii.m_pos
	while nsii.m_click('left'):

		x, y = nsii.m_pos
		background.show()

		if x < ox and y < oy:
			nsii.rect(x, y, ox-x, oy-y)

		elif x < ox:
			nsii.rect(x, oy, ox-x, y-oy)

		elif y < oy:
			nsii.rect(ox, y, x-ox, oy-y)

		else:
			nsii.rect(ox, oy, x-ox, y-oy)

		nsii.draw()

	if nsii.key_pressed(0x20):          # si la touche espace et pressée ->

		nsii.print((0, 0), 'entrez le nom de la fenêtre : ')
		nsii.draw()

		nsii.name = nsii.input((30, 0))  # définis le nom de la fenêtre par ce que l'utilisateur a entré

	pointer.pos = tuple(map(lambda x: x - 2, nsii.m_pos))  # positionne l'image aux coordonnées de la souris
	pointer.show(hide=(255, 255, 255))                     # affiche l'image sans les pixels de couleur blancs

	nsii.draw()  # affiche tout à l'écran
