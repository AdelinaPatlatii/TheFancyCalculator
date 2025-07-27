def power_calc(base: float, exp: int) -> float: # add tests
    if exp == 0:
        return 1.0
    if exp < 0:
        return 1.0 / power_calc(base, -exp)

    half = power_calc(base, exp // 2)
    if exp % 2 == 0:
        return half * half
    else:
        return half * half * base
