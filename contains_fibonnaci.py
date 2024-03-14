def contains_fibonacci(number: int):
    if number == 0 or number == 1:
        return True
    
    array = [0, 1]

    while array[1] <= number:
        array[0], array[1] = array[1], array[0] + array[1]

        value = array[0] + array[1]

        if value == number:
            return True
        
    return False
        
print(contains_fibonacci(21))