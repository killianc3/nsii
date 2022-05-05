import time

class Fps_handler:

	def __init__(self):

		self.last_frame = time.perf_counter()
		self.last_period = time.perf_counter()

		self.time_per_frame = None
		self.fps_target = 60
		self.counter = 1


	@property
	def fps(self):
		fps = self.counter / (time.perf_counter() - self.last_period)
		self.counter = 0
		self.last_period = time.perf_counter()
		return fps


	@property
	def fps_target(self):
		return self._fps_target
	
	@fps_target.setter
	def fps_target(self, new_target):
		if new_target == 'max':
			self.time_per_frame = 0
		else:
			self.time_per_frame = 1 / new_target
		self._fps_target = new_target


	def update(self):

		next_frame = self.last_frame + self.time_per_frame

		while time.perf_counter() <= next_frame:
			pass

		self.last_frame = time.perf_counter()
		self.counter += 1