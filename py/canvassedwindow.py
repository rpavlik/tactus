"""Module contains CanvassedWindow class - subclassing ManagedWindow with
details about canvas location, etc that only make sense in a multi-touch
'pile canvas' context."""

from managedwindow import ManagedWindow

from pymt import MTScatterImage

class CanvassedWindow(ManagedWindow):
	"""subclasses ManagedWindow with details about canvas location, etc that
	only make sense in a multi-touch 'pile canvas' context."""
	
	def __init__(self, window, canvas = None, position = (0,0) ):
		self.position = position
		self.canvas = canvas
		ManagedWindow.__init__(self, window)
		self.mtobject = MTScatterImage(filename=self.imgpath)
		if not canvas is None:
			self.canvas.add_widget(self.mtobject)

	def set_position(self, position):
		"""Changes the position of the window on the canvas, but does not
		animate the change.  (It's a 'set', not a 'move-to'.)"""
		
		self.position = position
		self.pile.update_child_position(self)
		
	
	