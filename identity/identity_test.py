from identity import identity
from hypothesis import given, strategies as st

# Identity matrix must include only ones and zeroes
@given(st.integers(min_value=1,max_value=10))
def test_identity_1(i) :
    matrix = identity(i)
    for row in matrix:
        for element in row:
            assert element in [0,1]

# Replace 'pass' with your own test here. Create as many
# tests as you need, but remember to rename them.
@given(st.integers(min_value=1,max_value=100))
def test_square(i) :
    matrix = identity(i)
    assert len(matrix) == i
    for row in matrix:
        assert len(row) == i

@given(st.integers(min_value=1,max_value=100))
def test_1_on_diagonal(i) :
    matrix = identity(i)
    for j in range(i):
        assert matrix[j][j] == 1

@given(st.integers(min_value=1,max_value=100))
def test_0_on_non_diagonal(i) :
    matrix = identity(i)
    for j in range(i):
        for k in range(i):
            if j != k:
                assert matrix[j][k] == 0

def test_threebythree() :
    matrix = identity(3)
    assert matrix == [[1,0,0],[0,1,0],[0,0,1]]
    print(matrix)