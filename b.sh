#!/bin/bash
youtube-dl http://www.youtube.com/watch?v=$1 -qo - | mplayer -monitorpixelaspect 0.5 - &> /dev/null
