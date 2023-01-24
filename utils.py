"""Utilities and constants."""


import hint as ht


# The tiles must be ordered in ascending order. If two tiles are of the same rank but of a different
# color, the black tile is placed to the left of the white tile (this is already reflected by the
# expression of tile rank/color over 20 elements). We note that the tile of rank 5 is neither black
# nor white (it is green).
# 0b = 0 | 2b = 4 | 4b = 8  | 6b = 12 | 8b = 16
# 0w = 1 | 2w = 5 | 4w = 9  | 6w = 13 | 8w = 17
# 1b = 2 | 3b = 6 | 5g = 10 | 7b = 14 | 9b = 18
# 1w = 3 | 3w = 7 | 5g = 11 | 7w = 15 | 9w = 19
TILES = ('0b', '0w', '1b', '1w',
         '2b', '2w', '3b', '3w',
         '4b', '4w', '5g', '5g',
         '6b', '6w', '7b', '7w',
         '8b', '8w', '9b', '9w')

HINTS = {'st': {'description': 'Sum of the tiles',
                'function': ht.hint_st},
         'sb': {'description': 'Sum of the black numbers',
                'function': ht.hint_sb},
         'sw': {'description': 'Sum of the white numbers',
                'function': ht.hint_sw},
         'sl': {'description': 'Sum of the 3 left-most numbers',
                'function': ht.hint_sl},
         'sr': {'description': 'Sum of the 3 right-most numbers',
                'function': ht.hint_sr},
         'sc': {'description': 'Sum of the central tiles',
                'function': ht.hint_sc},
         'te': {'description': 'Number of even tiles',
                'function': ht.hint_te},
         'to': {'description': 'Number of odd tiles',
                'function': ht.hint_to},
         'tb': {'description': 'Number of black numbers',
                'function': ht.hint_tb},
         'tw': {'description': 'Number of white numbers',
                'function': ht.hint_tw},
         'ts': {'description': 'Number of pairs of tiles with same numbers',
                'function': ht.hint_ts},
         '0': {'description': 'Location of the #0 tiles',
               'function': ht.hint_0},
         '1': {'description': 'Location of the #1 tiles',
               'function': ht.hint_1},
         '2': {'description': 'Location of the #2 tiles',
               'function': ht.hint_2},
         '3': {'description': 'Location of the #3 tiles',
               'function': ht.hint_3},
         '4': {'description': 'Location of the #4 tiles',
               'function': ht.hint_4},
         '5': {'description': 'Location of the #5 tiles',
               'function': ht.hint_5},
         '6': {'description': 'Location of the #6 tiles',
               'function': ht.hint_6},
         '7': {'description': 'Location of the #7 tiles',
               'function': ht.hint_7},
         '8': {'description': 'Location of the #8 tiles',
               'function': ht.hint_8},
         '9': {'description': 'Location of the #9 tiles',
               'function': ht.hint_9},
         'nc': {'description': 'Neighboring tiles with same color',
                'function': ht.hint_nc},
         'nn': {'description': 'Neighboring tiles with consecutive numbers',
                'function': ht.hint_nn},
         'd': {'description': 'Difference between highest and lowest number',
               'function': ht.hint_d},
         'c': {'description': 'C tile greater than 4',
               'function': ht.hint_c}}

BLACK_FTILES = (0, 2, 4, 6, 8, 12, 14, 16, 18)

WHITE_FTILES = (1, 3, 5, 7, 9, 13, 15, 17, 19)

EVEN_FTILES = (0, 1, 4, 5, 8, 9, 12, 13, 16, 17)

ODD_FTILES = (2, 3, 6, 7, 10, 11, 14, 15, 18, 19)

SIMULATION_ITERATIONS = 50

BLACK_COLOR = '\x1b[0;30;44m'

WHITE_COLOR = '\x1b[0;37;44m'

GREEN_COLOR = '\x1b[0;31;44m'

END_COLOR = '\x1b[0m'
