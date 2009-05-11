#!/bin/bash

THISSCRIPT="install.sh"
# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Ensures that dependencies are installed, and creates the startup symlink.

source globals.inc

if [ $? -ne 0 ]; then
	echo  "Whoops - you have to run this from within its directory."
	exit 1
fi

echo "Attempting to install dependencies for tactus-navigator..."
package_install python-gnome2-desktop python-gtk2

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

pushd . &> /dev/null
cd py/
python -c "import mainpymt"
RV=$?
popd &>/dev/null

if [ $RV -ne 0 ]; then
	echo "Hmm, there was an error above, you're still missing some Python packages."
	echo "Please report the message in that case, so this script can be updated."
else
	echo "Import test succeeded, creating startup symlink..."
	ln -s py/mainpymt.py tactus-navigator
	echo
	echo "You may now run ./tactus-navigator (or cd py/, ./mainpymt.py) to start!"
fi

