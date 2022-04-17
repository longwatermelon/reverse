#!/bin/sh

sleep .3
xdotool key Shift+Home
sleep .1
xdotool key Ctrl+c

txt=`xsel -ob`
reversed=`python3 reverse.py "$txt"`
echo -n $reversed | xclip -selection clipboard

xdotool key Ctrl+v
xdotool key Return

