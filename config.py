#!/usr/bin/python2
# -*- coding: utf-8 -*-
# This is a python file, pay attention to the indentation and syntax

# Your music folder emplacement
mus = '/home/antoine/Musique'

# Color
maincolor = '1;34m' # This is blue.

# Your music player's bindings. %u is the url of the album folder
bindings = {
	'play' : 'decibel-audio-player-remote pl-set %u &',
	'append' : 'decibel-audio-player-remote pl-add %u &'
		}

sleeptime = 0.5 # Time to wait before adding successive files to the queue.
# Longer time may be required depending on your music player.
# In seconds

display_line_numbers = True # Display line numbers when multiple choice (True or False)
