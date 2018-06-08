def answer(xs):
    negatives = list()
    positives = list()
    for num in xs:
        if num > 0:
            positives.append(num)
        elif num < 0:
            negatives.append(num)

    negatives.sort()

    if len(negatives) % 2 != 0:
        _ = negatives.pop()

    combined = negatives + positives

    product = 1
    for i in range(len(combined)):
        product = product * combined[i]

    if product == 1:
        product = 0

    return str(product)
