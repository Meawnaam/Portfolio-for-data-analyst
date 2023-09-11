import random as rd
import pandas as pd


def pyc_game() :
    win = 0
    lose = 0
    draw = 0
    sign = ["paper", "hammer", "scissor"]
    key = [0, 1, 2]
    pyc = pd.DataFrame({"key" : key,
                        "sign" : sign})

    user_name = input("What is your name? : ")
    while True :
    # greeting
        print(f"Hi! {user_name} I\'m pao ying chub game.\n")
        print("Press 1 to play game\n")
        print("Press 2 to quit\n")
        user_press = input("Play or quit? : ")

        if (user_press == "1") :
            while True :
                print("Bot choose XXX\n")
                print(pyc.to_string(index = False))
                user_choose = int(input("What do you want to choose ? 0, 1, 2 or 3 to get back?: "))
                user_choose_sign = pyc[pyc["key"]== user_choose]["sign"].to_string(index = False)
                print(f"You have choosed {user_choose_sign}. \n")
                bot_choose = rd.choice(sign)
                print(f"Bot has choosed {bot_choose}. \n")

                if (user_choose in key) :
                    # Win loop
                    if (user_choose_sign == "paper" and bot_choose == "hammer" or \
                        user_choose_sign == "hammer" and bot_choose == "scissor" or\
                        user_choose_sign == "scissor" and bot_choose == "paper") :
                        print("You win! \n")
                        win +=1
                        print(f"Win : {win} \n")
                        print(f"Lose : {lose} \n")
                        print(f"Draw : {draw} \n")

                    # Draw loop
                    elif (user_choose_sign == bot_choose) :
                        print("Draw! \n")
                        draw +=1
                        print(f"Win : {win} \n")
                        print(f"Lose : {lose} \n")
                        print(f"Draw : {draw} \n")

                    # Lose loop
                    elif (user_choose_sign == "hammer" and bot_choose == "paper" or \
                        user_choose_sign == "scissor" and bot_choose == "hammer" or\
                        user_choose_sign == "paper" and bot_choose == "scissor") :
                        print("You lose! \n")
                        lose +=1
                        print(f"Win : {win} \n")
                        print(f"Lose : {lose} \n")
                        print(f"Draw : {draw} \n")

                elif (user_choose == "3") :
                    break

                else :
                    print("Invalid input X!")
        elif (user_press == "2") :
            break

        else :
            print("Invalid Input!")






