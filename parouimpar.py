from random import randint

# cabeçalho
print('-' * 30)
print('PAR OU ÍMPAR: melhor de 3')
print('-' * 30)

# variaveis
cpuwins = 0
jwins = 0

# laço principal
while True:
    # escolhas do usuário
    j = int(input('digite um valor entre 0 e 10: '))
    if j > 10:
        print('você está trapaceando')
        break

    while True:
        pi = input('É par ou ímpar? [P/I]: ').upper().strip()
        if pi == 'P' or pi == 'I':
            break  # Sai do loop se a entrada for válida
        else:
            print("Por favor, insira apenas 'P' para par ou 'I' para ímpar.")

    cpu = randint(0, 10)
    total = j + cpu

    # resultado
    print('-' * 30)
    print(f'Você jogou {j} e a CPU jogou {cpu}, Total de {total}')
    print('-' * 30)

    # condições
    if (cpu + j) % 2 == 0 and pi == 'P':
        print('Jogador Vence')
        jwins += 1
        print(f'Você está com {jwins} vitorias e a CPU está {cpuwins} vitorias')
    elif (cpu + j) % 2 != 0 and pi == 'I':
        print('Jogador Vence')
        jwins += 1
        print(f'Você está com {jwins} vitorias e a CPU está {cpuwins} vitorias')
    elif (cpu + j) % 2 == 0 and pi != 'P':
        print('CPU vence')
        cpuwins += 1
        print(f'Você está com {jwins} vitorias e a CPU está {cpuwins} vitorias')
    elif (cpu + j) % 2 != 0 and pi != 'I':
        print('CPU vence')
        cpuwins += 1
        print(f'Você está com {jwins} vitorias e a CPU está {cpuwins} vitorias')

    print('-' * 30)

    # resultado final
    if cpuwins >= 2:
        print('=-' * 30)
        print('a CPU ganhou a melhor de 3')
        print('=-' * 30)
        break
    elif jwins >= 2:
        print('=-' * 30)
        print('Parabéns, você jogador venceu o par ou impar melhor de 3 com a CPU')
        print('=-' * 30)
        break
