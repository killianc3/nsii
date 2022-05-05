import nsii
from dico import Dico

import sys
import os
import pathlib

def main():

	script_location = pathlib.Path(__file__).absolute().parent

	lenght = 6
	indice = lenght - 6

	logo_file = open(script_location / 'logo.txt', 'r', encoding='utf-8')
	logo_content = logo_file.read()
	logo = list(logo_content.split('\n'))

	rectangle = ['█'*len(logo[0]) for a in range(len(logo))]

	lose_file = open(script_location / 'lose.txt', 'r', encoding='utf-8')
	lose_content = lose_file.read()
	lose = list(lose_content.split('\n'))

	win_file = open(script_location / 'win.txt', 'r', encoding='utf-8')
	win_content = win_file.read()
	win = list(win_content.split('\n'))

	grid_file = open(script_location / 'grid.txt', 'r', encoding='utf-8')
	grid_content = grid_file.read()
	grid_list = list(model.split('\n') for model in grid_content.split('<next>\n'))
	grid = list(grid_list[indice])

	header_file = open(script_location / 'header.txt', 'r', encoding='utf-8')
	header_content = header_file.read()
	header = list(header_content.split('\n'))

	widht = len(grid[0]) + len(header[0])
	height = len(grid)

	window = nsii.Window(widht, height, rgb_mode=True)

	reference = {' ':((0, 0, 0), (0, 0, 0)), '█':((80, 80, 80), (0, 0, 0))}
	grif_frame = window.layer.new_layer(0, 0, grid, grid, reference, True, ban_car='#')
	header_frame = window.layer.new_layer(len(grid[0]), 0, header, f_color=(220, 220, 220))

	lose_frame = window.layer.new_layer(widht//2 - len(lose[0])//2, height//2 - len(lose)//2, lose)
	win_frame = window.layer.new_layer(widht//2 - len(win[0])//2, height//2 - len(win)//2, win)

	logo_reference = {'X':((180, 0, 0), (0, 0, 0)), ':':((200, 200, 0), (0, 0, 0)), '!':((200, 140, 0), (0, 0, 0)), '/':((220, 220, 220), (0, 0, 0)), ' ':((40, 40, 180), (0, 0, 255))}
	logo_frame = window.layer.new_layer(0, len(grid), rectangle, logo, logo_reference, True, ban_car='9')

	dico = Dico(script_location)

	alpha_coord = get_alpha_coord(widht)

	while True:

		window.back_ground()
		grif_frame.show()
		header_frame.show()
		logo_frame.show()

		word = dico.random_word(lenght)
		current = list(word[0]) + list(' '*(len(word)-1))

		result = game_loop(window, widht, height, lenght, word, dico, alpha_coord, current)

		if result:

			window.back_ground()
			win_frame.show()
			window.text.write(widht//2 - (6*lenght)//2, height//2, word)

		else:

			window.back_ground()
			lose_frame.show()
			window.text.write(widht//2 - (6*lenght)//2, height//2, word)

		if window.cmd_input.wait_for_car() == 'escape':
			break

def game_loop(window, widht, height, lenght, word, dico, alpha_coord, current):

	max_tries = 6
	tries = 0

	while tries < max_tries:

		show_current(window, tries, current)
		show_score(window, lenght, max_tries - tries)

		attempt = get_word(window, lenght, tries)

		if attempt == word:

			return True

		elif dico.in_dico(attempt) and len(attempt) == lenght:

			current = checker(window, word, attempt, tries, alpha_coord, current)

		else:

			highlight(window, attempt, tries)

		tries += 1

	return False

def show_current(window, tries, current):

	for cursor in range(len(current)):

		if current[cursor] != ' ':

			window.text.write(cursor*7 +1, tries*7 +1, current[cursor], force_color=((0, 190, 0), (0, 0, 0)))

def highlight(window, attempt, tries):

	for cursor in range(len(attempt)):

		window.text.write(cursor*7 +1, tries*7 +1, attempt[cursor], force_color=((190, 0, 0), (0, 0, 0)))		


def checker(window, word, attempt, tries, alpha_coord, current):

	letter = list(word)

	for cursor in range(len(word)):

		if attempt[cursor] == word[cursor] and attempt[cursor] in letter:

			window.text.write(cursor*7 +1, tries*7 +1, attempt[cursor], force_color=((0, 210, 0), (0, 0, 0)))
			letter.remove(attempt[cursor])

			current[cursor] = attempt[cursor]

		elif attempt[cursor] in letter:

			window.text.write(cursor*7 +1, tries*7 +1, attempt[cursor], force_color=((210, 210, 0), (0, 0, 0)))
			letter.remove(attempt[cursor])

		else:

			window.text.write(cursor*7 +1, tries*7 +1, attempt[cursor], force_color=((190, 190, 190), (0, 0, 0)))

			x, y = alpha_coord[ord(attempt[cursor]) - 97]
			window.basics.dot(x, y, ' ')

	return current

def show_score(window, lenght, score):

	window.text.write(window.widht - 14, 30, ' ')
	window.text.write(window.widht - 14, 30, str(score), force_color=((210, 210, 210), (0, 0, 0)))


def get_word(window, lenght, tries):

	user_input = ''
	word = ''

	while user_input != 'enter':

		user_input = window.cmd_input.wait_for_car()

		if user_input.isalpha():

			if user_input == 'suppr':

				window.text.write((len(word)-1)*7 +1, tries*7 +1, ' ')
				word = word[:-1]

			elif len(user_input) == 1 and len(word) < lenght:

				window.text.write(len(word)*7 +1, tries*7 +1, ' ')
				window.text.write(len(word)*7 +1, tries*7 +1, user_input)

				word += user_input

	return word

def get_alpha_coord(widht):

	alpha_coord = []

	for y in range(4):
		for x in range(7):

			alpha_coord.append((x*3 + widht - 22, y*2 + 9))

	del alpha_coord[-1]
	del alpha_coord[-6]

	return alpha_coord

if __name__=='__main__':
	main()