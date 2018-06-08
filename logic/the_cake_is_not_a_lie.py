from operator import itemgetter


def answer(s):
    """function called answer(s) that, given a non-empty string less than 200 characters in length describing
    the sequence of M&Ms, returns the maximum number of equal parts that can be cut from the cake without
    leaving any leftovers.

    Steps to solving this problem:
        1. Initialize an empty dictionary to hold my values.
            _hash = {
                seq: (count_of_seq_instances, num_of_remaining_letters),
                ...
            }

        2. Iterate over the length of the string. I want to be able to grab each unique permutation, and base the
            length of the permutation from this loop
        3. Iterate again to create the steps for each permutation. Example:
            given 'aabbc',
            'aa', 'ab', 'bb', ..
        4. Extract the sequence from the phrase s based on i and j
        5. If we have seen this hash in the iteration before, continue over it
        6. Otherwise, determine how many times this sequence shows up in the phrase, as well as the leftover
            character count
        7. assign the values to the initialized hash
        8. First sort the hash by the amount of remaining characters. If there is a sequence with 0 remaining characters
            it has higher priority
        9. Then sort by the length of the sequence where the length of the remainder is equal to the highest sorted
            sequence
        10. return solution


    :param s:
    :return:
    """
    solution = 0
    # your code here
    if s and len(s) < 200:
        # I really only need to store the length of the sequence (key),
        # how many times it was found, and the leftover amt
        _hash = dict()
        _range = len(s)

        for i in range(1, _range):
            for j in range(0, _range):
                seq = s[j:j + i]

                if _hash.get(seq):
                    continue

                else:
                    seq_count = s.count(seq)
                    remaining_letters = _range - i*seq_count

                    _hash[seq] = (seq_count, remaining_letters)

        sorted_by_remainders = sorted(_hash.values(), key=itemgetter(1))
        solution = max({
            seq_values[0] for seq_values in sorted_by_remainders
            if seq_values[1] == sorted_by_remainders[0][1]
        })

    return solution
