def main():
    squares = [i**2 for i in range(1, 101) if i % 3 != 0]
    print(squares)

    divisibles_by_36 = [i for i in range(1,100000) if i % 36 == 0]
    print(divisibles_by_36)


if __name__ == '__main__':
    main()