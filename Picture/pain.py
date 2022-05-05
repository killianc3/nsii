import nsii
import os

from math import *

nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Consolas', (16, 8))


nsii.size = (120,60)
posx,posy = 0.005,0.008

logo_photos = nsii.new_image('image/logophotos.ppm')
logo_photos.size = (60, 19)
logo_photos.pos = (round(0*nsii.size[0]), round(-0.04*nsii.size[1]))

logo_albums = nsii.new_image('image/logo_albums.ppm')
logo_albums.size = (60, 16)
logo_albums.pos = (round(0.5*nsii.size[0]), round(-0.02*nsii.size[1]))

class Gal:
	def __init__(self):
		
		self.imagePath = os.path.abspath(".\galerie")
		self.imageList = os.listdir(self.imagePath)
	
	def ajout_photo(self, new_photo):
		dir = 'galerie/'
		transit = dir + new_photo
		self.imageList.append(transit)

	def renvoie(self):
		return self.imageList

	def bonne_direction(self):
		dir = 'galerie/'
		liste_bonne = []
		for element in self.imageList:
			
			transit = dir + element
			
			liste_bonne.append(transit)
		
		#liste_ligne = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]
		#self.imageList = liste_ligne(liste_bonne,3)
		self.imageList = liste_bonne
		

	def image_demande(self,position):
		seule_image = self.imageList[position]
		elem = nsii.new_image(seule_image)

		return elem


	def montre(self):
		posx,posy = 0.007,0.08
		liste_positions = []
		

		for element in self.imageList:

			for i in range(len(element)):

				image = nsii.new_image(element[i])
				image.size = (round(nsii.size[0]*0.3) , round(nsii.size[1]*0.29))
				image.pos = (round(posx*nsii.size[0]), round(posy*nsii.size[1]))
				liste_positions.append(image)
				posx += 0.34

			posy += 0.31
			posx = 0.007
			

		return liste_positions


gal = Gal()

gal.bonne_direction()


liste_base = gal.renvoie()

emplacement = 0

mama = gal.image_demande(emplacement)

x=1

while True:

	nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

	x += 1

	lala = (-1)**x

	if nsii.key_pressed(0x1B):
		exec(open("main.py").read())

	if nsii.key_pressed(0x27):
		if emplacement<len(liste_base)-1:
			emplacement += 1

	if nsii.key_pressed(0x25):
		if emplacement>0:
			emplacement -= 1

	mama = gal.image_demande(emplacement)
	mama.size = nsii.size

	
	mama.show()
	#icon.show()
	logo_photos.show()
	logo_albums.show()
	
	

	nsii.draw()



