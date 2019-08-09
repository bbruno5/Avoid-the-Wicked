# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : submit.py
#	Path name : bin/
#	Platform  : PAP KIII PLUS (Dingux)
#	Author    : bbruno5 <bbruno5.ever@gmail.com>
#	Date      : Thu, 09 Sep 2014
#	License   : GPLv3
#
#	This file can be modified and redistributed provided followed the
#	GPLv3 license included in the parent path. Any questions,
#	sugestions, complaints or notifications	about any bug, error or
#	incompatibility, send a email for me. :)

import os, urllib2
from os.path import expanduser

# Define paths
home = expanduser("~")
path = ".avoid_the_wicked/"
way = home + "/" + path
conf = "conf/"
road = way + conf

# Le o arquivo que apresenta o nivel de dificuldade
def name():
	txt = open(road + 'name', 'r')
	nam = txt.readline()
	name = nam.strip()
	return str(name)

def difficulty():
	txt = open(road + 'difficulty', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return str(diff)
	
def score():
	txt = open(road + 'bscore', 'r')
	sco = txt.readline()
	scor = sco.strip()
	return str(scor)

try:
	link = "https://b5team.com/atw/insert.php?name=" + name() + "&difficulty=" + difficulty() + "&score=" + score()
	f = urllib2.urlopen(link, timeout=0.5)
	result = f.readlines()
	print result
except:
	print "An error has ocurred in network. Verify your connection."

