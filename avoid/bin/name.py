# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : name.py
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
motor = False
# Define execucao constante ate que seja True
done = False
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
font2 = pygame.font.Font('fonts/font1.ttf', 10)
font3 = pygame.font.Font('fonts/font1.ttf', 15)
# Define repeticao de teclas
pygame.key.set_repeat(500, 30)
# Define wallpaper
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock
# Carrega titulo
title = pygame.image.load("imgs/title.png").convert_alpha()
title_rect = title.get_rect().move(0, 0)
# Carrega mensagem
msg = font1.render('Type your name and press A to save', True, (255, 255, 255))
msg_rect = msg.get_rect().move(30, 91)
# Carrega mensagem 2
msg2 = font2.render("or only press A to set as 'none'", True, (255, 255, 255))
msg2_rect = msg2.get_rect().move(135, 249)
# Carrega bar
bar = pygame.image.load("imgs/bar.png").convert_alpha()
bar_rect = bar.get_rect().move(480/2-232/2, 125)

# Define execs
menu = "bin/menu.py"
settings = "bin/settings.py"

def name():

    screen = screen = pygame.display.set_mode((480, 272), pygame.FULLSCREEN)
    name = ""

    while True:

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha() or event.unicode.isdigit():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_LCTRL:
                    bin = "echo " + str(name) + " > " + road + "name"
                    os.system(bin)
                    if name == "":
                    	bin = "echo 'none' > " + road + "name"
                    	os.system(bin)
                    execfile(menu)
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_LALT:
                    execfile(settings)
                    pygame.quit()
                    sys.exit()

        # Carrega tudo na tela
        screen.blit(background, brect)
        screen.blit(title, title_rect)

        block = font3.render(name, True, (0, 0, 0))
        rect = block.get_rect().move(240, 227)
        rect.center = screen.get_rect().center
        screen.blit(msg, msg_rect)
        screen.blit(msg2, msg2_rect)
        screen.blit(bar, bar_rect)
        screen.blit(block, rect)
        pygame.display.update()

if __name__ == "__main__":
    name()

