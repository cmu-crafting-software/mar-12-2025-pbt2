# Adapted from: https://rosettacode.org/wiki/Levenshtein_distance#Python
#
# The Levenshtein distance is a metric for measuring the amount of difference
# between two strings (i.e. an edit distance). The Levenshtein distance
# between two strings (`a` and `b`) is defined as the minimum number of edits
# needed to transform one string into the other, with the allowable edit
# operations being insertion, deletion, or substitution -- all of a single 
# character.
#
# Examples (key: S=substitute, D=delete, I=insert, _=no change)
#
# 1. 'sitting' -> 'kitty' = 4 (2 substitutions + 2 deletion)
#     S___SDD 
# 2. 'aaaa'    -> ''      = 4 (4 deletions)
#     DDDD
# 3. 'aaaa'    -> 'aaacb' = 2 (1 substitution + 1 add)
#     ___SA
#
# @param str1 the original string
# @param str2 the final string after editing `str1`
# @returns the number of edits needed to transform `str1` to `str2`
def levenshtein(str1, str2):
    m = len(str1)
    n = len(str2)
    d = [[i] for i in range(1, m + 1)]   # d matrix rows
    d.insert(0, list(range(0, n + 1)))   # d matrix columns
    for j in range(1, n + 1):
        for i in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:   # Python (string) is 0-based
                substitutionCost = 0
            else:
                substitutionCost = 1
            d[i].insert(j, min(d[i - 1][j],
                               d[i][j - 1] + 1,
                               d[i - 1][j - 1] + substitutionCost))
    return d[-1][-1]