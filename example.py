from random import randint

import nsii

nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Consolas', (16, 8))

background = nsii.new_image('image/silicon.ppm')

pointer = nsii.new_image('image/pointer.ppm')
pointer.size = (5, 5)

while True:

	#nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

	background.size = nsii.size  # taille de l'arrière-plan
	background.show()            # affichage de l'arrière-plan


	if nsii.key_pressed(0x20):          # si la touche espace et pressée ->
		nsii.name = nsii.input((0, 0))  # définis le nom de la fenêtre par ce que l'utilisateur a entré


	if nsii.key_pressed(0x25):  # décale la fenêtre à gauche si la flèche gauche est pressée
		x, y = nsii.pos
		nsii.pos = (x-1, y)

	if nsii.key_pressed(0x26):  # décale en haut
		x, y = nsii.pos
		nsii.pos = (x, y-1)

	if nsii.key_pressed(0x27):  # décale à droite
		x, y = nsii.pos
		nsii.pos = (x+1, y)

	if nsii.key_pressed(0x28):  # decale en bas
		x, y = nsii.pos
		nsii.pos = (x, y+1)


	pointer.pos = tuple(map(lambda x: x - 2, nsii.m_pos))  # positionne l'image aux coordonnées de la souris
	pointer.show(hide=(255, 255, 255))                     # affiche l'image sans les pixels de couleur blancs

	nsii.draw()  # affiche tout à l'écran
