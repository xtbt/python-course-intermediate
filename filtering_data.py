DATA = [
    {
        'name': 'Facundo',
        'age': 72,
        'organization': 'Platzi',
        'position': 'Technical Coach',
        'language': 'python',
    },
    {
        'name': 'Luisana',
        'age': 33,
        'organization': 'Globant',
        'position': 'UX Designer',
        'language': 'javascript',
    },
    {
        'name': 'Héctor',
        'age': 19,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'ruby',
    },
    {
        'name': 'Gabriel',
        'age': 20,
        'organization': 'Platzi',
        'position': 'Associate',
        'language': 'javascript',
    },
    {
        'name': 'Isabella',
        'age': 30,
        'organization': 'Platzi',
        'position': 'QA Manager',
        'language': 'java',
    },
    {
        'name': 'Karo',
        'age': 23,
        'organization': 'Everis',
        'position': 'Backend workereloper',
        'language': 'python',
    },
    {
        'name': 'Ariel',
        'age': 32,
        'organization': 'Rappi',
        'position': 'Support',
        'language': '',
    },
    {
        'name': 'Juan',
        'age': 17,
        'organization': '',
        'position': 'Student',
        'language': 'go',
    },
    {
        'name': 'Pablo',
        'age': 32,
        'organization': 'Master',
        'position': 'Human Resources Manager',
        'language': 'python',
    },
    {
        'name': 'Lorena',
        'age': 56,
        'organization': 'Python Organization',
        'position': 'Language Maker',
        'language': 'python',
    },
]

def main():
    all_python_workers = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print('PYTHON WORKERS --------------------------------------------')
    print(all_python_workers)

    all_platzi_workers = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print('PLATZI WORKERS --------------------------------------------')
    print(all_platzi_workers)

    adults = list(filter(lambda worker: worker['age'] > 18, DATA))
    print('ADULT WORKERS ---------------------------------------------')
    print(adults)

    adults = list(map(lambda worker: worker['name'], adults))
    print('ADULT WORKERS (ONLY NAMES) --------------------------------')
    print(adults)

    old_people = list(map(lambda worker: {**worker , **{'old': worker['age'] > 70}}, DATA)) # Python < 3.8
    #old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) # Python >= 3.9
    print('OLD WORKERS -----------------------------------------------')
    print(old_people)


if __name__ == '__main__':
    main()