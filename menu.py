"""Graphical menu."""


import os
from typing import List, Set, Tuple
import utils as ut


TITLE = """=============================
=== Break the Code Helper ===
=============================
"""

MAIN_MENU = """(h) Add hint
(s) Simulate hints
(c) Show remaining combinations
(u) Undo (remove last hint)
(q) Quit
"""

HINT_SHORTCUTS = """(st) What is the sum of your tiles?                              (te) How many even tiles do you have?
(sb) What is the sum of your black numbers?                      (to) How many odd tiles do you have?
(sw) What is the sum of your white numbers?                      (tb) How many of your tiles have a black number?
(sl) What is the sum of your 3 left-most tiles?                  (tw) How many of your tiles have a white number?
(sr) What is the sum of your 3 right-most tiles?                 (ts) How many of your tiles have the same number?
(sc) What is the sum of your central tiles (b, c, and d)?

(0) Where are your #0 tiles?                                     (5) Where are your #5 tiles?
(1) Where are your #1 tiles?                                     (6) Where are your #6 tiles?
(2) Where are your #2 tiles?                                     (7) Where are your #7 tiles?
(3) Where are your #3 tiles?                                     (8) Where are your #8 tiles?
(4) Where are your #4 tiles?                                     (9) Where are your #9 tiles?

(nc) Which neighboring tiles have the same color?                (d) What is the difference between your highest and lowest number?
(nn) Which neighboring tiles have consecutive numbers?           (c) Is your C tile greater than 4?

(q) Go back without choosing a hint
"""


def clear_screen() -> None:
    """Clear the screen."""
    clear_command = 'clear' if os.name == 'posix' else 'cls'
    os.system(clear_command)


def ftile_as_colored_tile(ftile: int) -> str:
    """Return an ftile as a colored tile."""
    if ftile in ut.BLACK_FTILES:
        return ut.BLACK_COLOR + str(ftile//2) + ut.END_COLOR
    if ftile in ut.WHITE_FTILES:
        return ut.WHITE_COLOR + str(ftile//2) + ut.END_COLOR
    return ut.GREEN_COLOR + str(ftile//2) + ut.END_COLOR


def ftiles_as_colored_tiles(ftiles: Tuple[int, ...]) -> str:
    """Return a sequence of ftiles as a sequence of colored tiles."""
    colored_tiles = ''
    for ftile in ftiles:
        colored_tiles += ftile_as_colored_tile(ftile)
    return colored_tiles


def ask_user_combination() -> Tuple[str, ...]:
    """Ask the user for their tiles and return them."""
    while True:
        tiles = input('Enter your tiles, separated by spaces '
                      '(e.g.: 3w 4b 5 5g 8w): ').lower().split()
        # There must be exactly five tiles
        if len(tiles) != 5:
            print('Error: You need to specify exactly five tiles')
            continue
        # Normalize the #5 tiles
        for index, tile in enumerate(tiles):
            if tile == '5':
                tiles[index] = '5g'
        # Make sure that the tiles entered are valid
        for tile in tiles:
            if tile not in ut.TILES:
                print(f'Error: Tile {tile} is not recognized as a valid tile')
                break
            if (len(set(tiles)) < 4) and \
               (tiles.count('5g') != 2):
                print('Error: Only the 5 tile can be specified twice')
                break
        # If we reach this point, the tiles are valid
        else:
            break
    return tuple(tiles)


def display_main_menu(our_fcombination: Tuple[int, ...],
                      opponent_fcombinations: List[Tuple[int, ...]],
                      hints: List[Tuple[str, int]],
                      simulations: List[Tuple[str, Tuple[float, float]]]) -> str:
    """Display the main menu and return a valid user choice."""
    choice = None
    while True:
        clear_screen()

        print(TITLE)

        print('Your tiles: ', end='')
        print(ftiles_as_colored_tiles(our_fcombination))

        print(f'\nOpponent tile possibilities ({len(opponent_fcombinations)} left) per position:')
        positions = [set(), set(), set(), set(), set()]  # type: List[Set[int]]
        for fcombination in opponent_fcombinations:
            for index, ftile in enumerate(fcombination):
                positions[index].add(ftile)
        for index, position in enumerate(positions):
            print(f"{'abcde'[index]}: ", end='')
            print(ftiles_as_colored_tiles(tuple(sorted(list(position)))))

        if len(hints) == 0:
            print('\nNo hints yet')
        else:
            print('\nCurrent hints:')
            for hint in hints:
                print('- ' +
                      ut.HINTS[hint[0][0]]['description'] +
                      f': {hint[0][1]} (-{hint[1]} combinations)')

        if len(simulations) == 0:
            print('\nNo simulation data (or the data is outdated)')
        else:
            print('\nSimulation data (average % combinations filtered, standard deviation):')
            for simulation in simulations:
                print('- ' +
                      f'{ut.HINTS[simulation[0]]["description"]:<45}' +
                      f'{simulation[1][0]:<5.1%} ({simulation[1][1]:.1f})')

        print('\nOptions:')
        print(MAIN_MENU)

        if choice is not None:
            print(f'Error: There is no \'{choice}\' option')
        choice = input('Choose option: ')
        if choice in ('h', 's', 'c', 'u', 'q'):
            break

    return choice


def display_hints_menu() -> Tuple[str, int | str | Tuple[str, ...]] | None:
    """Display the hints menu and return a valid hint and result."""
    choice = None
    while True:
        clear_screen()
        print(TITLE)
        print(HINT_SHORTCUTS)
        if choice is not None:
            print(f'Error: The hint \'{choice}\' is not valid')
        choice = input('Choose option: ')
        if choice in ut.HINTS or choice == 'q':
            break

    subchoice = ''  # type: int | str | Tuple[str, ...]
    match choice:
        case _ as choice if choice in ('st', 'sb', 'sw', 'sl', 'sr', 'sc',
                                       'te', 'to', 'tb', 'tw', 'ts', 'd'):
            while True:
                subchoice = input(ut.HINTS[choice]['description'] + ': ')
                try:
                    subchoice = int(subchoice)
                except ValueError:
                    print(f'Error: Value \'{subchoice}\' must be an integer')
                    continue
                break
        case _ as choice if choice in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
            while True:
                subchoice = input(f'Where are the #{choice} tiles? (e.g.: bc) '
                                  '[leave empty if no tiles]: ').lower()
                if subchoice not in ('', 'a', 'b', 'c', 'd', 'e', 'ab', 'bc', 'cd', 'de'):
                    print(f'Error: The position(s) \'{subchoice}\' is/are not valid')
                    continue
                break
        case 'nc':
            while True:
                subchoice = input('Neighboring tile groups with same color (e.g.: ab de): ').lower()
                if subchoice.split() not in ([],
                                             ['ab'], ['bc'], ['cd'], ['de'],
                                             ['ab', 'cd'], ['ab', 'de'], ['bc', 'de'],
                                             ['abc'], ['bcd'], ['cde'],
                                             ['abc', 'de'], ['ab', 'cde'],
                                             ['abcd'], ['bcde'], ['abcde']):
                    print(f'Error: The intervals(s) \'{subchoice}\' is/are not valid')
                    continue
                subchoice = tuple(subchoice.split())
                break
        case 'nn':
            while True:
                subchoice = input('Neighboring tile groups with consecutive numbers '
                                  '(e.g.: ab de): ').lower()
                if subchoice.split() not in ([],
                                             ['ab'], ['bc'], ['cd'], ['de'],
                                             ['ab', 'de'],
                                             ['abc'], ['bcd'], ['cde'],
                                             ['abcd'], ['bcde'], ['abcde']):
                    print(f'Error: The intervals(s) \'{subchoice}\' is/are not valid')
                    continue
                subchoice = tuple(subchoice.split())
                break
        case 'c':
            while True:
                subchoice = input('C tile is STRICTLY greater than 4 (y/n) : ').lower()
                if subchoice not in ('y', 'n'):
                    print('Error: You must answer \'y\' or \'n\'')
                    continue
                break
        case 'q':
            return None

    return choice, subchoice


def display_combinations_menu(opponent_fcombinations: List[Tuple[int, ...]]) -> None:
    """Display the combinations menu."""
    while True:
        clear_screen()
        print(TITLE)
        remaining = len(opponent_fcombinations)
        print(f'There are {remaining} combinations remaining', end='')
        if remaining < 20:
            print(':')
        else:
            print(' (showing only 20 of them):')
        for fcombination in opponent_fcombinations[:min(remaining, 20)]:
            print(ftiles_as_colored_tiles(fcombination))
        input('\nPress \'[Enter]\' to go back.')
        break


def display_simulation_menu() -> Tuple[str, ...] | None:
    """Display the simulation menu and return a valid sequence of hints to simulate."""
    wrong_hint = None
    while True:
        clear_screen()
        print(TITLE)
        print(HINT_SHORTCUTS)
        if wrong_hint is not None:
            print(f'Error: The hint \'{wrong_hint}\' is not a valid hint')
        choice = input('Choose the hints you want to simulate, separated by spaces (e.g., st tw nc): ')
        if choice == 'q':
            return None
        for hint in choice.split():
            if hint not in ut.HINTS:
                wrong_hint = hint
                break
        else:
            return tuple(choice.split())
