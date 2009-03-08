"""Main module to create demo GTK interface and serve as client to
ManagedWindow and WindowPile."""

import gtk
import gobject
import wnck

from managedwindow import ManagedWindow
from windowpile import WindowPile

class PileManagerDemo:
	"""Class to manage the demo window for the pile manager."""
	
	def __init__(self):
		
		self.builder = gtk.Builder()
		self.builder.add_from_file("demomain.ui")
		self.builder.connect_signals(self)
		
		self.window = self.builder.get_object("winMain")
		self.window.show()
		
		screen = wnck.screen_get_default()

		while gtk.events_pending():
			gtk.main_iteration()

		self.allwindows = []
		self.piles = []
		self.piles.append(WindowPile()) # Minimized pile
		self.piles.append(WindowPile()) # Unminimized pile
		for window in screen.get_windows():
			
			print window.get_window_type()
			if window.get_window_type() == 0 and not (
				window.get_name().startswith("The Magic Window") ):
					
				#WNCK_WINDOW_NORMAL
				x = ManagedWindow(window)
				self.allwindows.append(x)
				if window.is_minimized():
					self.piles[0].add(x)
					print "Minimized, pile 0: ", x.name
				else:
					self.piles[1].add(x)
					print "Not Minimized, pile 1: ", x.name
			else:
				print "Special window: ", window.get_name()
				
		# FIXME: Combo box doesn't work
		self.combo_model = gtk.ListStore(gobject.TYPE_STRING)
		self.combo_model.append(("Originally Unminimized",))
		self.combo_model.append(("Originally Minimized",))
		self.builder.get_object("comboPileList").set_model(self.combo_model)
		
		self.update_window_list()
		
	def update_window_list(self):
		"""Update list of windows in textbox following some change, usually
		to the toggle."""
		#FIXME: update_window_list not implemented
		pass
	
	## GTK+ Signal Handlers
	def on_winMain_destroy(self, _widget, _callback_data=None):
		"""Callback to exit mainloop on window destruction."""
		print "destroy signal occurred"
		gtk.main_quit()
	
	def on_btnMinimize_clicked(self, _widget, _callback_data=None):
		"""Callback to minimize selected pile."""
		print "Minimize clicked"
		while gtk.events_pending():
			gtk.main_iteration()
	
	def on_btnRestore_clicked(self, _widget, _callback_data=None):
		"""Callback to restore selected pile."""
		print "Restore clicked"
		while gtk.events_pending():
			gtk.main_iteration()

	def on_btnToggle_toggled(self, _widget, _callback_data=None):
		"""Callback to toggle restore state of initially-visible pile."""
		print "Toggled"
		while gtk.events_pending():
			gtk.main_iteration()

	def on_btnOrigVis_group_changed(self, _widget, _callback_data=None):
		"""Callback to update window according to pile radio btn."""
		
		# FIXME: callback only seems to fire upon window destroy
		print "Radio button"
		while gtk.events_pending():
			gtk.main_iteration()
		
		
	def main(self):
		"""Start the GTK mainloop"""
		gtk.main()
	
if __name__ == "__main__":
	app = PileManagerDemo()
	app.main()