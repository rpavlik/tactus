#!/bin/sh

THISSCRIPT="install_tactus_dependencies_ubuntu.sh"
# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Ensures that dependencies are installed.

echo "Installing dependencies for tactus-navigator..."
sudo aptitude install -y python-gnome2-desktop python-gtk2

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

cd py/
python -c "import mainpymt"
echo "If there was an error above, you're still missing some Python packages."
echo "Please report the message in that case, so this script can be updated."
echo
echo "Otherwise, you're good to go! cd py and ./mainpymt.py to start tactus-navigator!"
