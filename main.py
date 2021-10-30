from gopigo import *
import time
import easygopigo3 as easy

mysensor= EasyDistanceSensor()
servo_pos = 90
print("CONTROLS")
print("w: move robot forward")
print("a: move robot left")
print("d: move robot right")
print("s: move robot back")
print("4: move robot forward")
print("6: move servo right")
print("0: move servo home")
print("Press ENTER to send the commands")

gpg = easy.EasyGoPiGo3()
my_distance_sensor = gpg.init_distance_sensor()

while True:
    print("Distance Sensor Reading: {} mm ".format(my_distance_sensor.read_mm()))
    a = input()
    if a == 'w':
        fwd()
    elif a == 'a':
        left()
    elif a == 'd':
        right()
    elif a == 's':
        bwd()
    elif a == 'x':
        stop()
    elif a == 't':
        increase_speed()
    elif a == 'g':
        decrease_speed()
    elif a == '4':
        servo_pos = servo_pos + 10
    elif a == '6':
        servo_pos = servo_pos - 50
    elif a == '0':
        servo_pos = 90

    if my_distance_sensor.read_mm()>200:
    stop()

    if servo_pos > 90:
        servo_pos = 180
    if servo_pos < 0:
        servo_pos = 180

    servo(servo_pos)
    time.sleep(.1)

