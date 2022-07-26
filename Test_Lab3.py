import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending_lt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    if result != 2:
        raise AssertionError

def test_bubble_sort_descending_mt_10():
    input_arr = [64, 34, 25, 12, 22, 11, 90, 21, 69, 81, 99]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)
    if result != 1:
        raise AssertionError

def test_bubble_sort_invalid():
    input_arr = []
    result = Lab3.bubble_sort(input_arr, 3)
    if result != 0:
        raise AssertionError

def test_bubble_sort_not_int():
    input_arr = [64, 34, 25, "yeet", 22, 11, 90, "yolo", 'a',0]
    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)
    if result != 3:
        raise AssertionError
