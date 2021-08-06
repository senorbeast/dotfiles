# Linux 
# .config/fish/config.fish
function fish_greeting
    colorscript -e 26
    #neofetch
end

export NNN_PLUG='f:finder;o:fzopen;p:preview-tabbed;d:xdgdefault;t:nmount;v:imgview;g:gutenread'
export NNN_BMS="d:$HOME/Documents;w:$HOME/Downloads;c:$HOME/.config;b:$HOME/;l:$HOME/.local/share/;h:$HOME/Downloads/HueDOc/;"
export NNN_OPENER="/home/beasty/.config/nnn/plugins/nuke"
export NNN_FIFO='/tmp/nnn.fifo'
export NNN_TMPFILE='/tmp/.lastd'

export NNN_OPENER=xdg-open
export NNN_OPENER="gio open"
export NNN_OPENER=gvfs-open
alias n "nnn -P -d -A -a"

alias N "sudo nnn -e -P -d -A -a"

function neovidecloseterminal
    if count $argv > /dev/null 
        neovide "$argv" & disown
        exit
    else
        neovide & disown
        exit
    end
end

alias define='googler -n 4 define'

starship init fish | source
