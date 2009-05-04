"""Module contains CanvassedPile class - subclassing WindowPile with
details about canvas location, etc that only make sense in a multi-touch
'pile canvas' context."""

# Standard imports
from random import randint

# Third party imports
from pymt import MTScatterSvg, MTScatterPlane, MTSvg

# Internal imports
from windowpile import WindowPile, AlreadyPiledError, NotMyChildError
from managedwindow import WindowNotManagedError
from config import WIDTH, HEIGHT

class CanvassedPile(WindowPile, MTScatterSvg):
    """Subclasses ManagedWindow and MTScatterImage to bring the abstract concept
    into mt world."""
    
    def __init__(self, mtparent, managedwindows=None, position = (0,0) ):
        self.position = position
        self.parent_widget = mtparent
        WindowPile.__init__(self, managedwindows)
        MTScatterSvg.__init__(self, filename="pilestar.svg", do_rotation=False, do_scale=False)
        self.parent_widget.add_widget(self)

    def add(self, window):
        """Add a CanvassedWindow to this pile."""
        try:
            WindowPile.add(self, window)
        except (WindowNotManagedError, AlreadyPiledError):
            raise
        else:
            self.add_widget( window )

    def remove(self, window):
        """Remove a CanvassedWindow in this pile, from this pile."""
        try:
            WindowPile.remove(self, window)
        except (WindowNotManagedError, NotMyChildError):
            raise
        else:
            self.remove_widget(window)
    
    def find_bounds(self):
        """Find the smallest rectangle that would include all icon centers.
        Will be used for resizing of CanvassedPile background image upon the
        addition of a new window to it or the motion of an existing child."""
        
        xs = []
        ys = []
        for window in self.mngd_windows:
            xs.append(window.x)
            ys.append(window.y)
        
        minx=min(xs)
        miny=min(ys)
        maxx=max(xs)
        maxy=max(ys)
        return ( (minx, miny), (maxx, maxy) )
    
    def remove_overlaps(self, window):
        """Moves icons in this pile to eliminate overlaps (spread gesture needs
        this) - not implemented, currently just points to another function."""
        print self.find_bounds()
        #TODO: remove_overlaps not implemented, find_bounds called for no good
        #reason except testing
    