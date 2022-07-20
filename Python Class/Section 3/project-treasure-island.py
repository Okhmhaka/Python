print(''' _                                     _     _                 _
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|''')

print(''' _,-._
        ; ___ :           ,-----------------------------------.
    ,--' (. .) '--.__    |  Argh. Welcome to Treasure Island  |
  _;      |||        \   |   You'll not take me treasure      |
 '._,-----````=.____, "  |      It's hidden the island        |
   // / < o > |  # |     |      and you'll never find it      |
   (o)        \`- -'       //`---------------------------------'
  // /\ >>>> _\ << << //
 --._ >> >>>>>> << << << << /
 ___() >> >[| |||]<<<<
 `--'>>>>>>>> << << << <
      >>>>>> > << << <<
        >>>> > << << <
         >>ctr <<''')

print("************************************************************")
print("*                    INTRUCTIONS                           *")
print("*    THIS IS A CHOOSE YOUR ADVENTURE GAME AND YOU WILL     *")
print("*    BE ABLE TO DIRECT YOUR PATH BY THE ANSWERS YOU        *")
print("*    YOU GIVE TO THE SITUATION PRESENTED.  TO GET STARTED, *")
print("*    JUST FILL IN YOUR ADVENTURER NAME AND PRESS ENTER.    *")
print("*    YOU MUST BE CAREFUL THOUGH.  THERE ARE ROOMS OF FIRE, *")
print("*    BEASTS, FAKE DOORS, AN ANGRY TROUT, AND CLIFFS TO     *")
print("*    FALL FROM.  CHOOSE YOUR ANSWERS WISELY, YOUR LIFE     *")
print("*    DEPENDS ON IT!!!                                      *")
print("*                                                          *")
print("************************************************************")

print("You arrive by ship to what appears to be a deserted island.")
print("After washing ashore, you grab your boat and pull it out of the water.")
print("Up ahead you notice a opening in the island vegetation and you decide to explore.")
print("After walking down the paht for some time you come to a crossroad.")
direction = input(
    "You have a choice to go left or right.\nWhich way do you go? ")

direction = direction.lower()

if direction == "left":
    print("You've come to a lake with a small island in the middle.")
    boat_swim = input("Should you wait for a boat or swim? ")
    boat_swim.lower()
    if boat_swim == "swim":
        print("You arrived at the island unharmed but tired.")
        print("There is a house with three doors.  One red, one yellow, and one blue.")
        color = input("which color door do you choose? ")
        color = color.lower()
        if color == "red":
            print("The room is a trap and full of fire!!  Game Over!")
        elif color == 'yellow':
            print("You found the treasure!  You win!")
        else:
            print("You enter a room of beasts and are eaten!  Game Over!")

    else:
        print("There is not boat on the island. You died to wild animals waiting on a boat. Game Over!")

else:
    print("You fell in a hole covered by vegetation.  Game Over")
