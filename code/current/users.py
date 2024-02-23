'''
    Program to generate a random member from a list of users,
    the members of the  default list can be removed or added
    to your convenience
'''
import random
import pickle
import os
# three of the modules used in the below code
g = os.getlogin()
PASS_FILENAME = 'Z:/Resources/development/random_members.data'

# gets the name of the computer


def adduser():
    '''
        function definition for adding users to the list
    '''
    while True:
        print(a)
        k = input('enter the name of the user(leave blank if none):')
        if k == '':
            break
        a.append(k)
        with open(PASS_FILENAME,
                  'wb') as fadduser:
            pickle.dump(a, fadduser)


def deluser():
    '''
        function definition for deleting users from the list
    '''
    while True:
        print(a)
        k = input('enter the name of the user(leave blank if none):')
        if k == '':
            break
        for item in range(0, len(a)):
            if k == a[item-1]:
                del a[item-1]
                with open(PASS_FILENAME,
                          'wb') as fdeluser:
                    pickle.dump(a, fdeluser)


if os.path.isfile(PASS_FILENAME) is not True:
    # checking if the data file is already present in the computer,
    # will make one if it is being run for the first time
    a = ['warun',
         'Morpheus3000',
         'coolpcguy',
         'David_007',
         'fatalevolution',
         'erif',
         '[xubz]',
         'GTX OC']
    # default list of members
    with open(PASS_FILENAME,
              'wb') as fmain:
        pickle.dump(a, fmain)
        # dumps the default list
else:
    # this block grabs the list from the data file
    with open(PASS_FILENAME,
              'rb') as fmain:
        a = pickle.load(fmain)

y = input('would you like to add more users to the list y/n or press d to '
          'delete users:')
if y == 'y':
    # block for adding users
    adduser()
    print(a)
    t = input('do you want to delete some users(y/n):')
    # provides one chance to remove some users
    if t == 'y':
        deluser()
        # function call to delete users
        print(f'and the random member is {random.choice(a)}')
    else:
        print(f'and the random member is {random.choice(a)}')
elif y == 'n':
    # quickest way to get an output
    print(f'and the random member is{random.choice(a)}')
elif y == 'd':
    deluser()
    print(a)
    t = input('do you want to add new users(y/n):')
    # provides one chance to add some users
    if t == 'y':
        adduser()
        # function call to add users
        print(f'and the random member is{random.choice(a)}')
    else:
        print(f'and the random member is{random.choice(a)}')
else:
    # this block is used if the input taken is unrecognisable however,
    # I need to figure out a way to get it back to the beginning
    print('unrecognisable command')
