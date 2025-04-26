from functools import lru_cache

SQ = [i * i for i in range(10)]

def next_term(x: int) -> int:
    s = 0
    while x:
        s += SQ[x % 10]
        x //= 10
    return s

@lru_cache(maxsize=None)
def ends_at_89(x: int) -> bool:
    while x not in (1, 89):
        x = next_term(x)
    return x == 89

def count_numbers_with_89(n: int) -> int:
    return sum(ends_at_89(k) for k in range(1, n + 1))