def divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors


def main():
    number = int(input('Enter a number: '))
    print(divisors(number))


if __name__ == '__main__':
    main();