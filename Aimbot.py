import keyboard
import pyautogui
import time

# click com evento do windows é mais rapido
import win32api
import win32con


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


while keyboard.is_pressed('c') == False:

    sc = pyautogui.screenshot(region=(98, 365, 700, 600))

    sc.save('exemplo.png')
    width, height = sc.size

    # for começando de 0, até a largura total , passando de 12 em 12
    for x in range(0, width, 12):
        achou = 0
        for y in range(0, height, 12):
            r, g, b = sc.getpixel((x, y))

            if r == 255 and g == 219 and b == 195:
                achou = 1
                click(98+x, 365 + y)
                time.sleep(0.05)
                break

        if achou == 1:
            break
