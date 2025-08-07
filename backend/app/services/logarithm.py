import logging
import math

log_cache = {}


def log_base(a: float, b: float) -> float:
    key = (a, b)
    if key in log_cache:
        logging.info(f"[CACHE HIT] log_base({a}, {b})")
        return log_cache[key]

    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm: base must be > 0 and "
                         "≠ 1, argument must be > 0.")

    result = math.log(b) / math.log(a)
    log_cache[key] = result
    return result
