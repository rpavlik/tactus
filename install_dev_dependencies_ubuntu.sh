#!/bin/sh

THISSCRIPT="install_dev_dependencies_ubuntu.sh"
# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Ensures that dependencies are installed - these are only needed for development.

echo "Installing development dependencies for tactus-navigator..."
sudo aptitude install -y glade-gnome-3 drpython git-core giggle

if [ "$(dpkg -s pymt | grep -o install\ ok)" = "" ]; then
	echo "You don't have the pymt package installed systemwide..."
	echo "If you see 'No module named pymt' below, it's not installed at all"
	echo "and you need to install it yourself one way or another!"
	echo "I recommend the rp-mt-scripts to help you install it cleanly!"
	echo "http://github.com/rpavlik/rp-mt-scripts/"
	echo
	python -c "import pymt; print pymt"
else
	echo "pymt package detected to be installed.  That's a good start."
fi

