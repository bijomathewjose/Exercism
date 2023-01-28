def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    elif number==1:
        return 'deficient'
    total = sum(get_multiples(number))
    return 'perfect' if total == number else 'abundant' if total > number else 'deficient'
    pass


def get_multiples(number):
    multiples = []
    multiples.append(1)
    for value in range(2, (number//2)+1):
        if number % value == 0:
            multiples.append(value)
            multiples.append(number//value)
    return list(set(multiples))