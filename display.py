import colors
import pygame
import math
import time
from gopigo import *
import sys
from collections import Counter
distance_to_stop=20

'''def update_right()
    for (i, target.[angle], i++)
       if target.[angle]+30 < = 360
           target.[angle] = 11 +30
           i++
        if target.[angle]+30 >360
            target.[angle].i = 11 - 330
'''
def draw(radarDisplay, targets, angle, distance, fontRenderer):
     # draw initial screen
    radarDisplay.fill(colors.black)

    pygame.draw.circle(radarDisplay, colors.green, (700,800), 650, 1)

    pygame.draw.circle(radarDisplay, colors.green, (700,800), 550, 1)

    pygame.draw.circle(radarDisplay, colors.green, (700,800), 450, 1)

    pygame.draw.circle(radarDisplay, colors.green, (700,800), 300, 1)

    pygame.draw.circle(radarDisplay, colors.green, (700,800), 150, 1)

    radarDisplay.fill(colors.black, [0, 785, 1400, 20])

    # horizental line
    pygame.draw.line(radarDisplay, colors.green, (30, 780), (1370, 780), 1)

    # 45 degree line
    pygame.draw.line(radarDisplay, colors.green, (700, 780),(205, 285), 1)

    # 90 degree line
    pygame.draw.line(radarDisplay, colors.green, (700, 780), (700, 80), 1)

    # 135 degree line
    pygame.draw.line(radarDisplay, colors.green, (700, 780), (1195, 285), 1)

    # draw stastics board
    pygame.draw.rect(radarDisplay, colors.blue, [30, 30, 300, 200], 2)

    # write the 0 degree
    text = fontRenderer.render("0", 1, colors.green)
    radarDisplay.blit(text,(10,780))

    # write the 45 degree
    text = fontRenderer.render("45", 1, colors.green)
    radarDisplay.blit(text,(180,260))

    # write the 90 degree
    text = fontRenderer.render("90", 1, colors.green)
    radarDisplay.blit(text,(690,55))

    # write the 135 degree
    text = fontRenderer.render("135", 1, colors.green)
    radarDisplay.blit(text,(1205,270))

    # write the 180 degree
    text = fontRenderer.render("180", 1, colors.green)
    radarDisplay.blit(text,(1365,780))

    # draw the moving line
    a = math.sin(math.radians(angle)) * 700.0
    b = math.cos(math.radians(angle)) * 700.0
    pygame.draw.line(radarDisplay, colors.green, (700, 780), (700 - int(b), 780 - int(a)), 3)

    # write the current angle
    text = fontRenderer.render("Angle : " + str(abs(angle-180)), 1, colors.white)
    radarDisplay.blit(text,(40,40))
    
    text = fontRenderer.render("Forward : " + str('Up Arrow'), 1, colors.white)
    radarDisplay.blit(text, (40,60))
    

    text = fontRenderer.render("Backward : " + str('Down Arrow'), 1, colors.white)    
    radarDisplay.blit(text, (40,80))
    
    
    text = fontRenderer.render("Left : " + str('Left Arrow'), 1, colors.white)
    radarDisplay.blit(text, (40,100))
    
    text = fontRenderer.render("Right : " + str('Right Arrow'), 1, colors.white)     
    radarDisplay.blit(text, (40,120))
    
    text = fontRenderer.render("Radar Sweep : " + str('0'), 1, colors.white)
    radarDisplay.blit(text, (40,140))
    
    
    text = fontRenderer.render("Exit : " + str('1'), 1, colors.white)
    radarDisplay.blit(text, (40,160))


    # draw targets
    for angle in targets.keys():
        # calculate the coordinates and the remoteness of the target
        c = math.sin(math.radians(targets[angle].angle)) * 800.0
        d = math.cos(math.radians(targets[angle].angle)) * 800.0
        # change the scale if the range is changed
        e = math.sin(math.radians(targets[angle].angle)) * (700 / 50) * targets[angle].distance
        f = math.cos(math.radians(targets[angle].angle)) * (700 / 50) * targets[angle].distance
        

        if targets[angle].distance < 15:
            color = colors.red
        elif 35 >= targets[angle].distance >= 15:
            color = colors.orange
        elif targets[angle].distance > 35:
            color = colors.green
        

        # draw the line indicating the target
        pygame.draw.circle(radarDisplay, color, (700 - int(f), 780 - int(e)), 20)
        
        #pygame.draw.line(radarDisplay, targets[angle].color, (700 - int(f), 780 - int(e)), (700 - int(d), 780 - int(c)), 3)

    


    # update the screen
    pygame.display.update()
