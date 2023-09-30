# -*- coding: utf-8 -*-
# RemapApplicationsKey add-on: Key presses functions
# Copyright (C) 2021 Héctor J. Benítez Corredera <xebolax@gmail.com>
# Copyright (C) 2023 Rui Fontes <rui.fontes@tiflotecnia.com>
# This file is covered by the GNU General Public License.
#
# Code get from:
# https://stackoverflow.com/questions/13564851/how-to-generate-keyboard-events (answer 1)
#
# Microsoft keyboard codes.
# https://docs.microsoft.com/en/windows/win32/inputdev/virtual-key-codes?redirectedfrom=MSDN

# Import necessary modules
import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

INPUT_MOUSE    = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2

KEYEVENTF_EXTENDEDKEY = 0x0001
KEYEVENTF_KEYUP       = 0x0002
KEYEVENTF_UNICODE     = 0x0004
KEYEVENTF_SCANCODE    = 0x0008

MAPVK_VK_TO_VSC = 0

# msdn.microsoft.com/en-us/library/dd375731
VK_LBUTTON = 0x01 # Mouse left button
VK_RBUTTON = 0x02 # Mouse right button
VK_APPS = 0x5D # Applications key (Natural keyboard)
VK_SHIFT = 0x10 # Shift key

# C struct definitions

wintypes.ULONG_PTR = wintypes.WPARAM

class MOUSEINPUT(ctypes.Structure):
	_fields_ = (("dx",          wintypes.LONG),
		("dy",          wintypes.LONG),
		("mouseData",   wintypes.DWORD),
		("dwFlags",     wintypes.DWORD),
		("time",        wintypes.DWORD),
		("dwExtraInfo", wintypes.ULONG_PTR)
	)

class KEYBDINPUT(ctypes.Structure):
	_fields_ = (("wVk",         wintypes.WORD),
		("wScan",       wintypes.WORD),
		("dwFlags",     wintypes.DWORD),
		("time",        wintypes.DWORD),
		("dwExtraInfo", wintypes.ULONG_PTR)
	)

	def __init__(self, *args, **kwds):
		super(KEYBDINPUT, self).__init__(*args, **kwds)
		# some programs use the scan code even if KEYEVENTF_SCANCODE
		# isn't set in dwFflags, so attempt to map the correct code.
		if not self.dwFlags & KEYEVENTF_UNICODE:
			self.wScan = user32.MapVirtualKeyExW(self.wVk,
				MAPVK_VK_TO_VSC, 0)

class HARDWAREINPUT(ctypes.Structure):
	_fields_ = (("uMsg",    wintypes.DWORD),
		("wParamL", wintypes.WORD),
		("wParamH", wintypes.WORD)
	)

class INPUT(ctypes.Structure):
	class _INPUT(ctypes.Union):
		_fields_ = (("ki", KEYBDINPUT),
			("mi", MOUSEINPUT),
			("hi", HARDWAREINPUT)
		)
	_anonymous_ = ("_input",)
	_fields_ = (("type",   wintypes.DWORD),
		("_input", _INPUT)
	)

LPINPUT = ctypes.POINTER(INPUT)

def _check_count(result, func, args):
	if result == 0:
		raise ctypes.WinError(ctypes.get_last_error())
	return args

user32.SendInput.errcheck = _check_count
user32.SendInput.argtypes = (wintypes.UINT, # nInputs
	LPINPUT,       # pInputs
	ctypes.c_int)  # cbSize

# Functions

def PressKey(hexKeyCode):
	x = INPUT(type=INPUT_KEYBOARD,
		ki=KEYBDINPUT(wVk=hexKeyCode)
	)
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
	x = INPUT(type=INPUT_KEYBOARD,
		ki=KEYBDINPUT(wVk=hexKeyCode,
		dwFlags=KEYEVENTF_KEYUP)
	)
	user32.SendInput(1, ctypes.byref(x), ctypes.sizeof(x))

def key_aplicacion():
	PressKey(VK_APPS)
	ReleaseKey(VK_APPS)

def key_shift_aplicacion():
	PressKey(VK_SHIFT)
	PressKey(VK_APPS)
	ReleaseKey(VK_APPS)
	ReleaseKey(VK_SHIFT)
