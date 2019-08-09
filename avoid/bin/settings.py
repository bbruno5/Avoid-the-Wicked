# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : settings.py
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
# Define execucao constante ate que seja True
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
# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock
# Opcao de definir nome
name = font1.render('Set your name', True, (255, 255, 255))
name_rect = name.get_rect().move(168, 113)
""" --- """
# Seleciona o nivel de dificuldade
dif = font1.render('Difficulty', True, (255, 255, 255))
dif_rect = dif.get_rect().move(168, 159)
""" --- """
# Carrega barra de selecao
slct = pygame.image.load("imgs/select3.png").convert_alpha()
slct_rect = slct.get_rect().move(165, 117)
# Carrega Wicked de animacao
w3 = pygame.image.load("imgs/ex_wicked4.png").convert_alpha()
w3x = random.randrange(0, 326)
w3y = random.randrange(113, 236)
w3rect = w3.get_rect().move(w3x, w3y)
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)

# Define execs
menu = "bin/menu.py"
nome = "bin/name.py"
diff = "bin/difficulty.py"

def aud():
	txt = open(road + 'audio', 'r')
	aud = txt.readline()
	audd = aud.strip()
	if audd == '1':
		auddd = '0'
		return str(auddd)
	elif audd == '0':
		auddd = '1'
		return str(auddd)

while not done:
	# Le o arquivo que define audio on/off
	def audio():
		txt = open(road + 'audio', 'r')
		aud = txt.readline()
		audd = aud.strip()
		return int(audd)
	# Controle de audio
	if audio() == 1:
		audio = font1.render("Audio On", True, (255, 255, 255))
	else:
		audio = font1.render("Audio Off", True, (255, 255, 255))
	audio_rect = audio.get_rect().move(168, 136)
	""" --- """
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
	screen.blit(name, name_rect)
	screen.blit(audio, audio_rect)
	screen.blit(dif, dif_rect)
	pygame.display.update()
	clock().tick(60)
	for event in pygame.event.get():
		# Define movimento de selecao
		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speedw3[0] = -speedw3[0]
			if slct_rect.collidepoint(165, 118) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(165, 138) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(165, 158) == True:
				slct_rect.move_ip(0, -40)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speedw3[1] = -speedw3[1]
			if slct_rect.collidepoint(165, 158) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(165, 138) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(165, 118) == True:
				slct_rect.move_ip(0, 40)
		# Volta ao menu
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT:
			execfile(menu)
			pygame.quit()
			done = True
			sys.exit()
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
			if slct_rect.collidepoint(165, 117) == True:
				execfile(nome)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(165, 137) == True:
				bin = "echo " + aud() + " > " + road + "audio"
				os.system(bin)
			elif slct_rect.collidepoint(165, 157) == True:
				execfile(diff)
				pygame.quit()
				done = True
				sys.exit()
				
