from ctypes import windll, byref, wintypes, Structure, c_short, c_ulong, c_uint, c_wchar, sizeof, pointer, c_long
from ctypes.wintypes import SMALL_RECT, _COORD
import sys

import os
import io


class COORD(Structure):
    _fields_ = [("X", c_short), ("Y", c_short)]


class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [("cbSize", c_ulong),
                ("nFont", c_ulong),
                ("dwFontSize", COORD),
                ("FontFamily", c_uint),
                ("FontWeight", c_uint),
                ("FaceName", c_wchar * 32)]

class Config:

	def __init__(self):
		pass

	def cmd_config(self, widht, height):

		sys.stdout.reconfigure(line_buffering=True)

		kernel32 = windll.kernel32
		handle = kernel32.GetStdHandle(-11)

		font = CONSOLE_FONT_INFOEX()
		font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
		font.nFont = 0
		font.dwFontSize.X = 8
		font.dwFontSize.Y = 8
		font.FontFamily = 0
		font.FontWeight = 0
		font.FaceName = "Terminal"	

		kernel32.SetConsoleMode(handle, 7)
		kernel32.SetCurrentConsoleFontEx(handle, c_long(False), pointer(font))

		os.system(f'mode con: cols={widht} lines={height}')

		sys.stdout.write('\x1b[?25l\x1b[2J')
		sys.stdout.flush()

	def cmd_title(self, title):

		sys.stdout.write(f'\33]0;{title}\a')
		sys.stdout.flush()