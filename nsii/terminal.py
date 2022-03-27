import ctypes
import sys
import os

from ctypes import POINTER, WinDLL, Structure, sizeof, c_long, pointer
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE, RECT

class Terminal:

	def __init__(self):

		self.kernel32 = ctypes.windll.kernel32
		self.user32 = ctypes.windll.user32

		self.hWnd = self.kernel32.GetConsoleWindow()

		self.kernel32.SetConsoleMode(self.kernel32.GetStdHandle(-11), 7)
		#self.kernel32.SetConsoleMode(self.kernel32.GetStdHandle(-10), 128)

		self.__hide_cursor()

	@property
	def name(self):
		length = self.user32.GetWindowTextLengthW(self.hWnd) + 1
		title = ctypes.create_unicode_buffer(length)
		self.user32.GetWindowTextW(self.hWnd, title, length)
		return title.value

	@name.setter
	def name(self, new_name):
		sys.stdout.write(f'\33]0;{new_name}\a')
		sys.stdout.flush()


	@property
	def size(self):
		return (os.get_terminal_size()[0], os.get_terminal_size()[1])

	@size.setter
	def size(self, new_size):
		os.system('mode con: cols={} lines={}'.format(*new_size))


	@property
	def outter_size(self):
		rect = wintypes.RECT()
		self.user32.GetWindowRect(self.hWnd, ctypes.pointer(rect))
		return (rect.right - rect.left, rect.bottom - rect.top)

	@outter_size.setter
	def outter_size(self, new_size):
		self.user32.MoveWindow(self.hWnd, *self.pos, *new_size, True)


	@property
	def pos(self):
		rect = wintypes.RECT()
		self.user32.GetWindowRect(self.hWnd, ctypes.pointer(rect))
		return (rect.left, rect.top)
	
	@pos.setter
	def pos(self, new_pos):
		self.user32.MoveWindow(self.hWnd, *new_pos, *self.outter_size, True)


	@property
	def font(self):
		font = CONSOLE_FONT_INFOEX()
		font.cbSize = sizeof(CONSOLE_FONT_INFOEX)
		self.kernel32.GetCurrentConsoleFontEx(self.kernel32.GetStdHandle(-11), c_long(False), pointer(font))
		return font

	@font.setter
	def font(self, new_font):
		font = self.font
		font.FaceName = new_font[0]
		font.dwFontSize.Y = new_font[1]
		font.FontFamily = 0
		self.kernel32.SetCurrentConsoleFontEx(self.kernel32.GetStdHandle(-11), c_long(False), pointer(font))


	@staticmethod
	def __hide_cursor():
		sys.stdout.write('\x1b[?25l')
		sys.stdout.flush()


class COORD(Structure):
    _fields_ = [
        ("X", SHORT),
        ("Y", SHORT),
    ]


class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [
        ("cbSize", ULONG),
        ("nFont", DWORD),
        ("dwFontSize", COORD),
        ("FontFamily", UINT),
        ("FontWeight", UINT),
        ("FaceName", WCHAR * 32)
    ]