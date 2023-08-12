import time, pyautogui, win32api, win32con, keyboard

pyautogui.FAILSAFE = True

def main():
    time.sleep(5)
    while keyboard.is_pressed('s') == False:
        if pyautogui.pixelMatchesColor(420,375,(0,0,0)): press(420,375)
        if pyautogui.pixelMatchesColor(490,375,(0,0,0)): press(490,375)
        if pyautogui.pixelMatchesColor(555,375,(0,0,0)): press(555,375)
        if pyautogui.pixelMatchesColor(632,375,(0,0,0)): press(632,375)

def press(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

if __name__ == '__main__':
    main()