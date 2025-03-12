from roman import decode_roman, to_roman
from hypothesis import given, strategies as st

def test_4():
    assert decode_roman("IV") == 4

def test_IV():
    assert to_roman(4) == 'IV'

def test_V():
    assert to_roman(5) == 'V'

@given(st.integers(min_value=1, max_value=3999))
def test_decode_roman(n):
    assert decode_roman(to_roman(n)) == n

@given(st.text(min_size=1, max_size=5, alphabet='IVXLCDM'))
def test_decode_roman(s):
    assert to_roman(decode_roman(s)) == s
