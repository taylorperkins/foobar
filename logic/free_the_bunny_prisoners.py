import itertools


# Note, I cannot take full credit for the solution on this one. Full credit for understanding the tools needed to solve
# this problem goes to this guy. Very elegant solution.
# https://github.com/arinkverma/google-foobar/blob/master/4.1_bunny.py

def answer(num_buns, num_required):
    r = []

    # all potential combinations, all unique
    f = list(itertools.combinations(range(num_buns), num_required))

    # Ex, 5 and 3 makes 30
    total = len(f)*num_required
    repeat_times = num_buns - num_required + 1
    f1 = list(itertools.combinations(range(num_buns), repeat_times))

    # create an inddex per bun
    for i in range(num_buns):
        r.append([])

    # fill in all the indices
    for i in range(total/repeat_times):
        for j in f1[i]:
            r[j].append(i)

    return r
