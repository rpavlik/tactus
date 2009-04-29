#!/bin/sh

THISSCRIPT="install_tactus_dependencies_ubuntu.sh"
# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Ensures that dependencies are installed.

echo "Installing dependencies for tactus-navigator..."
sudo aptitude install -y python-gnome2-desktop python-gtk2

if [ "$(apt-cache search pymt | grep --invert-match None | grep -o Installed)" = "" ]; then
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

