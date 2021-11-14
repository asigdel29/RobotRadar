from gopigo import *

print ("CONTROLS")
print ("q: Radar Scan")
print ("w: move robot forward")
print ("a: move robot left")
print ("s: move robot backward")
print ("d: move robot right")
print ("z: stop robot")
print ("4: move servo left")
print ("6: move servo right")
print ("5: move servo home")
print ("1: Increase speed")
print ("2: Speed decreases")
print ("Exit to Terminate")
print ("Press ENTER to send the commands")


distance_to_stop=20 
while True:
    inp=raw_input()
    if inp=='w':
        fwd()
        while True:
            dist=us_dist(15)
            if dist<distance_to_stop:   
                print "Object too close"
                print "Stopping"
                stop()
                time.sleep(.1)
    elif inp=='a':
        left()  
    elif inp=='d':
        right() 
    elif inp=='s':
        bwd()   
    elif inp=='x':
        stop()  
    elif inp=='1':
        increase_speed()    # Increase speed
    elif inp=='2':
        decrease_speed()    # Decrease speed
    elif inp=='z':
        stop()
    elif inp =='exit':
        print ("Exiting")     # Exit
        sys.exit()             
    elif inp=='4':
        servo_pos=servo_pos+10
    elif inp=='6':
        servo_pos=servo_pos-10
    elif inp=='5':
        servo_pos=90
    elif inp =='q':
        from radar import *
   
    if servo_pos>180:
        servo_pos=180
    if servo_pos<0:
        servo_pos=0
        
    servo(servo_pos)        
    time.sleep(.1)  
