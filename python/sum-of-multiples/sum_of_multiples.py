def sum_of_multiples(limit, multiples):
    root = {number*multiple for multiple in multiples if not multiple==0 for number in range(
        1, (limit//multiple)+1) if number*multiple < limit}
    return sum(root)
    pass
