from merge import sort

def test_sort():
    assert sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort([1, 5, 2, 4, 3]) == [1, 2, 3, 4, 5]
    assert sort([4, 3, 2, 1]) == [1, 2, 3, 4]
    assert sort([3, 3, 3]) == [3, 3, 3]
    assert sort([2, 1]) == [1, 2]
    assert sort([1]) == [1]
    assert sort([]) == []
