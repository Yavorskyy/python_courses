__author__ = 'andriy'
#Game
name1 = raw_input("Enter name for Player1:")
name2 = raw_input("Enter name for Player2:")


# next word
def game(count, a):
    while i:
        if (count>0) and (count%2) != 0:
            word1 = raw_input(name1 + " turn:")
        else:
            word1 = raw_input(name2 + " turn:")

        try:
            b = word1[0]
        except IndexError:
            if (count>0) and (count%2) != 0:
                print "Player 2 won!"
                break
            else:
                print "Player 1 won!"
                break

        if a == b:
            a = word1[-1]
            count +=1
            continue
        else:
            print "You must enter word starting with",a,"!"
            continue


i = 1
count = 0
word = raw_input("Player1 " + name1 + " turn:")

try:
    a = word[-1]
except IndexError:
    print "Player 2 won!"
else:
    game(count, a)




