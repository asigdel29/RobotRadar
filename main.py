import sys
import time
from gopigo import *
from easygopigo3 import EasyGoPiGo3


print("Welcome")    
print("Please declare your minimum safe distance")
safedistance = input()
##print("Please declare initial speed")
##current_speed = input()

servo_pos=90
gpg = EasyGoPiGo3()
distance_sensor = gpg.init_distance_sensor()

while True:
    print("W = forward.")
    print("A= left.")
    print("S = backward.")
    print("D = right.")
    print("1 = Servo left")
    print("2 = Servo right")
    print("3 = Servo home")
    print("4 = Increase speed (Default speed = 100)")
    print("5= Decrease speed")
    print("z= Exit")

    command = input()
    if command == '4':  #Increase speed
        increase_speed()


    elif command == '5': #Decrease speed
        decrease_speed()

    elif command=='1':     #Servo left
        servo_pos=servo_pos+10
    elif command == '2':  #Servo right
        servo_pos = servo_pos - 10
    elif command=='3':    #Servo home(Default position)
        servo_pos=90

    if servo_pos > 180:
        servo_pos = 180
    if servo_pos < 0:
        servo_pos = 0

        servo(servo_pos)
        time.sleep(.1)

    elif command=='w': #Move forward
        fwd()
    elif command=='a': #Turn left
        left()
    elif command=='d': #Turn Right
        right()
    elif command=='s': #Move back
        bwd()
    elif command == 'x': #Stop
        stop()
    elif command == 'z': #Exit
        print("Exiting")
        sys.exit()

    if distance_sensor.read_mm() == 200:
        print("Obstacle detectd in path: " + str(distance_sensor.read_mm()))
        stop()

    else:
        print("Enter valid command")

    time.sleep(.1)
