import pyautogui
import time
import random

class Hubstaff:

	def __init__(self):
		print("Initializing Hubstaff...")
		self.CHANGE_WINDOW_TIME=15
		self.CHANGE_BROWSER_TIME=10
		self.MOVE_MOUSE_TIME=5
		self.SCROLL_MOUSE_TIME=10
		self.MOUSE_LIMIT=400
		self.SCROLL_CLICK=5
		self.controller()

	def change_browser(self):
		with pyautogui.hold('ctrl'):
			pyautogui.press('pgup')

	def change_window(self):
		with pyautogui.hold('alt'):
			pyautogui.press('tab')

	def mouse_move(self):
		mouse_movement_type = random.randint(0, 3)
		if mouse_movement_type == 0:
			pos_x = random.randint(0, self.MOUSE_LIMIT)
			pos_y = 0
			curr_x,curr_y = pyautogui.position()
			if pyautogui.onScreen(curr_x+pos_x,curr_y+pos_y)==False:
				pos_x = random.randint(-self.MOUSE_LIMIT, 0)
				pos_y = 0
			pyautogui.moveTo(curr_x+pos_x,curr_y+pos_y)
			pyautogui.click()
		elif mouse_movement_type == 1:
			pos_x = random.randint(-self.MOUSE_LIMIT, 0)
			pos_y = 0
			curr_x,curr_y = pyautogui.position()
			if pyautogui.onScreen(curr_x+pos_x,curr_y+pos_y)==False:
				pos_x = random.randint(0, self.MOUSE_LIMIT)
				pos_y = 0
			pyautogui.moveTo(curr_x+pos_x,curr_y+pos_y,2,pyautogui.easeInBounce)
			pyautogui.click()
		elif mouse_movement_type == 2:
			pos_x = 0
			pos_y = random.randint(0, self.MOUSE_LIMIT)
			curr_x,curr_y = pyautogui.position()
			if pyautogui.onScreen(curr_x+pos_x,curr_y+pos_y)==False:
				pos_x = 0
				pos_y = random.randint(-self.MOUSE_LIMIT, 0)
			pyautogui.moveTo(curr_x+pos_x,curr_y+pos_y)
			pyautogui.click()
		else:
			pos_x = 0
			pos_y = random.randint(-self.MOUSE_LIMIT, 0)
			curr_x,curr_y = pyautogui.position()
			if pyautogui.onScreen(curr_x+pos_x,curr_y+pos_y)==False:
				pos_x = 0
				pos_y = random.randint(0, self.MOUSE_LIMIT)
			pyautogui.moveTo(curr_x+pos_x,curr_y+pos_y,2,pyautogui.easeInBounce)
			pyautogui.click()

	def mouse_scroll(self):
		pyautogui.scroll(self.SCROLL_CLICK)

	def controller(self):
		while(True):
			actionType = random.randint(0, 3)
			if actionType == 0:
				self.change_window()
				time.sleep(self.CHANGE_WINDOW_TIME)
			elif actionType == 1:
				self.change_browser()
				time.sleep(self.CHANGE_BROWSER_TIME)
			elif actionType == 2:
				self.mouse_move()
				time.sleep(self.MOVE_MOUSE_TIME)
			else:
				self.mouse_scroll()
				time.sleep(self.SCROLL_MOUSE_TIME)


def __main__():
	print("Initializing Dependencies...")
	hubstaffInstance = Hubstaff()

if __name__=="__main__":
	__main__()