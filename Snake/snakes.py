import pygame,sys
import time,datetime
import random
import leaderboards as db
from pygame import mixer 

pygame.init()

white = (0,0,0)
black = (0,255,0)
red = (255,255,255)
window_width = 1080
window_height = 720


window = pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('slither')

font=pygame.font.Font('MonospaceTypewriter.ttf', 32)
text = font.render('SCORE:', True, black, white)
textRect = text.get_rect()
textRect.center = (window_height, window_width //10)
window.blit(text, textRect)

clock = pygame.time.Clock()
FPS = 10
blockSize = 20
noPixel = 0

font = pygame.font.SysFont(None, 25, bold=True)



def display_score(score):
    score='SCORE: '+ str(score)
    high_score="BEST :  "+str(db.snakes_highscore())
    score_line = font.render(score, True, black, white)
    
    score_text_rect = score_line.get_rect()
    score_text_rect.center = (950, 15 )
    window.blit(score_line, score_text_rect)
    
    high_score_line = font.render(high_score, True, black, white)
    high_score_text_rect = high_score_line.get_rect()
    high_score_text_rect.center = (952, 35 )
    window.blit(high_score_line, high_score_text_rect)
    
    
def quit_game():
    pygame.quit()
    
    sys.exit(0)


def enter_highscore(score):
        window.fill(white)
        pygame.display.update()
        h1_font=pygame.font.Font('neversaydie.regular.ttf', 96)
        h1_text = h1_font.render('HIGHSCORE', True, black, white)
        h1_textRect = h1_text.get_rect()
        h1_textRect.center = (500,150)
        window.blit(h1_text, h1_textRect)
        
        
        h3_font=pygame.font.Font('MonospaceTypewriter.ttf', 22)
        h3_text = h3_font.render('Congratulations! Enter your name : ', True, black, white)
        h3_textRect = h3_text.get_rect()
        h3_textRect.center = (500,300)
        window.blit(h3_text, h3_textRect)
        
        pygame.display.update()
        
        
        name=""
        flag=True
        while flag:
           
            for event in pygame.event.get():
                h3_text = h3_font.render(name, True, black, white)
                pygame.display.update()
                h3_textRect = h3_text.get_rect()
                h3_textRect.center = (800,300)
                window.blit(h3_text, h3_textRect)
                if event.type == pygame.QUIT:
                          pygame.quit()
                          sys.exit(0)
                if event.type == pygame.KEYDOWN:
                      if event.key == pygame.K_a:
                        name+='A'  
                        continue
                      if event.key == pygame.K_b:
                        name+='B'  
                        continue
                      if event.key == pygame.K_c:
                        name+='C'  
                        continue
                      if event.key == pygame.K_d:
                        name+='D'  
                        continue
                      if event.key == pygame.K_e:
                        name+='E'  
                        continue
                      if event.key == pygame.K_f:
                        name+='F'  
                        continue
                      if event.key == pygame.K_g:
                        name+='G'  
                        continue
                      if event.key == pygame.K_h:
                        name+='H'  
                        continue
                        name+='B'  
                        continue
                      if event.key == pygame.K_i:
                        name+='I'  
                        continue
                      if event.key == pygame.K_j:
                        name+='J'  
                        continue
                      if event.key == pygame.K_k:
                        name+='K'  
                        continue
                      if event.key == pygame.K_l:
                        name+='L'  
                        continue
                      if event.key == pygame.K_m:
                        name+='M'  
                        continue
                      if event.key == pygame.K_n:
                        name+='N'  
                        continue
                      if event.key == pygame.K_o:
                        name+='O'  
                        continue
                      if event.key == pygame.K_p:
                        name+='P'  
                        continue
                      if event.key == pygame.K_q:
                        name+='Q'  
                        continue
                      if event.key == pygame.K_r:
                        name+='R'  
                        continue
                      if event.key == pygame.K_s:
                        name+='S'  
                        continue
                      if event.key == pygame.K_t:
                        name+='T'  
                        continue
                      if event.key == pygame.K_u:
                        name+='U'  
                        continue
                      if event.key == pygame.K_v:
                        name+='V'  
                        continue
                      if event.key == pygame.K_w:
                        name+='W'  
                        continue
                      if event.key == pygame.K_x:
                        name+='X'  
                        continue
                      if event.key == pygame.K_y:
                        name+='Y'  
                        continue
                      if event.key == pygame.K_z:
                        name+='Z'  
                        continue
                      if event.key == pygame.K_RETURN:
                        db.insert_record(score, name, datetime.datetime.now())
                        flag=False
                        game_over_screen()
                       
                        return 
                        
             

def snake(blockSize, snake_list):
    #x = 250 - (segment_width + segment_margin) * i
    for size in snake_list:
        pygame.draw.rect(window, black,[size[0]+5,size[1],blockSize,blockSize],2)


def play_game_over_sound():
    mixer.music.load("gameover.mp3") 
    mixer.music.play() 
    mixer.music.set_volume(0.7) 
    mixer.music.play() 

def egg_eat_sound():
    mixer.init() 
    mixer.music.load("egg_break.mp3")  
    mixer.music.set_volume(0.7) 
    mixer.music.play() 

def game_over_screen():
    
        
        window.fill(white)
        pygame.display.update()
        h1_font=pygame.font.Font('neversaydie.regular.ttf', 64)
        h1_text = h1_font.render('LEADERBOARD', True, black, white)
        h1_textRect = h1_text.get_rect()
        h1_textRect.center = (500,80)
        window.blit(h1_text, h1_textRect)
        
        
        
        h2_font=pygame.font.Font('MonospaceTypewriter.ttf', 20)
        records=db.display_leaderboard()
        vertical_spacing=140
        for record in records[:10]:
            record=record[1][:10]+"   "+str(record[0])+"   "+record[2]
            h2_text = h2_font.render(record, True, black, white)
            h2_textRect = h2_text.get_rect()
            h2_textRect.center = (500,vertical_spacing)
            window.blit(h2_text, h2_textRect)
            vertical_spacing+=30
    
        
        
        h3_font=pygame.font.Font('MonospaceTypewriter.ttf', 22)
        h3_text = h3_font.render('Press <ESC> to exit, Press <C> to continue...', True, black, white)
        h3_textRect = h3_text.get_rect()
        h3_textRect.center = (500,vertical_spacing+140)
        window.blit(h3_text, h3_textRect)
        pygame.display.update()
        return
   

def game_play(score):
    exit_game = False
    game_over = False
    lead_x = window_width/2
    lead_y = window_height/2
    change_pixels_of_x = 0
    change_pixels_of_y = 0
    snake_list = []
    snake_length = 1
    randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
    randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0

    while not exit_game:
        while game_over == True:
            
            if score>db.bottom_record():
               enter_highscore(score)
               score=-1
            else:
                game_over_screen()
            
            interrupt=True
            while interrupt:
               
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = False
                        exit_game = True
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            exit_game = True
                            game_over = False
                            interrupt=False
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_ESCAPE:
                                quit_game()

                        if event.key == pygame.K_c:
                            game_play(score=0)
                        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quit_game()

                leftArrow = event.key == pygame.K_LEFT
                rightArrow = event.key == pygame.K_RIGHT
                upArrow = event.key == pygame.K_UP
                downArrow = event.key == pygame.K_DOWN

                if leftArrow:
                    change_pixels_of_x = -blockSize
                    change_pixels_of_y = noPixel
                elif rightArrow:
                    change_pixels_of_x = blockSize
                    change_pixels_of_y = noPixel
                elif upArrow:
                    change_pixels_of_y = -blockSize
                    change_pixels_of_x = noPixel
                elif downArrow:
                    change_pixels_of_y = blockSize
                    change_pixels_of_x = noPixel

            if lead_x >= window_width or lead_x < 0 or lead_y >= window_height or lead_y < 0:
                game_over = True
                play_game_over_sound()

        lead_x += change_pixels_of_x
        lead_y += change_pixels_of_y

        window.fill(white)
        AppleThickness = 20
       # print([int(randomAppleX),int(randomAppleY),AppleThickness,AppleThickness])
        pygame.draw.rect(window, red, [randomAppleX,randomAppleY,AppleThickness,AppleThickness])
		
        allspriteslist = []
        allspriteslist.append(lead_x)
        allspriteslist.append(lead_y)
        snake_list.append(allspriteslist)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for eachSegment in snake_list [:-1]:
            if eachSegment == allspriteslist:
                play_game_over_sound()
                game_over = True

        snake(blockSize, snake_list)
        display_score(score)
        pygame.display.update()
        if lead_x >= randomAppleX and lead_x <= randomAppleX + AppleThickness:
            if lead_y >= randomAppleY and lead_y <= randomAppleY + AppleThickness:
                randomAppleX = round(random.randrange(0, window_width-blockSize)/10.0)*10.0
                randomAppleY = round(random.randrange(0, window_height-blockSize)/10.0)*10.0
                snake_length += 1
                display_score(score)
                score+=1
                egg_eat_sound()
                pygame.display.update()      
        clock.tick(FPS)
    pygame.quit()
    quit_game()
score=0
game_play(score)



