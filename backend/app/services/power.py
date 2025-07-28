import logging
pow_cache = {}


def power_calc(base: float, exp: int) -> float:
    key = (base, exp)
    if key in pow_cache:
        logging.info(f"[CACHE HIT] power_calc({base}, {exp})")
        return pow_cache[key]

    if exp == 0:
        return 1.0
    if exp < 0:
        result = 1.0 / power_calc(base, -exp)
        pow_cache[key] = result
        return result

    half = power_calc(base, exp // 2)
    if exp % 2 == 0:
        result = half * half
    else:
        result = half * half * base

    pow_cache[key] = result
    return result
