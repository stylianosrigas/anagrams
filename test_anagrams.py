# import anagrams

# assert anagrams.inc(3) == 4

import pytest
import anagrams

def test_string():
	assert anagrams.of("") == ""

def test_one_letter():
	assert anagrams.of("A") == "A"

def test_two_letters():
	assert anagrams.of("AB") == ["AB", "BA"]

def test_three_letters():
	assert anagrams.of("ABC") == ["ABC", "ACB", "BAC", "BCA", "CAB", "CBA"]

def test_four_letters():
	assert len(anagrams.of("ABCD")) == 24
