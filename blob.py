import time #Imports a module to add a pause

#Figuring out how users might respond
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]

#Grabbing objects
gunk = 0
flashlight = 0

required = ("\nYou can only choose option A, B, or C\n") #Cutting down on duplication
required2 = ("\nYou can only choose option A or B\n")

def learn_more():
  print ("""
  You are at the beach.
  Everything is calm.
  Then all the water retracts.
  Then a slow slimmy white blob is coming to you\n\n""")
  time.sleep(1)
  choice2 = input("""
    A. You wait
    B. You Run
    C. Approach the Blob\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        blobShadow()
  elif choice2 in answer_B:
        at_facility()
  elif choice2 in answer_C:
        print ("\nGo on living with your head under a rock. "
        "\n\nBut don't come crying to me when darkness finds you.\n") ##NOT DONE
        raise SystemExit
  else:
        print(required)
        time.sleep(0.5)
        learn_more()
    #option_rock()

def blobShadow():
    print ("""
    The blob gets closer and its shadow is cast upon you.
    The white blob becomes an unscalable 20ft wall coming even closer to you.\n\n""")
    time.sleep(1)
    choice2 = input("""
    A. You wait
    B. You Run
    C. Approach the Blob\n
    >>> """)
    print("\n")
    if choice2 in answer_A:
        print("The blob consumes you and your thoughts. You are the blob and the blob is you.")
        raise SystemExit
    elif choice2 in answer_B:
        print("As you run away, the the blob collapses and some its slimy white substance affixes lands on you. \nNonetheless, you make it out.\n")
        gunk = 1
        at_facility()
    elif choice2 in answer_C:
        print ("\nAs your skin makes contact with the blob, it becomes part of the blob. As all the lipids and proteins in your body are transformed into this eery substance of white. You enjoy this organic transfer. You are euphoric. You plunge yourself into the blob. You are now the blob\n")
        raise SystemExit
    else:
        print(required)
        time.sleep(0.5)
        blobShadow()

def at_facility():
  print ("""You make it to the main beach facility, a shuttle ride away from the shore.\n\n""")
  time.sleep(1)
  choice2 = input("""
  A. Take a shower
  B. Use your phone to check the news
  C. Meet up with the rest of the survivors\n
  >>> """)
  print("\n")
  if choice2 in answer_A:
        tookShower()
  elif choice2 in answer_B:
        checkNews()
  elif choice2 in answer_C:
        meetSurvivors()
  else:
        print(required)
        time.sleep(0.5)
        at_facility()

def tookShower():
    print("""
    You took a nice shower and removed all the white gunk from your body.

    When you try to check your phone, you realize the internet is not available
    """)
    gunk = 0
    afterShower()


def checkNews():
  time.sleep(1)
  choice2 = input("""
    A. Go on Breitbart
    B. Go on Twitter
    C. Go on Apple News\n
    >>> """)
  print("\n")
  if choice2 in answer_A:
        print("You discover the yogurt is a chinese special weapons program. Before you try to acess another site, the internet cuts out.")
        afterShower()
  elif choice2 in answer_B:
        print("You discover the yogurt is another side effect of global warming. Before you try to acess another site, the internet cuts out.")
        afterShower()
  elif choice2 in answer_C:
        print("You discover the yogurt is sentient and possibly our first encounter with extra-terrestrial life. Before you try to acess another site, the internet cuts out.")
        afterShower()
  else:
        print(required)
        time.sleep(0.5)
        checkNews()

def afterShower():
  time.sleep(1)
  choice2 = input(""" With no internet, you
    A. Meet up with the other survivors
    B. Head inland
    >>> """)
  if choice2 in answer_A:
        meetSurvivors()
  elif choice2 in answer_B:
        print("You discover the yogurt is another side effect of global warming. Before you try to acess another site, the internet cuts out.")
        inland()
  else:
        print(required2)
        time.sleep(0.5)
        afterShower()

def meetSurvivors():
  time.sleep(1)
  choice2 = input(""" The leader of the survivors informs you that help is on the way and you must remain put until the military evac.\n\n\n
    A. Join the survivors and wait for the chopper
    B. Leave the survivors and head inland\n
    >>> """)
  if choice2 in answer_A:
          time.sleep(1)
          print("\n\n")
          choice2 = input(""" You are very hungry and you are offered food while you wait for the chopper.\n\n\n
    A. Accept the food
    B. You politely tell them "no thank you"\n
    >>> """)
          if choice2 in answer_A:
            eatFood()
          elif choice2 in answer_B:
            time.sleep(1)
            print("\n\n")
            choice2 = input("""The leader insists that you have some of the food as you are very famished from today's ordeal.\n\n\n
    A. Accept the food
    B. You politely tell them again "no thank you"\n
    >>> """)
            if choice2 in answer_A:
                        eatFood()
            elif choice2 in answer_B:
                        time.sleep(1)
                        print("\n\n")
                        choice2 = input("""This offer is becoming more of a demand and you begin to feel uncomfortable as all of the survivors begin to pressure you to have some of the food.\n\n\n
    A. Accept the food
    B. You politely tell them again "no thank you"
    C. Leave and head inland\n
    >>> """)
                        if choice2 in answer_A:
                          eatFood()
                        elif choice2 in answer_B:
                          time.sleep(1)
                          print("\n\n")
                          choice2 = input("""
    The survivors begin to surround you.
    You realize you have two choices.\n\n
    A. Accept the food
    B. Run\n
    >>> """)
                        if choice2 in answer_A:
                          eatFood()
                        elif choice2 in answer_B:
                          time.sleep(1)
                          print("\n\n")
                          print("You run to the door.\nThe door is locked.\nWithout any other option you hurl yourself through the window, falling two stories.\nYou make it out and head inland.")
                          inland()
  elif choice2 in answer_B:
        inland()
  else:
        print(required2)
        time.sleep(0.5)
        learn_more()

def eatFood():
  time.sleep(1)
  print("""
  Upon your first bite you notice the food was of an odd consistency.
  It looked normal appearing to be a hamburger and fries.
  But it felt mushy and somewhat sweet.
  You look again and the hamburger was no more.
  It was a white blob,
  and it was delicious
  You feel compelled to consume it entirely and all of the other treats available.

  Now you and the others wait for the next survivor.""")
  raise SystemExit

def inland():
  print("\n\nUpon reaching the inland city.\nIt is in a state of chaos.\nRiots. Gunfire. Looting.\nYou can either")
  time.sleep(.5)
  choice2 = input("""
    A. Find more information
    B. Get food
    C. Join the Riots\n
    >>> """)
  if (gunk == 1):
    print("You clutch your leg.\nThe gunk that landed on you earlier has grown.\nYour whole leg is in pain.\nYou collapse.\nOn the ground you remain until the blob reaches you yet again.")
    raise SystemExit
  elif (choice2 in answer_A) or (choice2 in answer_B) or (choice2 in answer_C):
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("\n")
    time.sleep(1)
    print("You got shot")
    raise SystemExit
  else:
        print(required2)
        time.sleep(0.5)
        learn_more()



#This is where you call all the functions so they run
learn_more()
appointment()
coffeeshop()
