file_name = "example.txt"
try:
    with open(file_name, 'r') as file:
        for line in file:
            print(line)


except FileNotFoundError:
    print(f" File'{file_name}'NotFoundError.")