import nsii
import os
import time
from math import *

nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Consolas', (16, 8))

# Redefini la taille en fonction de l'ecran
def resizeX(val):
    return int(val / 90 * nsii.size[0])


def resizeY(val):
    return int(val / 120 * nsii.size[1])


""" 1- Initialisation des images de fond """

background = nsii.new_image('image/noir.ppm')

fond_album1 = nsii.new_image('image/Album1.ppm')
fond_album2 = nsii.new_image('image/Album2.ppm')
fond_album3 = nsii.new_image('image/Album3.ppm')

ajout_album_image = nsii.new_image('image/ajout.ppm')
ajout_album_image.size = (12,12)
ajout_album_image.pos = (resizeX(40),resizeY(20))

nsii.size = (90,60)
uneseulephoto_taille = (120,60)


logo_photos = nsii.new_image('image/logophotos.ppm')
logo_photos.size = (resizeX(46), resizeY(15))
logo_photos.pos = (round(0*nsii.size[0]), round(-0.05*nsii.size[1]))

logo_albums = nsii.new_image('image/logo_albums.ppm')
logo_albums.size = (resizeX(46), resizeY(12))
logo_albums.pos = (round(0.5*nsii.size[0]), round(-0.02*nsii.size[1]))

logo_photos2 = nsii.new_image('image/logophotos.ppm')
logo_photos2.size = (resizeX(60), resizeY(19))
logo_photos2.pos = (round(0*uneseulephoto_taille[0]), round(-0.13*uneseulephoto_taille[1]))

logo_albums2 = nsii.new_image('image/logo_albums.ppm')
logo_albums2.size = (resizeX(60), resizeY(16))
logo_albums2.pos = (round(0.5*uneseulephoto_taille[0]), round(-0.09*uneseulephoto_taille[1]))


logo_selection = nsii.new_image('image/Selection2.ppm')
logo_selection.size = (round(nsii.size[0]*1),resizeY(13))
logo_selection.pos = (round(nsii.size[0]*-0.02),round(nsii.size[1]*-0.02))

AlbumNameGiver = nsii.new_image('image/AlbumNameGiver.ppm')
AlbumNameGiver.size = (resizeX(75), resizeY(40))
AlbumNameGiver.pos = (8,40)


#separe une liste en plusieurs liste avec un certain nombre d'élements
liste_ligne = lambda lst, sz: [lst[i:i+sz] for i in range(0, len(lst), sz)]

# Renvoie Vrai si la souris est sur une image spécifique (element)
def souris_dessus(element):
	x_souris, y_souris = nsii.m_pos
	taille_x, taille_y = element.size

	if x_souris <= element.pos[0] + taille_x and x_souris >= element.pos[0] and y_souris <= element.pos[1] + taille_y and y_souris >= element.pos[1]:
		return True
	else : 
		return False

# Renvoir Vrai si la souris entre des positions spécifiques
def souris_dessus_positions(xmin,xmax,ymin,ymax):
	x_souris, y_souris = nsii.m_pos
	xmin = resizeX(xmin)
	xmax = resizeX(xmax)
	ymin = resizeY(ymin)
	ymax = resizeY(ymax)
	if x_souris <= xmax  and x_souris >= xmin and y_souris <= ymax and y_souris >= ymin:
		return True
	else : 
		return False

class Gal:
	#Initialisation liste albums et liste image
	def __init__(self):	
		self.imagePath = os.path.abspath(".\\Picture\\galerie")
		self.imageList = os.listdir(self.imagePath)
		self.albumsPath = os.path.abspath(".\\Picture\\albums")
		self.albumsList = os.listdir(self.albumsPath)
		self.photos_ajoutees = []
		self.choix_ajout_photos = True

	def renvoie_liste_avec_images(self):
		return self.imageList

	#si il n'y a pas d'album dans le dossier album cela en cree un
	def ini_album(self):
		if self.albumsList == []:
			self.createAlbum('ALBUM')
			self.reinitialise_liste_albums()


	def reinitialise_liste_albums(self):
		self.albumsList = os.listdir(self.albumsPath)

	def renvoie_liste_albums(self):
		self.albumsList = os.listdir(self.albumsPath)
		return self.albumsList

	#fait en sorte d'avoir le bon emplacement pour plus tard rechercher les images
	def bonne_direction(self):
		dir = 'galerie/'
		liste_bonne = []
		for element in self.imageList:
			transit = dir + element	
			liste_bonne.append(transit)
		self.imageList = liste_bonne
	
	# Donne image lié à sa position dans le tableau
	def image_demande(self,position):
		seule_image = self.imageList[position]
		elem = nsii.new_image(seule_image)
		return elem


	def cree_pages(self):
		#separe en 9 puis en 3 pour chaque ligne
		self.imageList = liste_ligne(self.imageList,9)
		liste_bonne2 = []
		for element in self.imageList:
			page = liste_ligne(element,3)
			liste_bonne2.append(page)
		self.imageList = liste_bonne2


	def ajout_photo_liste_temporaire_pour_albums(self,photo):
		self.photos_ajoutees.append(liste_image[photo])


	# Initialise tous les positions, tailles des images données dans la liste
	def montre(self, liste):
		liste_positions = []
		for pages in liste:
			posx,posy = 0.007,0.08
			for element in pages:
				for i in range(len(element)):
					image = nsii.new_image(element[i])
					image.size = (round(nsii.size[0]*0.3) , round(nsii.size[1]*0.29))
					image.pos = (round(posx*nsii.size[0]), round(posy*nsii.size[1]))
					liste_positions.append(image)
					posx += 0.34
				posy += 0.31
				posx = 0.007
		return liste_positions
	

	def createAlbum(self, AlbumName):
		with open("./albums"+ '/' + AlbumName + '.txt', "w") as nAlbums:
			nAlbums.write("")

	# Ajoute les photos selectionnées dans l'album correspondant
	def ajout_photo_album(self,userChoice):
		#prends les photos de l'album
		self.albumsList = os.listdir(self.albumsPath)
		with open("./albums"+ '/' + self.albumsList[userChoice], 'r') as album:
			photos_deja_presentes = album.readlines()
		#ajoute les photos déjà dans l'album et les nouvelles
		with open("./albums"+ '/' + self.albumsList[userChoice] , "w") as Album:
			for element in photos_deja_presentes:
				Album.write(element)
			for element in self.photos_ajoutees:
				Album.write(element+'\n')
		self.photos_ajoutees = []

	#supprime l'album choisi
	def removeAlbum(self, userChoice):
		self.reinitialise_liste_albums()
		os.remove("./albums"+ '/' + self.albumsList[userChoice])

	# Initialise l'affichage pour les albums
	def album_photo(self,userChoice):
		self.albumsList = os.listdir(self.albumsPath)
		with open("./albums"+ '/' + self.albumsList[userChoice], 'r') as album:
			liste_photo_album = album.readlines()
		list_temp=[]
		for element in liste_photo_album:
			lolaa = element.strip()
			list_temp.append(lolaa)

		liste_photo_album = liste_ligne(list_temp,9)
		liste_bonne2 = []
		for element in liste_photo_album:
			page = liste_ligne(element,3)
			liste_bonne2.append(page)
		liste_photo_album = liste_bonne2

		positions = gal.montre(liste_photo_album)

		return positions



# Initialise Gallerie
gal = Gal()
gal.ini_album()
gal.bonne_direction()
liste_image = gal.renvoie_liste_avec_images()
gal.cree_pages()
liste_toutes_photos = gal.montre(gal.renvoie_liste_avec_images())
# True si on est en train d'ajouter des photos dans un album et False sinon
ajout_a_album = False
#True si on doit montre un album
albummontre = False

def main(album_montre,ajout_albumm,albummm):
	num_page = 0
	initialise = False
	liste_base = liste_toutes_photos
	while True:
		nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'
		x_souris, y_souris = nsii.m_pos
		background.size = nsii.size
		
		# Affichage en grand de la galerie de base si on appuie sur espace
		if nsii.key_pressed(0x20):
			Album_page = False
			break

		"""Changement des pages""" 
		if nsii.key_pressed(0x27):
			time.sleep(0.15)
			if num_page<ceil(len(liste_base)/9)-1:
				num_page += 1

		if nsii.key_pressed(0x25):
			time.sleep(0.15)
			if num_page > 0:
				num_page -= 1

		background.show()


		# Change pour aller dans le mode album
		if nsii.m_click('left'):
			if souris_dessus(logo_albums):
				Album_page = True
				break
			if souris_dessus(logo_photos):
				Album_page = True
				break
			if souris_dessus(logo_selection):
				Album_page = True
				break


		if album_montre:
			#on initialise seulement au départ ensuite c'est bon
			if not initialise:
				lol = gal.album_photo(albummm)
				liste_base = lol
				initialise = True
			else:
				liste_base = lol
		else:
			liste_base = liste_toutes_photos

		"""Affiche les photos d'apres leur page"""
		if num_page == ceil(len(liste_base)/9)-1:
			if liste_base == []:
				pass
			else:
				for i in range(9*num_page,len(liste_base)):
					liste_base[i].show()
					if nsii.m_click('left'):
						if souris_dessus(liste_base[i]):
							time.sleep(0.1)
							# ajoute l'image à l'album si on est en train de selectionner pour l'album
							if ajout_albumm:
								gal.ajout_photo_liste_temporaire_pour_albums(i)
		else:
			if liste_base == []:
				pass 
			else :
				for i in range(9*num_page,9+9*num_page):
					liste_base[i].show()
					if nsii.m_click('left'):
						if souris_dessus(liste_base[i]):
							time.sleep(0.1)
							if ajout_albumm:
								gal.ajout_photo_liste_temporaire_pour_albums(i)
		

		if ajout_albumm:
			logo_selection.show()
		else:
			logo_photos.show()
			logo_albums.show()

		nsii.draw()

	# On va dans le mode album
	if Album_page:
		if ajout_albumm:
			gal.ajout_photo_album(albummm)
		albums()
	# On va dans le mode en grand pour la galerie avec toutes les photos"
	else:
		nsii.size = (120,60)
		gal.ajout_photo_album(0)
		pain()

# Mode Album 
def albums():
	num_albums = 0
	liste_base2 = gal.renvoie_liste_albums()
	fond = fond_album3
	logo_photos.size = (resizeX(46),resizeY(23))
	logo_albums.size = (resizeX(46),resizeY(21))
	creationAlbum = False
	ajout_a_album = False
	album_montree = False
	imagecreation = False
	while True:
		nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'
		x_souris, y_souris = nsii.m_pos
		fond.size = nsii.size
		fond.show()
		if creationAlbum:
			imagecreation = True

		"""Changement des pages""" 
		if nsii.key_pressed(0x27):
			time.sleep(0.2)
			if num_albums<ceil(len(liste_base2)/3)-1:
				num_albums += 1

		if nsii.key_pressed(0x25):
			time.sleep(0.2)
			if num_albums > 0:
				num_albums -= 1

		"""Affiche les albums avec leur nom d'apres leur page"""
		if num_albums == ceil(len(liste_base2)/3)-1:
			if len(liste_base2)%3 == 0:
				fond = fond_album3
			elif len(liste_base2)%3 == 1:
				fond = fond_album1
			elif len(liste_base2)%3 == 2:
				fond = fond_album2
			text_posx = resizeX(30)
			text_posy = resizeY(45) 
			for i in range(3*num_albums,len(liste_base2)):
				temp = liste_base2[i]
				temp2 = temp[:-4]
				nsii.print((text_posx, text_posy), temp2)
				text_posy += resizeY(28)
		else:
			fond = fond_album3
			text_posx = resizeX(30)
			text_posy = resizeY(45)  	
			for i in range(3*num_albums,3+3*num_albums):
				temp = liste_base2[i]
				temp2 = temp[:-4]
				nsii.print((text_posx, text_posy), temp2)
				text_posy += resizeY(28)

		ajout_album_image.show()
		logo_photos.show()
		logo_albums.show()

		# Gere les clics sur les icones pour les cases d'ajout de photo, de suppression de photo et de changements de pages
		if nsii.m_click('left'):
			if souris_dessus_positions(76,86,21,30) :
				time.sleep(0.2)
				if num_albums<ceil(len(liste_base2)/3)-1:
					num_albums += 1

			if souris_dessus_positions(3,13,21,30):
				time.sleep(0.2)
				if num_albums > 0:
					num_albums -= 1

			if souris_dessus(ajout_album_image):
				creationAlbum = True

			if souris_dessus(logo_photos):
				logo_photos.size = (46,15)
				logo_albums.size = (46,12)
				main(albummontre,ajout_a_album,[])
				
			elif souris_dessus_positions(4,63,36,54):
				album_a_montre = num_albums*3
				album_montree = True
				break
			elif souris_dessus_positions(4,63,64,81):
				album_a_montre = num_albums*3 + 1
				album_montree = True
				break
			elif souris_dessus_positions(4,63,92,111):
				album_a_montre = num_albums*3 + 2
				album_montree = True
				break

			elif souris_dessus_positions(67,78,41,50):
				album_a_montre = num_albums*3 
				ajout_a_album = True
				break
			elif souris_dessus_positions(67,78,69,79):
				album_a_montre = num_albums*3 + 1
				ajout_a_album = True
				break
			elif souris_dessus_positions(67,78,97,106):
				album_a_montre = num_albums*3 + 2 
				ajout_a_album = True
				break

			elif souris_dessus_positions(79,90,41,50):	
				if not len(liste_base2) == 1:
					time.sleep(0.2)
					album_a_montre = num_albums*3 
					gal.removeAlbum(album_a_montre)
					gal.reinitialise_liste_albums()
					albums()
				
			elif souris_dessus_positions(79,90,69,79):
				time.sleep(0.2)
				album_a_montre = num_albums*3 + 1
				gal.removeAlbum(album_a_montre)
				gal.reinitialise_liste_albums()
				albums()
				
			elif souris_dessus_positions(79,90,97,106):
				time.sleep(0.2)
				album_a_montre = num_albums*3 + 2 
				gal.removeAlbum(album_a_montre)
				gal.reinitialise_liste_albums()
				albums()

		# Gère quand l'utilisateur crée un album
		if creationAlbum:
			AlbumNameGiver.show()
			if imagecreation:
				nom_album = nsii.input((resizeX(21),resizeY(65)))
				gal.createAlbum(nom_album)
				creationAlbum = False
				albums()
		
		nsii.draw()
	nsii.size = (90,60)
	logo_photos.size = (resizeX(46),resizeY(15))
	logo_albums.size = (resizeX(46),resizeY(12))
	main(album_montree,ajout_a_album,album_a_montre)

def pain():
	gal2 = Gal()
	gal2.bonne_direction()
	liste_base2 = gal2.renvoie_liste_avec_images()
	emplacement = 0
	mama = gal2.image_demande(emplacement)
	Album_page = False

	while True:
		nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

		# Change mode 
		if nsii.m_click('left'):
			if souris_dessus(logo_photos2):
				break
			if souris_dessus(logo_albums2):
				Album_page = True

		# Si on appuie sur echap on revient sur la galerie avec toutes les photos version petit
		if nsii.key_pressed(0x1B):
			break

		"""Change de photo"""
		if nsii.key_pressed(0x27):
			time.sleep(0.1)
			if emplacement<len(liste_base2)-1:
				emplacement += 1

		if nsii.key_pressed(0x25):
			time.sleep(0.1)
			if emplacement>0:
				emplacement -= 1

		mama = gal2.image_demande(emplacement)
		mama.size = nsii.size
		mama.show()
		logo_photos2.show()
		logo_albums2.show()
		nsii.draw()

	nsii.size = (90,60)
	if Album_page:
		albums()
	else:
		main(albummontre,ajout_a_album,[])

main(albummontre,ajout_a_album,[])

