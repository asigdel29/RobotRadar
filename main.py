import RPi.GPIO as GPIO
import pygame
import math
import time
import colors
import sys
from target import *
from display import draw
from ultrasonicsensor import ultrasonicRead
import keyboard

while True:
    if dist<distance_to_stop:
        print("Dist:", dist, 'cm')
        print("Object to Close")
        print('Stopping')
        stop()
    a = input()
    try:

        if keyboard.is_pressed('w'):
            x = pygame.init()
            pygame.font.init()
            defaultFont = pygame.font.get_default_font()
            fontRenderer = pygame.font.Font(defaultFont, 20)
            radarDisplay = pygame.display.set_mode((1400, 800))
            pygame.display.set_caption('Radar Screen')

            # setup the servo and ultrasonic
            GPIO.setmode(GPIO.BOARD)
            GPIO.setwarnings(False)

            servoPin = 12
            GPIO.setup(servoPin, GPIO.OUT)
            servo = GPIO.PWM(servoPin, 50)
            servo.start(7)

            TRIG = 16
            ECHO = 18
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)

            # targets list
            targets = {}

            try:
                while True:

                    # rotate from 0 to 180
                    for angle in range(0, 180):
                        distance = ultrasonicRead(GPIO, TRIG, ECHO)

                    # change the condition if the range is changed
                        if distance != -1 and distance <= 50:
                            targets[angle] = Target(angle, distance)
                            draw(radarDisplay, targets, angle, distance, fontRenderer)
                            angle = 180 - angle
                            dc = 1.0 / 18.0 * angle + 2
                            servo.ChangeDutyCycle(dc)
                            time.sleep(0.001)

                    # rotate from 180 to 0
                    for angle in range(180, 0, -1):
                        distance = ultrasonicRead(GPIO, TRIG, ECHO)

                    # change the condition if the range is changed
                        if distance != -1 and distance <= 50:
                            targets[angle] = Target(angle, distance)

                        draw(radarDisplay, targets, angle, distance, fontRenderer)

                        angle = 180 - angle
                        dc = 1.0 / 18.0 * angle + 2
                        servo.ChangeDutyCycle(dc)

                        time.sleep(0.001)

                    # detect if close is pressed to stop the program
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            raise KeyboardInterrupt

            except KeyboardInterrupt:
                servo.stop()
                GPIO.cleanup()

            except Exception as e:
                servo.stop()
                GPIO.cleanup()

            fwd()
            time.sleep(.1)

        if keyboard.is_pressed('a'):
            left()

        if keyboard.is_pressed('d'):
            right()

        if keyboard.is_pressed('s'):
            bwd()

        if keyboard.is_pressed('x'):
            stop()

        if keyboard.is_pressed('t'):
            increase_speed()

        if keyboard.is_pressed('g'):
            decrease_speed()
        elif a == '4':
            servo_pos = servo_pos + 10

        elif a == '6':
            servo_pos = servo_pos - 50

        elif a == '0':
            servo_pos = 90

        if servo_pos > 90:
            servo_pos = 180
        if servo_pos < 0:
            servo_pos = 180

        servo(servo_pos)
        time.sleep(.1)

    except:
        break

pygame.quit()
sys.exit()