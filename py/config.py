"""Constants and other similar configuration."""

import pyglet

def prepare_display_settings():
    display=pyglet.window.get_platform().get_default_display()
    screens = display.get_screens()
    if len(screens) > 1:
        # Xinerama or nVidia TwinView: two screens accessible but one display
        fullscreen=True
        navscreen=screens[1]  #default screen is screens[0] so skip it
        
        width=navscreen.width
        height=navscreen.height
        barsize=height*STDBARSIZE/STDHEIGHT
    else:
        # single display - mini touch for demo mode
        width = 640
        height = 480
        barsize = 125
        fullscreen=False
        navscreen=None   # won't be used - not fullscreen
    return (width, height, barsize, fullscreen, navscreen)

    

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

def bar_location():
    #FIXME: implement using above. use in canvassedwindow
    pass

#############################
# Run dynamic configuration #
#############################

STDHEIGHT=768
STDWIDTH=1024
STDBARSIZE=200
BARLOC="top"
ICONSIZE=64 #32
print prepare_display_settings()
(WIDTH, HEIGHT, BARSIZE, FULLSCREEN, NAVSCREEN)=prepare_display_settings()

WALLFILENAME='wallpaper'+str(WIDTH)+'.png'