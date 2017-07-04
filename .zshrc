# Lines configured by zsh-newuser-install
HISTFILE=~/.zsh_history
HISTSIZE=10000
SAVEHIST=10000
setopt autocd extendedglob notify
#setopt SOURCE_TRACE
unsetopt beep nomatch
bindkey -v
# End of lines configured by zsh-newuser-install
# The following lines were added by compinstall
zstyle :compinstall filename '/home/pseudonick/.zshrc'

autoload -Uz compinit
compinit
# End of lines added by compinstall

source ~/.antigen/antigen.zsh
source /usr/share/fzf/completion.zsh
source /usr/share/fzf/key-bindings.zsh

# Load the oh-my-zsh's library.
antigen use oh-my-zsh

# Bundles from the default repo (robbyrussell's oh-my-zsh).
antigen bundle git
antigen bundle archlinux
antigen bundle common-aliases
antigen bundle command-not-found
#antigen bundle ssh-agent

# Syntax highlighting bundle.
antigen bundle zsh-users/zsh-autosuggestions
antigen bundle zsh-users/zsh-syntax-highlighting

# Load the theme.
antigen theme agnoster
# Tell antigen that you're done.
antigen apply


export VISUAL="vim"
export EDITOR="vim"
export XDG_CONFIG_HOME="/home/pseudonick/.config"

#bindkey "\033[H" beginning-of-line
#bindkey "\033[F" end-of-lin


#  Aliases

alias -g ll='ls --color -lha --group-directories-first'
alias -g l='ls --color -lh --group-directories-first'
alias -g '...'='../..'
alias -g cdl='cd ~/ && cl'
alias -g cl='clear'
alias -g q='exit'
alias -g rmr='rm -r'
alias -g mdr='mkdir'
alias -g sleep='sudo systemctl suspend'
alias -g df='df -h'
alias -g du='du -h'
alias -g ssh='env TERM=xterm-256color ssh'
# grep
alias -g G='| grep --color=auto'

alias -g mute='amixer set Master toggle'
alias -g volume_max='amixer set Master 100%'

# Programs
alias -g ra='ranger'
alias -g yar='yaourt'
alias -g update='yaourt -Syua'
alias -g daj='yaourt -S'
alias -g open='xdg-open'
alias -g paja-ssh='ssh-allow-friend --github paxy97'
alias -g tmux="TERM=screen-256color-bce tmux"

# Config
alias -g zshconf='vim ~/.zshrc'
alias -g i3conf='vim ~/.config/i3/config'

# Curl
alias -g myip='curl icanhazip.com'
alias -g weather='curl wttr.in/Novi_Sad'

source ~/.vim/bundle/gruvbox/gruvbox_256palette.sh

eval $(keychain --eval --quiet id_rsa)
