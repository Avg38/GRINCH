import random

me = 0
cp = 0

choice_nbr_round = int(input('How many round ? '))
nbr_round = 0

while nbr_round < choice_nbr_round:

    user_choice = input('Choisi entre -pierre- -feuille- et -ciseaux- ')
    if (user_choice == 'pierre' or user_choice == 'feuille' or user_choice == 'ciseaux'):
        print('-------------------------------------')

        can_use = ['pierre','feuille','ciseaux']
        cp_choice = random.choice(can_use)

        print('L\'ia a choisi : ', cp_choice)

        if (user_choice == cp_choice):
            print('Egalitée')

        elif (user_choice == 'pierre' and cp_choice == 'feuille'):
            print('L\'ordi gagne !')
            cp += 1
        elif (user_choice == 'pierre' and cp_choice == 'ciseaux'):
            print('Vous avez gagné !')
            me += 1
        elif user_choice == 'feuille' and cp_choice == 'pierre':
            print('Vous avez gagné !')
            me += 1
        elif user_choice == 'feuille' and cp_choice == 'ciseaux':
            print('L\'ordi gagne !')
            cp += 1
        elif user_choice == 'ciseaux' and cp_choice == 'pierre':
            print('L\'ordi gagne !')
            cp += 1
        elif user_choice == 'ciseaux' and cp_choice == 'feuille':
            print('Vous avez gagné !')
            me += 1

        nbr_round += 1
        print('Manche numero ', nbr_round,' sur ', choice_nbr_round)

        print('Vous avez ', me, ' points')
        print('L\'ordi a ', cp, ' points')

    else:
        print('Je ne comprend pas...')

if(me > cp):
    print('----Partie finie sur une victoire ! (/°O°)/----')
elif(cp > me):
    print('----Partie finie sur une défaite ! (,.ỗ~ỗ),----')
else:
    print('----Partie finie sur une égalitée (~_~¨)----')
