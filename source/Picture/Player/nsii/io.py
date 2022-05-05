import sys
import msvcrt

def input(draw, coord):

	while msvcrt.kbhit():
		msvcrt.getch()

	sys.stdout.write(f'\x1b[{coord[1]//2+1};{coord[0]+1}H\x1b[48;2;0;0;0m\x1b[38;2;255;255;255m')
	sys.stdout.flush()

	user_input = sys.stdin.readline()
	draw(force=True)

	return user_input


def key_pressed(user32, key):
	return user32.GetKeyState(key) & 0x8000