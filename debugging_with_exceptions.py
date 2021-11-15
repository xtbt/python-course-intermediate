def divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors


def main():
    while True:
        try:
            number = int(input('Enter a number: '))
            if number < 0:
                raise ValueError('Error!')
            print(divisors(number))
            break;
        except ValueError:
            print('You must enter a positive number.')


if __name__ == '__main__':
    main();