#!/usr/bin/python2
# -*- coding: utf-8 -*-
 
from config import *
from functions import *
import player
import os
import sys

if len(sys.argv) <= 1:
	print 'You need to add your request as a parameter.\n\
	The request is "part of artist name/part of album name".\n\
	Adding + before the request will cause the album to be queued\n\
	at the end of the current playlist.\n\
	Make sure to edit the config file to have it work with your music\n\
	player.'
else:
	firststep(sys.argv[1])
