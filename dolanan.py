#1
import pygame
from pygame.locals import *
from random import randint
import math
import assets 
import config
#2
pygame.init()
musuh=[[config.lebar,100]]
#4

font4 = pygame.font.SysFont(None, 20)

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)
 
    return newText

def main_menu():
    menu=True
    selected="start"
    while menu:
        # pygame.mixer.music.load("resources/audio/theme1.mp3")
        # pygame.mixer.music.play(-1)
        # pygame.mixer.music.set_volume(0.25)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game()
                    if selected=="quit":
                        pygame.quit()
                        quit()
 
        # Main Menu UI
        config.layar.fill(0)
        for x in range(int(config.lebar/assets.rumput.get_width()+1)):
            for y in range(int(config.tinggi/assets.rumput.get_height()+1)):
                config.layar.blit(assets.rumput,(x*100, y*100))
        title=text_format("Ngepet Tower Defense", config.font, 90, config.yellow)
        if selected=="start":
            text_start=text_format("START", config.font, 75, config.white)
        else:
            text_start = text_format("START", config.font, 75, config.black)
        if selected=="quit":
            text_quit=text_format("QUIT", config.font, 75, config.white)
        else:
            text_quit = text_format("QUIT", config.font, 75, config.black)
 
        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()
 
        # Main Menu Text
        config.layar.blit(title, (config.lebar/2 - (title_rect[2]/2), 80))
        config.layar.blit(text_start, (config.lebar/2 - (start_rect[2]/2), 300))
        config.layar.blit(text_quit, (config.lebar/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        config.clock.tick(config.FPS)
        pygame.display.set_caption("Ngepet Tower Defense")
        config.layar.blit(title, (config.lebar/2 - (title_rect[2]/2), 80))
        config.layar.blit(text_start, (config.lebar/2 - (start_rect[2]/2), 300))
        config.layar.blit(text_quit, (config.lebar/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        config.clock.tick(config.FPS)
        pygame.display.set_caption("Ngepet Tower Defense")


def game():
    while(config.executed):
        config.layar.fill(0)
        for x in range(int(config.lebar/assets.rumput.get_width()+1)):
            for y in range(int(config.tinggi/assets.rumput.get_height()+1)):
                config.layar.blit(assets.rumput,(x*100, y*100))
        config.layar.blit(assets.kastil,(0,30))
        config.layar.blit(assets.kastil,(5,135))
        config.layar.blit(assets.kastil,(0,240))
        config.layar.blit(assets.kastil,(0,345))

        posisiMouse=pygame.mouse.get_pos()
        angle=math.atan2(posisiMouse[1]-(config.pos[1]+32),posisiMouse[0]-(config.pos[0]+26))
        muter=pygame.transform.rotate(assets.pemain,360-angle*57.29)
        newPos=(config.pos[0]-muter.get_rect().width/2,config.pos[1]-muter.get_rect().height/2)
        config.layar.blit(muter,newPos)

        for peluru in config.panah:
            panahIndex=0
            Vx=math.cos(peluru[0])*10
            Vy=math.sin(peluru[0])*10
            peluru[1]+=Vx
            peluru[2]+=Vy
            if peluru[1]<-64 or peluru[1]>config.lebar or peluru[2]<-64 or peluru[2]>config.tinggi:
                config.panah.pop(panahIndex)
            panahIndex+=1
            for tembak in config.panah:
                panahBaru=pygame.transform.rotate(assets.panah1,360-tembak[0]*57.29)
                config.layar.blit(panahBaru,(tembak[1],tembak[2]))

        config.musuhT-=1
        if config.musuhT==0:
            musuh.append([config.lebar,randint(50, config.tinggi-32)])
            config.musuhT=randint(1,100)
        
        musuhIndex=0
        for ms in musuh:
            ms[0]-=5
            if ms[0]<-64:
                musuh.pop(musuhIndex)
            
            RMusuh=pygame.Rect(assets.musuh1.get_rect())
            RMusuh.top=ms[1]
            RMusuh.left=ms[0]
                
            if RMusuh.left<64:
                musuh.pop(musuhIndex)
                config.HP-=randint(5,20)
                assets.hit.play()
                print(F"Ya Salam")
        
            panahIndex=0
            for peluru in config.panah:
                RPeluru=pygame.Rect(assets.panah1.get_rect())
                RPeluru.left=peluru[1]
                RPeluru.top=peluru[2]
                if RMusuh.colliderect(RPeluru):
                    config.skor+=1
                    musuh.pop(musuhIndex)
                    assets.enemyHit.play()
                    #print(F"Headshoot!")
                    #print("Score: {}".format(config.skor))
                panahIndex+=1
            musuhIndex+=1

        for ms in musuh:
            config.layar.blit(assets.musuh1,ms)

        config.layar.blit(assets.wadahdarah,(5,5))
        for hp in range(config.HP):
            config.layar.blit(assets.darah,(hp+8, 8))

        text=pygame.font.Font(None,24)
        menit=int((config.TIMER-pygame.time.get_ticks())/60000)
        detik=int((config.TIMER-pygame.time.get_ticks())/1000%60)
        waktu="{} {:02}:{:02}".format("Waktu: ",menit,detik)
        clock=text.render(waktu,True,(255,255,255))
        textRect=clock.get_rect()
        textRect.topright=[635,5]
        config.layar.blit(clock,textRect)

        textScore=pygame.font.Font(None, 24)
        convertScore="{} {}".format("Skor: ", config.skor)
        score=textScore.render(convertScore, True, (255,255,255))
        scoreRect=score.get_rect()
        scoreRect.bottomright=[635, 475]
        config.layar.blit(score, scoreRect)

        #7
        pygame.display.flip()

        #8
        for jadi in pygame.event.get():
            if jadi.type == pygame.QUIT:
                pygame.quit()
                exit(0)
            if jadi.type==pygame.MOUSEBUTTONDOWN:
                config.panah.append([angle, newPos[0]+32, newPos[1]+32])
                assets.shoot.play()
            if jadi.type==pygame.KEYDOWN:
                if jadi.key==K_w:
                    config.tombol["U"]=True
                elif jadi.key==K_a:
                    config.tombol["L"]=True
                elif jadi.key==K_s:
                    config.tombol["D"]=True
                elif jadi.key==K_d:
                    config.tombol["R"]=True
            if jadi.type==pygame.KEYUP:
                if jadi.key==K_w:
                    config.tombol["U"]=False
                elif jadi.key==K_a:
                    config.tombol["L"]=False
                elif jadi.key==K_s:
                    config.tombol["D"]=False
                elif jadi.key==K_d:
                    config.tombol["R"]=False
        #9
        if config.tombol["U"]:
            config.pos[1] -=5
        elif config.tombol["D"]:
            config.pos[1] +=5
        elif config.tombol["L"]:
            config.pos[0] -=5
        elif config.tombol["R"]:
            config.pos[0] +=5

        if pygame.time.get_ticks() > config.TIMER:
            config.executed = False
            config.exitGame = config.win
        if config.HP <= 0:
            config.executed = False
            config.exitGame = config.gameover

    if config.exitGame==config.gameover:
        config.layar.blit(assets.GO, (0, 0))
    else:
        config.layar.blit(assets.YW, (0, 0))

    totalRect=score.get_rect()
    totalRect.center=[320, 280]
    config.layar.blit(score, totalRect)

    while True:
        for keluar in pygame.event.get():
            if keluar.type==pygame.QUIT:
                pygame.quit()
                exit(0)
        pygame.display.flip()

# def options():
#     running = True
#     while running:
#         config.layar.fill((0,0,0))
#         draw_text('options', font4, (255, 255, 255), config.layar, 20, 20)
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#         pygame.display.update()
#        # mainClock.tick(60)

main_menu()