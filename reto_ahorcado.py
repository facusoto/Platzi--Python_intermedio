import random


def read_data():
    words = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words


def random_choise():
    words = read_data()
    random_word = random.choice(words)
    random_word_bars = ["_"] * len(random_word)
    return random_word, random_word_bars


def run():
    word = random_choise()[0]
    word_bars = random_choise()[1].join()
    print(word)
    print(word_bars)
    

if __name__ == '__main__':
    run()


# No tengo ganas de hacer esto. En otro momento que no 
# me duela el brazo ni tampoco este medio mareado, bye