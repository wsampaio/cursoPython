def computador_escolhe_jogada(n, m):
    pecas = m

    if n % (m+1) < m:
        pecas = n % (m+1)

    return pecas

def usuario_escolhe_jogada(n, m):

    jogada_ok = False
    pecas = -1

    while not jogada_ok:
        pecas = int(input("Quantas peças você vai tirar? "))
        jogada_ok = True

        if pecas > m or pecas < 1:
            print()
            print("Oops! Jogada inválida! Tente de novo.")
            print()
            jogada_ok = False

    if pecas > n:
        pecas = n

    return pecas

def partida():

    comp_play = True

    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    print()
    
    if n % (m+1) == 0:
        print("Voce começa!")
        comp_play = False
    else:
        print("Computador começa!")

    print()

    while n > 0:
        if comp_play:
            pecas_retiradas = computador_escolhe_jogada(n, m)
            n = n - pecas_retiradas
            comp_play = False

            if pecas_retiradas == 1:
                print("O computador tirou uma peça.")
            else:
                print("O computador tirou", pecas_retiradas, "peças.")

        else:
            pecas_retiradas = usuario_escolhe_jogada(n, m)
            n = n - pecas_retiradas
            comp_play = True

            if pecas_retiradas == 1:
                print("Você tirou uma peça.")
            else:
                print("Você tirou", pecas_retiradas, "peças.")

        if n > 1:
            print("Agora restam", n, "peças no tabuleiro.")
        elif n == 1:
            print("Agora resta uma peça no tabuleiro.")
        else:
            if comp_play:
                print()
                print("Fim do jogo! Você ganhou!")
            else:
                print()
                print("Fim do jogo! O computador ganhou!")
    
        print()



def campeonato():
    print("**** Rodada 1 ****")
    print()
    partida()
    print("**** Rodada 2 ****")
    print()
    partida()
    print("**** Rodada 3 ****")
    print()
    partida()
    print("**** Final do campeonato! ****")
    print("Placar: Você 0 X 3 Computador")
    print()
	
	# TODO - falta um jeito de somar o placar

print("Bem-vindo ao jogo do NIM! Escolha:")
print()
print("1 - para jogar uma partida isolada")
tipo_jogo = int(input("2 - para jogar um campeonato "))

print()

if tipo_jogo == 1:
    print("Voce escolheu partida isolada!")
    print()
    partida()
else:
    print("Voce escolheu um campeonato!")
    print()
    campeonato()





