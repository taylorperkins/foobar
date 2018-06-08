def calculate_first_ind_row(h):
    col = list()
    # Go one higher in order to see if highest val has parent
    for i in range(h):
        try:
            col.append((col[-1]*2) + 1)
        except IndexError:
            col.append(1)

    return col


def answer(h, q):
    first_col = calculate_first_ind_row(h)

    max_val = first_col[-1]

    parents = list()
    for val in q:
        if val >= max_val:
            parents.append(-1)

        else:
            found = False
            # i will be used to reference which row you are on in the traversal
            for ind, col_val in enumerate(first_col):
                if found:
                    break

                # val is in the first column, so the parent is the next one up
                elif val == col_val:
                    parents.append(first_col[ind + 1])
                    break

                elif val < col_val:
                    is_even = True  # 0 and 1 grouping

                    while not found:
                        # We can only go down if even
                        if is_even:
                            col_val = col_val - 1
                            if val == col_val:
                                parents.append(col_val + 1)
                                found = True
                                break
                            else:
                                # We want to simulate moving down the tree
                                is_even = False
                                ind = ind - 1

                        else:
                            """
                            If you are an add value on the 0 - 1 grouping throughout the tree,
                            you can both move down, and move to the side. 
                            The relationship between the 0-1 groups throughout the tree are
                            x_0 = x_1 - row[ind][0] 
                            """
                            sibling = col_val - first_col[ind]
                            if val == sibling:
                                parents.append(col_val + 1)
                                found = True
                                break
                            elif val < sibling:
                                col_val = sibling
                                is_even = True
                            # sibling relationship not found, repeat the process of going down
                            else:
                                col_val = col_val - 1
                                if val == col_val:
                                    parents.append(col_val + 1)
                                    found = True
                                    break
                                else:
                                    # We want to simulate moving down the tree
                                    is_even = False
                                    ind = ind - 1

    return parents

