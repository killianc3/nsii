import ctypes
import sys
import os

from ctypes import POINTER, WinDLL, Structure, sizeof, c_long, pointer
from ctypes.wintypes import BOOL, SHORT, WCHAR, UINT, ULONG, DWORD, HANDLE, RECT

class Terminal:

	def __init__(self):

		self.kernel32 = ctypes.windll.kernel32
		self.user32 = ctypes.windll.user32
		self.dwmapi = ctypes.WinDLL("dwmapi")

		self.hWnd = self.kernel32.GetConsoleWindow()

		self.kernel32.SetConsoleMode(self.kernel32.GetStdHandle(-11), 7)
		#self.kernel32.SetConsoleMode(self.kernel32.GetStdHandle(-10), 128)

		#self._rx = self.size[0] / (self.outter_size[0] - 28)
		#self._ry = self.size[1] / (self.outter_size[1] - 28)


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
	def client_size(self):
		rect = RECT()
		self.user32.GetClientRect(self.hWnd, pointer(rect))
		return (rect.right - rect.left, rect.bottom - rect.top)

	@client_size.setter
	def client_size(self, new_size):
		width, height = new_size[0] + 32, new_size[1] + 38
		self.user32.MoveWindow(self.hWnd, *self.pos, width, height, True)


	@property
	def pos(self):
		rect = RECT()
		#self.dwmapi.DwmGetWindowAttribute(self.hWnd, DWORD(9), pointer(rect), sizeof(rect))
		self.user32.GetWindowRect(self.hWnd, pointer(rect))
		return (rect.left, rect.top)
	
	@pos.setter
	def pos(self, new_pos):
		rect = RECT()
		self.user32.GetWindowRect(self.hWnd, pointer(rect))
		self.user32.MoveWindow(self.hWnd, *new_pos, rect.right - rect.left, rect.bottom - rect.top, True)


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


	@property
	def m_pos_client(self):
		pt = POINT()
		self.user32.GetCursorPos(pointer(pt))
		self.user32.ScreenToClient(self.hWnd, pointer(pt))
		return (pt.x, pt.y)

	@m_pos_client.setter
	def m_pos_client(self, new_pos):
		self.user32.SetCursorPos(*new_pos)


	@property
	def m_pos(self):
		px, py = round(self.m_pos_client[0]/self.client_size[0]*self.size[0]), round(self.m_pos_client[1]/self.client_size[1]*self.size[1])
		if px < 0: px = 0
		elif px > self.size[0]: px = self.size[0]
		if py < 0: py = 0
		elif py > self.size[1]: py = self.size[1]
		return (px, min(self.size[1], py))
	

class POINT(Structure):
    _fields_ = [("x", c_long), ("y", c_long)]
	

class COORD(Structure):
    _fields_ = [("X", SHORT), ("Y", SHORT),]


class CONSOLE_FONT_INFOEX(Structure):
    _fields_ = [
        ("cbSize", ULONG),
        ("nFont", DWORD),
        ("dwFontSize", COORD),
        ("FontFamily", UINT),
        ("FontWeight", UINT),
        ("FaceName", WCHAR * 32)
    ]