import logging

gcd_cache = {}


def gcd(a: int, b: int) -> int:
    key = (a, b)
    if key in gcd_cache:
        logging.info(f"[CACHE HIT] gcd({a}, {b})")
        return gcd_cache[key]

    while b:
        a, b = b, a % b
    result = abs(a)
    gcd_cache[key] = result
    return result
