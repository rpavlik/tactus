"""Module contains WindowPile class - a brainy group of ManagedWindows, and
affiliated exceptions."""

# Standard imports
# none yet

# Third party imports
import gtk
import wnck

# Internal imports
from managedwindow import ManagedWindow, WindowNotManagedError

class PileError(Exception):
	"""Base class for Pile-related exceptions."""
	
	def __init__(self, msg):
		Exception.__init__(self, msg)


class AlreadyPiledError(PileError):
	"""Exception raised when attempting to add a window to a pile that has
	been registered to another pile."""
	
	def __init__(self, new_pile, window):
		self.new_pile = new_pile
		self.window = window
		self.current_pile = window.pile
		self.window_name = window.name
		PileError.__init__(self, "Window: '" + self.window_name + "', Pile: '"
			+ self.current_pile + "', Attempted new pile: '" +
			self.new_pile + "'")


class NotYetPiledError(PileError):
	"""Exception raised when attempting to reassign a window to a pile when
	that window isn't yet assigned to a pile."""
	
	def __init__(self, new_pile, window):
		self.new_pile = new_pile
		self.window = window
		self.window_name = window.name
		PileError.__init__(self, "Window: '" + self.window_name + 
			"', Attempted new pile: '" + self.new_pile + "'")


class NotMyChildError(PileError):
	"""Exception raised when a pile is asked to handle signals or manipulate
	its data regarding a window that it isn't responsible for."""
	
	def __init__(self, wrong_pile, window):
		self.wrong_pile = wrong_pile
		self.window = window
		self.window_name = window.name
		self.actual_window_pile = window.pile
		PileError.__init__(self, "Window: '" + self.window_name + 
			"', Attempted Pile: '" 	+ wrong_pile + "', Actual pile: '" +
			self.actual_window_pile + "'")


class WindowPile:
	"""An collection of 0 or more ManagedWindows, manipulated as a group."""
	
	def __init__(self, managed_windows=None):
		self.__windows = set()
		
		if managed_windows != None:
			# connect each of the given ManagedWindows to this pile.
			for window in managed_windows:
				self.add(window)

	def add(self, window):
		"""Add a window, not already assigned to a pile, to this pile."""
		
		if window == None:
			return
		
		if not hasattr(window, "pile"):
			raise WindowNotManagedError(window)
		
		if not window.pile == None:
			raise AlreadyPiledError(self, window)
		
		window.register_pile(self)
		self.__windows.add(window)
	
	def reassign(self, window):
		"""Reassign a window already assigned to another pile to this pile."""
		
		if not hasattr(window, "pile"):
			raise WindowNotManagedError(window)
		
		if window.pile == None:
			raise NotYetPiledError(self, window)

		window.pile.remove(window)
		self.add(window)
		
	def remove(self, window):
		"""Remove a window from this pile, and unassign the window."""
		
		if not hasattr(window, "pile"):
			raise WindowNotManagedError(window)
		if window.pile != self:
			raise NotMyChildError(self, window)
		if window not in self.__windows:
			raise NotMyChildError(self, window)
		
		window.pile = None
		self.__windows.remove(window)
