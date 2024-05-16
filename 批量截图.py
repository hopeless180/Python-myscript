import pygetwindow as gw
from PIL import ImageGrab
import pyautogui
import keyboard
import time

def get_active_window():
    # 获取当前活动窗口
    window = gw.getActiveWindow()
    if window:
        print(f"Active window: {window.title}")
        return window
    else:
        print("No active window found.")
        return None

def screenshot_window(window):
    # 截图窗口
    bbox = (window.left, window.top, window.right, window.bottom)
    screenshot = ImageGrab.grab(bbox)
    return screenshot

def scroll_window(scrolls, delay=0.5):
    # 滑动滚动条
    window = pyautogui.getActiveWindow()
    time.sleep(4)
    pyautogui.moveTo(window.centerx, window.centery)
    pyautogui.dragTo(window.centerx, window.centery-200, duration=1)
    time.sleep(1)
    # for _ in range(scrolls):
    #     pyautogui.scroll(-1000)  # 负值向下滚动，正值向上滚动
    #     time.sleep(delay)

def main():
    all_windows = gw.getWindowsWithTitle('')
    for window in all_windows:
        print(window)
    window = gw.getWindowsWithTitle('崩坏：星穹铁道')[0]
    window.activate()
    idx = 1
    while(True):
        pyautogui.click()
        pyautogui.moveTo(window.centerx, window.centery)
        pyautogui.dragTo(window.centerx, window.centery-200, duration=1)
        # screenshot = screenshot_window(window)
        # screenshot.save(f"screenshot-{idx}.png")
        # # 滑动滚动条
        # scroll_window(window, 3)  # 滑动 5 次，延迟 0.5 秒
        # idx += 1


if __name__ == "__main__":
    main()