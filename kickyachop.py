import pyautogui as py
import numpy as np
import cv2 as cv
import keyboard
import time

scstop = py.screenshot()
scstop = np.array(scstop) 
# Convert RGB to BGR 
scstop= scstop[:, :, ::-1].copy()

lwood = cv.imread('leftchop.png')
rwood = cv.imread('rightchop.png')
flag = 0 

def windowcaptureLeft():
    screenshot = py.screenshot(region = (515, 665, 950, 666))
    sc = np.array(screenshot) 
    # Convert RGB to BGR 
    sc= sc[:, :, ::-1].copy()
    # cv.imshow('left', sc)
    # cv.waitKey(0)
    return sc

def windowcaptureRight():
    screenshot = py.screenshot(region = (600, 640, 1250, 764))
    sc = np.array(screenshot) 
    # Convert RGB to BGR 
    sc= sc[:, :, ::-1].copy()
    return sc

def kick(sc):
    
    result = cv.matchTemplate(sc, lwood, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    w = lwood.shape[1]
    h = lwood.shape[0]

    if (max_val>=0.5):
        py.click(x=1200, y=400, clicks=1, button='left')
        
        cv.rectangle(sc, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,255,255), 2)
    else:
        py.click(x=600, y=400, clicks=1, button='left')
        
def stop():
    flag = 0
    stop = cv.imread('stop.png')
    result = cv.matchTemplate(scstop, stop, cv.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
    if max_val>0.60:
        flag = 1
    return flag 





keyboard.wait('s')
while flag == 0:
    sc = windowcaptureLeft()
    
    flag = stop()
    kick(sc)

    if keyboard.is_pressed('q'):
        break



cv.waitKey(0)


