import random 

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number: 
        guess = int(input('Digite um número entre 1 e {x}: '))
        if guess < random_number:
            print('Puts, seu número é menor, tente novamente.')
        elif guess > random_number:
            print('Puts, seu número é maior, tente novamente!')
    print(f'Parabéns, você acertou o número {random_number}.')

guess(10)