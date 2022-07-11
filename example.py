import nsii

nsii = nsii.Nsii()       # nsii class initialization

nsii.fps_target = 'max'  # set frame rate target
nsii.p_size = 8          # set pixel size

background = nsii.new_image('image.ppm')  # initializing a new image

while True:

	background.size = nsii.size  # set background size to window size
	background.show()            # show the background

	ox, oy = nsii.m_pos
	while nsii.m_click('left'):  # while the left mouse button is pressed

		x, y = nsii.m_pos  # get mouse coordinates 
		background.show()  # show the background

		if x < ox and y < oy:
			nsii.rect(x, y, ox-x, oy-y)  # draw a rectangle

		elif x < ox:
			nsii.rect(x, oy, ox-x, y-oy)  # draw a rectangle

		elif y < oy:
			nsii.rect(ox, y, x-ox, oy-y)  # draw a rectangle

		else:
			nsii.rect(ox, oy, x-ox, y-oy)  # draw a rectangle

		# display information
		nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

		nsii.draw()  # draw a new frame

	# display information
	nsii.name = f'framerate : {nsii.fps:.1f} size : {nsii.size} client_size : {nsii.client_size} win_pos : {nsii.pos} m_pos : {nsii.m_pos}'

	nsii.draw()  # draw a new frame