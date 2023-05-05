
import pygame as pg

#en funksjon som representerer ball animasjon

def ball_animasjon():
	global ball_fart_x, ball_fart_y
	
	ball.x += ball_fart_x
	ball.y += ball_fart_y

	if ball.top <= 0 or ball.bottom >= vindu_hoyde:
		ball_fart_y *= -1
	if ball.left <= 0 or ball.right >= vindu_bredde:
		ball_fart_x *= -1

	if ball.colliderect(spiller) or ball.colliderect(motstanderen):
		ball_fart_x *= -1

def spiller_animasjon():
	spiller.y += spiller_fart

	if spiller.top <= 0:
		spiller.top = 0
	if spiller.bottom >= vindu_hoyde:
		spiller.bottom = vindu_hoyde


# Generelt oppsett # Initialiserer/starter pygame

pg.init()
klokka = pg.time.Clock()


# Hovedvindu # Oppretter et vindu der vi skal "tegne" innholdet vårt

vindu_bredde = 500
vindu_hoyde = 500
vindu = pg.display.set_mode((vindu_bredde,vindu_hoyde))
pg.display.set_caption('Pong')

# farger

lysegrå = (200,200,200)
farger = pg.Color('grey12')


# Spillrektangler

ball = pg.Rect(vindu_bredde / 2 - 15, vindu_hoyde / 2 - 15, 30, 30)
spiller = pg.Rect(vindu_bredde - 20, vindu_hoyde / 2 - 70, 10,140)
motstanderen = pg.Rect(10, vindu_hoyde / 2 - 70, 10,140)


# Spillvariabler

ball_fart_x = 7
ball_fart_y = 7
spiller_fart = 0
motstanderen_hastighet = 7


while True:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
			
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_DOWN:
				spiller_fart += 7
			if event.key == pg.K_UP:
				spiller_fart -= 7
		if event.type == pg.KEYUP:
			if event.key == pg.K_DOWN:
				spiller_fart -= 7
			if event.key == pg.K_UP:
				spiller_fart += 7
	
	# Spilllogikk

	ball_animasjon()
	spiller_animasjon()
	if motstanderen.top < ball.y:
		motstanderen.top += motstanderen_hastighet
	if motstanderen.bottom > ball.y:
		motstanderen.bottom -= motstanderen_hastighet
	
	

	# Visuals #metode for å tegne 
	vindu.fill(farger)
	pg.draw.rect(vindu, lysegrå, spiller)
	pg.draw.rect(vindu, lysegrå, motstanderen)
	pg.draw.ellipse(vindu, lysegrå, ball)
	pg.draw.aaline(vindu, lysegrå, (vindu_bredde / 2, 0),(vindu_bredde / 2, vindu_hoyde))


	pg.display.flip()
	klokka.tick(60)