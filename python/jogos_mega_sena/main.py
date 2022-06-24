import random
import datetime


def get_jogo():
    all_numbers = [x for x in range(1, 61)]
    returned_number = []

    for _ in range(6):
        randon_number = random.randint(0, len(all_numbers)-1)
        returned_index = all_numbers.pop(randon_number)
        returned_number.append('{:02}'.format(returned_index))

    returned_number.sort()

    return returned_number


if __name__ == '__main__':

    print("Digiti aqui a quantidade de jogos da mega que deseje: ")
    number_games = int(input())

    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('jogos.txt', 'a') as f:
        f.write('===============================\n')
        f.write(f'Jogo criado em {date_time}\n')
        f.write(f'Quantidade de jogos: {number_games}\n')

    print()
    for i in range(number_games):
        print(f'Jogo {i+1}:')
        sep = '-'
        jogo = get_jogo()
        jogo_print = sep.join(jogo)
        print(jogo_print + '\n')

        with open('jogos.txt', 'a') as f:
            f.write('\t'+jogo_print + '\n')

    with open('jogos.txt', 'a') as f:
        f.write('\n')