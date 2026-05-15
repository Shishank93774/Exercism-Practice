def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    decimal_representation = 0
    place_value = 1
    for digit in reversed(digits):
        if digit >= input_base or digit < 0:
            raise ValueError("all digits must satisfy 0 <= d < input base")
        decimal_representation = decimal_representation + place_value * digit

        place_value *= input_base

    if decimal_representation == 0:
        return [0]

    rebase_digits = []
    place_value = 1
    while(decimal_representation > 0):
        digit = decimal_representation % output_base
        rebase_digits.append(digit)
        decimal_representation = decimal_representation // output_base

    rebase_digits = rebase_digits[::-1]

    return rebase_digits
        
