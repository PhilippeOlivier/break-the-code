"""Break the Code Helper.

- A `tile` is a string of one number and one color (e.g., "2b").
- A `number` is the rank of a tile, from 0 to 9.
- A `color` is the color of a tile: "b" for black, "w" for white, and "g" for green.
- A `combination` is an array of tiles.

- A `ftile` (flattened tile) is numbered from 0 to 19, and that number holds both the rank and color
of the tile (e.g., "2b" would be "5").
- A `fcombination` is an array of ftiles.
"""


import sys
from typing import List, Tuple
import board as bd
import combination as cb
import menu as mn


combination = mn.ask_user_combination()
fcombination = cb.combination_to_fcombination(combination)
board = bd.Board(combination)
hints = []  # type: List[Tuple[str, int]]
simulations = []  # type: List[Tuple[str, Tuple[float, float]]]
while True:
    choice = mn.display_main_menu(fcombination,
                                  board.get_opponent_fcombinations(),
                                  hints,
                                  simulations)
    match choice:
        case 'h':
            hint = mn.display_hints_menu()
            if hint is not None:
                num_opponent_combs_before = len(board.get_opponent_fcombinations())
                board.apply_hint(hint[0], hint[1])
                num_opponent_combs_after = len(board.get_opponent_fcombinations())
                improvement = num_opponent_combs_before - num_opponent_combs_after
                hints.append((hint, improvement))
                simulations = []
        case 's':
            hints_to_simulate = mn.display_simulation_menu()
            if hints_to_simulate is not None:
                for hint in hints_to_simulate:
                    if hint not in [simulation[0] for simulation in simulations]:
                        simulations.append((hint, board.simulate(hint)))
        case 'c':
            mn.display_combinations_menu(board.get_opponent_fcombinations())
        case 'u':
            if len(hints) > 0:
                hints.pop()
                simulations = []
            board = bd.Board(combination)
            for hint in hints:
                board.apply_hint(hint[0][0], hint[0][1])
        case 'q':
            really = input('Really quit? Press \'y\' to quit, anything else to go back: ')
            if really.lower() == 'y':
                sys.exit(0)
        case _:
            pass
