def remove_vowels(phrase : str):
    new_str = ""
    for char in phrase.lower():
        if char not in "aeiou":
            new_str += char
    return new_str

if __name__ == "__main__":
    print(remove_vowels("Gonzaga"))


# A unit test is a function that tests another function for correctness.
# A unit test is comprised of one or more test cases.
# test cases should include simple/common input/output pairs (e.g., the "happy path")

# We will use the pytest testing framework
# test modules and unit tests start with test_