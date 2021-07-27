# Linux 
# .config/fish/config.fish
function fish_greeting
    colorscript random
    #neofetch
end

export NNN_PLUG='f:finder;o:fzopen;p:mocplay;d:diffs;t:nmount;v:imgview;g:gutenread'
alias nnn "nnn -e"

# alias nvim "xfce4-terminal --drop-down && neovide"
starship init fish | source
