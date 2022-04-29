import sys
import msvcrt


def input(draw, print, pos, max_len=60, f_col=(255, 255, 255), b_col=(0, 0, 0)):

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

			if len(word) <= max_len:

				print((pos[0] + cursor, pos[1]), user_input, f_col=f_col, b_col=b_col)
				cursor += 1
				word.append(user_input)

		draw()
		user_input = '%c' % msvcrt.getwch()

	return ''.join(word)


def print(buffer, state, pos, word, f_col=(255, 255, 255), b_col=(0, 0, 0)):

	if pos[1] % 2 != 0:
		pos = (pos[0], pos[1] - 1)

	buffer[pos[1]][pos[0]] = '\x1b[48;2;%d;%d;%dm\x1b[38;2;%d;%d;%dm%s' % (*b_col, *f_col, word[0])
	state[pos[1]][pos[0]] = True

	for cursor in range(1, len(word)):

		buffer[pos[1]][pos[0] + cursor] = word[cursor]
		state[pos[1]][pos[0] + cursor] = True