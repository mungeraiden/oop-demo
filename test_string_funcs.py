# Unit test for remove vowles

from string_funcs import remove_vowels


def test_remove_vowels():
    result = remove_vowels("gonzaga")
    assert result == "gnzg"

test_remove_vowels()