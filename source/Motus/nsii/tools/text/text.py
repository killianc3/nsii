from .model import alpha, numeric, specific

class Text:

	def __init__(self, window):

		self.new_layer = window.layer.new_layer
		self.draw = window.draw

		self.layer_alpha = [self.new_layer(0, 0, letter, color_mode=False) for letter in alpha]
		self.layer_numeric = [self.new_layer(0, 0, number, color_mode=False) for number in numeric]
		self.layer_specific = [self.new_layer(0, 0, car, color_mode=False, ban_car='x') for car in specific]

	def write(self, x=0, y=0, word='', inter_line=1, draw=True, force_color=None):

		cursor = x
		
		for car in word:

			if car.isalpha():

				current_layer = self.layer_alpha[ord(car.lower()) - 97]

				current_layer.change_pos(cursor, y)
				current_layer.show(draw=False, force_color=force_color)
				cursor += current_layer.widht + inter_line

			elif car.isnumeric():

				current_layer = self.layer_numeric[ord(car.lower()) - 49]

				current_layer.change_pos(cursor, y)
				current_layer.show(draw=False, force_color=force_color)
				cursor += current_layer.widht + inter_line

			elif car == ' ':

				current_layer = self.layer_specific[0]

				current_layer.change_pos(cursor, y)
				current_layer.show(draw=False, force_color=force_color)
				cursor += current_layer.widht + inter_line

			else:

				cursor += 6

		if draw:
			self.draw()