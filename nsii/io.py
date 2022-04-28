import sys
import msvcrt

class Io:

	def __init__(self):
		pass


	def input(self, draw, print, pos):

		while msvcrt.kbhit():
			msvcrt.getch()

		cursor = 0
		word = []
		user_input = '%c' % msvcrt.getwch()

		while user_input != '\r':

			if user_input == '':

				if len(word) > 0:

					cursor -= 1
					print((pos[0] + cursor, pos[1]), ' ')
					word.pop()

			else:

				print((pos[0] + cursor, pos[1]), user_input)
				cursor += 1
				word.append(user_input)

			draw()
			user_input = '%c' % msvcrt.getwch()

		return ''.join(word)


	def print(self, buffer, state, pos, word, f_col=(255, 255, 255), b_col=(0, 0, 0)):

		buffer[pos[1]][pos[0]] = '\x1b[48;2;%d;%d;%dm\x1b[38;2;%d;%d;%dm%s' % (*b_col, *f_col, word[0])
		state[pos[1]][pos[0]] = True

		for cursor in range(1, len(word)):

			buffer[pos[1]][pos[0] + cursor] = word[cursor]
			state[pos[1]][pos[0] + cursor] = True