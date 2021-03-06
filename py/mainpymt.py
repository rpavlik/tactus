#! /usr/bin/env python
"""Main module for the Multi-Touch implementation of this window navigator,
built using PyMT"""

# Standard imports
from random import uniform
from sys import exit

# Third party library imports
from pymt import MTWallpaperWindow, MTWindow, MTScatterSvg, MTKinetic, MTButton, runTouchApp
import wnck
import gtk
import pyglet

# Internal imports
from canvassedpile import CanvassedPile
from canvassedwindow import CanvassedWindow
from config import *

class PileCanvas(MTKinetic):
	"""A PileCanvas handles management of all normal window, by tracking both
	the pymt parent widget and the CanvassedWindows."""
	def __init__(self, mtwindow):
		MTKinetic.__init__(self, velstop=1, friction=3)
		self.mtwindow = mtwindow
		
		self.allwindows = []
		if PILES:
			self.piles = []
			self.piles.append(CanvassedPile(mtparent=mtwindow)) # Minimized pile
			self.piles.append(CanvassedPile(mtparent=mtwindow)) # Unminimized pile
		
		#setup wnck and gtk bits
		self.screen = wnck.screen_get_default()
		while gtk.events_pending():
			gtk.main_iteration()
		
		for window in self.screen.get_windows():
			print "Got a window", window.get_window_type()
			if window.get_window_type() == 0 and not (
				window.get_name().endswith("mainpymt.py")
				and window.get_name().startswith("/home") ):
				# WNCK_WINDOW_NORMAL and not us
				
				x = CanvassedWindow(window=window,
						pos=(uniform(0,mtwindow.width),
						uniform(0, mtwindow.height-BARSIZE ) ) )
				self.add_widget(x)
				if window.is_minimized():
					if PILES:
						self.piles[0].add(x)
					print "Minimized, pile 0: ", x.name
				else:
					if PILES:
						self.piles[1].add(x)
					print "Not Minimized, pile 1: ", x.name
				self.allwindows.append(x)
			else:
				print "Special window: ", window.get_name()
				if window.get_name().endswith("mainpymt.py") and (
					window.get_name().startswith("/home") ):
						
					# this is our window: let's make it special and
					# not manage it either.
					window.set_window_type(2) #WNCK_WINDOW_DOCK
					
		
		# now add ourselves to the window
		self.process_kinetic()
		self.mtwindow.add_widget(self)



# Main
if __name__ == '__main__':
	if FULLSCREEN:
		# Xinerama or nVidia TwinView: two screens accessible but one display
		# Put the nav display on the non-primary screen.
		w = MTWallpaperWindow(wallpaper=WALLFILENAME, fullscreen=True,
			config=NAVSCREEN.get_best_config()) 
	else:
		w = MTWallpaperWindow(wallpaper=WALLFILENAME, fullscreen=False,
			width=WIDTH, height=HEIGHT)

	thisCanvas=PileCanvas(w)
	
	btnExit=MTButton(label="exit", width=50, height=50)
	w.add_widget(btnExit)
	
	# Event handler for button
	@btnExit.event
	def on_release(touchID, x, y):
		exit()


	#TODO: Add button for 180 deg rotation of everything (for when we want it...
	# but don't have rotate support in the driver)
	
	# Start event loop
	runTouchApp()

