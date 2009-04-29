"""Module contains ManagedWindow class - wrapping wnck.Window for WindowPile"""

# Standard imports
from random import randint
import os
# none yet

# Third party imports
import gtk
import wnck

# Internal imports
# none

class ManagedWindowError(Exception):
	"""Base class for ManagedWindow exceptions."""
	
	def __init__(self, msg):
		Exception.__init__(self, msg)

class WindowNotManagedError(ManagedWindowError):
	"""Exception raised by client classes when passed a non-ManagedWindow when
	they expected a ManagedWindow.  Also checks to see if a wnck.Window was
	passed, to help the developer with a likely mistake."""
	
	def __init__(self, not_mngd_window):
		self.not_mngd_window = not_mngd_window
		if isinstance(not_mngd_window, wnck.Window):
			self.is_wnck_window = True
		else:
			self.is_wnck_window = False
		ManagedWindowError.__init__(self, "Attempted Window: '" +
			self.not_mngd_window +"', Is raw wnck window? " +
			self.is_wnck_window)
			

class ManagedWindow:
	"""This class wraps wnck.Window to organize windows into a WindowPile."""
	def __init__(self, window):
		# Create temporary storage location
		iconroot=os.path.expanduser("~/.tactus/icons100/")
		try:
			os.makedirs(iconroot)
		except OSError:
			# well, the path already exists.  No harm done.
			pass
		
		#FIXME: a random number is bad here, we want a hash or something.
		self.imgpath = os.path.join(iconroot, str(randint(0,100))+".png")
		self.__window = window
		self.was_active = self.__window.is_active()
		self.icon = self.__window.get_icon()
		self.icon.save(self.imgpath, "png")
		self.name = ["Unknown Name", self.__window.get_name()] [
			self.__window.has_name()]
		self.iconized_name = ["Unknown Icon Name", 
			self.__window.get_icon_name()] [self.__window.has_icon_name()]
		self.pile = None
		
		# set signal handlers
		self.name_changed_handler = self.__window.connect(
			"name-changed", self.update_name, 0)
		self.icon_changed_handler = self.__window.connect(
			"icon-changed", self.update_icon, 0)
		self.__state_changed_handler = self.__window.connect(
			"state-changed", self.update_state, 0)
		return
	
	def register_pile(self, pile):
		"""Called by a WindowPile that owns this window to let us know that."""
		self.pile = pile
		return
	
	## Signal handlers
	def update_name(self, _widget, _callback_data):
		"""Callback function handing name-changed signal, passes to
		parent pile, too."""
		
		print "in update_name for ", self.name
		self.name = ["Unknown Name", self.__window.get_name()] [
			self.__window.has_name()]
		self.iconized_name = ["Unknown Icon Name", 
			self.__window.get_icon_name()] [self.__window.has_icon_name()]

		if not self.pile is None:
			self.pile.update_child_name(self)
		return

	def update_icon(self, _widget, _callback_data):
		"""Callback function handing icon-changed signal, passes to
		parent pile, too."""
		
		print "in update_icon for ", self.name
		self.icon = self.__window.get_icon()
		if not self.pile is None:
			self.pile.update_child_icon(self)
		return
	
	def update_state(self, _widget, _changed_mask, _new_state, _callback_data):
		"""STUB: Callback function handing state-changed signal, passes to
		parent pile, too.
		
		This is a more complex function, because of the variety of changes
		included in this signal. It may trigger a pile-wide update (for
		instance, active window changes, etc)."""
		
		# FIXME: ManagedWindow::update_state is not implemented
		print "in update_state for ", self.name
		return
	
	## setters/mutators
	def minimize(self):
		"""Minimize the window, without notifying the pile or adjusting active
		status.
		
		To be used by Piles or other minimization that isn't coming from the
		user or window manager."""
		self.__window.minimize()
		return
	
	def restore(self, thetime=None):
		"""Restore (unminimize) the window, without notifying the pile or
		adjusting active status.
		
		To be used by Piles or other unminimizing that isn't coming from the
		user or window manager."""
		
		if thetime == None:
			thetime = gtk.get_current_event_time()
		self.__window.unminimize(thetime)
		return	
