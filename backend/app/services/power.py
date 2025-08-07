import logging
pow_cache = {}


def power_calc(base: float, exp: float) -> float:
    key = (base, exp)
    if key in pow_cache:
        logging.info(f"[CACHE HIT] power_calc({base}, {exp})")
        return pow_cache[key]

    if base < 0 and not exp.is_integer():
        raise ValueError("Let's keep it real please.")

    if isinstance(exp, int) or exp.is_integer():
        exp = int(exp)
        if exp == 0:
            result = 1.0
        elif exp < 0:
            result = 1.0 / power_calc(base, -exp)
        else:
            half = power_calc(base, exp // 2)
            result = half * half if exp % 2 == 0 else half * half * base
    else:
        result = pow(base, exp)

    pow_cache[key] = result
    return result
