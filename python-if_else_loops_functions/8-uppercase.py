def uppercase(str):
    for char in str:
        if char >= 'a' and char <= 'z':
            char = ord(char) - 32
            char = chr(char)
        print("{}".format(char), end='')
    print()
