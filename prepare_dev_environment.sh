#!/bin/bash

THISSCRIPT="prepare_dev_environment.sh"
# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Ensures that dependencies are installed - these are only needed for development.
source globals.inc

if [ $? -ne 0 ]; then
	echo  "Whoops - you have to run this from within its directory."
	exit 1
fi

echo "Installing development dependencies for tactus-navigator..."
package_install glade-gnome-3 drpython git-core giggle

if [ "$(is_installed pymt)" != "" ]; then
	echo
	echo "pymt package detected to be installed - hopefully it is recent enough."
	echo
else
	echo
	echo "You don't seem to have the pymt package installed systemwide..."
	echo "If you see 'No module named pymt' below, it's not installed at all"
	echo "and you need to install it yourself one way or another!"
	echo "I recommend the rp-mt-scripts to help you install it cleanly!"
	echo "http://github.com/rpavlik/rp-mt-scripts/"
	echo
	python -c "import pymt"
	echo
fi

