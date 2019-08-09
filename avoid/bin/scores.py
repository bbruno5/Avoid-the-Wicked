# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : scores.py
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

import os, sys, pygame, urllib2
from pygame.locals import *
from os.path import expanduser
sys.path.append('lib/')
import level

# Carrega o pygame
pygame.init()
# Define execucao constante ate que seja True
done = False
# Define tamanho da tela
size = width, height = 480, 272
w = 480
# Define a surface
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# Define mouse off
pygame.mouse.set_visible(0)
# Define paths
home = expanduser("~")
path = ".avoid_the_wicked/"
way = home + "/" + path
conf = "conf/"
road = way + conf
# Define fonte
font1 = pygame.font.Font('fonts/font1.ttf', 15)
font1.set_bold(True)
""" --- """
font2 = pygame.font.Font('fonts/font2.ttf', 19)
font2.set_bold(True)
""" --- """
font3 = pygame.font.Font('fonts/font1.ttf', 10)
# Define repeticao de teclas
pygame.key.set_repeat(500, 30)
# Define wallpaper
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)
# Define cabecalho
tam = font2.size("NAME")
cab = font2.render("NAME", True, (100, 0, 0))
cab_rect = cab.get_rect().move(w/2-tam[0]/2, 102)
""" --- """
tam = font2.size("DIFFICULTY")
cab2 = font2.render("DIFFICULTY", True, (100, 0, 0))
cab2_rect = cab2.get_rect().move(w/2-tam[0]/2, 153)
""" --- """
tam = font2.size("SCORE")
cab3 = font2.render("SCORE", True, (100, 0, 0))
cab3_rect = cab3.get_rect().move(w/2-tam[0]/2, 204)
""" --- """
alert = "Your score is better than this. Press Y to submit now!"
tam = font3.size(alert)
al = font3.render(alert, True, (255, 255, 255))
al_rect = al.get_rect().move(w/2-tam[0]/2, 249)

# Define execs
menu = "bin/menu.py"
submit = "bin/submit.py"
restart = "bin/scores.py"

# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock

# Le o arquivo que apresenta o melhor score
def bscore():
	txt = open(road + 'bscore', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return float(diff)
	
def lista():
	# Define leitura ou erro de leitura dos scores
	try:
		link = "https://b5team.com/atw/scores.txt"
		f = urllib2.urlopen(link, timeout=0.5)
		n = f.readline()
		name = n.strip()
		lev = level.level
		f.readline()
		s = f.readline()
		score = s.strip()
		comp = float(score)
		# Carrega dados
		tam = font1.size(name)
		name = font1.render(name, True, (255, 255, 255))
		name_rect = name.get_rect().move(w/2-tam[0]/2, 119)
		""" --- """
		levl = font1.render(lev, True, (255, 255, 255))
		tam = font1.size(lev)
		levl_rect = name.get_rect().move(w/2-tam[0]/2, 170)
		""" --- """
		tam = font1.size(score + ' secs.')
		score = font1.render(score + ' secs.', True, (255, 255, 255))
		score_rect = name.get_rect().move(w/2-tam[0]/2, 221)
		""" --- """
		if bscore() > comp:
			screen.blit(al, al_rect)
		screen.blit(cab, cab_rect)
		screen.blit(cab2, cab2_rect)
		screen.blit(cab3, cab3_rect)
		screen.blit(name, name_rect)
		screen.blit(levl, levl_rect)
		screen.blit(score, score_rect)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
				if bscore() > comp:
					execfile(submit)
					execfile(restart)
					pygame.quit()
					motor = True
					sys.exit()
	except:
		error = "An error has ocurred in network."
		error2 = "Verify your connection."
		# Carrega mensagem de erro
		tam1 = font1.size(error)
		tam2 = font1.size(error2)
		lists = font1.render(error, True, (255, 255, 255))
		lists2 = font1.render(error2, True, (255, 255, 255))
		lists_rect = lists.get_rect().move(w/2-tam1[0]/2, 119)
		lists2_rect = lists2.get_rect().move(w/2-tam2[0]/2, 170)
		screen.blit(lists, lists_rect)
		screen.blit(lists2, lists2_rect)

# Carrega tudo na tela
screen.blit(background, brect)
screen.blit(title, title_rect)
lista()
pygame.display.update()
clock().tick(1)

while not done:
	for event in pygame.event.get():
		# Volta ao menu
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT:
			execfile(menu)
			pygame.quit()
			done = True
			sys.exit()

