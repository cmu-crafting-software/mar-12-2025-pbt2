from hypothesis import given, strategies as st
from wordle_parts import is_yellow, is_green, is_grey

@given(st.text(min_size=5, max_size=5, alphabet='ABC'),st.text(min_size=5, max_size=5, alphabet='ABC'), st.integers(min_value=0, max_value=4))
def test_is_any_color(secret: str, guess: str, pos: int) :
    if is_yellow(secret, guess, pos):
        assert not is_green(secret, guess, pos) 
        assert not is_grey(secret, guess, pos)
    elif is_green(secret, guess, pos) :
        assert not is_yellow(secret, guess, pos) 
        assert not is_grey(secret, guess, pos)
    elif is_grey(secret, guess, pos) :
        assert not is_yellow(secret, guess, pos) 
        assert not is_green(secret, guess, pos)
    else :
        assert False

@given(st.text(min_size=5, max_size=5, alphabet='ABCDE'),st.text(min_size=5, max_size=5, alphabet='ABCDE'), st.integers(min_value=0, max_value=4))
def test_is_grey_multiples(guess: str, secret: str, pos: int) :
    #count the number of occurence of the letter at pos in guess
    letter = guess[pos]
    letters_in_guess = []
    for i in range(len(guess)):
        if letter == guess[i]:
            letters_in_guess.append(i)
    #count the number of occurence of the letter at pos in secret
    count_secret = 0
    for i in range(len(secret)):
        if letter == secret[i]:
            count_secret += 1
    if len(letters_in_guess) > count_secret:
        assert is_grey(guess, secret, letters_in_guess[count_secret])


# def test_is_grey() :
#     assert is_grey("aabcd", "afbcd", 1)

# def test_is_grey2() :
#     assert is_grey("seeds", "sends", 2)

# def test_is_yellow2() :
#     assert is_yellow("aabcd", "bcdaf", 0)

# def test_is_grey3() :
#     assert is_grey("aabcd", "bcdaf", 1)

# def test_is_yellow() :
#     assert not is_yellow("aabcd", "afbcd", 1)

# def test_is_green() :
#     assert not is_green("aabcd", "afbcd", 1)