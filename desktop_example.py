import nsii

nsii = nsii.Nsii()

nsii.fps_target = 'max'
nsii.font = ('Terminal', 6)

background = nsii.new_image('image/win11.ppm')

icon = nsii.new_image('image/winxp.ppm')
icon.size = (16, 16)

while True:

	nsii.name = f'size : {nsii.size} fps : {nsii.fps:.2f}'

	background.size = nsii.size

	icon.pos = (round(0.25*nsii.size[0]), round(0.5*nsii.size[1]))

	background.show()
	icon.show()

	nsii.draw()