import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
from target import *
from display import draw
from gopigo import *
from collections import Counter

print 'Radar Start'

# initialize the program
x = pygame.init()

pygame.font.init()

defaultFont = pygame.font.get_default_font()

fontRenderer = pygame.font.Font(defaultFont, 20)

radarDisplay = pygame.display.set_mode((1400, 800))
    
pygame.display.set_caption('Radar Screen')


def us_map():
    delay=.02
    debug =0                    #True to print all raw values
    num_of_readings=45          #Number of readings to take 
    incr=180/num_of_readings    #increment of ang in servo
    ang_l=[0]*(num_of_readings+1)   #list to hold the ang's of readings
    dist_l=[0]*(num_of_readings+1)  #list to hold the distance at each ang
    x=[0]*(num_of_readings+1)   #list to hold the x coordinate of each point
    y=[0]*(num_of_readings+1)   #list to hold the y coordinate of each point
    buf=[0]*40
    ang=0
    lim=250     #maximum limit of distance measurement (any value over this which be initialized to the limit value)
    index=0
    sample=2
    targets = {}
    enable_servo()
    servo_pos=180

    while True:
        for i in range(sample): 
            dist=us_dist(15)
            if dist<lim and dist>=0:
                buf[i]=dist
            else:
                buf[i]=lim
            
        max=Counter(buf).most_common()  
        rm=-1
        for i in range (len(max)):
            if max[i][0] <> lim and max[i][0] <> 0:
                rm=max[i][0]
            break
        if rm==-1:
            rm=lim
        
        if debug==1:
            print index,ang,rm
        ang_l[index]=ang
        dist_l[index]=rm
        index+=1
            
        servo(ang)  
        time.sleep(delay)
        ang+=incr
            
        #print ang
        #if ang>90:
        #    break
        
        if dist != -1 and dist <= 50:
            targets[ang] = Target(ang, dist)      
    
        draw(radarDisplay, targets, ang, dist, fontRenderer)

        #ang = 180 - ang
        #dc = 1.0 / 18.0 * ang + 2
        #servo.ChangeDutyCycle(dc)
        time.sleep(0.001)

while True:
    enable_com_timeout(2000)
    enc_tgt(1,1,18) #Set encoder targetting. Stop after 4 rotations of both the wheels
    time.sleep(.2)
    while True:
        enc=read_enc_status()
        ts=read_timeout_status()
        time.sleep(.05)
        if enc == 0:    #Stop when target is reached
            break
        if  ts==0:
            break
    if us_map() <20:    #If any obstacle is closer than 20 cm, stop
        break
    disable_servo()
        # detect if close is pressed to stop the program
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            raise KeyboardInterrupt
            
disable_servo()
pygame.quit()
sys.exit()
