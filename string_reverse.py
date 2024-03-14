def string_reverse(string: str):
    new_string = ''
    size = len(string) - 1

    for caractere in range(size, -1, -1):
        new_string += string[caractere]

    return new_string


new_string = string_reverse('paralelepipedo')
print(new_string)