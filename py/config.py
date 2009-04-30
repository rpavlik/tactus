"""Constants and other similar configuration."""

WIDTH = 640 #1024
HEIGHT = 480 # 768
BARSIZE=125 #200
BARLOC="top"

def is_in_bar(x, y):
    if      BARLOC=="top":
        return (y>HEIGHT-BARSIZE and y<HEIGHT)
    elif    BARLOC=="bottom":
        return (y>0 and y<BARSIZE)
    elif    BARLOC=="right":
        return (x>WIDTH-BARSIZE and x<WIDTH)
    elif    BARLOC=="left":
        return (x>0 and x<BARSIZE)
    else:
        raise Exception("invalid bar location specified in config")
