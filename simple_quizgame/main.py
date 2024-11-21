#Maisha Tapia Paredes, proficiency test

score = 0 
global question_1 , question_2 , question_3 , question_4, question_5


question_1 = input("Who is luigis nemisis? \n A. Mario \n B. Waluigi \n C. Egg guy \n D. Sonic ")
if question_1.lower() == "b":
    print("Correct")
    score += 1

elif question_1.lower() != "b":
    print("Nope!")
    score += 0
print(score)

question_2 = input("Which character in Super Smash Bros Ultamite has the same powers as princess peach? \n A. Donkey Kong \n B. Rosalina \n C. Daisy \n D. Toadette ")
if question_2.lower() == "c":
    print("Correct")
    score += 1

elif question_2.lower() != "c":
    print("Nope!")
    score += 0
print(score)

question_3 = input("A game was made where Wario and Waluigi first made appearances in nintendo, the theme of the game was a sport. Which sport?  \n A. Volleyball \n B. Football \n C. Lacrosse \n D. Tennis ")
if question_3.lower() == "d":
    print("Correct")
    score += 1

elif question_3.lower() != "d":
    print("wrong.")
    score += 0
print(score)

question_4 = input("What game does the nintendo character rosalina come from?  \n A. Super mario RPG \n B. Mario Party Superstars \n C. Mario galaxy  \n D. Mario kart 8 deluxe ")
if question_4.lower() == "c":
    print("Correct")
    score += 1

elif question_4.lower() != "c":
    print("No, thats not right!")
    score += 0

question_5 = input("""Which Mario brother marries princess peach? 
                   A. Luigi 
                   B. Wario
                   C. Mario
                   D. Mario 2.0 """)
if question_5.lower() == "d":
    print("Yep!")
    score += 1

elif question_5.lower() != "d":
    print("No, thats not right!")
    score += 0




