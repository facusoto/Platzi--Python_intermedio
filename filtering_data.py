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
        'position': 'Backend Developer',
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

def run():
    # Agrega el nombre del "worker" luego del ciclo for si el "worker" tiene la llave "language" == "python"
    all_python_devs = [worker["name"] for worker in DATA if worker["language"] == "python"]

    # Lo mismo pero con llave "organization" == "platzi"
    all_platzy_workers = [worker["name"] for worker in DATA if worker["organization"] == "Platzi"]

    # Utiliza filter() con los objetos DATA (A iterar) y lambda, el cual a su vez con el argumento "worker" busca dentro
    # de la lista de diccionarios donde "age" sea > 18 y luego lo enlista con list()
    adults = list(filter(lambda worker: worker["age"] > 18, DATA))

    # Utiliza map() con los objetos adults (El cual es la variable anterior) y lambda, el cual a su vez con el 
    # argumento "worker" busca dentro de la lista de diccionarios "name" simplemente y luego lo enlista con list()
    adults = list(map(lambda worker: worker["name"], adults))

    # Lo mismo anterior, solo que ahora map() esta agregando una llave nueva a cada uno de los diccionarios
    # devolviendo True o False de acuerdo al if > 70
    old_people = list(map(lambda worker: worker | {"old": worker["age"] > 70}, DATA))

    # Itera todo a la vez porque flojera...
    for worker in all_python_devs, all_platzy_workers, adults, old_people:
        print(worker)

if __name__ == '__main__':
    run()