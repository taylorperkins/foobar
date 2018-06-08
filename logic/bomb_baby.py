
class SolvedError(Exception):
    """raise when problem solved"""


def is_solvable(M, F):
    return all([M > 0, F > 0, M != F])


def recursive_steps(M, F, steps=0):
    if M == 1 and F == 1:
        return str(steps)

    if is_solvable(M, F):
        if F > M:
            divisible = F // M

            if divisible > 2 and M != 1:
                steps += divisible
                F = F - M * divisible
            else:
                steps += 1
                F -= M

        else:
            divisible = M // F

            if divisible > 2 and F != 1:
                steps += divisible
                M = M - F * divisible
            else:
                steps += 1
                M -= F

        return recursive_steps(M, F, steps=steps)

    else:
        return "impossible"


def answer(M, F):
    M, F = int(M), int(F)

    result = recursive_steps(M, F)

    return result
