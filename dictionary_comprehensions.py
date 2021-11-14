import math
def main():
    my_dictionary = {i: i**3 for i in range(1,101)}
    print('CUBIC NUMBERS -------')
    print (my_dictionary)

    not_divisible_by_3 = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print('CUBIC NUMBERS NOT DIVISIBLE BY 3 -------')
    print (not_divisible_by_3)

    first_1000_with_sqrt = {i: math.sqrt(i) for i in range (1,1001)}
    print('FIRST 1000 NUMBERS AS KEYS, AND RESPECTIVE SQRT AS VALUES -------')
    print(first_1000_with_sqrt)


if __name__ == '__main__':
    main()