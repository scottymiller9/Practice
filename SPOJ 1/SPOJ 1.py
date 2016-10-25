def print_numbers():
    s = input()
    while s!=42:
        print(s)
        print_numbers()

print_numbers()