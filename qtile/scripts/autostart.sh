#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# 
# #Load correct screen positions
# xrandr --output DVI-D-0 --left-of HDMI-A-0
# #Faster cursor
# xset r rate 300 50
# #Remapping caps lock to super
# setxkbmap -option caps:super
# #Acts as escape when pressed once
# killall xcape 2>/dev/null; xcape -e 'Super_L=Escape'
# #Double layout fr/ara
# setxkbmap -model pc105 -layout fr,ara -variant oss_nodeadkeys, -option grp:alt_shift_toggle

xrandr --output eDP1 --off
#autohide cursor
unclutter &
setxkbmap -option "ctrl:swap_rwin_rctl" 
setxkbmap -option "caps:swapescape" 

#Some ways to set your wallpaper besides variety or nitrogen
feh --bg-fill ~/.config/variety/Favorites/OHR.IrohazakaRoad_EN-US5310275011_1920x1080.jpg

#start sxhkd to replace Qtile native key-bindings
#run sxhkd -c ~/.config/qtile/sxhkd/sxhkdrc &

#starting utility applications at boot time
lxsession &
run nm-applet &
run pamac-tray &
numlockx on &
blueman-applet &
run variety &
/usr/bin/emacs --daemon &
#flameshot &
picom --config $HOME/.config/picom/picom.conf &
#picom --config .config/picom/picom-blur.conf --experimental-backends &
#/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
dunst &
# feh --randomize --bg-fill /usr/share/wallpapers/garuda-wallpapers/*
#starting user applications at boot time
run volumeicon &
#run discord &
#nitrogen --random --set-zoom-fill &
#run caffeine -a &
#run vivaldi-stable &
#run firefox &
#run thunar &
#run dropbox &
#run insync start &
#run spotify &
#run atom &
#run telegram-desktop &
