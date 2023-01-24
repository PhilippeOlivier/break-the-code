"""Board of the game."""


import copy
import itertools
import random
import statistics
from typing import List, Tuple
import combination as cb
import utils as ut


class Board:
    """Store information on possible opponent hands."""

    def __init__(self, combination: Tuple[str, ...]) -> None:
        """Generate initial opponent hands."""
        self._our_fcombination = cb.combination_to_fcombination(combination)
        # Generate the opponent fcombinations
        self._opponent_fcombinations = self._generate_opponent_fcombinations()

    def _generate_opponent_fcombinations(self) -> List[Tuple[int, ...]]:
        """Generate all the possible fcombinations of the opponent."""
        raw_fcombinations = list(itertools.combinations(list(i for i in range(20)), 5))
        filtered_fcombinations = []
        our_fives = self._our_fcombination.count(10) + self._our_fcombination.count(11)
        for fcombination in raw_fcombinations:
            # Remove a hand that has any of our tiles
            if len(set(self._our_fcombination).intersection(set(fcombination))) > 0:
                continue
            # If we have no 5 tiles, remove symmetric opponent hands with one 5 tile
            if our_fives == 0 and \
               fcombination.count(10) + fcombination.count(11) == 1 and \
               11 in fcombination:
                continue
            filtered_fcombinations.append(tuple(fcombination))

        return filtered_fcombinations

    def _filter_combinations(self,
                             fcombinations: List[Tuple[int, ...]],
                             hint: str,
                             answer: int | str | List[str]) -> List[Tuple[int, ...]]:
        """Return the filtered fcombinations after applying the given hint with its result."""
        return [fcombination for fcombination in fcombinations
                if ut.HINTS[hint]['function'](fcombination) == answer]

    def get_opponent_fcombinations(self) -> List[Tuple[int, ...]]:
        """Return the possible fcombinations of the opponent."""
        return copy.deepcopy(self._opponent_fcombinations)

    def apply_hint(self, hint: str, answer: int | str | List[str]) -> None:
        """Apply a hint on the current board state."""
        self._opponent_fcombinations = self._filter_combinations(self._opponent_fcombinations,
                                                                 hint,
                                                                 answer)

    def simulate(self, hint: str) -> Tuple[float, float]:
        """Return the average % of filtered combinations, and the standard deviation."""
        results = []
        for _ in range(ut.SIMULATION_ITERATIONS):
            opponent_fcombinations = copy.deepcopy(self._opponent_fcombinations)
            before_filtering = len(opponent_fcombinations)
            sample_fcombination = random.choice(opponent_fcombinations)
            sample_answer = ut.HINTS[hint]['function'](sample_fcombination)
            opponent_fcombinations = [fcombination for fcombination in opponent_fcombinations
                                      if ut.HINTS[hint]['function'](fcombination) == sample_answer]
            after_filtering = len(opponent_fcombinations)
            percentage_filtered = (before_filtering - after_filtering) / before_filtering
            results.append(percentage_filtered)
        return sum(results) / len(results), statistics.stdev(results) * 100
