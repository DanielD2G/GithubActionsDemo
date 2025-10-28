"""
Simple string tests
"""
import pytest


def reverse_string(s):
    return s[::-1]


def capitalize_words(s):
    return s.title()


def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)


class TestStringOperations:
    """Test basic string operations"""

    def test_reverse_string(self):
        assert reverse_string("hello") == "olleh"

    def test_reverse_empty_string(self):
        assert reverse_string("") == ""

    def test_capitalize_words(self):
        assert capitalize_words("hello world") == "Hello World"

    def test_count_vowels(self):
        assert count_vowels("hello") == 2

    def test_count_vowels_no_vowels(self):
        assert count_vowels("xyz") == 0

    def test_count_vowels_all_vowels(self):
        assert count_vowels("aeiou") == 5

    def test_reverse_python(self):
        """This test intentionally fails - wrong expected value"""
        assert reverse_string("python") == "NOHTYP"  # Wrong! Should be "nohtyp" in lowercase

    def test_count_vowels_test_string(self):
        """This test has wrong expected count"""
        assert count_vowels("beautiful") == 3  # Wrong! Actually has 5 vowels (e,a,u,i,u)
