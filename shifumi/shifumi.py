import random

me = 0
cp = 0

choice_nbr_round = int(input('Choisi le nombre de tour : ')) 
nbr_round = 0

while nbr_round < choice_nbr_round:

    #aesthetic
    print(' ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    user_choice = input('Choisi entre -pierre- -feuille- et -ciseaux- : ')
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print(' ')

    if (user_choice == 'pierre' or user_choice == 'feuille' or user_choice == 'ciseaux' or user_choice == 'puit'):
        
        print('-------------------------------------')

        can_use = ['pierre','feuille','ciseaux']
        cp_choice = random.choice(can_use)

        print('Ton adversaire a choisi : ', cp_choice)

        if (user_choice == cp_choice):
            print('Ton adversaire a fais le même choix')

        elif (user_choice == 'pierre' and cp_choice == 'feuille'):
            print('Looser!')
            cp += 1
        elif (user_choice == 'pierre' and cp_choice == 'ciseaux'):
            print('T\'as dead ça !')
            me += 1
        elif user_choice == 'feuille' and cp_choice == 'pierre':
            print('GG bg !')
            me += 1
        elif user_choice == 'feuille' and cp_choice == 'ciseaux':
            print('Ton adversaire t\'as détruit !')
            cp += 1
        elif user_choice == 'ciseaux' and cp_choice == 'pierre':
            print('tié null frréroot !')
            cp += 1
        elif user_choice == 'ciseaux' and cp_choice == 'feuille':
            print('tié devin ou quoi ?!')
            me += 1
        elif user_choice == 'puit' and (cp_choice == 'pierre' or cp_choice == 'ciseaux'):
            print('OOOoh ti joues à quoi ma parole, fada va...')
            me += 1
        elif user_choice == 'puit' and cp_choice == 'feuille':
            print('Ti as essayé de triché là, je té vu, c\'est raté frérot !')
            cp += 1

        nbr_round += 1
        print('Manche numero ', nbr_round,' sur ', choice_nbr_round)
        print('Vous avez ', me, ' points')
        print('L\'ordi a ', cp, ' points')
        print('-------------------------------------')

    elif (user_choice == 'lezard' or user_choice == 'spock'):
        
        print('-------------------------------------')

        can_use = ['pierre','feuille','ciseaux','lezard','spock']
        cp_choice = random.choice(can_use)

        print('Ton adversaire a choisi: ', cp_choice)

        if (user_choice == cp_choice):
            print('Egalité !')
        elif (user_choice == 'lezard' and (cp_choice == 'pierre' or cp_choice == 'ciseaux')):
            print('T\'essaye de faire le malin, eh beh c perdu haha !')
            cp += 1
        elif (user_choice == 'lezard' and (cp_choice == 'feuille' or cp_choice == 'spock')):
            print('Bien ouaij frère !')
            me += 1
        elif (user_choice == 'spock' and (cp_choice == 'lezard' or cp_choice == 'feuille')):
            print('Perduuu cheh')
            cp += 1
        elif (user_choice == 'spock' and (cp_choice == 'pierre' or cp_choice == 'ciseaux')):
            print('T\'es un malin toi, bien joué, mais ne t\'avises surtout pas de recommencer')
            me += 1

        nbr_round += 1
        print('Manche numero ', nbr_round,' sur ', choice_nbr_round)
        print('Vous avez ', me, ' points')
        print('L\'ordi a ', cp, ' points')
        print('-------------------------------------')
    else:
        print('Qu\'est-ce que tu racontes, je ne comprend pas...')

if(me > cp):
    print('----Partie finie sur une victoire ! (/°O°)/----')
elif(cp > me):
    print('----Partie finie sur une défaite ! (,.ỗ~ỗ),----')
else:
    print('----Partie finie sur une égalitée (~_~¨)----')
