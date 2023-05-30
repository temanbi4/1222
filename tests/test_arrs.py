from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -5, "test") == "test"
    with pytest.raises(IndexError):
        arrs.gassert 


def test_slice():
        assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
        assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
        assert arrs.my_slice([], 1) == []
        assert arrs.my_slice([1, 2, 3], -1) == [3]
        assert arrs.my_slice([1, 2, 3], 5) == []
        assert arrs.my_slice([1, 2, 3], 10) == []
        assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
        assert arrs.my_slice([1, 2, 3], -4) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3], end=-1) == [1, 2]
        assert arrs.my_slice([1, 2, 3], end=-5) == []
        assert arrs.my_slice([1, 2, 3], -2, -1) == [2]
        assert arrs.my_slice([1, 2, 3], end=5) == [1, 2, 3]
        assert arrs.my_slice([1, 2, 3], end=10) == [1, 2, 3]
