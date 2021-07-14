from random import randint # allows you to generate a random number
alive = True
stamina = 10

def report(stamina):
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    elif stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    elif stamina > 3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    elif stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")

# main function - accepts your input for fight with the alien
def fight(stamina): # stamina
    while stamina < 0:
        response = input("> Enter a move 1.Hit 2.attack 3.fight 4.run")
        if "hit" in response or "attack" in response:
            less = randint(0, stamina)
            print(less)
            stamina -= less # subtract random int from stamina
            report(stamina) # see function above
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run."),
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            report(stamina)
            return True
    return False

print ("A threatening alien wants to fight ,yes/no")
alive=fight(stamina)

if alive==True: # means if alive == True
    print ("The alien lives on, and you, sadly, do not")
else:
    print ("The alien has been vanquished,Good work!") 

