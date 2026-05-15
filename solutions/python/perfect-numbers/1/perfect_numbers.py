def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    # if a number to be classified is less than 1.
    if number <= 0:
        raise ValueError("Classification is only possible for positive integers.")

    aliquot_sum = 0
    i = 1
    while i*i <= number:
        if number%i == 0:
            aliquot_sum += i
            if number != i*i:
                aliquot_sum += number/i
        i += 1

    aliquot_sum -= number
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    return "deficient"