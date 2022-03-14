import pygame

lebar,tinggi=640,480
layar=pygame.display.set_mode((lebar,tinggi))
tombol={
    "U": False,
    "D": False,
    "L": False,
    "R": False
}
musuhT=100
HP = 10
TIMER = 90000
executed=True
pos=[200,200]
exitGame=0
gameover=0
win=1
skor=0
panah=[]

white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

font = "GangsarLight.ttf"

clock = pygame.time.Clock()
FPS=60