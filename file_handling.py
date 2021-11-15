def read_file():
    numbers = []
    with open('assets/numbers.txt', 'r', encoding='utf-8') as f:
        for line in f:
            if line.replace('\n', '').isnumeric():
                numbers.append(int(line))
    print(numbers)


def write_file():
    names = ['Ingrd', 'Jonathan', 'Alberto', 'Monaliza', 'Luna', 'Foxy', 'Firulais', 'María']
    with open('assets/names.txt', 'a', encoding='utf-8') as f:
        for name in names:
            f.write(name)
            f.write('\n')


def main():
    read_file()
    write_file()


if __name__ == '__main__':
    main()