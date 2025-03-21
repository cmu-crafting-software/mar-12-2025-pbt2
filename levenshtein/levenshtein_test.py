from levenshtein import levenshtein
from hypothesis import given, strategies as st

# levenshteinDistance must always return >= 0
@given(st.text(alphabet='abcd',max_size=3),st.text(alphabet='abcd',max_size=3))
def test_levenshtein_1(s1: str, s2: str) :
    assert levenshtein(s1,s2) >= 0

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.text(alphabet='abcd',max_size=3),st.text(alphabet='abcd',max_size=3))
def test_levenshtein_2(s1: str, s2: str) :
    pass