def is_armstrong_number(number):
    required_sum = number
    sum = 0
    num_dig = len(str(number))
    while number > 0:
        dig = number % 10
        sum += dig**num_dig

        number //= 10

    return required_sum == sum
    
