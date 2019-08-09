# -*- coding: utf-8 -*-
#!/usr/bin/env python

#	Project   : Avoid the Wicked
#	File name : avoid.py
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

import os, sys, pygame, time, random, urllib2
from time import sleep
from os.path import expanduser
# Carrega o pygame
pygame.init()
# Inicia, verifica e define joystick
pygame.joystick.init()
try:
	j = pygame.joystick.Joystick(0)
	j.init()
except pygame.error:
	j = None
	print 'no joystick found.'
# Define execucao constante ate que seja True
motor = False
# Define jogo perdido como falso (por enquanto)
lose = False
# Define tamanho da tela
size = width, height = 480, 272
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
# Define fontes
font1 = pygame.font.Font('fonts/font1.ttf', 10)

font2 = pygame.font.Font('fonts/font2.ttf', 19)
font2.set_bold(True)
# Define repeticao de teclas
pygame.key.set_repeat(30, 1)
pygame.time.set_timer(pygame.USEREVENT, 1)
# Carrega o background
background = pygame.image.load("imgs/background.png").convert_alpha()
brect = background.get_rect()
# Carrega musica de background
trilha = music.load("audio/trilha_game.ogg")
music.set_volume(1)
# Carrega o Justo
fair = pygame.image.load("imgs/fair.png").convert_alpha()
fairrect = fair.get_rect().move(216, 118)
# Carrega sangrento.png
sangue = pygame.image.load("imgs/sangrento.png").convert_alpha()
sangue_rect = sangue.get_rect().move(0, 0)
# Carrega splash.png
splash = pygame.image.load("imgs/splash.png").convert_alpha()
splash_rect = splash.get_rect().move(0, 0)
# Variáveis utilizadas no sistema de velocidade dinamica do justo
veloc = 1
# Altera a velocidade do justo dinamicamente, de acordo com o tempo de KEYDOWN de cada tecla
def vel():
	global veloc
	if veloc < 10:
		veloc += 1
# Define posicoes aleatorias para x e y
def pos_x():
	x1 = random.randrange(0, 109)
	x2 = random.randrange(291, 326)
	
	if random.randint(1, 2) == 1:
		return x1
	else:
		return x2

def pos_y():
	y1 = random.randrange(0, 136)
	y2 = random.randrange(137, 262)
	
	if random.randint(1, 2) == 1:
		return y1
	else:
		return y2

# Carrega o primeiro Impio
w1 = pygame.image.load("imgs/wicked1.png").convert_alpha()
w1rect = w1.get_rect().move(pos_x(), pos_y())
# Carrega o segundo Impio
w2 = pygame.image.load("imgs/wicked2.png").convert_alpha()
w2rect = w2.get_rect().move(pos_x(), pos_y())
# Carrega o terceiro Impio
w3 = pygame.image.load("imgs/wicked3.png").convert_alpha()
w3rect = w3.get_rect().move(pos_x(), pos_y())
# Carrega o quarto Impio
w4 = pygame.image.load("imgs/wicked4.png").convert_alpha()
w4rect = w4.get_rect().move(pos_x(), pos_y())
# Carrega o quinto Impio
w5 = pygame.image.load("imgs/wicked5.png").convert_alpha()
w5rect = w5.get_rect().move(pos_x(), pos_y())
# Carrega mais Impios para os niveis mais dificeis
w6 = w1.copy()
w6rect = w6.get_rect().move(pos_x(), pos_y())
w7 = w2.copy()
w7rect = w7.get_rect().move(pos_x(), pos_y())
w8 = w3.copy()
w8rect = w8.get_rect().move(pos_x(), pos_y())
w9 = w4.copy()
w9rect = w9.get_rect().move(pos_x(), pos_y())
w10 = w5.copy()
w10rect = w10.get_rect().move(pos_x(), pos_y())
# Carrega imagem ao perder
score = pygame.image.load("imgs/score.png").convert_alpha()
score_rect = score.get_rect().move(0, 0)
# Define o clock para uso global
def clock():
	clock = pygame.time.Clock()
	return clock
# Le o arquivo que apresenta o nivel de dificuldade
def difficulty():
	txt = open(road + 'difficulty', 'r')
	dif = txt.readline()
	diff = dif.strip()
	return float(diff)
# Define nomenclatura da dificuldade
def name():
	if difficulty() == 2:
		name = "I'm a baby"
	elif difficulty() == 3:
		name = "Very Easy"
	elif difficulty() == 4:
		name = "Easy"
	elif difficulty() == 6:
		name = "Normal"
	elif difficulty() == 8:
		name = "Hard"
	elif difficulty() == 10:
		name = "Very Hard"
	elif difficulty() == 12:
		name = "Legendary"
	elif difficulty() == 16:
		name = "I'm perfect"
	return name
# Define velocidade de cada wicked
speedw1 = [1, difficulty()]
speedw2 = [difficulty(), 1]
speedw3 = [1, difficulty()]
speedw4 = [difficulty(), 1]
speedw5 = [1, difficulty()]
speedw6 = [difficulty(), 1]
speedw7 = [1, difficulty()]
speedw8 = [difficulty(), 1]
speedw9 = [1, difficulty()]
speedw10 = [difficulty(), 1]
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
	return float(diff)
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
# Funcao de chamada de riso ^_^
def riso():
	txt = open(road + 'audio', 'r')
	aud = txt.readline()
	audd = aud.strip()
	if audd == '1':
		if music.get_busy() == False:
			if float(time) == bscore():
				music.set_volume(0.8)
				terror = music.load("audio/terror.ogg")
			elif float(time) > global_score():
				music.set_volume(1.0)
				grito = music.load("audio/grito.ogg")
			else:
				music.set_volume(0.7)
				time_init = pygame.time.get_ticks()
				riso = music.load("audio/risada.ogg")
			music.play(0)

# Define execs
menu = "bin/menu.py"
submit = "bin/submit.py"
restart = "bin/avoid.py"

# Carrega latest score
lscore = font3.render('Latest score: ' + lscore() + ' secs.', True, (100, 0, 0))
lscore_rect = lscore.get_rect().move(293, 249)

# Carrega best score
bescore = font3.render('My best score: ' + str(bscore()) + ' secs.', True, (100, 0, 0))
bescore_rect = bescore.get_rect().move(15, 249)

# Le arquivo de best score global
def global_score():
	try:
		link = "https://b5team.com/atw/scores.txt"
		f = urllib2.urlopen(link, timeout=0.5)
		f.readline()
		f.readline()
		scores = f.readline()
		onscore = scores.strip()
		return float(onscore)
	except:
		error = "Unable to check the score online. Verify your connection."
		# Carrega mensagem de erro
		lists = font1.render(error, True, (255, 255, 255))
		lists_rect = lists.get_rect().move(44, 11)
		screen.blit(lists, lists_rect)

# Verifica se best score e maior que best score global
ismybs = font1.render("Congratulations! Your score is the worldwide better!", True, (100, 0, 0))
ismybs2 = font1.render("Press Y to submit your score now!", True, (100, 0, 0))
ismybs_rect = ismybs.get_rect().move(60, 215)
ismybs2_rect = ismybs2.get_rect().move(120, 227)

def cwgs():
	if bscore() > global_score():
		screen.blit(ismybs, ismybs_rect)
		screen.blit(ismybs2, ismybs2_rect)
		pygame.display.update()

# Function to try to soft move the player with fuck fake joystick in PAP KIII
def fair_move(axis, negative, value):
	if axis == 'x':
		if negative == True:
			for i in range(value):
				fairrect.move_ip(-1, 0)
		else:
			for i in range(value):
				fairrect.move_ip(1, 0)
	elif axis == 'y':
		if negative == True:
			for i in range(value):
				fairrect.move_ip(0, -1)
		else:
			for i in range(value):
				fairrect.move_ip(0, 1)

# Coloca os dados iniciais na tela
screen.blit(background, brect)
screen.blit(fair, fairrect)
screen.blit(w1, w1rect)
screen.blit(w2, w2rect)
screen.blit(w3, w3rect)
screen.blit(w4, w4rect)
screen.blit(w5, w5rect)

# Coloca de acordo com o nível
if difficulty() >= 6:
	screen.blit(w6, w6rect)
if difficulty() >= 8:
	screen.blit(w7, w7rect)
if difficulty() >= 10:
	screen.blit(w8, w8rect)
if difficulty() >= 12:
	screen.blit(w9, w9rect)
if difficulty() >= 16:
	screen.blit(w10, w10rect)

screen.blit(lscore,lscore_rect)
screen.blit(bescore,bescore_rect)
cwgs()
pygame.display.update()
# Define loop do jogo
while not motor:
	riso()
	for event in pygame.event.get():
		# Volta ao menu
		if event.type == pygame.KEYDOWN and event.key == pygame.K_LALT:
			pygame.mixer.quit()
			execfile(menu)
			pygame.quit()
			motor = True
			sys.exit()
		# Zera posicoes e recomeca o jogo
		if lose == True:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
				pygame.mixer.quit()
				execfile(restart)
				pygame.quit()
				motor = True
				sys.exit()
		# Submete pontos para score online
		if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			if bscore() > global_score():
				execfile(submit)
				pygame.mixer.quit()
				execfile(restart)
				pygame.quit()
				motor = True
				sys.exit()
		# Sai
		if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
			motor = True
			sys.exit()
		# Start
		if not lose and event.type == pygame.KEYDOWN and event.key == pygame.K_LCTRL:
			time_init = pygame.time.get_ticks()
			done = False
			while not done:
				# Faz os Impios se moverem constantemente
				w1rect = w1rect.move(speedw1)
				w2rect = w2rect.move(speedw2)
				w3rect = w3rect.move(speedw3)
				w4rect = w4rect.move(speedw4)
				w5rect = w5rect.move(speedw5)
				
				# Faz a mesma coisa se nivel > 6
				if difficulty() >= 6:
					w6rect = w6rect.move(speedw6)
				if difficulty() >= 8:
					w7rect = w7rect.move(speedw7)
				if difficulty() >= 10:
					w8rect = w8rect.move(speedw8)
				if difficulty() >= 12:
					w9rect = w9rect.move(speedw9)
				if difficulty() >= 16:
					w10rect = w10rect.move(speedw10)
				
				# Define colisao dos Impios com as paredes
				if w1rect.left < 0 or w1rect.right > width:
					speedw1[0] = -speedw1[0]
				if w1rect.top < 0 or w1rect.bottom > height:
					speedw1[1] = -speedw1[1]								
				""" --- """
				if w2rect.left < 0 or w2rect.right > width:
					speedw2[0] = -speedw2[0]
				if w2rect.top < 0 or w2rect.bottom > height:
					speedw2[1] = -speedw2[1]
				""" --- """
				if w3rect.left < 0 or w3rect.right > width:
					speedw3[0] = -speedw3[0]
				if w3rect.top < 0 or w3rect.bottom > height:
					speedw3[1] = -speedw3[1]
				""" --- """
				if w4rect.left < 0 or w4rect.right > width:
					speedw4[0] = -speedw4[0]
				if w4rect.top < 0 or w4rect.bottom > height:
					speedw4[1] = -speedw4[1]
				""" --- """
				if w5rect.left < 0 or w5rect.right > width:
					speedw5[0] = -speedw5[0]
				if w5rect.top < 0 or w5rect.bottom > height:
					speedw5[1] = -speedw5[1]
				""" --- """
				if w6rect.left < 0 or w6rect.right > width:
					speedw6[0] = -speedw6[0]
				if w6rect.top < 0 or w6rect.bottom > height:
					speedw6[1] = -speedw6[1]
				""" --- """
				if w7rect.left < 0 or w7rect.right > width:
					speedw7[0] = -speedw7[0]
				if w7rect.top < 0 or w7rect.bottom > height:
					speedw7[1] = -speedw7[1]
				""" --- """
				if w8rect.left < 0 or w8rect.right > width:
					speedw8[0] = -speedw8[0]
				if w8rect.top < 0 or w8rect.bottom > height:
					speedw8[1] = -speedw8[1]
				""" --- """
				if w9rect.left < 0 or w9rect.right > width:
					speedw9[0] = -speedw9[0]
				if w9rect.top < 0 or w9rect.bottom > height:
					speedw9[1] = -speedw9[1]
				""" --- """
				if w10rect.left < 0 or w10rect.right > width:
					speedw10[0] = -speedw10[0]
				if w10rect.top < 0 or w10rect.bottom > height:
					speedw10[1] = -speedw10[1]
				# Define colisao dos Impios consigo mesmos
				if w1rect.colliderect(w2rect) or w1rect.colliderect(w3rect) or w1rect.colliderect(w4rect) or w1rect.colliderect(w5rect) or w1rect.colliderect(w6rect) or w1rect.colliderect(w7rect) or w1rect.colliderect(w8rect) or w1rect.colliderect(w9rect) or w1rect.colliderect(w10rect):
					speedw3[0] = -speedw3[0]
				if w2rect.colliderect(w1rect) or w2rect.colliderect(w3rect) or w2rect.colliderect(w4rect) or w2rect.colliderect(w5rect) or w2rect.colliderect(w6rect) or w2rect.colliderect(w7rect) or w2rect.colliderect(w8rect) or w2rect.colliderect(w9rect) or w2rect.colliderect(w10rect):
					speedw1[1] = -speedw1[1]
				if w3rect.colliderect(w1rect) or w3rect.colliderect(w2rect) or w3rect.colliderect(w4rect) or w3rect.colliderect(w5rect) or w3rect.colliderect(w6rect) or w3rect.colliderect(w7rect) or w3rect.colliderect(w8rect) or w3rect.colliderect(w9rect) or w3rect.colliderect(w10rect):
					speedw5[0] = -speedw5[0]
				if w4rect.colliderect(w1rect) or w4rect.colliderect(w2rect) or w4rect.colliderect(w3rect) or w4rect.colliderect(w5rect) or w4rect.colliderect(w6rect) or w4rect.colliderect(w7rect) or w4rect.colliderect(w8rect) or w4rect.colliderect(w9rect) or w4rect.colliderect(w10rect):
					speedw2[1] = -speedw2[1]
				if w5rect.colliderect(w1rect) or w5rect.colliderect(w2rect) or w5rect.colliderect(w3rect) or w5rect.colliderect(w4rect) or w5rect.colliderect(w6rect) or w5rect.colliderect(w7rect) or w5rect.colliderect(w8rect) or w5rect.colliderect(w9rect) or w5rect.colliderect(w10rect):
					speedw4[0] = -speedw4[0]
				if w6rect.colliderect(w2rect) or w6rect.colliderect(w3rect) or w6rect.colliderect(w4rect) or w6rect.colliderect(w5rect) or w6rect.colliderect(w6rect) or w6rect.colliderect(w7rect) or w6rect.colliderect(w8rect) or w6rect.colliderect(w9rect) or w6rect.colliderect(w10rect):
					speedw5[0] = -speedw5[0]
				if w7rect.colliderect(w2rect) or w7rect.colliderect(w3rect) or w7rect.colliderect(w4rect) or w7rect.colliderect(w5rect) or w7rect.colliderect(w6rect) or w7rect.colliderect(w7rect) or w7rect.colliderect(w8rect) or w7rect.colliderect(w9rect) or w7rect.colliderect(w10rect):
					speedw6[0] = -speedw6[0]
				if w8rect.colliderect(w2rect) or w8rect.colliderect(w3rect) or w8rect.colliderect(w4rect) or w8rect.colliderect(w5rect) or w8rect.colliderect(w6rect) or w8rect.colliderect(w7rect) or w8rect.colliderect(w8rect) or w8rect.colliderect(w9rect) or w8rect.colliderect(w10rect):
					speedw10[0] = -speedw10[0]
				if w9rect.colliderect(w2rect) or w9rect.colliderect(w3rect) or w9rect.colliderect(w4rect) or w9rect.colliderect(w5rect) or w9rect.colliderect(w6rect) or w9rect.colliderect(w7rect) or w9rect.colliderect(w8rect) or w9rect.colliderect(w9rect) or w9rect.colliderect(w10rect):
					speedw7[0] = -speedw7[0]
				if w10rect.colliderect(w2rect) or w10rect.colliderect(w3rect) or w10rect.colliderect(w4rect) or w10rect.colliderect(w5rect) or w10rect.colliderect(w6rect) or w10rect.colliderect(w7rect) or w10rect.colliderect(w8rect) or w10rect.colliderect(w9rect) or w10rect.colliderect(w10rect):
					speedw9[0] = -speedw9[0]
				# Inicia a acao em si
				screen.blit(background, brect)
				screen.blit(fair, fairrect)
				screen.blit(w1, w1rect)
				screen.blit(w2, w2rect)
				screen.blit(w3, w3rect)
				screen.blit(w4, w4rect)
				screen.blit(w5, w5rect)
				
				# Apenas se nivel > 6
				if difficulty() >= 6:
					screen.blit(w6, w6rect)
				if difficulty() >= 8:
					screen.blit(w7, w7rect)
				if difficulty() >= 10:
					screen.blit(w8, w8rect)
				if difficulty() >= 12:
					screen.blit(w9, w9rect)
				if difficulty() >= 16:
					screen.blit(w10, w10rect)
				
				pygame.display.update()
				clock().tick(120)
				# Define controles do jogador
				for event in pygame.event.get():
					# Restaura velocidade inicial do justo pra 1 quando KEYUP
					if event.type == pygame.KEYUP:
						veloc -= 2
					# Direcionais
					if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
						# Atualiza velocidade do justo
						vel()
						# Captura as teclas utilizadas
						keys = pygame.key.get_pressed()
						# Esquerda
						if keys[pygame.K_LEFT]:
							if fairrect.left < 5:
								fairrect.move_ip(0, 0)
							else:
								fair_move('x', True, veloc)
						# Direita
						if keys[pygame.K_RIGHT]:
							if fairrect.right > width-5:
								fairrect.move_ip(0, 0)
							else:
								fair_move('x', False, veloc)
						# Acima
						if keys[pygame.K_UP]:
							if fairrect.top < 5:
								fairrect.move_ip(0, 0)
							else:
								fair_move('y', True, veloc)
						# Abaixo
						if keys[pygame.K_DOWN]:
							if fairrect.bottom > height-5:
								fairrect.move_ip(0, 0)
							else:
								fair_move('y', False, veloc)
						# Pausa o jogo
						if keys[pygame.K_LCTRL]:
							done = True
						# Retorna ao menu e cancela jogo atual
						if keys[pygame.K_LALT]:
							pygame.mixer.quit()
							execfile(menu)
							pygame.quit()
							motor = True
							sys.exit()
						# Sai durante o correr do jogo
						if keys[pygame.K_ESCAPE]:
							done = True
							sys.exit()
				# Quando perde o jogo
				if fairrect.colliderect(w1rect) or fairrect.colliderect(w2rect) or fairrect.colliderect(w3rect) or fairrect.colliderect(w4rect) or fairrect.colliderect(w5rect) or (difficulty() >= 6 and fairrect.colliderect(w6rect)) or (difficulty() >= 8 and fairrect.colliderect(w7rect)) or (difficulty() >= 10 and fairrect.colliderect(w8rect)) or (difficulty() >= 12 and fairrect.colliderect(w9rect)) or (difficulty() >= 16 and fairrect.colliderect(w10rect)):
					music.stop()
					time_lose = pygame.time.get_ticks()
					lose = True
					done = True
					full_time = int(time_lose) - int(time_init)
					t = float(full_time) / 1000
					time = str(t)
					if float(time) < global_score():
						screen.blit(sangue, sangue_rect)
					elif float(time) > global_score():
						screen.blit(splash, splash_rect)
					bin = "echo " + time + " > " + road + "lscore"
					os.system(bin)
					if float(time) > bscore():
						bin = "echo " + time + " > " + road + "bscore"
						os.system(bin)
						cwgs()
					screen.blit(score, score_rect)
					ti = font2.render(time + ' sec.', True, (255, 0, 0))
					ti_rect = ti.get_rect().move(168, 136)
					screen.blit(ti, ti_rect)
					pygame.display.update()
