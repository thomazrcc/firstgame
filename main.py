######### JOGO DA VELHA ###########
import random


user_score = 0
computer_score = 0

opcoes = ['r', 't', 'p']

while True:
   
    resposta = input('Digite R para Pedra / T para tesoura / P para papel / Q para sair: ').lower()
    if resposta == 'q':
        print('Jogo terminado!')

        break

    if resposta not in opcoes:
        continue

    resposta_computador = random.randint(0, 2)
    # 0 = r / 1 = t / 2 = p
    resposta_computador = opcoes[resposta_computador]

    print('O computador escolheu ' + resposta_computador)

   


    if resposta == resposta_computador:
        print('Empate!')

    elif resposta == 'r' and resposta_computador == 't':
        print('Você Ganhou!')
        user_score = user_score + 1

    elif resposta == 't' and resposta_computador == 'p':
        print('Você Ganhou!')
        user_score = user_score + 1
        
    elif resposta == 'p' and resposta_computador == 'r':
        print('Você Ganhou!')
        user_score = user_score + 1
        
    else:
        print('Você Perdeu!')
        computer_score = computer_score + 1

    print(f'Sua porntuação é: ' + str(user_score))
    print(f'Pontuação do computador: ' + str(computer_score))







print('Jogo terminado!')



