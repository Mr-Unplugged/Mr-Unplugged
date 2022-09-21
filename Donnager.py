room1_waitTracker = 0
if room1_waitTracker == 2: 
    print("You can no longer breath and relise that you've waited too long")

print('''
          -= Wecome to Donnager =-

                  __|__
                   _|_
                  |   |
               __/ (_) \__
          ____/_ ======= _\____
 ________/ _ \(_)_______(_)/ _ \________
<___+____ (_) | /   _   \ | (_) ____+___>
  O O O  \___/ |   (_)   | \___/  O O O
             \__\_______/__/

            by Slightly Toasted

''')

#darkroom
print("You wake up in a dark room. The floor shakes beneath you. You must escape the ship.")
choice1 = input("What do you do? Type 'wait' or 'explore'. :").lower()
if choice1 == "explore":
    print("You explore and find a door...")
    choice2 = input('What do you do? Type "Open" or "Listen". :').lower()
    if choice2 == "listen":
        print("You Listen and hear someone running down the hall. Eventually, it is quiet and you enter the hallway.")

        #hallway
        choice3 = input('The hallway is well lit but it is filling with smoke. What do you do? Type “Look” or “Crawl”. :').lower()
        if choice3 == "crawl":
            print("You crawl and come across a bathroom with the door open. Just then you hear someone running down the hall in front of you.")
            choice4 = input('What do you do? “Hide” in the bathroom or “Ambush” the individual. :').lower()
            if choice4 == "hide":

                # bathroom
                print("You hide in the bathroom. Someone approaches the door and knocks, demanding entrance.")
                choice5 = input('What do you do? “Scream” like you need more fiber in your diet, or remain “silent”. :').lower()
                if choice5 == "scream":
                    print("You scream like it hurts. The guard comments about adding fiber in your diet and then runs off. You open the door and see a hatch for an escape pod.")
                    choice6 = input('What do you do? You can “enter” the escape pod or you can “wait” like an idiot for the ship to blow up. :').lower()
                    if choice6 == "enter":

                        #escapepod
                        print("You jump into the pod, and launch yourself into space. You loiter in space for 2 weeks before dying of dehydration. Its space, no one survives in space.")

                        #death
                    else: 
                        print("You opt to wait because why not? Whats the point anyway… You blow up and die.")
                else: 
                    print("You remain silent and the guard shoots through the door. You die on the toilet, congrats.")
            else:
                print("You try to ambush the individual and find out that they have a gun, and that gun is used to kill you. You are dead. ")
        else: 
            print("You stand still and try to peer through the smoke, but eventually you begin to cough due to the smoke. You soon die.")
    else:
        print("You open the door and are greeted with a guard and his gun. He shoots you and you die.")
else:
    print("You wait, but eventually you cannot breathe and you die.")



