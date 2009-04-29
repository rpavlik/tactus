#! /usr/bin/env python
"""Main module for the Multi-Touch implementation of this window navigator,
built using PyMT"""

# Standard imports

# Third party library imports
from pymt import MTWallpaperWindow, MTScatterSvg, MTKinetic, runTouchApp
import wnck
import gtk

# Internal imports
from windowpile import WindowPile
from canvassedwindow import CanvassedWindow

class PileCanvas:
	"""A PileCanvas handles management of all normal window, by tracking both
	the pymt parent widget and the CanvassedWindows."""
	def __init__(self, mtwindow):
		self.mtwindow = mtwindow
		self.piles = []
		self.allwindows = []
		self.piles.append(WindowPile()) # Minimized pile
		self.piles.append(WindowPile()) # Unminimized pile
		
		#setup wnck and gtk bits
		self.screen = wnck.screen_get_default()
		while gtk.events_pending():
			gtk.main_iteration()
		
		for window in self.screen.get_windows():
			print "Got a window", window.get_window_type()
			if window.get_window_type() == 0 and not (
				window.get_name().startswith("The Magic Window") ):
					
				#WNCK_WINDOW_NORMAL
				x = CanvassedWindow(window, self.mtwindow)
				self.allwindows.append(x)
				if window.is_minimized():
					self.piles[0].add(x)
					print "Minimized, pile 0: ", x.name
				else:
					self.piles[1].add(x)
					print "Not Minimized, pile 1: ", x.name
			else:
				print "Special window: ", window.get_name()
			

# Main
if __name__ == '__main__':
	w = MTWallpaperWindow(wallpaper='wallpaper.png', fullscreen=False)
	k = MTKinetic()
	thisCanvas=PileCanvas(k)
	k.process_kinetic()
	w.add_widget(k)
	runTouchApp()

