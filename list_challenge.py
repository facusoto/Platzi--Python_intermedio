def run():

    # lst = []
    # for i in range(1, 101):
    #     if i % 3 != 0:
    #         lst.append(i*i)

    lst = [i for i in range(1, 900) if i % 36 == 0]

    print(f'Lista normal: {lst}')

if __name__ == '__main__':
    run()