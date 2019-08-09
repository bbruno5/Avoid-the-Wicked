# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : avoid_the_wicked.py
#	Path name : /
#	Platform  : PAP KIII PLUS (Dingux)
#	Author    : bbruno5 <bbruno5.ever@gmail.com>
#	Date      : Thu, 09 Sep 2014
#	License   : GPLv3
#
#	This file can be modified and redistributed provided followed the
#	GPLv3 license included in the parent path. Any questions,
#	sugestions, complaints or notifications	about any bug, error or
#	incompatibility, send a email for me. :)

# Importa modulos
import os, sys
from os.path import expanduser

# Define paths
home = expanduser("~")
path = ".avoid_the_wicked/"
way = home + "/" + path
conf = "conf/"
road = way + conf

#Verifica existencia de pastas e arquivos e os cria se necessario
def verify():
	if os.path.exists(way):
		print "Ok!"
	else:
		os.mkdir(way)
		
	if os.path.exists(road):
		print "Ok!"
	else:
		os.mkdir(road)
		
	if os.path.isfile(road + 'audio'):
		print "Ok!"
	else:
		txt = open(road + "audio", "w")
		txt.write("1")
		txt.close()
		
	if os.path.isfile(road + 'bscore'):
		print "Ok!"
	else:
		txt = open(road + "bscore", "w")
		txt.write("0")
		txt.close()
		
	if os.path.isfile(road + 'lscore'):
		print "Ok!"
	else:
		txt = open(road + "lscore", "w")
		txt.write("0")
		txt.close()
		
	if os.path.isfile(road + 'difficulty'):
		print "Ok!"
	else:
		txt = open(road + "difficulty", "w")
		txt.write("120")
		txt.close()
		
	if os.path.isfile(road + 'name'):
		print "Ok!"
	else:
		txt = open(road + "name", "w")
		txt.write("none")
		txt.close()
		
verify()

# Carrega avoid
avoid = 'bin/menu.py'
execfile(avoid)

