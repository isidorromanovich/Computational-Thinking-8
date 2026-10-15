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
          # you got 15 points
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 2s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 4s":
          # you got 15 points
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 4s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 5s":
        # you got 15 points
        points += 15
    input ("Would you like to pass")
    if answer3 == "four 5s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 6s":
          # you got 15 points
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 6s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 7s":
          # you got 15 points
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 7s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 8s":
          # you got 15 points
          points += 15
    input ("Would you like to pass")
    if answer3 == "four 8s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 9s":
         # you got 15 points
         points += 15
    input ("Would you like to pass")
    if answer3 == "four 9s":
          # you got 20 points
          points += 20
    input ("Would you like to pass")
    if answer3 == "three 10s":
          # you got 30 points
          points += 30
    input ("Would you like to pass")
    if answer3 == "four 10s":
          # you got 40 points
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Js":
      # you got 30 points
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Js":
          # you got 40 points
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Qs":
          # you got 30 points
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Qs":
          # you got 40 points
          points += 40
    input ("Would you like to pass")
    if answer3 == "three Ks":
          # you got 30 points
          points += 30
    input ("Would you like to pass")
    if answer3 == "four Ks":
          # you got 40 points
          points += 40
    input ("Would you like to pass")
    if answer3 == "three As":
          # you got 45 points
          points += 45
    input ("Would you like to pass")
    if answer3 == "four As":
          # you got 60 points
          points += 60
    input ("Would you like to pass")
    if answer3 == "Ah 2h 3h":
          # you got 25 points
          points += 25
          input ("Would you like to pass")     
    if answer3 == "Ah 2h 3h 4h":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "Ah 2h 3h 4h 5h":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "Ah 2h 3h 4h 5h 6h":
            # you got 40 points
            points += 40
            input ("Would you like to pass")
    if answer3 == "Ah 2h 3h 4h 5h 6h 7h":
            # you got 45 points
            points += 45
            input ("Would you like to pass")
    if answer3 == "2h 3h 4h":
            # you got 15 points
            points += 15
            input ("Would you like to pass")
    if answer3 == "2h 3h 4h 5h":
            # you got 20 points
            points += 20
            input ("Would you like to pass")
    if answer3 == "2h 3h 4h 5h 6h":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "2h 3h 4h 5h 6h 7h":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "2h 3h 4h 5h 6h 7h 8h":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "3h 4h 5h":
            # you got 15 points
            points += 15
            input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h":
            # you got 20 points
            points += 20
            input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h 8h":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h 8h 9h":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "4h 5h 6h":
            # you got 15 points
            points += 15
            input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h":
             # you got 20 points
             points += 20
             input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h 9h":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h 9h 10h":
            # you got 40 points
            points += 40
            input ("Would you like to pass")
    if answer3 == "5h 6h 7h":
            # you got 15 points
            points += 15
            input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h":
            # you got 20 points
            points += 20
            input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h 10h":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h 10h Jh":
            # you got 45 points
            points += 45
            input ("Would you like to pass")
    if answer3 == "6h 7h 8h":
            # you got 15 points
            points += 15
            input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h":
            # you got 20 points
            points += 20
            input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h Jh":
            # you got 40 points
            points += 40
            input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h Jh Qh":
            # you got 50 points
            points += 50
            input ("Would you like to pass")
    if answer3 == "7h 8h 9h":
            points += 15
            # you got 15 points
            input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh Qh":
            # you got 45 points
            points += 45
            input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh Qh Kh":
            # you got 55 points
            points += 55
            input ("Would you like to pass")
    if answer3 == "8h 9h 10h":
            # you got 20 points
            points += 20
            input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh":
            # you got 40 points
            points += 40
            input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh Kh":
            # you got 50 points
            points += 50
            input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh Kh Ah":
            # you got 65 points
            points += 65
            input ("Would you like to pass")
    if answer3 == "9h 10h Jh":
            # you got 25 points
            points += 25
            input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh":
            # you got 35 points
            points += 35
            input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh Kh":
            # you got 45 points
            points += 45
            input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh Kh Ah":
            # you got 60 points
            points += 60
            input ("Would you like to pass")
    if answer3 == "10h Jh Qh":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "10h Jh Qh Kh":
            # you got 40 points
            points += 40
            input ("Would you like to pass")
    if answer3 == "10h Jh Qh Kh Ah":
            # you got 55 points
            points += 55
            input ("Would you like to pass")
    if answer3 == "Jh Qh Kh":
            # you got 30 points
            points += 30
            input ("Would you like to pass")
    if answer3 == "Jh Qh Kh Ah":
            # you got 45 points
            points += 45
            input ("Would you like to pass")
    if answer3 == "Qh Kh Ah":
            # you got 35 points
            points += 35
    if answer3 == "Ad 2d 3d":
                # you got 25 points
                points += 25
                input ("Would you like to pass")     
    if answer3 == "Ad 2d 3d 4d":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "Ad 2d 3d 4d 5d":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "Ad 2d 3d 4d 5d 6d":
                  # you got 40 points
                  points += 40
                  input ("Would you like to pass")
    if answer3 == "Ad 2d 3d 4d 5d 6d 7d":
                  # you got 45 points
                  points += 45
                  input ("Would you like to pass")
    if answer3 == "2d 3d 4d":
                  # you got 15 points
                  points += 15
                  input ("Would you like to pass")
    if answer3 == "2d 3d 4d 5d":
                  # you got 20 points
                  points += 20
                  input ("Would you like to pass")
    if answer3 == "2d 3d 4d 5d 6d":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "2d 3d 4d 5d 6d 7d":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "2h 3h 4h 5h 6h 7h 8h":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "3h 4h 5h":
                  # you got 15 points
                  points += 15
                  input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h":
                  # you got 20 points
                  points += 20
                  input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h 8h":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "3h 4h 5h 6h 7h 8h 9h":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "4h 5h 6h":
                  # you got 15 points
                  points += 15
                  input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h":
                   # you got 20 points
                   points += 20
                   input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h 9h":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "4h 5h 6h 7h 8h 9h 10h":
                  # you got 40 points
                  points += 40
                  input ("Would you like to pass")
    if answer3 == "5h 6h 7h":
                  # you got 15 points
                  points += 15
                  input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h":
                  # you got 20 points
                  points += 20
                  input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h 10h":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "5h 6h 7h 8h 9h 10h Jh":
                  # you got 45 points
                  points += 45
                  input ("Would you like to pass")
    if answer3 == "6h 7h 8h":
                  # you got 15 points
                  points += 15
                  input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h":
                  # you got 20 points
                  points += 20
                  input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h Jh":
                  # you got 40 points
                  points += 40
                  input ("Would you like to pass")
    if answer3 == "6h 7h 8h 9h 10h Jh Qh":
                  # you got 50 points
                  points += 50
                  input ("Would you like to pass")
    if answer3 == "7h 8h 9h":
                  points += 15
                  # you got 15 points
                  input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh Qh":
                  # you got 45 points
                  points += 45
                  input ("Would you like to pass")
    if answer3 == "7h 8h 9h 10h Jh Qh Kh":
                  # you got 55 points
                  points += 55
                  input ("Would you like to pass")
    if answer3 == "8h 9h 10h":
                  # you got 20 points
                  points += 20
                  input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh":
                  # you got 40 points
                  points += 40
                  input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh Kh":
                  # you got 50 points
                  points += 50
                  input ("Would you like to pass")
    if answer3 == "8h 9h 10h Jh Qh Kh Ah":
                  # you got 65 points
                  points += 65
                  input ("Would you like to pass")
    if answer3 == "9h 10h Jh":
                  # you got 25 points
                  points += 25
                  input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh Kh":
                  # you got 45 points
                  points += 45
                  input ("Would you like to pass")
    if answer3 == "9h 10h Jh Qh Kh Ah":
                  # you got 60 points
                  points += 60
                  input ("Would you like to pass")
    if answer3 == "10h Jh Qh":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "10h Jh Qh Kh":
                  # you got 40 points
                  points += 40
                  input ("Would you like to pass")
    if answer3 == "10h Jh Qh Kh Ah":
                  # you got 55 points
                  points += 55
                  input ("Would you like to pass")
    if answer3 == "Jh Qh Kh":
                  # you got 30 points
                  points += 30
                  input ("Would you like to pass")
    if answer3 == "Jh Qh Kh Ah":
                  # you got 45 points
                  points += 45
                  input ("Would you like to pass")
    if answer3 == "Qh Kh Ah":
                  # you got 35 points
                  points += 35
                  input ("Would you like to pass")
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
                            if "yes" and "No":
                                    print ("You did both yes and no awnsers")
                                    
                    else:
                            print ("uh that's not how yoy play this game you have to do yes or no")
        else:
                print ("uh that's not how you play this game you have to do yes or no")
    else:
        print ("uh that's not how you play this game you have to do yes or no")
else:
    print ("uh that's not how you play this game you have to do yes or no")