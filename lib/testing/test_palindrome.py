import pytest
from lib.palindrome import longest_palindromic_substring

# --- Basic Palindrome Cases ---
def test_simple_palindrome():
    # check a standard odd-length palindrome
    assert longest_palindromic_substring("babad") in ["bab", "aba"]

def test_even_length_palindrome():
    # check a standard even-length palindrome
    assert longest_palindromic_substring("cbbd") == "bb"

def test_single_character():
    # a single character string should return itself
    assert longest_palindromic_substring("a") == "a"

def test_two_characters_non_palindrome():
    # when there is no real palindrome, any single character is valid
    assert longest_palindromic_substring("ac") in ["a", "c"]

def test_full_string_palindrome():
    # the entire string is already a palindrome
    assert longest_palindromic_substring("racecar") == "racecar"


# --- Edge Cases ---
def test_empty_string():
    # empty string should return empty
    assert longest_palindromic_substring("") == ""

def test_all_unique_characters():
    # no repeating characters, so any single character is valid
    result = longest_palindromic_substring("abcdefg")
    assert result in list("abcdefg")

def test_repeated_characters():
    # all characters the same, the whole string is the palindrome
    assert longest_palindromic_substring("aaaa") == "aaaa"

def test_long_string_mixed():
    # mixed pattern with longest palindrome in the middle
    assert longest_palindromic_substring("abaxyzzyxf") == "xyzzyx"

def test_numeric_string():
    # numeric palindromes should be handled just like letters
    assert longest_palindromic_substring("1234321") == "1234321"
