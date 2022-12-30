# Test
def turn_left():
    False


def turn_right():
    turn_left()
    turn_left()
    turn_left()


# Need to check of there is a wall in front of the robot.
while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else turn_left()
