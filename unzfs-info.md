# UNZFS Info

UNZFS is a command-line utility that can extract and (if necessary) decompress the contents of ZFS files used by various Activision games from the 90s, including Interstate '76 and Nitro Pack. It was originally written for the game [Battlezone](https://en.wikipedia.org/wiki/Battlezone_(1998_video_game)).

## Sources

* I obtained UNZFS at http://dummyworld.net/files/Battlezone/unzfs.zip (the URL is provided on [this page](https://interstate76.fandom.com/wiki/Tricks)).
    * Incidentally, the creator of UNZFS, Blake Robinson, composed several pieces of music for The Stanley Parable ([Bandcamp link](https://syntheticorchestra.bandcamp.com/album/bits-of-music-from-the-stanley-parable)) and the expanded Ultra Deluxe version ([Bandcamp link](https://crowscrowscrows.bandcamp.com/album/the-stanley-parable-ultra-deluxe-the-complete-soundtrack)). A Wikipedia article about him is [here](https://en.wikipedia.org/wiki/Blake_Robinson_Synthetic_Orchestra).
    * I've included a copy of `unzfs.zip` in this repository [here](unzfs.zip) in case dummyworld.net goes offline in the future (the site is excluded from [the Wayback Machine](https://web.archive.org/) and cannot be archived).
* An updated version of UNZFS is available [here](https://github.com/BattlezoneUtilities/unzfs), but I haven't tried it.

## Contents of UNZFS README

For ease of reference, the README of the original version of UNZFS contains the following:

```
----------------------------
UNZFS extracter/uncompressor
----------------------------

Name:		UNZFS 0.1a
Type:		Editing tool
Author:		Blake "Dummy" Robinson,
Created:	27th June 2003
Tools used:	MSVC++ 6
Target game:	Battlezone

Description:
UNZFS allows you to extract and uncompress Activision ZFS
files used by Battlezone (and probably other Activision
titles that use it). Now I know you're probably thinking
'Hey wait up, theres already an UNZFS extractor'. This one
is different as if also uncompresses the files inside the
archive. This means that you can finally unlock all those
files you wanted to edit in Battlezone but never could.

This program is a console application. To use it click the
start menu, select Run and type CMD. Then type

CD c:\program files\activision\battlezone\

(or wherever your Battlezone is installed) and type

unzfs /? 

for a list of commands that the program uses.
-----------------------------------------------------------


Installation:
Extract and run UNZFS.exe from the ZIP archive
-----------------------------------------------------------


Uninstallation:
If you wish to remove this plugin you can simply delete the 
following file(s):

UNZFS.exe

-----------------------------------------------------------


Distribution:

These files may only be redistributed if this readme is included.

-----------------------------------------------------------


Thanks:

Thanks to the team that bought us Battlezone, the only RTS I 
ever enjoyed playing.

-----------------------------------------------------------

UNZFS extractor/uncompressor by Dummy. (c) 2003 Paradum Games
http://games.paradum.com
```
