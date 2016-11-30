from insertion import sort

def test_sort():
    assert sort([1, 2, 3]) == [1, 2, 3]
    assert sort([3, 2, 1]) == [1, 2, 3]
    assert sort([1, 3, 2]) == [1, 2, 3]
    assert sort([3, 3, 3]) == [3, 3, 3]
    assert sort([1]) == [1]
    assert sort([]) == []
