import src.array

def test_find_equilibrium_index():
    test_data_pass = [-7, 1, 5, 2, -4, 3, 0]
    assert src.array.find_equilibrium_index(test_data_pass) == 3

def test_find_equilibrium_index_no_eq_index():
    test_data_no_eq = [-7, 1, 5, 2, -4, 3, 0, 5]
    assert src.array.find_equilibrium_index(test_data_no_eq)