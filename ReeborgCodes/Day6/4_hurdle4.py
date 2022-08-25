def turn_right():
    turn_left()
    turn_left()
    turn_left()

def checkAndMoveWall():
    if not wall_on_right():
        turn_right()
        move() 
    elif wall_in_front():
        turn_left()       
    elif front_is_clear():
        move()   
        
while not at_goal(): 
    checkAndMoveWall()
        
        


