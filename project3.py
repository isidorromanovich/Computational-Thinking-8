print ("When writing ♡ use 'h', then for ♤ use 's', for ♧ use 'c', and for ⟡ use 'd'")
discard = []
points = 0
import random
deck = ["A♡", "2♡", "3♡", "4♡", "5♡", "6♡", "7♡", "8♡", "9♡", "10♡", "J♡", "Q♡", "K♡","A♤", "2♤", "3♤", "4♤", "5♤", "6♤", "7♤", "8♤", "9♤", "10♤", "J♤", "Q♤", "K♤", "A♧", "2♧", "3♧", "4♧", "5♧", "6♧", "7♧", "8♧", "9♧", "10♧", "J♧", "Q♧", "K♧", "A⟡", "2⟡", "3⟡", "4⟡", "5⟡", "6⟡", "7⟡", "8⟡", "9⟡", "10⟡", "J⟡", "Q⟡", "K⟡"]
hand= random.sample (deck,7) 
print (hand)
answer1 = input ("Do you want to play anything?")
if answer1 == "yes" or answer1 == "Yes" or answer1 == " yes" or answer1 == " Yes":
    answer3 = input ("Type here what you want to play it has to be written like: [written out number of cards like three or the word set niether with a space before it] a space then [a number like 3 with a lower case s after it for three or more of a kind for a set write the set out like 3h 4h 5h with spaces between them but not before or after] note:A,J,Q,K has to be uper case ")

    if answer3 == "three 2s":
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 2s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 4s":
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 4s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 5s":
        points += 15
    input ("Would you like to pass")
    if answer3 == "four 5s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 6s":
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 6s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 7s":
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 7s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 8s":
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 8s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 9s":
         points += 15
    input ("Would you like to pass")
    if answer3 == "four 9s":
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 10s":
          points += 30
    input ("Would you like to pass")
    if answer3 == "four 10s":
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Js":
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Js":
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Qs":
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Qs":
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Ks":
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Ks":
          points += 40
    input ("Would you like to pass")
    if answer3 == "three As":
          points += 45
    input ("Would you like to pass")
    if answer3 == "four As":
          points += 60
    input ("Would you like to pass")
    if answer3 == "Ah 2h 3h":
          points += 25
          input ("Would you like to pass")
    if answer3 == "Ah 2h 3h":
      points += 25      
      if answer3 == "Ah 2h 3h 4h":
            points += 30
            input ("Would you like to pass")
      if answer3 == "Ah 2h 3h 4h 5h":
            points += 35
            input ("Would you like to pass")
      if answer3 == "Ah 2h 3h 4h 5h 6h":
            points += 40
            input ("Would you like to pass")
      if answer3 == "Ah 2h 3h 4h 5h 6h 7h":
            points += 45
            input ("Would you like to pass")
      if answer3 == "2h 3h 4h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "2h 3h 4h 5h":
            points += 20
            input ("Would you like to pass")
      if answer3 == "2h 3h 4h 5h 6h":
            points += 25
            input ("Would you like to pass")
      if answer3 == "2h 3h 4h 5h 6h 7h":
            points += 30
            input ("Would you like to pass")
      if answer3 == "2h 3h 4h 5h 6h 7h 8h":
            points += 35
            input ("Would you like to pass")
      if answer3 == "3h 4h 5h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "3h 4h 5h 6h":
            points += 20
            input ("Would you like to pass")
      if answer3 == "3h 4h 5h 6h 7h":
            points += 25
            input ("Would you like to pass")
      if answer3 == "3h 4h 5h 6h 7h 8h":
            points += 30
            input ("Would you like to pass")
      if answer3 == "3h 4h 5h 6h 7h 8h 9h":
            points += 35
            input ("Would you like to pass")
      if answer3 == "4h 5h 6h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "4h 5h 6h 7h":
             points += 20
             input ("Would you like to pass")
      if answer3 == "4h 5h 6h 7h 8h":
            points += 25
            input ("Would you like to pass")
      if answer3 == "4h 5h 6h 7h 8h 9h":
            points += 30
            input ("Would you like to pass")
      if answer3 == "4h 5h 6h 7h 8h 9h 10h":
            points += 40
            input ("Would you like to pass")
      if answer3 == "5h 6h 7h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "5h 6h 7h 8h":
            points += 20
            input ("Would you like to pass")
      if answer3 == "5h 6h 7h 8h 9h":
            points += 25
            input ("Would you like to pass")
      if answer3 == "5h 6h 7h 8h 9h 10h":
            points += 35
            input ("Would you like to pass")
      if answer3 == "5h 6h 7h 8h 9h 10h Jh":
            points += 45
            input ("Would you like to pass")
      if answer3 == "6h 7h 8h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "6h 7h 8h 9h":
            points += 20
            input ("Would you like to pass")
      if answer3 == "6h 7h 8h 9h 10h":
            points += 30
            input ("Would you like to pass")
      if answer3 == "6h 7h 8h 9h 10h Jh":
            points += 40
            input ("Would you like to pass")
      if answer3 == "6h 7h 8h 9h 10h Jh Qh":
            points += 50
            input ("Would you like to pass")
      if answer3 == "7h 8h 9h":
            points += 15
            input ("Would you like to pass")
      if answer3 == "7h 8h 9h 10h":
            points += 25
            input ("Would you like to pass")
      if answer3 == "7h 8h 9h 10h Jh":
            points += 35
            input ("Would you like to pass")
      if answer3 == "7h 8h 9h 10h Jh Qh":
            points += 45
            input ("Would you like to pass")
      if answer3 == "7h 8h 9h 10h Jh Qh Kh":
            points += 55
            input ("Would you like to pass")
      if answer3 == "8h 9h 10h":
            points += 20
            input ("Would you like to pass")
      if answer3 == "8h 9h 10h Jh":
            points += 30
      if answer3 == "8h 9h 10h Jh Qh":
            points += 40
      if answer3 == "8h 9h 10h Jh Qh Kh":
            points += 50
      if answer3 == "8h 9h 10h Jh Qh Kh Ah":
            points += 65
      if answer3 == "9h 10h Jh":
            points += 25
      if answer3 == "9h 10h Jh Qh":
            points += 35
      if answer3 == "9h 10h Jh Qh Kh":
            points += 45
      if answer3 == "9h 10h Jh Qh Kh Ah":
            points += 60
      if answer3 == "10h Jh Qh":
            points += 30
      if answer3 == "10h Jh Qh Kh":
            points += 40
      if answer3 == "10h Jh Qh Kh Ah":
            points += 55
      if answer3 == "Jh Qh Kh":
            points += 30
      if answer3 == "Jh Qh Kh Ah":
            points += 45
      if answer3 == "Qh Kh Ah":
            points += 35
elif answer1 == "no" or answer1 == "No" or answer1 == " no" or answer1 == " No":
    answer2 = input ("Would you like to pass then")
    if answer2 == "yes" or answer1 == "Yes" or answer1 == " yes" or answer1 == " Yes":
        print ("Hi")
    elif answer2 == "no" or answer1 == "No" or answer1 == " no" or answer1 == " No":
        answer1 = input ("Do you want to play anything than?")
        if answer1 == "yes" or answer1 == "Yes" or answer1 == " yes" or answer1 == " Yes":
                    input ("Type here what you want to play")

        elif answer1 == "no" or answer1 == "No" or answer1 == " no" or answer1 == " No":
                    print ("would you like to pass")
                    if answer2 == "yes" or answer1 == "Yes" or answer1 == " yes" or answer1 == " Yes":
                        print ("Hi")
                    elif answer2 == "no" or answer1 == "No" or answer1 == " no" or answer1 == " No":
                            # sorry you lost
                            print ("You made the same mistake twice if you cant play or don't want to than you pass")
                            print ("This counts as a forfeight")
                    else:
                            print ("uh that's not how yoy play this game you have to do yes or no")
        else:
                print ("uh that's not how you play this game you have to do yes or no")
    else:
        print ("uh that's not how you play this game you have to do yes or no")
else:
    print ("uh that's not how you play this game you have to do yes or no")