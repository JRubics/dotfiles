#no caps, caps = esc, esc = esc
setxkbmap rs &
setxkbmap -layout rs -variant latin &
setxkbmap us &
setxkbmap -layout us -variant colemak &
#setxkbmap -option ctrl:swapcaps &
setxkbmap -option ctrl:nocaps &
xcape -e 'Control_L=Escape' &
xset -b &
twmnd &

firefox &
telegram-desktop &

# i3
exec i3

# cinnamon
#exec cinnamon-session
