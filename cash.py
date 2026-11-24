# Estou aprendendo a programar e criei esse sistema simples para um trabalho da faculdade.
# Ideia principal: um mini sistema de apostas simuladas (sem dinheiro real) com login.
# Os times e os gols são sorteados com random.
# Entrada: usuário, senha, depósito e valor da aposta.
# Saída: mensagens de login, saldo, e se o jogador ganhou ou perdeu.

import random
from time import sleep

USUARIO_CORRETO = 'adm1'
SENHA_CORRETA = 'adm1234test'
MAX_TENTATIVAS = 3

TIMES_JOGADOR = [
    'Athletico Paranaense', 'Atlético Mineiro', 'Bahia', 'Botafogo',
    'Chapecoense', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Flamengo',
    'Fluminense',
]
TIMES_PC = [
    'Grêmio', 'Internacional', 'Mirassol', 'Palmeiras',
    'Red Bull Bragantino', 'Remo', 'Santos', 'São Paulo',
    'Vasco da Gama', 'Vitória',
]


def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um valor válido."""
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print('Digite apenas números inteiros.')


def autenticar():
    """Pede usuário e senha. Após 3 erros, espera um pouco e tenta de novo."""
    while True:
        for _ in range(MAX_TENTATIVAS):
            usuario = input('Insira o usuário: ')
            senha = input('Informe a senha: ')
            if usuario == USUARIO_CORRETO and senha == SENHA_CORRETA:
                return
            print('Usuário ou senha incorretos.')

        print('Muitas tentativas erradas. Tente de novo daqui a alguns segundos...')
        sleep(5)


def depositar():
    """Pede o valor do depósito inicial e devolve o saldo."""
    print('Seu saldo é de R$ 0, adicione fundos.')
    deposito = ler_inteiro('Valor do depósito: R$ ')
    while deposito <= 0:
        print('O depósito precisa ser maior que 0.')
        deposito = ler_inteiro('Valor do depósito: R$ ')

    print('Carregando depósito...')
    sleep(3)
    print('Adicionando fundos à conta...')
    sleep(4)
    return deposito


def aposta(saldo):
    """Faz uma rodada de aposta e devolve o novo saldo."""
    valor = ler_inteiro('Saldo: R$ {}. Quanto você quer apostar? R$ '.format(saldo))

    while valor <= 0 or valor > saldo:
        print('Valor inválido. Aposte mais que 0 e no máximo o seu saldo.')
        valor = ler_inteiro('Quanto você quer apostar? R$ ')

    time_jogador = random.choice(TIMES_JOGADOR)
    time_pc = random.choice(TIMES_PC)
    gols_jogador = random.randint(0, 8)
    gols_pc = random.randint(0, 8)

    print(f'\nResultado final: {time_jogador} {gols_jogador} x {gols_pc} {time_pc}')

    if gols_jogador > gols_pc:
        saldo += valor
        print('Você ganhou R$ {}!'.format(valor))
    elif gols_jogador < gols_pc:
        saldo -= valor
        print('Você perdeu R$ {}.'.format(valor))
    else:
        print('Empate, seu saldo não mudou.')

    print('Seu saldo agora é R$ {}'.format(saldo))
    return saldo


def main():
    autenticar()

    print('=' * 50)
    print('Logando...')
    print('=' * 50)
    sleep(5)
    print('Login realizado com sucesso!')
    sleep(2)

    saldo = depositar()
    print('Seu saldo agora é R$ {}'.format(saldo))

    while saldo > 0:
        saldo = aposta(saldo)

        if saldo == 0:
            print('Seu saldo acabou. Fim de jogo.')
            break

        if input('Apostar de novo? (s/n) ').strip().lower() != 's':
            print('Você saiu com R$ {}. Até a próxima!'.format(saldo))
            break


if __name__ == '__main__':
    main()
