import logging

factorial_cache = {}
def fact(n: int) -> int:
    if n in factorial_cache:
        logging.info(f"[CACHE HIT] fact({n})")
        return factorial_cache[n]
    if n < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    factorial_cache[n] = result
    return result
