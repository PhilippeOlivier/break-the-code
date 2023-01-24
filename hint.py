"""Hints and their answers."""


from typing import Tuple
import combination as cb
import utils as ut


def hint_st(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the tiles."""
    return sum(cb.fcombination_to_numbers(fcombination))


def _hint_sum_color(fcombination: Tuple[int, ...], color: str) -> int:
    """Return the sum of the tiles of a given color 'b' or 'w'."""
    numbers = cb.fcombination_to_numbers(fcombination)
    colors = cb.fcombination_to_colors(fcombination)
    return sum(numbers[i] for i in range(len(fcombination)) if colors[i] == color)


def hint_sb(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the black tiles."""
    return _hint_sum_color(fcombination, 'b')


def hint_sw(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the white tiles."""
    return _hint_sum_color(fcombination, 'w')


def hint_sl(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the three left-most tiles."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return sum(numbers[0:3])


def hint_sr(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the three right-most tiles."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return sum(numbers[-3:])


def hint_sc(fcombination: Tuple[int, ...]) -> int:
    """Return the sum of the center tiles."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return sum(numbers[1:-1])


def hint_te(fcombination: Tuple[int, ...]) -> int:
    """Return the number of even tiles."""
    return len([i for i in fcombination if i in ut.EVEN_FTILES])


def hint_to(fcombination: Tuple[int, ...]) -> int:
    """Return the number of odd tiles."""
    return len([i for i in fcombination if i in ut.ODD_FTILES])


def hint_tb(fcombination: Tuple[int, ...]) -> int:
    """Return the number of black tiles."""
    return len([i for i in fcombination if i in ut.BLACK_FTILES])


def hint_tw(fcombination: Tuple[int, ...]) -> int:
    """Return the number of white tiles."""
    return len([i for i in fcombination if i in ut.WHITE_FTILES])


def hint_ts(fcombination: Tuple[int, ...]) -> int:
    """Return the number of pairs of tiles with the same number."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return len(numbers) - len(set(numbers))


def hint_nc(fcombination: Tuple[int, ...]) -> Tuple[str, ...]:
    """Return the neighboring tiles with the same color."""
    colors = cb.fcombination_to_colors(fcombination)
    current_color = colors[0]
    current_neighbors = 'a'
    neighbors = []
    for i in range(1, len(colors)):
        if colors[i] == current_color:
            current_neighbors += 'abcde'[i]
        else:
            neighbors.append(current_neighbors)
            current_color = colors[i]
            current_neighbors = 'abcde'[i]
    neighbors.append(current_neighbors)
    neighbors = [x for x in neighbors if len(x) > 1]
    return tuple(neighbors)


def hint_nn(fcombination: Tuple[int, ...]) -> Tuple[str, ...]:
    """Return the neighboring tiles with consecutive numbers."""
    numbers = cb.fcombination_to_numbers(fcombination)
    current_number = numbers[0]
    current_neighbors = 'a'
    neighbors = []
    for i in range(1, len(numbers)):
        if numbers[i] == current_number + 1:
            current_neighbors += 'abcde'[i]
            current_number += 1
        else:
            neighbors.append(current_neighbors)
            current_number = numbers[i]
            current_neighbors = 'abcde'[i]
    neighbors.append(current_neighbors)
    neighbors = [x for x in neighbors if len(x) > 1]
    return tuple(neighbors)


def hint_d(fcombination: Tuple[int, ...]) -> int:
    """Return the difference between the highest and lowest number."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return numbers[-1] - numbers[0]


def hint_c(fcombination: Tuple[int, ...]) -> bool:
    """Return a boolean indication if the C tile is strictly greater than 4."""
    numbers = cb.fcombination_to_numbers(fcombination)
    return numbers[2] > 4


def _hint_x(fcombination: Tuple[int, ...], x_tile: int) -> str:
    """Return the location(s) of the X tiles. Return an empty string if there are no X tiles."""
    numbers = cb.fcombination_to_numbers(fcombination)
    location = ''
    for i, _ in enumerate(numbers):
        if numbers[i] == x_tile:
            location += 'abcde'[i]
    return location


def hint_0(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 0 tiles. Return an empty string if there are no 0 tiles."""
    return _hint_x(fcombination, 0)


def hint_1(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 1 tiles. Return an empty string if there are no 1 tiles."""
    return _hint_x(fcombination, 1)


def hint_2(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 2 tiles. Return an empty string if there are no 2 tiles."""
    return _hint_x(fcombination, 2)


def hint_3(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 3 tiles. Return an empty string if there are no 3 tiles."""
    return _hint_x(fcombination, 3)


def hint_4(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 4 tiles. Return an empty string if there are no 4 tiles."""
    return _hint_x(fcombination, 4)


def hint_5(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 5 tiles. Return an empty string if there are no 5 tiles."""
    return _hint_x(fcombination, 5)


def hint_6(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 6 tiles. Return an empty string if there are no 6 tiles."""
    return _hint_x(fcombination, 6)


def hint_7(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 7 tiles. Return an empty string if there are no 7 tiles."""
    return _hint_x(fcombination, 7)


def hint_8(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 8 tiles. Return an empty string if there are no 8 tiles."""
    return _hint_x(fcombination, 8)


def hint_9(fcombination: Tuple[int, ...]) -> str:
    """Return the location(s) of the 9 tiles. Return an empty string if there are no 9 tiles."""
    return _hint_x(fcombination, 9)
