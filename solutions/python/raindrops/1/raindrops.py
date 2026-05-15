def convert(number):
    return_string = ""
    if number%3 == 0:
        return_string += "Pling"
    if number%5 == 0:
        return_string += "Plang"
    if number%7 == 0:
        return_string += "Plong"
    if (number%3 and number%5 and number%7):
        return_string += str(number)

    return return_string
        
