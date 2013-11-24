#!/usr/bin/python2
# -*- coding: utf-8 -*-

from config import *
import os
from time import sleep

# useful functions

def ls(path): # Lists only directories
	return os.walk(path).next()[1]
	
def red(txt): # Display some red message
	print('\033['+maincolor+txt+'\033[1;m')

def printall(ls): # Print a list of possible matches
	content = ''
	for num,i in enumerate(ls):
		if display_line_numbers:
			content += str(num) + '. ' + i + '\n'
		else:
			content += i + '\n'
	print(content)

def firststep(req): # Starting a new query
	global appendmode
	appendmode = False

	while (req == '' or req == '+'):
		req = raw_input('\033['+maincolor+'>\033[1;m ')
	
	if req[-1] == '+':
		req = req[:-1]
		appendmode = True

	artalb = req.split('/')
	# Looking for options
	if len(artalb) >= 2: # We find both the artist and album at the same time
		matches = both (artalb[0],artalb[1])
		matches = narrow(matches)
		if len(matches) == 0:
			red('Aucun résultat.\n')
		else:
			play_all(matches)
	else: # In this mode we find only the artist first
		matches = artist_only (artalb[0])

def match_art(req): # Find the artist
	ls_mus = ls(mus)
	art_candidates = [] # This will contain all the matching artists

	for i in ls_mus:
		if req.lower() in i.lower():
			art_candidates.append(i)
			
	return art_candidates

def match_alb(art_candidates,req):
	alb_candidates = [] # This will contain all the matching albums
	
	for i in art_candidates:
		ls_art = ls(mus+'/'+i)
		for j in ls_art:
			if req.lower() in j.lower():
				alb_candidates.append(i+'/'+j)
	
	return alb_candidates

def narrow(ls): # Narrows the results according to new user input
	global appendmode
	result = []
	ls = sorted(ls)
	while(len(ls) > 1):

		if appendmode :
			red('Be more precise! (To be queued)\n')
		else:
			red('Be more precise!\n')
		printall(ls)
		req = raw_input('\033['+maincolor+'+\033[1;m ')
		
		if req == '':
			continue
		elif req == '+':
			appendmode = True
			continue

		if req[-1] == '+':
			req = req[:-1]
			appendmode = True

		if req[0] == '!': # Stop bothering me and play it all
			red('Now playing : everything')
			break

		if req[0] == '#':
			if req[1:].isdigit():
				ls = [ ls[ int (req [1:]) ] ]
				break
			else:
				continue

		new_ls = [] # The actual narrowing process
		for i in ls:
			if req.lower() in i.lower():
				new_ls.append(i)
		ls = sorted(new_ls)
			
	return(ls)
	
def play_all(ls):
	if appendmode:
		red ('Queued to playlist:')
		for i in ls:
			append(i)
	else:
		red ('Now playing: ')
		play(ls[0])
		for i in ls[1:]:
			append(i)

def both(art,alb): # Find albums matching both artist and album
	matches = match_alb(match_art(art),alb)
	return matches

def artist_only(req): # Find artist in artist only mode
	possibleartists = match_art(req)
	if len(possibleartists) == 0:
		red ('Aucun résultat.\n')
	elif len(possibleartists) == 1: # We found it
		possiblealbums = [ possibleartists[0]+'/'+a for a in ls (mus+'/'+possibleartists[0]) ]
		possiblealbums = narrow(possiblealbums)
		if len(possiblealbums) == 0:
			red('Aucun résultat.\n')
		else:
			play_all(possiblealbums)
	else: # Several artists found
		possibleartists = narrow(possibleartists)
		if len(possibleartists) == 0:
			red('Aucun résultat.\n')
		else:
			possiblealbums = [ possibleartists[0]+'/'+a for a in ls (mus+'/'+possibleartists[0]) ]
			possiblealbums = narrow(possiblealbums)
			if len(possiblealbums) == 0:
				red('Aucun résultat.\n')
			else:
				play_all(possiblealbums)
				
# These are the functions that interface with the music player.
def play(url):
	print(url)
	album = files(url)
	os.system(bindings['play'].replace('%u',album))
	sleep(sleeptime)

def append(url):
	print(url+' (queued)')
	album = files (url)
	os.system(bindings['append'].replace('%u',album))
	sleep(sleeptime)

def files(url):
	filetypes = ['mp3','flac','ogg','m4a','wav','ape','mpc','aac','aiff','alac']
	fich = os.listdir(mus+'/'+url)
	album = '' #: This will contain the files		
	for track in sorted(fich):
		for ft in filetypes:
			if '.'+ft in track.lower():
				album += '"'+mus+'/'+url+'/'+track+'" '# full url of the track plus a space
	if len(album) == 0: # Looking up in the subdirectories just in case
		for subdir in ls (mus+'/'+url):
			fich = os.listdir(mus+'/'+url+'/'+subdir)
			for track in sorted(fich):
				for ft in filetypes:
					if '.'+ft in track.lower():
						album += '"'+mus+'/'+url+'/'+subdir+'/'+track+'" '
	return album

# IT'S HAPPENING
red('')
firststep('')
sleep(0.3)
