# -------------- Initialisation -------------- #

import nsii        # Importe le module

nsii = nsii.Nsii() # Obligatoire au début d'un programme

# -------------- Initialisation -------------- #

# 1) Récupérer les valeurs du paramètre
variable = nsii.parametre


# 2) Saisir les valeurs du paramètre
nsii.parametre = variable


# 3) Les paramètres disponibles

nsii.name         # Nom de la fenêtre  -> str()

nsii.fps_target   # Cible du taux de rafraichissement  -> int() or 'max'

nsii.size         # Taille de la fenêtre en nombre de caractère  -> (int(), int())

nsii.pos          # Position de la fenêtre en pixel, et sur le bureau  -> (int(), int())

nsii.fps          # Taux de rafraîchissement  -> float()

nsii.m_pos        # Position la souris en nombre de caractère  -> (int(), int())

nsii.p_size       # Taille des pixels, spoiler ça affecte les performances  -> int()

# 4) Les fonctions disponibles

nsii.draw()  # Affiche le contenu du buffer à l'écran

nsii.m_click('left')   # Renvoie True si un bouton de la souris est pressé  -> bool()
nsii.m_click('right')

nsii.input((x, y))          # Même comportement que 'input()', mais nécessite une position dans la fenêtre  -> str()
nsii.print((x, y), max_len) # Même comportement que 'print()', mais nécessite une position dans la fenêtre 
							# possibilité de changer la couleur du texte avec f_col=(r,g,b), b_col=(r,g,b))

nsii.key_pressed(key)  # Renvoie True si la touche est pressé  -> bool()
					   # La liste des touches est disponible ici : https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes
					   # 'key' correspond à la colonne 'value' du site

nsii.dot(x, y)                  # Affiche le caractère aux coordonnées x, y
nsii.line(x0, y0, x1, y1)       # Affiche une ligne
nsii.circle(x, y, radius)       # Affiche un cercle
nsii.rect(x, y, width, height)  # Affiche un rectangle

# Pour ces 4 fonctions, il est possible de définir la couleur des caractères
# en ajoutant l'argument -> f_col=(r, g, b), avec une valeur rgb valide

nsii.dot(0, 0, f_col=(255, 0, 0))

# ---------------- Class image --------------- #

# 1) Initialisation

variable_image = nsii.new_image('exemple_fichier.ppm')

# 2) Paramètres

variable_image.size  # Taille de l'image en nombre de caractère  -> (int(), int())

variable_image.pos  # Position de l'image en nombre de caractère  -> (int(), int())

# 3) Fonctions

variable_image.show()  # Ajoute l'image dans le buffer (nsii.draw() pour l'afficher)

# Pour la fonction show() il y a possibilité de saisir une couleur qui ne sera pas
# afficher avec : hide=(r, g, b), utile pour des images qui nécessitent de la transparence

exemple.show(hide=(255, 255, 255))

# ---------------- Class image --------------- #