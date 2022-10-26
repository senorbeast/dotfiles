#!/bin/bash

# Add color in paru list
function edit_color_pacman(){
	sudo perl -pi -e 's/\n#Color/\nColor/g;' /etc/pacman.conf
}

# Add paru conf with BottomUp
function add_paru_conf(){

	# touch /usr/share/X11/xkb/symbols/custom_opts
    mkdir ~/.config/paru

	paru_conf_content="$(cat <<-EOF
		#
        # $PARU_CONF
        # /etc/paru.conf
        # ~/.config/paru/paru.conf
        #
        # See the paru.conf(5) manpage for options

        #
        # GENERAL OPTIONS
        #
        [options]
        PgpFetch
        Devel
        Provides
        DevelSuffixes = -git -cvs -svn -bzr -darcs -always -hg -fossil
        #AurOnly
        BottomUp
        #RemoveMake
        #SudoLoop
        #UseAsk
        #SaveChanges
        #CombinedUpgrade
        #CleanAfter
        #UpgradeMenu
        #NewsOnUpgrade

        #LocalRepo
        #Chroot
        #Sign
        #SignDb
        #KeepRepoCache

        #
        # Binary OPTIONS
        #
        #[bin]
        #FileManager = vifm
        #MFlags = --skippgpcheck
        #Sudo = doas
	EOF
	)"

	echo "$paru_conf_content" > ~/.config/paru/paru.conf
}

function begin_install(){
	
    FILE=~/.config/paru/paru.conf
    if [ -f "$FILE" ]; then
        echo "$FILE exists. Nothing changed."
    else 
        edit_color_pacman
        add_paru_conf
        echo "Added paru conf, updated color in pacman.conf"
    fi
}

begin_install
