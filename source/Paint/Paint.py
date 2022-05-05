import nsii

pinceau = 0
crayon = 0
seau = 0
gomme = 0
rouge = 0
vert = 0
bleu = 0
jaune = 0
rose = 0
orange = 0
noir = 1
couleur = ['rouge', 'vert', 'bleu', 'jaune', 'noir', 'rose', 'orange']
 

class Paint:
	
	def __init__(self):
		self.nsii = nsii.Nsii()   #initialisation du moteur graphique 
		self.nsii.fps_target = 'max'  #initialisation des fps au "max"
		self.bg = self.nsii.new_image('bgPaint.ppm')  #initialisation de l'image qui sert de background 
		self.pointeur = self.nsii.new_image('pointeur.ppm')   #initialisation de l'image qui sert de pointeur 
		self.pointeur.size = (5, 5)   #définition de la taille du pointeur 
		self.pinceau = self.nsii.new_image('pinceau.ppm') #initialisation de l'image qui sert de bouton pour le pinceau  
		self.pinceauApp = self.nsii.new_image('pinceauApp.ppm')   #initialisation de l'image qui sert de bouton appuyé pour le pinceau  
		self.gomme = self.nsii.new_image('gomme.ppm') #initialisation de l'image qui sert de bouton pour la gomme
		self.gommer = self.nsii.new_image('blanc.ppm')    #initialisation de l'image qui sert de gomme
		self.gommeApp = self.nsii.new_image('gomme v2.ppm')   #initialisation de l'image qui sert de bouton appuyé pour la gomme 
		self.crayon = self.nsii.new_image('crayon.ppm')   #initialisation de l'image qui sert de bouton pour le crayon
		self.crayonApp = self.nsii.new_image('crayonApp.ppm') #initialisation de l'image qui sert de bouton appuyé pour le crayon 
		self.seau = self.nsii.new_image('seau.ppm')   #initialisation de l'image qui sert de bouton pour le seau 
		self.seauApp = self.nsii.new_image('seau v2.ppm') #initialisation de l'image qui sert de bouton appuyé pour le seau  
		self.couleurs = [self.nsii.new_image('rouge.ppm'), self.nsii.new_image('vert.ppm'), self.nsii.new_image('bleu.ppm'), self.nsii.new_image('jaune.ppm'), self.nsii.new_image('noir.ppm'), self.nsii.new_image('rose.ppm'), self.nsii.new_image('orange.ppm') ]  #liste de tputes les couleurs disponibles
		self.couleurActuelle = '' #initialisation de la couleur selectionnée
		self.bleu = self.couleurs[2]  #correspondance entre self.bleu et l'image de la liste
		self.bleuApp = self.nsii.new_image('bleu v2.ppm') #initialisation de l'image qui sert de bouton appuyé bleu  
		self.rouge = self.couleurs[0] #correspondance entre self.rouge et l'image de la liste
		self.rougeApp = self.nsii.new_image('rouge v2.ppm')   #initialisation de l'image qui sert de bouton appuyé rouge 
		self.vert = self.couleurs[1]  #correspondance entre self.vert et l'image de la liste
		self.vertApp = self.nsii.new_image('vert v2.ppm') #initialisation de l'image qui sert de bouton appuyé vert 
		self.noir = self.couleurs[4]  #correspondance entre self.noir et l'image de la liste
		self.noirApp = self.nsii.new_image('noir v2.ppm') #initialisation de l'image qui sert de bouton appuyé noir 
		self.jaune = self.couleurs[3] #correspondance entre self.jaune et l'image de la liste
		self.jauneApp = self.nsii.new_image('jaune v2.ppm')   #initialisation de l'image qui sert de bouton appuyé jaune 
		self.rose = self.couleurs[5]  #correspondance entre self.rose et l'image de la liste
		self.roseApp = self.nsii.new_image('rose v2.ppm') #initialisation de l'image qui sert de bouton appuyé rose 
		self.orange = self.couleurs[6]    #correspondance entre self.orange et l'image de la liste
		self.orangeApp = self.nsii.new_image('orange v2.ppm') #initialisation de l'image qui sert de bouton appuyé orange 
		self.reset = self.nsii.new_image('reset.ppm') #initialisation de l'image reset 
		self.Paint_loop() #démarrage de la boucle 
		
	def Paint_loop(self):
		while True:
			x, y = self.nsii.m_pos   #récupère la position x et y de la souris 
			x1, y1 = self.nsii.size  #taille x et y de la fenetre 
			
			#récuperation des variables globales pour éviter un reset à 0 à chaque tour de boucle
			global pinceau
			global crayon
			global gomme
			global seau
			global vert 
			global jaune
			global bleu
			global rouge
			global noir 
			global rose
			global orange 
			
			if pinceau == 0 and crayon == 0 and seau == 0 and gomme == 0:    #si les aucun outil n'est sélectionné
				self.bg.size = self.nsii.size   #la taille du background est adapté à la taille de la fenetre 
				self.bg.show()  #affiche le background 
	
				self.pointeur.pos = x - 2, y - 2    #centre de l'image du pointeur au niveau de la souris 
				if x > 0.19*x1 and y < 0.80*y1: #si le pointeur se trouve sur la partie dessinable
					self.pointeur.show()   #affiche le pointeur
			

			self.pinceau.pos = x1 // 22 , 5  #positionnement du bouton pinceau 
			self.pinceau.size = (x1 // 12 ,x1//12)   #définition de la taille du bouton pinceau 
			if pinceau == 0 :    #si le pinceau n'est pas selectionné 
				self.pinceau.show() #image normale du pinceau affichée 
			if ((x >= x1 // 22 and x <= (x1 // 22 + x1 // 12)) and (y>=5 and y<= 5 + x1//12)) and self.nsii.key_pressed(0x01):   #si la souris se trouve sur les coordonnées du bouton et que le clic gauche est pressé
				pinceau, seau, gomme, crayon = 0, 0, 0, 0   #tout les outils sont deselectionnées 
				pinceau = 1 #pinceau est selectionné
			if pinceau == 1: #si pinceau est selectionné 
				self.pinceauApp.pos = x1 // 22 , 5  #positionnement du bouton pinceau appuyé sur bouton pinceau 
				self.pinceauApp.size = (x1 // 12 ,x1//12)   #ajustement de la taille 
				self.pinceauApp.show()  #affichage du bouton pinceau appuyé
			if pinceau == 1: 
				for i in range (len(couleur)):  #parcours de la liste des couleurs 
					if couleur[i] == self.couleurActuelle: #si la couleur correspond à la couleur actuelle 
						indice = i    #sauvegarde de l'indice de la couleur 
				self.couleurs[indice].pos = x, y    #l'image de la couleur est positionnée sur la souris 
				if x > 0.165*x1 and y < 0.82*y1:    #si la souris se trouve sur la partie dessinable 
					if self.nsii.key_pressed(0x01):    #si le clic gauche est pressé
						self.couleurs[indice].size = (3, 3)   #taille de l'image de la couleur 
						self.couleurs[indice].show()  #affichage de l'image de la couleur 


			self.crayon.pos = x1 // 22, (int(y1*0.25) + 5)   #positionnement du bouton du crayon
			self.crayon.size = (x1 // 12 ,x1//12)    #definition de la taille du bouton
			self.crayon.show()   #affiche le bouton
            #même fonctionnement que pour le pinceau, sauf la taille de l'image de la couleur, qui est de 1 par 1
			if ((x >= (x1 // 22) and x <= (x1 // 22 + x1 // 12)) and (y>= int(y1*0.25) + 5 and y<= (int(y1*0.25) + 5) + x1//12)) and self.nsii.key_pressed(0x01):
				pinceau, seau, gomme, crayon = 0, 0, 0, 0
				crayon = 1 
			if crayon == 1:
				self.crayonApp.pos = x1 // 22, (int(y1*0.25) + 5)
				self.crayonApp.size = (x1 // 12, x1//12)
				self.crayonApp.show()
			if crayon == 1:
				for i in range (len(couleur)):
					if couleur[i] == self.couleurActuelle:
						indice = i
				self.couleurs[indice].pos = x, y 
				if x > 0.165*x1 and y < 0.84*y1:
					if self.nsii.key_pressed(0x01):
						self.couleurs[indice].size = (1, 1)
						self.couleurs[indice].show()
			

			self.seau.pos = (x1 // 22) , (int(y1*0.50) + 5)  #placement du bouton du seau 
			self.seau.size = (x1 // 12 ,x1//12)  #définition de la taille du bouton
			self.seau.show() #affiche le bouton
			#même fonctionnement que pour le pinceau et le crayon sauf que le clic sur la partie dessinable colore toute cette dernière sans distinction
			if ((x >= (x1 // 22) and x<= (x1 // 22 + x1 // 12)) and (y>= int(y1*0.50) + 5 and y<= (int(y1*0.50) + 5) + x1 // 12)) and self.nsii.key_pressed(0x01):
				pinceau, seau, gomme, crayon = 0, 0, 0, 0
				seau = 1 
			if seau == 1:
				self.seauApp.pos = x1 // 22, (int(y1*0.5) + 5)
				self.seauApp.size = (x1 // 12 ,x1//12)
				self.seauApp.show()
			for i in range (len(couleur)):
					if couleur[i] == self.couleurActuelle:
						indice = i
						if x > 0.17*x1 and y < 0.85*y1:
							if self.nsii.key_pressed(0x01):
								if seau == 1: 
									self.couleurs[indice].pos = (int(0.17*x1), 0)
									self.couleurs[indice].size = (int(x1 - 0.16*x1), int(y1 - 0.15*y1))
									self.couleurs[indice].show()


			self.gomme.pos = (x1 // 22) , (int(y1*0.75) + 5) #positionnement de du bouton de la gomme
			self.gomme.size = (x1 // 12 ,x1//12) #definition de la taille du bouton
			self.gomme.show()    #affiche le bouton
			#même fonctionnement que le pinceau, sauf que la couleur est blanche pour effacer les pixels colorés 
			if ((x >= (x1 // 22) and x<= (x1 // 22 + x1 // 12)) and (y>= int(y1*0.75) + 5 and y<= (int(y1*0.75) + 5) + x1 // 12)) and self.nsii.key_pressed(0x01):
				pinceau, seau, gomme, crayon = 0, 0, 0, 0
				gomme = 1 
			if gomme == 1:
				self.gommeApp.pos = x1 // 22, (int(y1*0.75) + 5)
				self.gommeApp.size = (x1 // 12 ,x1//12)
				self.gommeApp.show()
			if gomme == 1:
				if x > 0.165*x1 and y < 0.82*y1:
					if self.nsii.key_pressed(0x01):
						self.gommer.pos = x, y 
						self.gommer.size = (3, 3)
						self.gommer.show()


			self.reset.pos = int(x1*0.2) , int(y1*0.88)  #positionnement du bouton
			self.reset.size = (x1 // 20, x1//20) #definition de la taille du bouton 
			self.reset.show()    #affiche le bouton 
			if (x >= int(x1*0.2)) and x<= (int(x1*0.2) + (x1 // 20)) and (y>= int(y1*0.88)  and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):    #si la souris se trouve sur les coordonnées du bouton et que le clic gauche est pressé 
				pinceau, seau, gomme, crayon = 0, 0, 0, 0   #tout les outils sont deselectionnés ce qui permet le reset du background 



			self.rouge.pos = int(x1*0.3) , int(y1*0.88)  #positionnement du bouton de la couleur 
			self.rouge.size = (x1 // 20 ,x1//20) #definition de la taille du bouton
			self.rouge.show()    #affichage du bouton
			if (x >= int(x1*0.3)) and x<= (int(x1*0.3) + (x1 // 20)) and (y>= int(y1*0.88)  and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):    #si le bouton se trouve sur les coordonnées du bouton et que le clic gauche est pressé
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0  #toutes les couleurs sont deselectionnées 
				rouge = 1   #la couleur rouge est selectionnée 
			if rouge == 1 :  #si rouge est selectionné 
				self.rougeApp.pos = int(x1*0.3) , int(y1*0.88)  #le bouton rouge appuyé est positionné sur le bouton rouge 
				self.rougeApp.size = (x1 // 20 ,x1//20) #ajustement de la taille
				self.rougeApp.show()    #affichage du bouton
				self.couleurActuelle = 'rouge'  #actualisation de la couleur actuelle
			
            
            #toutes les couleurs qui se trouvent après fonctionnent exactement comme la couleur rouge
			self.vert.pos = int(x1*0.4) , int(y1*0.88)
			self.vert.size = (x1 // 20 ,x1//20)
			self.vert.show()
			if (x >= int(x1*0.4)) and x<= (int(x1*0.4) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0
				vert = 1
			if vert == 1 :
				self.vertApp.pos = int(x1*0.4) , int(y1*0.88)
				self.vertApp.size = (x1 // 20 ,x1//20)
				self.vertApp.show()
				self.couleurActuelle = 'vert'

			self.bleu.pos = int(x1*0.5) , int(y1*0.88)
			self.bleu.size = (x1 // 20 ,x1//20)
			self.bleu.show()
			if (x >= int(x1*0.5)) and x<= (int(x1*0.5) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0
				bleu = 1
			if bleu == 1 :
				self.bleuApp.pos = int(x1*0.5) , int(y1*0.88)
				self.bleuApp.size = (x1 // 20 ,x1//20)
				self.bleuApp.show()
				self.couleurActuelle = 'bleu'
			

			self.jaune.pos = int(x1*0.6) , int(y1*0.88)
			self.jaune.size = (x1 // 20 ,x1//20)
			self.jaune.show()
			if (x >= int(x1*0.6)) and x<= (int(x1*0.6) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0
				jaune = 1
			if jaune == 1 :
				self.jauneApp.pos = int(x1*0.6) , int(y1*0.88)
				self.jauneApp.size = (x1 // 20 ,x1//20)
				self.jauneApp.show()
				self.couleurActuelle = 'jaune'
	

			self.orange.pos = int(x1*0.7) , int(y1*0.88)
			self.orange.size = (x1 // 20 ,x1//20)
			self.orange.show()
			if (x >= int(x1*0.7)) and x<= (int(x1*0.7) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0 
				orange = 1
			if orange == 1 :
				self.orangeApp.pos = int(x1*0.7) , int(y1*0.88)
				self.orangeApp.size = (x1 // 20 ,x1//20)
				self.orangeApp.show()
				self.couleurActuelle = 'orange'


			self.rose.pos = int(x1*0.8) , int(y1*0.88)
			self.rose.size = (x1 // 20 ,x1//20)
			self.rose.show()
			if (x >= int(x1*0.8)) and x<= (int(x1*0.8) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0
				rose = 1
			if rose == 1 :
				self.roseApp.pos = int(x1*0.8) , int(y1*0.88)
				self.roseApp.size = (x1 // 20 ,x1//20)
				self.roseApp.show()
				self.couleurActuelle = 'rose'
				

			self.noir.pos = int(x1*0.9) , int(y1*0.88)
			self.noir.size = (x1 // 20 ,x1//20)
			self.noir.show()
			if (x >= int(x1*0.9)) and x<= (int(x1*0.9) + (x1 // 20)) and (y>= int(y1*0.88) and y<= int(y1*0.88) + (x1//20)) and self.nsii.key_pressed(0x01):
				bleu, vert, rouge, jaune, noir, rose, orange = 0, 0, 0, 0, 0, 0, 0
				noir = 1
			if noir == 1 :
				self.noirApp.pos = int(x1*0.9) , int(y1*0.88)
				self.noirApp.size = (x1 // 20 ,x1//20)
				self.noirApp.show()
				self.couleurActuelle = 'noir'
			
			self.nsii.draw()    #commande qui permet d'afficher tout ce qui est show()




paint = Paint() #lance la classe paint

