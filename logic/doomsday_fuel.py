from collections import deque

from fractions import Fraction, gcd


def inverse_sign(num):
    """Used to help determine addition or subtraction, usually based off index of list.

    :param num: int()
    :return: int()
    """
    if num % 2:
        return -1
    return 1


def get_q_r(m):
    """When solving Markov Absorbing Chain, you really only need the R and Q quadrant (1,0) and (1,1) of the
    standard form of a matrix. This method determines the transitional and absorbing states for the matrix,
    and creates both the R (transitional relates to absorbing) and Q (transitional relates to transitional)
    matrices to further the operation.

    :param m: matrix
    :return: (matrix, matrix)
    """
    terminal_states = list()
    transitional_states = list()

    for ind, row in enumerate(m):
        row_sum = sum(row)
        if row_sum:
            transitional_states.append((ind, row_sum))
        else:
            terminal_states.append((ind, row_sum))  # should always be 0

    R, Q = deque(), deque()

    for ind, state in enumerate(transitional_states):
        row_ind, row_sum = state[0], state[1]

        state_terminal = list()
        state_transitional = list()

        for term in terminal_states:
            state_terminal.append(Fraction(m[row_ind][term[0]], row_sum))

        for trans in transitional_states:
            state_transitional.append(Fraction(m[row_ind][trans[0]], row_sum))

        R.append(state_terminal)
        Q.append(state_transitional)

    return R, Q


def subract_matrix_from_identity(m):
    """Iterates over a matrix's rows and columns, and subtracts the value from either 0 or 1 depending on the indices
    of the row and column.

    :param m: matric
    :return: matrix
    """
    identity_minus_matrix = list()
    for r_ind, row in enumerate(m):
        r = list()

        for c_ind, val in enumerate(row):
            if r_ind == c_ind:
                r.append(Fraction(1) - val)
            else:
                r.append(Fraction(0) - val)

        identity_minus_matrix.append(r)

    return identity_minus_matrix


def get_matrix_minor(i, j, m):
    """Iterates over a matrix and creates a subset of the matrix minor by excluding the row associated with i,
    and each column index associated with j. Example:
    Given: 1, 1 and A as
        [
            [0, 1, 2],
            [0, 1, 2],
            [0, 1, 2]
        ]

    M(A)^ij would then be:

        [
            [0, 2],
            [0, 2]
        ]

    :param i: int()
    :param j: int()
    :param m: matrix
    :return: matrix --> subset
    """
    minor = list()
    for row_ind, row in enumerate(m):
        if row_ind != i:
            minor_row = list()

            for col_ind, val in enumerate(row):
                if col_ind != j:
                    minor_row.append(val)

            if minor_row:
                minor.append(minor_row)

    return minor


def get_matrix_determinant(m):
    """Recursive function used to find the determinant of any nxn matrix with n >=2. 
    
    :param m: matrix
    :return: Fraction()
    """
    row_len = len(m)
    col_len = len(m[0])

    if row_len > 2 and col_len > 2:
        # Initialize sum
        determinant_sum = 0

        # Get the determinant of the minor for matrix m at every m[0][:n] and add the value to the sum.
        for i in range(col_len):
            m_minor = get_matrix_minor(0, i, m)
            minor_determinant = get_matrix_determinant(m_minor)

            # Important to flip the sign at this stage.
            determinant_sum += inverse_sign(0 + i) * m[0][i] * minor_determinant

        # Ultimately return the sum
        return determinant_sum

    else:
        # Handle 2x2
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]


def get_cofactor_matrix(m):
    """Method for creating the cofactor matrix of any given matrix. This is especially important for finding the inverse
    of an nxn matrix where n > 2.

    :param m: matrix
    :return: matrix
    Example: A = 3x3 matrix
      [
        [(m[0][0] * |m[0][0]|) - (m[1][1] * |m[1][1]|) + (m[2][2] * |m[2][2]|)],
        [- (m[1][0] * |m[1][0]|) + (m[1][1] * |m[1][1]|) - (m[1][2] * |m[1][2]|)],
        [(m[2][0] * |m[2][0]|) + (m[2][1] * |m[2][1]|) - (m[2][2] * |m[2][2]|)]
      ]
    """
    cofactor_matrix = list()

    for i in range(len(m)):
        row_i = list()

        # per row in m
        sign = inverse_sign(i)

        for j in range(len(m[0])):
            m_minor = get_matrix_minor(i, j, m)
            minor_determinant = get_matrix_determinant(m_minor)

            row_i.append(sign * inverse_sign(j) * minor_determinant)

        cofactor_matrix.append(row_i)

    return cofactor_matrix


def transpose_cofactor(cofactor):
    """Transpose a matrix (doesn't have to be a cofactor matrix, but that's the only time I am using it).

    :param cofactor: matrix
    :return: matrix
    Example: Given
        [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]

        Return
        [
            [1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]
        ]

    """
    return [[cofactor[j][i] for j in range(len(cofactor))] for i in range(len(cofactor[0]))]


def get_2x2_adjoint(m):
    """Swap (0,0) and (1,1) while flipping signs for both (0,1) and (1,0)

    :param m: 2x2 matrix
    :return: matrix
    """
    return [
        [m[1][1], -m[0][1]],
        [-m[1][0], m[0][0]]
    ]


def adjoint_divided_by_determinant(det, adj):
    """Used for inverse matrix operations

    :param det: Fraction()
    :param adj: matrix
    :return: matrix
    """
    for r in range(len(adj)):
        for c in range(len(adj)):
            adj[r][c] = adj[r][c] / det

    return adj


def inverse_2x2_matrix(m):
    """Base method for inversing a 2x2 matrix. Don't need to worry about cofactors here.. Just the determinant and
    adjoint.

    :param m: matrix
    :return: matrix
    """
    determinant = get_matrix_determinant(m)
    adjoint = get_2x2_adjoint(m)

    return adjoint_divided_by_determinant(determinant, adjoint)


def inverse_nxn_matrix(m):
    """Base method for inverting a nxn matrix. Get the determinant of matrix, then the cofactor. Transpose the cofactor
    to create the adjoint. Then divide the adjoint by the determinant to create your inverse.

    :param m: matrix
    :return: matrix
    """
    assert len(m) == len(m[0])
    determinant = get_matrix_determinant(m)

    cofactor = get_cofactor_matrix(m)
    adjoint = transpose_cofactor(cofactor)

    return adjoint_divided_by_determinant(determinant, adjoint)


def multiply_matrices(m_1, m_2):
    """Multiplying matrices.
    m_1 --> 2x4
    m_2 --> 4x3

    return would be a 2x3 matrix

    :param m_1: matrix
    :param m_2: matrix
    :return: matrix
    """
    m = list()

    for i in range(len(m_1)):
        row_i = list()

        for j in range(len(m_2[0])):
            sums = sum([m_1[i][i2] * m_2[i2][j] for i2 in range(len(m_1[0]))])
            row_i.append(sums)

        m.append(row_i)

    return m


def get_gcd(fractions):
    """Get gcd from a list of fractions

    :param fractions: list(Fraction(), ..)
    :return: int()
    """
    track = Fraction(0, 1)

    for fraction in fractions:
        track = gcd(track, fraction)

    return track.denominator


def answer(m):
    # Default for a [[0]] matrix
    if len(m) == 1:
        return [1, 1]

    # Determine the R and Q quadrants from the standard form of m
    R, Q = get_q_r(m)

    # subtract Q from I
    I_minus_Q = subract_matrix_from_identity(Q)

    # Inverse I - Q to create F
    if len(I_minus_Q) == 2 and len(I_minus_Q[0]) == 2:
        F = inverse_2x2_matrix(I_minus_Q)
    else:
        F = inverse_nxn_matrix(I_minus_Q)

    # Multiply F and R
    FR = multiply_matrices(F, R)

    # determine denominator
    denominator = get_gcd(FR[0])

    # determine numerators by denominator
    numerators = [frac.numerator * (denominator / frac.denominator) for frac in FR[0]]

    return numerators + [denominator]
