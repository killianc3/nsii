import msvcrt

class Cmd_input:

	def __init__(self):
		pass

	def wait_for_car(self):

		code = ord(msvcrt.getch())

		if code == 3:
			raise KeyboardInterrupt

		elif code == 224:

			second = ord(msvcrt.getch())

			if second == 72:
				return 'upp'

			elif second == 75:
				return 'left'

			elif second == 77:
				return 'right'

			elif second == 80:
				return 'down'

			elif second == 83:
				return 'del'

			else:
				return chr(second)

		elif code == 13:
			return 'enter'

		elif code == 8:
			return 'suppr'

		elif code == 32:
			return 'space'

		elif code == 27:
			return 'escape'

		elif code == 9:
			return 'tab'

		else:
			return chr(code)

	def wait_for_word(self, raw=False):

		word = ''
		car = self.wait_for_car()

		while car != 'enter':

			if raw:
				word += car

			else:

				if len(car) == 1:
					word += car

			car = self.wait_for_car()

		return word