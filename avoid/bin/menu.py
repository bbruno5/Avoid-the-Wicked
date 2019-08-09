# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : menu.py
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

import os, sys, pygame, random
from os.path import expanduser
# Carrega o pygame
pygame.init()
# Carrega mixer
music = pygame.mixer.music
# Define execução constante ate que seja True
done = False
# Define tamanho da tela
size = width, height = 480, 272
# Define velocidade do Wicked
speedw3 = [1, 3]
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
font3 = pygame.font.Font('fonts/font1.ttf', 10)
# Define repeticao de teclas
pygame.key.set_repeat(500, 30)
# Define wallpaper
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Carrega musica de background
trilha = music.load("audio/trilha_menu.ogg")
music.set_volume(1)

# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock
# Le o arquivo que apresenta o ultimo score
def lscore():
	txt = open(road + 'lscore', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return str(diff)
# Le o arquivo que apresenta o melhor score
def bscore():
	txt = open(road + 'bscore', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return str(diff)
# Le o conf de audio
def audio():
	txt = open(road + 'audio', 'r')
	aud = txt.readline()
	audd = aud.strip()
	if audd == '1':
		music.play(-1)
	elif audd == '0':
		music.stop()
audio()
# Opcoes de menu
play = font1.render('Play', True, (255, 255, 255))
play_rect = play.get_rect().move(118, 113)
""" --- """
sco = font1.render('Global best score', True, (255, 255, 255))
sco_rect = sco.get_rect().move(118, 136)
""" --- """
abo = font1.render('About', True, (255, 255, 255))
abo_rect = abo.get_rect().move(118, 159)
""" --- """
sett = font1.render('Settings', True, (255, 255, 255))
sett_rect = sett.get_rect().move(118, 181)
""" --- """
exi = font1.render('Exit', True, (255, 255, 255))
exi_rect = exi.get_rect().move(118, 204)
# Carrega barra de selecao
slct = pygame.image.load("imgs/select.png").convert_alpha()
slct_rect = slct.get_rect().move(115, 111)
# Carrega Wicked de animacao
w3 = pygame.image.load("imgs/ex_wicked1.png").convert_alpha()
w3x = random.randrange(0, 432)
w3y = random.randrange(85, 236)
w3rect = w3.get_rect().move(w3x, w3y)
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)
# Carrega latest score
lscore = font3.render('Latest score: ' + lscore() + ' secs.', True, (100, 0, 0))
lscore_rect = lscore.get_rect().move(293, 249)
# Carrega best score
bescore = font3.render('My best score: ' + bscore() + ' secs.', True, (100, 0, 0))
bescore_rect = bescore.get_rect().move(15, 249)

# Define execs
game = "bin/avoid.py"
scores = "bin/scores.py"
settings = "bin/settings.py"
about = "bin/about.py"

while not done:
	#Define movimentacao e colisao do Wicked
	w3rect = w3rect.move(speedw3)
	if w3rect.left < 0 or w3rect.right > width:
		speedw3[0] = -speedw3[0]
	if w3rect.top < 85 or w3rect.bottom > height:
		speedw3[1] = -speedw3[1]
	# Carrega tudo na tela
	screen.blit(background, brect)
	screen.blit(w3, w3rect)
	screen.blit(title, title_rect)
	screen.blit(slct, slct_rect)
	screen.blit(play, play_rect)
	screen.blit(sco, sco_rect)
	screen.blit(abo, abo_rect)
	screen.blit(sett, sett_rect)
	screen.blit(exi, exi_rect)
	screen.blit(lscore,lscore_rect)
	screen.blit(bescore,bescore_rect)
	pygame.display.update()
	clock().tick(60)
	
	for event in pygame.event.get():
		# Define movimento de selecao
		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speedw3[0] = -speedw3[0]
			if slct_rect.collidepoint(115, 112) == True:
				slct_rect.move_ip(0, 23)
			elif slct_rect.collidepoint(115, 135) == True:
				slct_rect.move_ip(0, 23)
			elif slct_rect.collidepoint(115, 158) == True:
				slct_rect.move_ip(0, 23)
			elif slct_rect.collidepoint(115, 181) == True:
				slct_rect.move_ip(0, 23)
			elif slct_rect.collidepoint(115, 204) == True:
				slct_rect.move_ip(0, -92)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speedw3[1] = -speedw3[1]
			if slct_rect.collidepoint(115, 204) == True:
				slct_rect.move_ip(0, -23)
			elif slct_rect.collidepoint(115, 181) == True:
				slct_rect.move_ip(0, -23)
			elif slct_rect.collidepoint(115, 158) == True:
				slct_rect.move_ip(0, -23)
			elif slct_rect.collidepoint(115, 135) == True:
				slct_rect.move_ip(0, -23)
			elif slct_rect.collidepoint(115, 112) == True:
				slct_rect.move_ip(0, 92)
		# Escolhe uma das opcoes
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
			# Inicia o jogo
			if slct_rect.collidepoint(165, 112) == True:
				pygame.mixer.quit()
				execfile(game)
				pygame.quit()
				done = True
				sys.exit()
			# Ve os Scores online
			if slct_rect.collidepoint(165, 135) == True:
				execfile(scores)
				pygame.quit()
				done = True
				sys.exit()				
			# Sobre o jogo
			if slct_rect.collidepoint(165, 158) == True:
				execfile(about)
				pygame.quit()
				done = True
				sys.exit()
			# Configuracoes basicas
			if slct_rect.collidepoint(165, 181) == True:
				execfile(settings)
				pygame.quit()
				done = True
				sys.exit()
			# Sair
			if slct_rect.collidepoint(165, 204) == True:
				sys.exit()

