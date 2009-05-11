# Ryan Pavlik <ryan.pavlik@snc.edu> 2009

# Globals for shell scripts

is_installed ()
{
	if [ "$APT" != "" ]; then
		echo $(dpkg -s $1 | grep -o "install ok")
	else
		echo
	fi
}

package_install ()
{
	if [ "$APT" != "" ]; then
		# OK, we can try to install somehow
		if [ "$UBUNTU" != "yes" ]; then
			echo "NOTE: You're not on Ubuntu - make sure the equivalent of these are installed:"
			echo "$@"
			echo "Trying to install them..."
		fi
		$APT $@
	else
		echo "ERROR: You're not using a Debian/Ubuntu derivative - install these yourself:"
		echo "$@"
	fi
}

# Attempt to find package install tool in Ubuntu, Debian, and similar
APT=""
if [ "$(which aptitude)" != "" ]; then
	APT="sudo aptitude -y -q --with-recommends install"
else
	if [ "$(which apt-get)" != "" ]; then
		APT="sudo apt-get -y -qq install"
	fi
fi

# For the sake of warnings, find out if we're on ubuntu.
UBUNTU=""
if [ "$(lsb_release -i -s)" = "Ubuntu" ]; then
	UBUNTU=yes
	UBUNTUVER="$(lsb_release -r -s)"
	DISTCODENAME="$(lsb_release -c -s)"
else
	if [ "$(lsb_release -i -s)" = "Debian" ]; then
		UBUNTU=Debian
		DISTCODENAME="$(lsb_release -c -s)"
	fi
fi

# Make sure we return a 0 errval if all succeeded.
echo
