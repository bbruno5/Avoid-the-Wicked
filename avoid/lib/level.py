#!/usr/bin/env python

"""
Project   : Avoid the Wicked
File name : level.py
Path name : lib/
Platform  : PAP KIII PLUS (Dingux)
Author    : bbruno5 <bbruno5.ever@gmail.com>
Date      : Thu, 09 Sep 2014
License   : GPL

This file can be modified and redistributed provided that it is non-profit and
preserve my credentials. Any questions, sugestions, complaints or notifications
about any bug, error or incompatibility, send a email for me. :)
"""

import os, sys, pygame, urllib
from pygame.locals import *

try:
	link = "http://b5team.com/atw/scores.txt"
	f = urllib.urlopen(link)
	f.readline()
	l = f.readline()
	le = l.strip()
	level = str(le)
	# Define retorno da funcao com nome do nivel
	if level == '2':
		level = "I'm a baby"
	elif level == '3':
		level = "Very Easy"
	elif level == '4':
		level = "Easy"
	elif level == '6':
		level = "Normal"
	elif level == '8':
		level = "Hard"
	elif level == '10':
		level = "Very Hard"
	elif level == '12':
		level = "Legendary"
	elif level == '16':
		level = "I'm perfect"
except:
	level = ''

