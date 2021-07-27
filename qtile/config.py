# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Install fonts : CaskaydiaCove Nerd Fonts, Noto Sans
# FiraCode NF + Mono
# Some emoji font (Noto Color Emoji) or yay -S emoji-keyboard-git
import os
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser("~")
myTerm = "alacritty"


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


keys = [
    # Most of our keybindings are in sxhkd file - except these
    # SUPER + FUNCTION KEYS
    Key([mod], "f", lazy.window.toggle_fullscreen()),
    Key([mod], "q", lazy.window.kill()),
    Key([mod], "Return", lazy.spawn(myTerm)),
    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "q", lazy.window.kill()),
    Key([mod, "shift"], "r", lazy.restart()),
    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),
    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),
    # RESIZE UP, DOWN, LEFT, RIGHT
    Key(
        [mod, "control"],
        "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
    ),
    Key(
        [mod, "control"],
        "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
    ),
    Key(
        [mod, "control"],
        "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
    ),
    Key(
        [mod, "control"],
        "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
    ),
    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),
    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),
    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),
    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),
    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()),
]

groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6"]

# FOR AZERTY KEYBOARDS
# group_names = ["ampersand", "eacute", "quotedbl", "apostrophe", "parenleft", "section", "egrave", "exclam", "ccedilla", "agrave",]

# group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
# group_labels = ["", "", "", "", "", "", "", "", "", "",]
group_labels = [
    " WWW",
    "  DEV",
    "  SYS",
    "  DOC",
    "  CHAT",
    "  NEW",
]
group_layouts = [
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
    "monadtall",
]
# group_layouts = ["monadtall", "matrix", "monadtall", "bsp", "monadtall", "matrix", "monadtall", "bsp", "monadtall", "monadtall",]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        )
    )

for i in groups:
    keys.extend(
        [
            # CHANGE WORKSPACES
            Key([mod], i.name, lazy.group[i.name].toscreen()),
            Key([mod], "Tab", lazy.screen.next_group()),
            Key([mod, "shift"], "Tab", lazy.screen.prev_group()),
            Key(["mod1"], "Tab", lazy.screen.next_group()),
            Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
            # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name),
                lazy.group[i.name].toscreen(),
            ),
        ]
    )


def init_layout_theme():
    return {
        "margin": 5,
        "border_width": 2,
        "border_focus": "#6790eb",
        "border_normal": "#4c566a",
    }


layout_theme = init_layout_theme()

layouts = [
    layout.MonadTall(
        margin=8, border_width=2, border_focus="#6790eb", border_normal="#4c566a"
    ),
    layout.MonadWide(
        margin=8, border_width=2, border_focus="#6790eb", border_normal="#4c566a"
    ),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme),
]

# COLORS FOR THE BAR


def init_colors():
    return [
        ["#282c34", "#282c34"],  # 0 panel background
        ["#3d3f4b", "#434758"],  # 1 background for current screen tab
        ["#ffffff", "#ffffff"],  # 2 font color for group names
        ["#ff5555", "#ff5555"],  # 3 border line color for current tab
        [
            "#74438f",
            "#74438f",
        ],  # 4 border line color for 'other tabs'
        ["#4f76c7", "#4f76c7"],  # 5 color for the 'even widgets '
        ["#e1acff", "#e1acff"],  # 6window name
        # ["#ecbbfb", "#ecbbfb"], # 7  backbround for inactive screens
        ["#88c0d0", "#88c0d0"],  # 7 Blue
        ["#6790eb", "#6790eb"],  # color 8
        ["#a9a9a9", "#a9a9a9"],
    ]  # color 9


colors = init_colors()


# WIDGETS FOR THE BAR


def init_widgets_defaults():
    return dict(font="Noto Sans", fontsize=12, padding=2, background=colors[1])


widget_defaults = init_widgets_defaults()


def init_widgets_list():
    prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())
    widgets_list = [
        widget.Sep(linewidth=0, padding=9, foreground=colors[2], background=colors[0]),
        widget.TextBox(
            text="ऋ",
            font="Noto Color Emoji",
            fontsize=23,
            foreground=colors[2],
            background=colors[0],
            margin_x=5,
            padding_y=4,
        ),
        widget.Sep(linewidth=0, padding=5, foreground=colors[2], background=colors[0]),
        widget.GroupBox(
            font="CaskaydiaCove Nerd Font",
            fontsize=13,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            disable_drag=True,
            active=colors[2],
            inactive=colors[9],
            rounded=True,
            highlight_method="line",
            this_current_screen_border=colors[8],  # Underline Highlight
            this_screen_border=colors[8],  # Active window border
            other_current_screen_border=colors[6],
            other_screen_border=colors[6],
            foreground=colors[2],
            background=colors[0],
        ),
        widget.Sep(linewidth=1, padding=16, foreground=colors[0], background=colors[0]),
        widget.WindowName(
            font="CaskaydiaCove Nerd Font",
            fontsize=13,
            foreground=colors[2],
            background=colors[0],
            padding=0,
        ),
        widget.Chord(
            chords_colors={
                "launch": ("#5e81ac", "#ffffff"),
            },
            name_transform=lambda name: name.upper(),
        ),
        # widget.Net(
        #          font="Noto Sans",
        #          fontsize=12,
        #          interface="enp0s31f6",
        #          foreground=colors[2],
        #          background=colors[1],
        #          padding = 0,
        #          ),
        # # do not activate in Virtualbox - will break qtile
        # widget.ThermalSensor(
        #          foreground = colors[5],
        #          foreground_alert = colors[6],
        #          background = colors[0],
        #          metric = True,
        #          padding = 3,
        #          threshold = 80
        #          ),
        # # battery option 1  ArcoLinux Horizontal icons do not forget to import arcobattery at the top
        # arcobattery.BatteryIcon(
        #          padding=0,
        #          scale=0.7,
        #          y_poss=2,
        #          theme_path=home + "/.config/qtile/icons/battery_icons_horiz",
        #          update_interval = 5,
        #          background = colors[0]
        #          ),
        # battery option 2  from Qtile
        # widget.Battery(
        #          font="Noto Sans",
        #          update_interval = 10,
        #          fontsize = 12,
        #          foreground = colors[5],
        #          background = colors[0],
        # 	                    ),
        # widget.CheckUpdates(
        #                      update_interval = 1800,
        #           distro = "ArchoLinux",
        #                      display_format = "Updates {updates}",
        #                      foreground = colors[2],
        #                      mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e sudo pacman -Syyuu')},
        #                      background = colors[0],
        #                      no_update_string = "0",
        #                      padding = 0,
        #                      ),
        #
        #  widget.Volume(
        #              foreground = colors[2],
        #              background = colors[4],
        #              padding = 5
        #              ),
        #,
        widget.CPU(
                    font="CaskaydiaCove Nerd Font",
                    fontsize=13,
                    foreground=colors[2],
                    background=colors[0],
                    format="  CPU {load_percent}%"
                ),
        widget.Memory(
                    # font="SF Pro Display",
                    font="CaskaydiaCove Nerd Font",
                    fontsize=13,
                    foreground=colors[2],
                    background=colors[0],
                    format='  {MemUsed: .0f}/{MemTotal:.0f} MB ',
                ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[0],
            background=colors[5],
            padding=0,
            scale=0.7,
        ),
        # widget.CurrentLayout(
        #    font="CaskaydiaCove Nerd Font",
        #    fontsize=13,
        #    foreground=colors[2],
        #    background=colors[5],
        #    padding=5,
        # ),
        widget.Systray(background=colors[0], padding=7),
        widget.Sep(linewidth=1, padding=7, foreground=colors[0], background=colors[0]),
        widget.Clock(
            font="CaskaydiaCove Nerd Font",
            fontsize=14,
            foreground=colors[0],
            background=colors[7],
            format=" %a %d %b : %H:%M:%S ",
        ),
    ]
    return widgets_list


widgets_list = init_widgets_list()


def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1


widgets_screen1 = init_widgets_screen1()


def init_screens():
    return [
        Screen(
            top=bar.Bar(
                widgets=init_widgets_screen1(), size=26, opacity=1, margin=[9, 9, 0, 9]
            )
        )
    ]  # NESW


screens = init_screens()


# MOUSE CONFIGURATION
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
]

dgroups_key_binder = None
dgroups_app_rules = []

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN

#########################################################
################ assgin apps to groups ##################
#########################################################
# @hook.subscribe.client_new
# def assign_app_group(client):
#     d = {}
#     #####################################################################################
#     ### Use xprop fo find  the value of WM_CLASS(STRING) -> First field is sufficient ###
#     #####################################################################################
#     d[group_names[0]] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
#               "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]
#     d[group_names[1]] = [ "Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
#                "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]
#     d[group_names[2]] = ["Inkscape", "Nomacs", "Ristretto", "Nitrogen", "Feh",
#               "inkscape", "nomacs", "ristretto", "nitrogen", "feh", ]
#     d[group_names[3]] = ["Gimp", "gimp" ]
#     d[group_names[4]] = ["Meld", "meld", "org.gnome.meld" "org.gnome.Meld" ]
#     d[group_names[5]] = ["Vlc","vlc", "Mpv", "mpv" ]
#     d[group_names[6]] = ["VirtualBox Manager", "VirtualBox Machine", "Vmplayer",
#               "virtualbox manager", "virtualbox machine", "vmplayer", ]
#     d[group_names[7]] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
#               "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]
#     d[group_names[8]] = ["Evolution", "Geary", "Mail", "Thunderbird",
#               "evolution", "geary", "mail", "thunderbird" ]
#     d[group_names[9]] = ["Spotify", "Pragha", "Clementine", "Deadbeef", "Audacious",
#               "spotify", "pragha", "clementine", "deadbeef", "audacious" ]
#     ######################################################################################
#
# wm_class = client.window.get_wm_class()[0]
#
#     for i in range(len(d)):
#         if wm_class in list(d.values())[i]:
#             group = list(d.keys())[i]
#             client.togroup(group)
#             client.group.cmd_toscreen(toggle=False)

# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME


main = None


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/scripts/autostart.sh"])


@hook.subscribe.startup
def start_always():
    # Set the cursor to something sane in X
    subprocess.Popen(["xsetroot", "-cursor_name", "left_ptr"])


@hook.subscribe.client_new
def set_floating(window):
    if (
        window.window.get_wm_transient_for()
        or window.window.get_wm_type() in floating_types
    ):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        {"wmclass": "Arcolinux-welcome-app.py"},
        {"wmclass": "Arcolinux-tweak-tool.py"},
        {"wmclass": "Arcolinux-calamares-tool.py"},
        {"wmclass": "confirm"},
        {"wmclass": "dialog"},
        {"wmclass": "download"},
        {"wmclass": "error"},
        {"wmclass": "file_progress"},
        {"wmclass": "notification"},
        {"wmclass": "splash"},
        {"wmclass": "toolbar"},
        {"wmclass": "confirmreset"},
        {"wmclass": "makebranch"},
        {"wmclass": "maketag"},
        {"wmclass": "Arandr"},
        {"wmclass": "feh"},
        {"wmclass": "Galculator"},
        {"wmclass": "arcolinux-logout"},
        {"wmclass": "xfce4-terminal"},
        {"wname": "branchdialog"},
        {"wname": "Open File"},
        {"wname": "pinentry"},
        {"wmclass": "ssh-askpass"},
    ],
    fullscreen_border_width=0,
    border_width=0,
)
auto_fullscreen = True

focus_on_window_activation = "focus"  # or smart

wmname = "LG3D"
