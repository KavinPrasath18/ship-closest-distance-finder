from main import *

def test_func():
    value = {0: (34, 2), 1: (43, 18), 2: (30, 41), 3: (20, 7), 4: (14, 14), 5: (31, 10), 6: (30, 26), 7: (47, 2), 8: (7, 24), 9: (23, 25)}

    result = closest_distance_finder(value)

    assert result[0] == (6, 9)
    assert result[1] == ((30, 26), (23, 25))