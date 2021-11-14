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
    print('PYTHON WORKERS USING COMPREHENSIONS --------------------------------')
    all_python_workers_comprehensions = [worker['name'] for worker in DATA if worker['language'] == 'python']
    print(all_python_workers_comprehensions)
    print('PYTHON WORKERS USING HIGH ORDER FUNCTIONS --------------------------')
    all_python_workers_lambda = list(filter(lambda worker: worker['language'] == 'python', DATA))
    all_python_workers_lambda = list(map(lambda worker: worker['name'], all_python_workers_lambda))
    print(all_python_workers_lambda)

    print('PLATZI WORKERS USING COMPREHENSIONS --------------------------------')
    all_platzi_workers_comprehensions = [worker['name'] for worker in DATA if worker['organization'] == 'Platzi']
    print(all_platzi_workers_comprehensions)
    print('PLATZI WORKERS USING HIGH ORDER FUNCTIONS --------------------------')
    all_platzi_workers_lambda = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    all_platzi_workers_lambda = list(map(lambda worker: worker['name'], all_platzi_workers_lambda))
    print(all_platzi_workers_lambda)

    print('ADULT WORKERS USING HIGH ORDER FUNCTIONS ---------------------------')
    adults_lambda = list(filter(lambda worker: worker['age'] >= 18, DATA))
    adults_lambda = list(map(lambda worker: worker['name'], adults_lambda))
    print(adults_lambda)
    print('ADULT WORKERS USING LIST COMPREHENSIONS ----------------------------')
    adults_comprehensions = [worker['name'] for worker in DATA if worker['age'] >= 18]
    print(adults_comprehensions)

    print('OLD WORKERS USING HIGH ORDER FUNCTIONS -----------------------------')
    old_people = list(map(lambda worker: {**worker , **{'old': worker['age'] > 70}}, DATA)) # Python < 3.8
    #old_people = list(map(lambda worker: worker | {'old': worker['age'] > 70}, DATA)) # Python >= 3.9
    print(old_people)


if __name__ == '__main__':
    main()