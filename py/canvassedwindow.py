"""Module contains CanvassedWindow class - subclassing ManagedWindow and
MTScatterImage to bring the abstract concept into mt world."""

# Standard imports
import random

# Third party imports
from pymt import MTScatterImage, Vector

# Internal imports
from managedwindow import ManagedWindow
from config import WIDTH, HEIGHT, is_in_bar

class CanvassedWindow(ManagedWindow, MTScatterImage):
	"""Subclasses ManagedWindow and MTScatterImage to bring the abstract concept
	into mt world."""
	
	def __init__(self, **kwargs):
		ManagedWindow.__init__(self, kwargs.get('window'))
		position=(random.uniform(0,WIDTH), random.uniform(0,HEIGHT))
		MTScatterImage.__init__(self, filename=self.imgpath, do_rotation=False,
			do_scale=False, size=(32,32), pos=position)

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
		if (is_in_bar(x, y)) and (self.is_minimized):
			print self.name, "Restoring!"
			self.restore()
		elif (not is_in_bar(x, y)) and (not self.is_minimized):
			print self.name, "Minimizing!"
			self.minimize()
		self.update_minimization()
		#print "hey, touch up: ",self.name, touchlist, touchID, x, y
	