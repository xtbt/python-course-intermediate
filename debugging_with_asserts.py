def divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors


def main():
    number = input('Enter a number: ')
    assert number.isnumeric() and int(number) >= 0, 'Only positive numbers are allowed'
    print(divisors(int(number)))
    print('END OF PROGRAM')


if __name__ == '__main__':
    main();