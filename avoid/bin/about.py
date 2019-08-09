# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : about.py
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

import sys, pygame, time
from time import sleep
# Carrega o pygame
pygame.init()
# Define tamanho da tela
size = width, height = 480, 272
# Define a surface
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
# Define mouse off
pygame.mouse.set_visible(0)
# Define execucao constante ate que seja True
done = False
# Define fonte
font1 = pygame.font.Font('fonts/font1.ttf', 14)
# Define repeticao de teclas
pygame.key.set_repeat(500, 30)
# Define wallpaper
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)

# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock

# Define execs
menu = "bin/menu.py"

def name():
	done = False
	
	screen.blit(background, brect)
	screen.blit(title, title_rect)
	line1 = "Project made first for dead dingoo.."
	line2 = "All images were found in the Web and have free license.."
	line4 = "If you want to contact me, please write to::"
	line5 = "<bbruno5.ever@gmail.com>>"
	line6 = "Follow my projects in <http://www.bbruno5.us.to>>"
	lista = [line1, line2, line4, line5, line6]
	textrect = pygame.Rect(10, 90, 100, 15)
	for i in lista:
		text = font1.render(i[:-1], True, (255, 255, 255))
		screen.blit(text, textrect)
		textrect.centery += 20
		pygame.display.update()
	
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
				
if __name__ == "__main__":
    pygame.init()
    name()
    
