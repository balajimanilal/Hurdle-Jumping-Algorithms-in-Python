def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

    
# Option 1    
move()
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_left()
jump()
jump()
jump()
jump()
jump()

# Option 2
for step in range(6):
    jump()

# Option 3
number_of_hurdles = 6
while number_of_hurdles > 0:
    jump()
    number_of_hurdles -= 1