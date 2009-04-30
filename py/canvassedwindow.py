"""Module contains CanvassedWindow class - subclassing ManagedWindow and
MTScatterImage to bring the abstract concept into mt world."""

# Standard imports
import random

# Third party imports
from pymt import MTScatterImage, Vector

# Internal imports
from managedwindow import ManagedWindow
from config import WIDTH, HEIGHT, BARSIZE, ICONSIZE, is_in_bar

class CanvassedWindow(ManagedWindow, MTScatterImage):
	"""Subclasses ManagedWindow and MTScatterImage to bring the abstract concept
	into mt world."""
	
	def __init__(self, **kwargs):
		ManagedWindow.__init__(self, kwargs.get('window'))
		if self.is_minimized:
			position=(random.uniform(ICONSIZE/2, WIDTH-ICONSIZE/2), random.uniform(ICONSIZE/2, HEIGHT-BARSIZE-ICONSIZE/2))
		else:
			position=(random.uniform(ICONSIZE/2, WIDTH-ICONSIZE/2), random.uniform(HEIGHT-BARSIZE+ICONSIZE/2, HEIGHT-ICONSIZE/2))
		MTScatterImage.__init__(self, filename=self.imgpath, do_rotation=False,
			do_scale=False, size=(ICONSIZE,ICONSIZE), pos=position)

#	def set_position(self, position):
#		"""Changes the position of the window on the canvas, but does not
#		animate the change.  (It's a 'set', not a 'move-to'.)"""
#		
#		
#		# default values for opengl transform - even though we just translate
#		intersect = Vector(0,0)
#		rotation = 0
#		scale = 1
#		newposvec = Vector(position)
#		posvec = Vector(self.position)
#		trans = newposvec - posvec
#		# apply transformation
#		self.apply_angle_scale_trans(rotation, scale, trans, intersect)
#		
#		self.position = position
#		self.pile.update_child_position(self)
#		

	def on_touch_up(self, touchlist, touchID, x, y):
		if is_in_bar(x, y):
			if self.is_minimized:
				print self.name, "Restoring!"
				self.restore()
			else:
				print self.name, "already restored"
		else: # (not is_in_bar(x, y))
			if not self.is_minimized:
				print self.name, "Minimizing!"
				self.minimize()
			else:
				print self.name, "already minimized"
				
		self.update_minimization()
		return MTScatterImage.on_touch_up(self, touchlist, touchID, x, y)
		#print "hey, touch up: ",self.name, touchlist, touchID, x, y
	