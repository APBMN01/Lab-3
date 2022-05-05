import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending_lt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 2)

def test_bubble_sort_descending_mt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 21, 69, 81, 99]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    assert (result == 1)

def test_bubble_sort_invalid():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, 3)
    assert (result == 0)

def test_bubble_sort_not_int():
    input_arr = [64, 34, 25, "yeet", 22, 11, 90, "yolo", 'a',0]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    assert (result == 3)