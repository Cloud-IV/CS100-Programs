# Abrar Rouf
# CS 100 2017F Section H01
# Bagels (Part 1), Nov 12, 2017

import random


def bagels_game():
    rand = str(random.randint(0, 999))
    rand_zeroes = rand.zfill(3)
    bagel_count = 0
    pico_count = 0
    fermi_count = 0
    rtn_list = ['', '', '']
    user_guess = input('Please input a 3-digit integer. Include any zeroes.\n')
    while user_guess != rand_zeroes:
        for i in range(len(user_guess)):
            if user_guess[i] == rand_zeroes[i]:
                fermi_count += 1
                rtn_list[i] = 'Fermi'
            elif user_guess[i] in rand_zeroes:
                pico_count += 1
                rtn_list[i] = 'Pico'
            else:
                bagel_count += 1
        if bagel_count == 3:
            print('Bagels, no correct digits.')
            user_guess = input('Try again! \n Please input a 3-digit integer. Include any zeroes.\n')
            bagel_count = 0
            continue
        elif pico_count == 1 and fermi_count == 0:
            print(rtn_list, '\n' + '%d digit correct but in the wrong place' % pico_count)
            user_guess = input('Try again!\nPlease input a 3-digit integer. Include any zeroes.\n')
            rtn_list = ['', '', '']
            pico_count = 0
            continue
        elif pico_count > 1 and fermi_count == 0:
            print(rtn_list, '\n' + '%d digits correct but in the wrong place' % pico_count)
            user_guess = input('Try again! \n Please input a 3-digit integer. Include any zeroes.\n')
            rtn_list = ['', '', '']
            pico_count = 0
            continue
        elif pico_count > 0 and fermi_count > 0:
            print(rtn_list, '\n' + '%d digits correct, but %d in the wrong place' % ((pico_count + fermi_count), pico_count))
            user_guess = input('Try again! \n Please input a 3-digit integer. Include any zeroes.\n')
            rtn_list = ['', '', '']
            pico_count = 0
            fermi_count = 0
            continue
        elif pico_count == 0 and fermi_count == 1:
            print(rtn_list, '\n' + '%d digit correct and in the right place' % fermi_count)
            user_guess = input('Try again! \n Please input a 3-digit integer. Include any zeroes.\n')
            rtn_list = ['', '', '']
            fermi_count = 0
        elif pico_count == 0 and fermi_count > 1:
            print(rtn_list, '\n' + '%d digits correct and in the right place' % fermi_count)
    print(['Fermi', 'Fermi', 'Fermi'], '\n' + 'Congratulations - you guessed correctly!')


bagels_game()
