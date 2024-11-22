#Maisha Tapia Paredes, proficiency test

score = 0 


question_1 = input("Who is luigis nemisis? \n A. Mario \n B. Waluigi \n C. Egg guy \n D. Sonic ")
if question_1.lower() == "b":
    print("Correct")
    score += 1

elif question_1.lower() != "b":
    print("Nope!")
    score += 0
    print(score)
    extra_question1 = input("What year was Nintendo founded?? \n A. 1890 \n B. 1550 \n C. 1988 \n D. 1989 ")
    if extra_question1.lower() == "d":
        print("Correct!")
        score += 1

    elif extra_question1.lower() != "d":
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
    extra_question2 = input("In what year did Nintendo become a public company?\n A. 1962 \n B. 1550 \n C. 1788 \n D. 1959 ")
    if extra_question2.lower() == "a":
        print("Correct!")
        score += 1

    elif extra_question2.lower() != "a":
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
    extra_question3 = input("Who is nintendos mascot?\n A. Princess peach \n B. 1989 luigi \n C. Just normal luigi and mario\n D. mario!")
    if extra_question3.lower() == "d":
        print("Correct!")
        score += 1

    elif extra_question3.lower() != "d":
        print("No..")
    score += 0
    print(score)


question_4 = input("What game does the nintendo character rosalina come from?  \n A. Super mario RPG \n B. Mario Party Superstars \n C. Mario galaxy  \n D. Mario kart 8 deluxe ")
if question_4.lower() == "c":
    print("Correct")
    score += 1

elif question_4.lower() != "c":
    print("No, thats not right!")
    score += 0
    extra_question4 = input("What was the first game released for the NES? \n A. Fun mario brothers \n B. Rainbow road \n C. Super Mario Bros \n D. EVR race ")
    if extra_question1.lower() == "c":
        print("Correct!")
        score += 1

    elif extra_question4.lower() != "c":
        print("Nope!")
    score += 0
    print(score)


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
    
    extra_question5 = input("What does the name Nintendo mean? \n A. The mario brothers in latin \n B. Game console \n C. Leave luck to heaven \n D. Happiness in the mundane")
    if extra_question5.lower() == "c":
        print("Correct!")
        score += 1

    elif extra_question5.lower() != "c":
        print("Nope!")
    score += 0
    print(score)



