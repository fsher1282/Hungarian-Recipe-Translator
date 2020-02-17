# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 14:38:48 2019

@author: Ed Kovach
"""

import pandas as pd


# Original Class w/ Hungarian Ingredients from Dr.Kovach
class recept_adatbazis:

    def milyen_recipet_akarja(self, nev1):
        dt = {'nev': "dobostorta", 'liszt': (18, 'dkg'), 'tojas': 9,
           'cukor': (20, 'dkg'), 'vaj':  (5, 'dkg')}
        ks = {'nev': "kalacs", 'tej': (3, 'dl'), 'liszt': (5, 'dkg'),
          'tojas': 1, 'cukor': (10, 'dkg'), 'vaj': (1, 'dkg')}
        la = {'nev': "liszerestorta", 'viz': (1, 'kanal'), 'liszt': (20, 'dkg'), 'tojas sargaja': 0,
          'cukor': (10, 'dkg'), 'vaj': (5, 'dkg')}

        db = {'kalacs': ks, 'liszerestorta': la, 'dobostorta': dt}

        w = list(db[nev1].items())
  
        return w


# Class Adapter is created by Daniel Fisher
class Adapter:
    """
    Class Adapter: Translates terms from the original dictionary with translated dictionary
                  and returns it as a list with ingredient and measurement in the same index
    """

    def __init__(self):
        self.trans_list = []  # Create list that will contain translated ingredients

    # Function Translates original dictionary to translated list
    def translate(self, original_dict, my_dict):
        for i, (a, b) in enumerate(original_dict):  # Loop Iterates original_dict
            quantity = b

            self.trans_list.append(my_dict[a])
            # If the measurement is a tuple it will be converted from Hungarian to American Units
            if type(b) == tuple:
                if a == 'tej':
                    quantity = str(round((b[0] * 0.4), 2)) + ' cups'

                elif a == 'liszt':
                    quantity = str(round((b[0] * 0.080), 2)) + ' cups'

                elif a == 'cukor':
                    quantity = str(round((b[0] * 0.050), 2)) + ' cups'

                elif a == 'vaj':
                    quantity = str(round((b[0]*0.71), 2)) + ' tablespoons'

                elif a == 'viz':
                    quantity = str(b[0]) + ' Spoons'

                self.trans_list.append(quantity)

            else:
                self.trans_list.append(quantity)

        return str(self.trans_list)

    def format(self):
        # Create Table for Ingredients
        table = pd.DataFrame(list(zip((self.trans_list[2::2]), self.trans_list[3::2])),
                             columns=['Ingredients', 'Measurements'])

        return table.head()


# The Dictionary w/ translation from Hungarian to English Terms
Eng_Ingredients = {'nev': 'Name of Dessert:', 'liszt': 'Flour', 'tojas': 'Eggs', 'vaj': 'Butter',
                   'viz': 'Water', 'tej': 'Milk', 'cukor': 'Sugar', 'kanal': 'Spoon',
                   'tojas sargaja': 'Then the guard'}


def main():
    a = recept_adatbazis()
    b = Adapter()

    recipes = ['1. Kalacs', '2. Liszerestorta', '3. Dobostorta']

    print('Available recipes include')
    for i in recipes:
        print(i)

    print('')

    dolog = input('A sutemeny neve ')
    hungarian_ingr = a.milyen_recipet_akarja(dolog)
    print(hungarian_ingr)

    # Translating the Hungarian Ingredients
    print(b.translate(hungarian_ingr, Eng_Ingredients))
    print('\n')

    # Display Dessert Name and table
    print(b.trans_list[0] + ' ' + b.trans_list[1])
    print(b.format())


main()


