import pygame

pemain=pygame.image.load("resources/images/dude.png")
rumput=pygame.image.load("resources/images/grass.png")
kastil=pygame.image.load("resources/images/castle.png")
panah1=pygame.image.load("resources/images/bullet.png")
musuh1=pygame.image.load("resources/images/badguy.png")
wadahdarah=pygame.image.load("resources/images/healthbar.png")
darah=pygame.image.load("resources/images/health.png")
GO=pygame.image.load("resources/images/gameover.png")
YW=pygame.image.load("resources/images/youwin.png")

pygame.mixer.init()

hit=pygame.mixer.Sound("resources/audio/explode.wav")
enemyHit=pygame.mixer.Sound("resources/audio/enemy.wav")
shoot=pygame.mixer.Sound("resources/audio/shoot.wav")
hit.set_volume(0.05)
enemyHit.set_volume(0.05)
shoot.set_volume(0.05)

pygame.mixer.music.load("resources/audio/theme2.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.25)