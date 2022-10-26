#!/bin/bash

   #################################################################
   #                                                         #
   #            Super & Esc with Capslock  v0.5.0                  #
   #                                                               #
   #  A simple (scriptable) way to change Caplock on Wayland to    #
   #         to work simultaneosly as Super and Esc!               #      
   #       Author: Hrishikesh Sawant                               #
   #       License: MIT                                            #
   #                                                               #
   #     https://github.com/senorbeast/dotfiles/scripts            #
   #                                                               #
   #################################################################

#vars
script_revision="v1.2.1"
args_count="$#"

# message colors.
info_text_blue=$(tput setaf 7);
normal_text=$(tput sgr0);
error_text=$(tput setaf 1);
status_text_yellow=$(tput setaf 3);


# Bail immediately if running as root.
function CheckIfRunningAsRoot(){
    if [ "$(id -u)" = 0 ]; then
        printf "
${error_text}Running this script as root is discouraged and won't work since it needs user directories to operate. Retry as normal user.
Note: If you're trying to install extensions for another user on this computer, try 'su <user_account_name>' and proceed.
Abort.
${normal_text}"

        exit 1
    fi
}

# Bail immediately if running as root.
# CheckIfRunningAsRoot

# Trap SIGINT and SIGTERM.
function _term() {
    printf "\n\n${normal_text}";
    trap - INT TERM # clear the trap
    kill -- -$$
}

# Trap SIGINT and SIGTERM for cleanup.
trap _term INT TERM


# check if current (active) desktop instance is GNOME.
function IsEnvGNOME(){

    if [ "$XDG_CURRENT_DESKTOP" = "" ]; then
        desktop=$(echo "$XDG_DATA_DIRS" | sed 's/.*\(xfce\|kde\|gnome\).*/\1/')
    else
        desktop=$XDG_CURRENT_DESKTOP
    fi

    desktop=${desktop,,}
 
    if [[ $desktop == *"gnome"* ]]; then
        return 0
    else
        return 1
    fi
}

function confirm_action() {
    while true; do
        printf "\n${normal_text}";
        read -p "$1" -n 1 yn
        case $yn in
            [Yy]* ) return 0;;
            [Nn]* ) return 1;;
            * ) printf "\nPlease answer with 'y' or 'n'.";;
        esac
    done
}

# Create /usr/share/X11/xkb/symbols/custom_opts
function add_custom_opts(){

	# touch /usr/share/X11/xkb/symbols/custom_opts
	
	custom_opts_content="$(cat <<-EOF
		// Make Caps an additional Escape
		hidden partial modifier_keys
		xkb_symbols "super_esc" {
			key <CAPS> { [ Escape ] };
			modifier_map Mod4 { <CAPS> };
		};
	EOF
	)"

	sudo echo "$custom_opts_content" > /usr/share/X11/xkb/symbols/custom_opts
    
}

# Edit /usr/share/X11/xkb/rules/evdev and add a new line in the ! option = symbols section
function edit_options_symbols_evdev(){
	sudo perl -pi -e 's/(! option)+(\s)+(=)+(\s)+(symbols)+(\n)/$&  custom:super_esc = +custom_opts(super_esc) \n/g;' /usr/share/X11/xkb/rules/evdev
}

# Edit /usr/share/X11/xkb/rules/evdev.lst and add a new line the ! option section:
function edit_options_evdevlst(){
	sudo perl -pi -e 's/(! option)+(\n)/$&  custom:super_esc     Make Caps Lock an additional ESC and Mod4 \n/g;' /usr/share/X11/xkb/rules/evdev.lst
}

function print_banner(){
printf "${normal_text}

   ================================================================
             Super & Esc with Capslock  v0.5.0                 
                                                                 
     A simple (scriptable) way to change Caplock on Wayland to   
            to work simultaneosly as Super and Esc!                     
          Author: Hrishikesh Sawant                               
          License: MIT                                            
                                                                  
        https://github.com/senorbeast/dotfiles/scripts           

   ================================================================\n";
}

function begin_install(){
	
	print_banner
	# Dont run multiple times
    FILE=/usr/share/X11/xkb/symbols/custom_opts
    if [ -f "$FILE" ]; then
        echo "$FILE exists. Nothing changed."
    else 
        add_custom_opts
        edit_options_symbols_evdev
        edit_options_evdevlst
        echo "Updated keybinds, Please add bind to your DE"
    fi
}

begin_install