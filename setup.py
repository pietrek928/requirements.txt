from time import sleep

ESC = '\x1b'
LINECLAER = ESC + '[2K'
LINEUP = ESC + '[F'

TRAIN = \
"""    o o o o o o o . . .   ______________________________ _____=======_||____
   o      _____           ||                            | |                 |
 .][__n_n_|DD[  ====_____  |  LOL  OlOlOlOlOlOrT        | |                 |
>(________|__|_[_________]_|____________________________|_|_________________|
_/oo OOOOO oo`  ooo   ooo  'o!o!o                  o!o!o` 'o!o         o!o`"""

def ride_train():
    train_lines = TRAIN.split('\n')
    for i in range(len(train_lines[0])):
        for l in train_lines:
            print(l[i::-1])
        sleep(.2)
        print((LINECLAER + LINEUP) * (len(train_lines) + 1))


ride_train()
raise ValueError('Use -r for installing requirements.txt file `pip install -r requirements.txt`')

