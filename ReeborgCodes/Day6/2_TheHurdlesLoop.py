def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def move_oneBlock():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for x in range(0,6):
    move_oneBlock()
