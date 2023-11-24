def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (check_head(s) and check_for_symbols(s) and
            check_numbers(s) and check_length(s))


def check_head(s):
    return s[:2].isalpha()

def check_length(s):
    return 2 <= len(s) <= 6

def check_for_symbols(s):
    return s.isalnum()

def check_numbers(s):
    if s.isalpha():
        return True

    sub = ""

    for i in range(len(s)):
        if s[i].isdigit():
            sub = s[i:]
            break

    return sub.isdigit() and sub[0] != '0'


main()