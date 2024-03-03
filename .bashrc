#    _               _              
#   | |__   __ _ ___| |__  _ __ ___ 
#   | '_ \ / _` / __| '_ \| '__/ __|
#  _| |_) | (_| \__ \ | | | | | (__ 
# (_)_.__/ \__,_|___/_| |_|_|  \___|
# 
# by Stephan Raabe (2023)
# -----------------------------------------------------
# ~/.bashrc
# -----------------------------------------------------

# If not running interactively, don't do anything
[[ $- != *i* ]] && return
PS1='\n\[$(tput setaf 6)╭─ \u@\h [\t]\n⎬─ \W\n╰┄┈> '
# -----------------------------------------------------
# ALIASES
# -----------------------------------------------------

alias c='clear'
alias nf='neofetch'
alias pf='pfetch'
alias ls='eza -al'
alias shutdown='systemctl poweroff'
alias v='nvim'
alias ts='~/dotfiles/scripts/snapshot.sh'
alias matrix='cmatrix'
alias wifi='iwgtk'
alias od='~/private/onedrive.sh'
alias rw='~/dotfiles/waybar/reload.sh'
alias winclass="xprop | grep 'CLASS'"
alias dot="cd ~/dotfiles && ls"
alias ..="cd .."
alias ...= "cd ../.."
alias ....="cd ../../.."
alias work="cd ~/Work && code && clear"
alias scribe="nohup python ~/PyScribe/main.py >/dev/null 2>&1 & exit"
alias vs="code && exit"
alias browser="yandex-browser-stable && exit"
alias tt="python ~/Work/PyScribe/main.py"
alias code="cd ~/Work/PyScribe/ && nvim main.py"
alias prof="nano ~/dotfiles/.bashrc"
export PATH=/home/stand4r/.local/bin:$PATH
# -----------------------------------------------------
# Window Managers
# -----------------------------------------------------

alias Qtile='startx'
# alias QtileWayland='qtile start -b wayland'
# Hyprland with Hyprland

# -----------------------------------------------------
# GIT
# -----------------------------------------------------

alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gp="git push"
alias gpl="git pull"
alias gst="git stash"
alias gsp="git stash; git pull"
alias gcheck="git checkout"

# -----------------------------------------------------
# SCRIPTS
# -----------------------------------------------------

alias gr='python ~/dotfiles/scripts/growthrate.py'
alias ChatGPT='python ~/mychatgpt/mychatgpt.py'
alias chat='python ~/mychatgpt/mychatgpt.py'
alias ascii='~/dotfiles/scripts/figlet.sh'

# -----------------------------------------------------
# VIRTUAL MACHINE
# -----------------------------------------------------

alias vm='~/private/launchvm.sh'
alias lg='~/dotfiles/scripts/looking-glass.sh'
alias vmstart='virsh --connect qemu:///system start win11'
alias vmstop='virsh --connect qemu:///system destroy win11'

# -----------------------------------------------------
# EDIT CONFIG FILES
# -----------------------------------------------------

alias confq='nvim ~/dotfiles/qtile/config.py'
alias confp='nvim ~/dotfiles/picom/picom.conf'
alias confb='nvim ~/dotfiles/.bashrc'

# -----------------------------------------------------
# EDIT NOTES
# -----------------------------------------------------

alias notes='vim ~/notes.txt'

# -----------------------------------------------------
# SYSTEM
# -----------------------------------------------------

alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias setkb='setxkbmap de;echo "Keyboard set back to de."'

# -----------------------------------------------------
# SCREEN RESOLUTINS
# -----------------------------------------------------

# Qtile
alias res1='xrandr --output DisplayPort-0 --mode 2560x1440 --rate 120'
alias res2='xrandr --output DisplayPort-0 --mode 1920x1080 --rate 120'

export PATH="/usr/lib/ccache/bin/:$PATH"


# -----------------------------------------------------
# PFETCH if on wm
# -----------------------------------------------------
echo ""
cd Work/
clear
if [[ $(tty) == *"pts"* ]]; then
   neofetch
else
    if [ -f /bin/qtile ]; then
        echo "Start Qtile X11 with command Qtile"
    fi
	if [ -f /bin/hyprctl ]; then
    	echo "Start Hyprland with command Hyprland"
	fi
fi
