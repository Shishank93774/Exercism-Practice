def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    def steps_helper(num):
        if num == 1:
            return 0
        return steps_helper(num//2) + 1 if (num&1 == 0) else steps_helper(3*num + 1) + 1

    return steps_helper(number)
