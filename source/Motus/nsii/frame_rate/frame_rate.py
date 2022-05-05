import time

class Frame_rate:

	def __init__(self, window, time_sample):

		self.time_sample = time_sample
		self.start_time = time.perf_counter()
		self.elapsed_time = 0
		self.frame_counter = 0

		self.last_frame = time.perf_counter()
		self.offset = 0.00001

		self.target_fps = window.target_fps
		self.time_per_frame = 1 / self.target_fps

		self.cmd_title = window.config.cmd_title

	def update_and_wait(self):

		now = time.perf_counter()

		self.elapsed_time = now - self.start_time
		self.frame_counter += 1

		if self.elapsed_time > self.time_sample:

			frame_rate = self.frame_counter / self.elapsed_time
			self.cmd_title(f'{frame_rate:.2f} fps')

			self.start_time = time.perf_counter()
			self.frame_counter = 0

		next_frame = self.last_frame + self.time_per_frame

		while time.perf_counter() < next_frame - self.offset:
			pass

		self.last_frame = time.perf_counter()