def main():
    card = get_numbers()

    if is_valid(card):
        print(company(card))
    else:
        print("INVALID")

def get_numbers():
    while True:
        number = input("Number: ").strip()

        if number.isdigit():
            return number
        
def is_valid(number):
    sum1 = 0
    sum2 = 0

    for i in number[-2::-2]:
        i = int(i) * 2

        if i > 9:
            sum1 += (i % 10 + i // 10)
        else:
            sum1 += i

    for i in number[-1::-2]:
        sum2 += int(i)

    return (sum1 + sum2) % 10 == 0


def company(number):
    l = len(number)

    if number[:2] in ['34', '37'] and l == 15:
        return "AMEX"
    elif number[:2] in ['51', '52', '53', '54', '55'] and l == 16:
        return "MASTERCARD"
    elif number[0] == '4' and (l == 13 or l == 16):
        return "VISA"
    else:
        return "INVALID"
    
main()