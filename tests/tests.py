import pytest

import src.array_algs

def test_find_equilibrium_index():
    test_data_pass = [-7, 1, 5, 2, -4, 3, 0]
    assert src.array_algs.find_equilibrium_index(test_data_pass) == 3

def test_find_equilibrium_index_no_eq_index():
    test_data_no_eq = [-7, 1, 5, 2, -4, 3, 0, 5]
    assert src.array_algs.find_equilibrium_index(test_data_no_eq)

def test_find_triplets_should_pass():
    test_data_pass = [-1, 0, 1, 2, -1, -4]
    assert src.array_algs.find_triplets_with_zero_sum(test_data_pass) == [[-1, -1, 2], [-1, 0, 1]]

def test_find_sum_of_even_numbers():
    assert src.array_algs.find_sum_of_even_numbers(14) == 56
    assert src.array_algs.find_sum_of_even_numbers(16) == 72
    assert src.array_algs.find_sum_of_even_numbers(114) == 3306

def test_find_sum_of_even_numbers_should_fail():
    with pytest.raises(ValueError):
        src.array_algs.find_sum_of_even_numbers(17)