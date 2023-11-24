def main():
    mario(get_number())


def get_number():
    while True:
        number = int(input("Number: "))

        if 0 < number < 9:
            return number
        
def mario(n):
    for i in range(n + 1):
        print(" " * (n - i), "#" * i, end=" ")

        print("#" * i)


main()