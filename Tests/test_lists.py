"""
Simple list tests
"""
import pytest


def find_max(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return max(numbers)


def find_min(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return min(numbers)


def calculate_average(numbers):
    if not numbers:
        raise ValueError("List is empty")
    return sum(numbers) / len(numbers)


class TestListOperations:
    """Test basic list operations"""

    def test_find_max(self):
        assert find_max([1, 5, 3, 9, 2]) == 9

    def test_find_min(self):
        assert find_min([1, 5, 3, 9, 2]) == 1

    def test_calculate_average(self):
        assert calculate_average([2, 4, 6, 8]) == 5.0

    def test_find_max_empty_list(self):
        with pytest.raises(ValueError):
            find_max([])

    def test_find_min_empty_list(self):
        with pytest.raises(ValueError):
            find_min([])

    def test_calculate_average_empty_list(self):
        with pytest.raises(ValueError):
            calculate_average([])
