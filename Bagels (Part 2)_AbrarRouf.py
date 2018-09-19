# Abrar Rouf
# CS 100 2017F Section H01
# Bagels (Part 2), Nov 13, 2017


def bagels_test(rand_num):
    bagel_count = 0
    pico_count = 0
    fermi_count = 0
    rtn_list = ['', '', '']
    print('This is a test case trial. The "random number" is 456. \nStart with any combination of integers that are NOT'
          ' 456 and continue the game according to the clues given. All clues will prove to be correct.')
    user_guess = input('Please input a 3-digit integer. Include any zeroes.\n')
    while user_guess != rand_num:
        for i in range(len(user_guess)):
            if user_guess[i] == rand_num[i]:
                fermi_count += 1
                rtn_list[i] = 'Fermi'
            elif user_guess[i] in rand_num:
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


bagels_test('456')
"""Play game and hints should show up as correct."""


import random


def bagels_game():
    rand = str(random.randint(0, 999))
    rand_zeroes = rand.zfill(3)
    bagel_count = 0
    pico_count = 0
    fermi_count = 0
    guess_count = 0
    success_count = 0
    rtn_list = ['', '', '']
    digits = '3456789'
    user_guess = '012'
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
        if rtn_list == ['', '', '']:
            print('Bagels, no correct digits.')
            user_guess = digits[:4]
            guess_count += 1
            bagel_count = 0
            if guess_count == 2:
                user_guess = digits[4:7]
            continue
        elif rtn_list == ['Pico', '', ''] or rtn_list == ['', 'Pico', ''] or rtn_list == ['', '', 'Pico']:
            for element in rtn_list:
                if element == '':
                    rtn_list.remove(element)

                    pass
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