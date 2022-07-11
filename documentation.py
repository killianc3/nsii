# initialization
import nsii
nsii = nsii.Nsii()

# retrieve values of a parameter
values = nsii.parameter

# set values of a parameter
nsii.parameter = values

# available parameters
nsii.name         # window name  ->  str
nsii.size         # window size  ->  (int, int)
nsii.pos          # window position  ->  (int, int)

nsii.fps          # frame rate  ->  float
nsii.fps_target   # frame rate target  ->  int or 'max'

nsii.m_pos        # mouse coordinates  ->  (int, int)
nsii.p_size       # pixel size  -> int

# available functions
nsii.draw()  # displays all changes

nsii.m_click('left')   # mouse button status  ->  bool
nsii.m_click('right')

nsii.input((x, y))        # retrieve user input  ->  str
nsii.print((x, y), text)  # same as print()

nsii.key_pressed(key)  # retrieve the status of the given key code  ->  bool
					   # for key code see https://docs.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes

nsii.dot(x, y)                  # draw dot
nsii.line(x0, y0, x1, y1)       # draw line
nsii.circle(x, y, radius)       # draw circle
nsii.rect(x, y, width, height)  # drax rectangle

# note that you can use a custom color by entering these parameters
f_col=(r, g, b)  # front color
b_col=(r, g, b)  # back color

# image initialisation
image = nsii.new_image('example.ppm')

# available parameter
image.size  # image size  ->  (int, int)
image.pos   # image position  ->  (int, int)

# available functions
image.show()  # displays the image

# note that you can hide a specific color by entering this parameter.
hide=(255, 255, 255)