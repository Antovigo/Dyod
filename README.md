Dyod Is Your Own Dj
==================
Dyod is a remote control for your music player.
It's aimed at ricers and patricians.
You can use it with only your keyboard, allowing you to quickly find an album
in your insanely huge music library.

Which music player is it made for?
=============================
It's designed for Decibel Audio Player, but it supposedly work with anything,
as long as your music player has some CLI controls for playing and queuing files.
Edit the ~/.config/dyod.conf to set the right commands to be executed
(default commands are for Decibel).

How do I use that?
================
Simply launch Dyod, then type "part_of_artist_name/part_of_album_name",
without the quotes, and press enter.
Example : wh/st would play An Electric Storm by White Noise

Add + before your request to queue the album at the end of the playlist.
Ex : +wh/st

When proposed several choices, type ! to play everything.

You can always type #n where n is the number of the line you want to select.
There is an option in the config file to display the line numbers.

Try to create a keybinding that launches "yourterminal -x dyod".

The dyod-cli command directly accepts your request as a command line argument, if you
are into this kind of scripting shenanigans.

License
=======
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Soft
ware Foundation, either version 3 of the License, or (at your option) any lat
er version. 
This program is distributed in the hope that it will be useful, but WITHOUT 
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
 or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public Li
 cense for more details. 
You should have received a copy of the GNU General Public License along w
ith this program. If not, see <http://www.gnu.org/licenses/>. 
