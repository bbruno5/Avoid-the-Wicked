# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : difficulty.py
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

import os, sys, pygame
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
# Define repeticao de teclas
pygame.key.set_repeat(500, 30)
# Define wallpaper
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock
	
# Le o arquivo que apresenta o nivel de dificuldade
def difficulty():
	txt = open(road + 'difficulty', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return int(diff)
# Opcoes de menu
if difficulty() == 2:
	one = font1.render("- I'm a baby", True, (255, 0, 0))
else:
	one = font1.render("- I'm a baby", True, (255, 255, 255))
one_rect = one.get_rect().move(44, 113)
""" --- """
if difficulty() == 3:
	two = font1.render('- Very Easy', True, (255, 0, 0))
else:
	two = font1.render('- Very Easy', True, (255, 255, 255))
two_rect = two.get_rect().move(44, 133)
""" --- """
if difficulty() == 4:
	three = font1.render('- Easy', True, (255, 0, 0))
else:
	three = font1.render('- Easy', True, (255, 255, 255))
three_rect = three.get_rect().move(44, 153)
""" --- """
if difficulty() == 6:
	four = font1.render('- Normal', True, (255, 0, 0))
else:
	four = font1.render('- Normal', True, (255, 255, 255))
four_rect = four.get_rect().move(44, 173)
""" --- """
if difficulty() == 8:
	five = font1.render('- Hard', True, (255, 0, 0))
else:
	five = font1.render('- Hard', True, (255, 255, 255))
five_rect = five.get_rect().move(273, 113)
""" --- """
if difficulty() == 10:
	six = font1.render('- Very Hard', True, (255, 0, 0))
else:
	six = font1.render('- Very Hard', True, (255, 255, 255))
six_rect = six.get_rect().move(273, 133)
""" --- """
if difficulty() == 12:
	seven = font1.render('- Legendary', True, (255, 0, 0))
else:
	seven = font1.render('- Legendary', True, (255, 255, 255))
seven_rect = seven.get_rect().move(273, 153)
""" --- """
if difficulty() == 16:
	eight = font1.render("- I'm perfect", True, (255, 0, 0))
else:
	eight = font1.render("- I'm perfect", True, (255, 255, 255))
eight_rect = eight.get_rect().move(273, 173)
# Carrega barra de selecao
slct = pygame.image.load("imgs/select2.png").convert_alpha()
slct_rect = slct.get_rect().move(44, 110)
# Carrega Wicked de animacao
w3 = pygame.image.load("imgs/ex_wicked3.png").convert_alpha()
w3rect = w3.get_rect().move(432, 85)
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)

# Define execs
settigs = "bin/settings.py"
menu = "bin/menu.py"

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
	screen.blit(one, one_rect)
	screen.blit(two, two_rect)
	screen.blit(three, three_rect)
	screen.blit(four, four_rect)
	screen.blit(five, five_rect)
	screen.blit(six, six_rect)
	screen.blit(seven, seven_rect)
	screen.blit(eight, eight_rect)
	pygame.display.update()
	clock().tick(60)
	for event in pygame.event.get():
		# Volta para settings
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT:
			execfile(settings)
			pygame.quit()
			done = True
			sys.exit()
		# Define movimento de selecao
		if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			speedw3[0] = -speedw3[0]
			if slct_rect.collidepoint(44, 111) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(44, 131) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(44, 151) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(44, 171) == True:
				slct_rect.move_ip(229, -60)
			elif slct_rect.collidepoint(273, 111) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(273, 131) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(273, 151) == True:
				slct_rect.move_ip(0, 20)
			elif slct_rect.collidepoint(273, 171) == True:
				slct_rect.move_ip(-229, -60)
		if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			speedw3[1] = -speedw3[1]
			if slct_rect.collidepoint(273, 171) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(273, 151) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(273, 131) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(273, 111) == True:
				slct_rect.move_ip(-229, 60)
			elif slct_rect.collidepoint(44, 171) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(44, 151) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(44, 131) == True:
				slct_rect.move_ip(0, -20)
			elif slct_rect.collidepoint(44, 111) == True:
				slct_rect.move_ip(229, 60)
		# Seleciona dificuldade
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
			if slct_rect.collidepoint(44, 111) == True:
				bin = "echo 2 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(44, 131) == True:
				bin = "echo 3 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(44, 151) == True:
				bin = "echo 4 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(44, 171) == True:
				bin = "echo 6 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(273, 111) == True:
				bin = "echo 8 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(273, 131) == True:
				bin = "echo 10 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(273, 151) == True:
				bin = "echo 12 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()
			elif slct_rect.collidepoint(273, 171) == True:
				bin = "echo 16 > " + road + "difficulty"
				os.system(bin)
				execfile(menu)
				pygame.quit()
				done = True
				sys.exit()

