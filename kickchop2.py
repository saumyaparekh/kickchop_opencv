import cv2 as cv
import time
import numpy as np
import pyautogui as py
import keyboard

keyboard.wait('s')
lwood = cv.imread('leftchop.png')
rwood = cv.imread('rightchop.png')
def quit():
    flag = 0
    stop = cv.imread('stop.png')
    sc = py.screenshot()
    sc = np.array(sc) 
    sc= cv.cvtColor(sc, cv.COLOR_RGB2BGR) # Convert RGB to BGR
    result = cv.matchTemplate(sc, stop, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if max_val>0.60:
        flag = 1
    return flag

side = 'L'
flag = 0

while flag!=1:


    if side == 'L':
        sc = py.screenshot(region = (700, 650, 250, 150))
        sc = np.array(sc) 
        sc= cv.cvtColor(sc, cv.COLOR_RGB2BGR) # Convert RGB to BGR 
        result = cv.matchTemplate(sc, lwood, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val >= 0.75 :
            side = 'R'
            py.click(x=1200, y=400, clicks=1, button='left')
        else:
            py.click(x=600, y=400, clicks=1, button='left')

    if side == 'R':
        sc = py.screenshot(region = (1000, 650, 250, 150))
        sc = np.array(sc) 
        sc= cv.cvtColor(sc, cv.COLOR_RGB2BGR) # Convert RGB to BGR 
        result = cv.matchTemplate(sc, rwood, cv.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val >= 0.75 :
            side = 'L'
            py.click(x=600, y=400, clicks=1, button='left')
        else:
            py.click(x=1200, y=400, clicks=1, button='left')
        
    flag = quit()