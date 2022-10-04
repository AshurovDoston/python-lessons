from itertools import count
import random as r

def son_top(x):
    son = r.randint(1, x)
    print(son)
    my_count = 1
    guessed_numb = int(input(f"1 dan {x} gacha son o'yladim, topa olasizmi?\n>>> "))
    while guessed_numb != son:
        if son > guessed_numb:
            guessed_numb = int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling!\n>>> "))
        else:
            guessed_numb = int(input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling!\n>>> "))
        my_count += 1
    print(f"Men {son} sonini o'ylagan edim. {my_count} ta urinish bilan to'g'ri sonni topdingiz!")
    return my_count


def son_top_pc(y):
    print(f"1 dan {y} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Press Enter to continue...")
    low = 1
    high = y
    comp_count = 0
    while True:
        comp_count += 1
        comp_guess = r.randint(low, high)
        my_hint = input(f"Siz {comp_guess} sonini o'yladingiz."
        "To'gri (t), men o'ylagan son bundan kattaroq (+), kichikroq (-) \n>>> ".lower())
        if my_hint == '-':
            high = comp_guess - 1
        elif my_hint == '+':
            low = comp_guess + 1
        elif my_hint == 't':
            break
    print(f"Soningizni {comp_count} tahmin bilan topdim.")
    return comp_count


def play(x):
    again = True
    while again:
        counts_user = son_top(x)
        counts_pc = son_top_pc(x)

        if counts_user > counts_pc:
            print(f"Men {counts_pc} tahmin bilan topdim. \nYutdim!")
        elif counts_user < counts_pc:
            print (f"Siz {counts_user} tahmin bilan topdingiz. \nYutdingiz!")
        else:
            print("Durang bo'ldi!")
        again = int(input("Yana o'ynaysizmi? Ha(1)/ Yo'q(0): "))

play(20)