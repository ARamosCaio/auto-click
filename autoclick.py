import pyautogui as pg

def autoclick_regfreq(password):
   
    pg.moveTo(1024, 610, 0.5)
    pg.click()
    pg.moveTo(296, 248, 0.5)
    pg.click()
    pg.write(password)
    pg.moveTo(265, 293, 0.5)
    pg.click()




