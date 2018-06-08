
def base_n(num, b, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
    return ((num == 0) and numerals[0]) or (base_n(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])


def answer(n, b):
    # Define a place to hold all of previous n. This is used to determine if n has been seen before
    tally = []

    while True:
        # If n reaches 0, return 1 as instructed
        if int(n, b) == 0:
            return 1

        # If we have seen n before, then a loop has been found. Count the num of iterations since last n
        elif n in tally:
            return len(tally) - tally.index(n)

        else:
            k = len(n)

            # assign x and y based on instructions, making sure to use the same base
            x = int("".join(sorted(n, reverse=True)), b)
            y = int("".join(sorted(n)), b)

            # determine z
            z = str(x - y)

            # If the len of z is less than k, prepend '0's to z
            len_z = len(z)
            if len_z < k:
                z = ('0'*(k-len_z)) + z

            # add n to the tally
            tally.append(n)

            # Convert z back to the original base, and reassign n
            n = base_n(int(z), b)
