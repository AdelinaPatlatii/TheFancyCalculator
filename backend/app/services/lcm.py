import logging
from app.services.gcd import gcd

lcm_cache = {}


def lcm(a: int, b: int) -> int:
    key = (a, b)
    if key in lcm_cache:
        logging.info(f"[CACHE HIT] lcm({a}, {b})")
        return lcm_cache[key]

    if a == 0 or b == 0:
        result = 0
    else:
        result = abs(a * b) // gcd(a, b)

    lcm_cache[key] = result
    return result
