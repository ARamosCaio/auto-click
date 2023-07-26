import pyautogui
import time
import random


def autoclick_regfreq():
   
    pg.moveTo(1024, 610, 0.5)
    pg.click()
    pg.moveTo(296, 248, 0.5)
    pg.click()
    pg.write('8899')
    pg.moveTo(265, 293, 0.5)
    pg.click()

while True:
    t = random.randrange(1740, 1860)
    print(f'Random time: {t//60} min e {t%60} seg')
    time.sleep(t)
    autoclick_regfreq()


autoclick_regfreq()