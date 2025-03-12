import re

weights_symbols = [
    (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
    (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
]

def decode_roman(str_val: str) -> int:
    result = 0
    for weight, symbol in weights_symbols:
        regex = re.compile(symbol)
        while regex.match(str_val):
            result += weight
            str_val = regex.sub("", str_val, 1) #replace only first occurance.
    return result

def to_roman(n: int) -> str:
    roman = ""
    i = 0
    while i < len(weights_symbols) and n > 0:
        weight = weights_symbols[i][0]
        while n >= weight:
            roman += weights_symbols[i][1]
            n -= weight
        i += 1
    return roman