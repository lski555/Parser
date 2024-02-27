
import pyautogui
import time
i = +79993333333, "taburetovich@mail.ru"
S = i[1]
B = S.find("@")
C = S[B:]
print(C)
# Получение размеров экрана
screen_width, screen_height = pyautogui.size()

# Задержка перед началом захвата
time.sleep(3)

try:
    for i in range(10):
        # Получение изображения экрана
        screenshot = pyautogui.screenshot()

        # Отзеркаливание изображения
        mirrored_screenshot = screenshot.transpose(method=pyautogui.ImageTransparency)

        # Отображение отзеркаленного изображения
        pyautogui.screenshot(mirrored_screenshot)

except KeyboardInterrupt:
    print("\nОтзеркаливание завершено.")