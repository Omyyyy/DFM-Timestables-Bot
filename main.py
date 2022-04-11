from pyautogui import moveTo, click, typewrite, hotkey
import pyautogui
import time
from pyperclip import paste
import webbrowser
pyautogui.PAUSE = 0.065
def start():
    rounds = int(input("target score? "))
    webbrowser.open('https://www.drfrostmaths.com/timestables-game.php')
    moveTo(397, 531)
    time.sleep(3)
    click()
    start_time = time.time()
    for i in range(rounds):
        click(x=389, y=498, clicks = 3)
        hotkey('ctrl', 'c')
        click(x = 1053, y = 274)
        typewrite(str(int(eval(paste().replace("×", "*").replace("÷", "/")))))	
        if i >= 70:
            break

    return [time.time() - start_time, rounds]

time_taken, rounds = start()
print(f"{rounds} questions in {time_taken} seconds")