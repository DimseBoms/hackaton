# Author: Dmitriy Safiullin, Artur Lobocki
import sys, time, threading

# Global variables for different print speeds to simulate speech
# as well as a timer to use in between dialogue
time_fast = 0.08
time_slow = 0.2
time_wait = 2
time_halt = 6

# Reusable for loop to print characters one by one at varying speeds
def speech(spk, speed):
    for character in spk:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(speed)

# Story paths
# Intro
def path_1():
    print("")
    print("You are standing in the middle of IKEA.")
    print("")
    time.sleep(time_wait)
    print("You suddenly feel a deep rumble coming from the depths of your bowels")
    print("")
    time.sleep(time_wait)
    spk = '"...Oh no.. Not now..."\n"...In the middle of Ikea..."\n"...I need to find a toilet..."'
    speech(spk, time_fast)
    print("")
    print("")
    time.sleep(time_wait)
    print("You find yourself at and intersection with three different choices.")
    print("")
    time.sleep(time_wait)
    print("\nTo your left you hear something topple over")
    print("")
    time.sleep(time_wait)
    print("In front of you there is a long-winded corridor")
    print("")
    time.sleep(time_wait)
    print("To your right you see nothing of interest")
    time.sleep(time_wait)
    print("")
    # Need to start timer_doom at this choice
    input_1 = input("Which path do you choose to go?\n1: To the left\n2: Straight ahead\n3: to the right\n(1/2/3): ")
    if input_1 == "1":
        path_1_1()
    elif input_1 == "2":
        path_2()
    elif input_1 == "3":
        path_3()

# Node 1_1 from the map. Here you meet the old lady
def path_1_1():
    print("")
    print("As you walk you suddenly see what made the noise from earlier")
    print("")
    time.sleep(time_wait)
    print("You can see an old lady laying flat beneath a pile of boxes")
    print("")
    time.sleep(time_wait)
    print("It looks like she was trying to reach something on top of the shelf")
    print("")
    time.sleep(time_wait)
    input_1_1 = input("What will you do?\n1: Help the lady (She might know where the toilet is)\n2: Continue straight ahead. Nature calls\n3: Go to the right\n(1/2/3): ")
    if input_1_1 == "1":
        conv_1_1()
    elif input_1_1 == "2":
        path_1_2()
    elif input_1_1 == "3":
        path_1_4()
    
# Node 1_2 here you slip and fall because of the milkshake
def path_1_2():
    print("")
    print("Oh no...")
    print("")
    time.sleep(time_wait)
    print("As you were running from the scene with the old lady you slip and fall cause of a milkshake spilled across the floor\n")
    print("")
    # Remove 1 min from timer_doom(If there is time to implent the timer at all)
    time.sleep(time_wait)
    print("You push on anyway. Nature calls")
    time.sleep(time_wait)
    path_1_3()

def path_1_3():
    print("")
    print("On your left you notice a seemingly brand new bathroom..")
    print("")
    time.sleep(time_wait)
    print("The toilet is squeaky clean...")
    print("")
    time.sleep(time_wait)
    print("On your right there is another way that continues onwards")
    print("")
    time.sleep(time_wait)
    input_1_3 = input("What will you do?\n1: Use the shiny porcelain throne to relieve yourself\n2: Continue on towards the right. This toilet seems too suspicious\n(1/2): ")
    if input_1_3 == "1":
        toilet_death()
    elif input_1_3 == "2":
        path_3()

# Møte med ansatt
def path_1_4():
    print("")
    print("As you are running away from the scene a worker captures your attention.")
    print("")
    time.sleep(time_wait)
    print("You get trapped by the sales man!")
    print("")
    time.sleep(time_wait)
    print("He will not stop trying to sell you this desk!")
    print("")
    time.sleep(time_halt)
    print("After some time he realizes that you aren\'t really interested and he let\'t you go")
    path_3()
    time.sleep(time_wait)
    path_3()


# Møte med dama
def path_2():
    print("")
    print("You meet a lady seemingly in distress")
    print("")
    time.sleep(time_wait)
    spk = '"Hello, sir have you seen my son?"'
    speech(spk, time_fast)
    print("\n")
    time.sleep(time_wait)
    spk = '"He is a 9 year old with a hat and a cute dog hoodie"'
    speech(spk, time_fast)
    time.sleep(time_wait)
    print("\n")
    print("it takes a while but you manage to pass her by. Nature can\'t wait")
    print("")
    time.sleep(time_wait)
    print("You must find the toilet")
    print("")
    time.sleep(time_wait)
    path_3()
    
# Direkte forbipassering
def path_3():
    print("")
    print('You come by an opening with a sign that says. "Toilet this way"')
    print("")
    time.sleep(time_wait)
    print("You suddenfly feel a rush of motivation to push on")
    print("")
    time.sleep(time_wait)
    print("You enter the opening")
    print("")
    time.sleep(time_halt)
    path_4()


def path_4():
    print("")
    print("You are standing at a fork in the road")
    time.sleep(time_wait)
    print("")
    print("You can go either left or right")
    time.sleep(time_wait)
    print("")
    print("The choice you make might seal your fate...")
    time.sleep(time_halt)
    print("")
    input_4 = input("Which path do you choose?\n\n1: the left\n2: the right \n(1/2): ")
    if input_4 == "1":
        path_4_1()
    elif input_4 == "2":
        path_5()

# You get hit by a shopping cart
def path_4_1():
    print("")
    print("Unfortunately, as you were walking along looking for a toilet...")
    print("")
    time.sleep(time_wait)
    print("A stressed shopper manages so slam his shopping cart straight in your stomach...")
    time.sleep(time_wait)
    print("")
    print("He slams you with such a force that")
    time.sleep(time_wait)
    print("")
    print("you poop so hard you not only rip your pants open")
    print("")
    time.sleep(time_wait)
    print("but you also end up covering the wall behind you in your own excrement")
    time.sleep(time_halt)
    print("")
    game_over()

# Final choice between a fake and a real toilet. Make sure the real toilet is portrayed real dingy
def path_5():
    print("")
    print("You have come a long way... You are now left with a final choice")
    time.sleep(time_wait)
    print("")
    print("On the left you see an amazingly clean, brand spanking new toilet")
    time.sleep(time_wait)
    print("")
    print("On the right you have a disgusting looking toilet. The walls leading to it are stained")
    time.sleep(time_wait)
    print("")
    input_5 = input("Which do you choose?\n1: Amazing looking toilet? \n2: Disgusting, stained toilet? \n(1/2): ")
    if input_5 == "1":
        toilet_death() # fake toilet
    elif input_5 == "2":
        toilet_win() # finish (win)

# Game over screen for fake toilet
def toilet_death():
    print("")
    print("You sit down on the toilet and relieve yourself...")
    print("")
    time.sleep(time_wait)
    print("But unfortunately for you this toilet was only for display...")
    print("")
    time.sleep(time_wait)
    print("This is Ikea after all")
    print("")
    time.sleep(time_wait)
    game_over()

# Winne situasjonen
def toilet_win():
    print("")
    print("############################################################")
    print("#                 Congratulations!!                        #")
    print("#                                                          #")
    print("#           You made it to the toilet!                     #")                  
    print("#                                                          #")
    print("# You have managed to excorcice all your excrement demons! #")
    print("############################################################")
    print("")
    
# Game Over node
def game_over():
    print("GAME OVER")
    input_game_over = input("Would you like to try again? (y/n): ").lower().strip()
    if input_game_over == "y":
        path_1()
    elif input_game_over == "n":
        print("See ya around")
        time.sleep(time_wait)
        exit()

# Conversation paths (-1 min on timer_doom)
def conv_1_1():
    print("")
    print("You help the lady out from under the pile of rubble")
    print("")
    time.sleep(time_wait)
    spk = ('"...Thanks, sonny..."\n"...Ah... A Toilet you say..."\n"...I think I saw a toilet further down this way..."\n"...It\'s just further down this way, and to the left..."\n"...Good luck!..."')
    speech(spk, time_slow)
    print("")
    time.sleep(time_wait)
    
    path_1_2()

# Introduction sequence
print()
print("##############################")
print("#                            #")
print("#        Nightmare in        #")
print("#            IKEA            #")
print("#                            #")
print("##############################")
print()
time.sleep(time_wait)

start_game = input("Would you like to play? (y/n)\n").lower().strip()
if start_game == 'n':
    print("Maybe some other time then")
elif start_game == 'y':
    path_1()
    
    