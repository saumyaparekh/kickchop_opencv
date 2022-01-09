result = cv.matchTemplate(sc, rwood, cv.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
# if max_val >= 0.80 :
#     side = 'R'
#     py.click(x=1200, y=400, clicks=1, button='left')