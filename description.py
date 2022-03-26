import nsii        # pour importer 
nsii = nsii.Nsii() # le module

# paramètres (renvoie la valeur et peut etre modifié)

nsii.name         # str()
nsii.fps_target   # int() ou 'max'
nsii.size         # tuple(int(), int())
nsii.pos          # tuple(int(), int())
nsii.fps          # float()

nsii.mouse_pos    # en développement
nsii.keyboard     # en développement

nsii.outter_size  # tuple(int(), int()) (pas vraiment utile)
nsii.font         # tuple(str(), int()) (pas touche)

# fonctions

nsii.new_image('fichier.ppm')  # renvoie une classe image
nsii.new_window()              # renvoie une classe window
nsii.draw()                    # affiche tout à l'écran

# class image

exemple = nsii.new_image('fichier.ppm')

# paramètres

exemple.pos 
exemple.size

# fonction

exemple.show()

# class window

exemple2 = nsii.new_window()

# paramètres

exemple2.pos
exemple2.size

# fonctions

exemple2.dot(x, y, caractere)
exemple2.line(x0, y0, x1, y1, caractere)
exemple2.circle(x, y, radius, caractere)
exemple2.rect(x, y, width, height, caractere)