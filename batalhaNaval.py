import random

def criar_matriz(h, w):
    return [["-" for _ in range(w)] for _ in range(h)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    print()

def navios():
    count = 4
    counter = 4
    for i in range(3):
        print(f"Escolha o navio com {count} posições")
        colocar_navios(matriz, count)
        count -= 1
        mostrar_matriz(matriz)

    for i in range(3):
        print(f"Bot está posicionando navio com {counter} posições...")
        escolhas_bot(bot_matriz, counter)
        counter -= 1
        mostrar_matriz(bot_matriz)

def colocar_navios(matriz, count):
    while True:
        try:
            entrada = input(f"Escolha a posição inicial do seu navio (x y) com {count} posições: ")
            saida = input("Escolha a posição final do seu navio (x y): ")
            x, y = map(int, entrada.split())
            xf, yf = map(int, saida.split())

            if (0 <= x < h and 0 <= y < w and 0 <= xf < h and 0 <= yf < w):
                if (x == xf):
                    if abs(yf - y) == count - 1:
                        menor = min(y, yf)
                        if menor + count - 1 < w:
                            if all(matriz[x][menor + i] == "-" for i in range(count)):
                                posicao = []
                                for i in range(count):
                                    matriz[x][menor + i] = "N"
                                    posicao.append(f"{x}, {menor + i}")
                                posicaoTotal.append(posicao)
                                break
                elif (y == yf):
                    if abs(xf - x) == count - 1:
                        menor = min(x, xf)
                        if menor + count - 1 < h:
                            if all(matriz[menor + i][y] == "-" for i in range(count)):
                                posicao = []
                                for i in range(count):
                                    matriz[menor + i][y] = "N"
                                    posicao.append(f"{menor + i}, {y}")
                                posicaoTotal.append(posicao)
                                break
                elif abs(xf - x) == count - 1 and abs(yf - y) == count - 1:
                    menor_x = min(x, xf)
                    menor_y = min(y, yf)
                    if menor_x + count - 1 < h and menor_y + count - 1 < w:
                        if all(matriz[menor_x + i][menor_y + i] == "-" for i in range(count)):
                            posicao = []
                            for i in range(count):
                                matriz[menor_x + i][menor_y + i] = "N"
                                posicao.append(f"{menor_x + i}, {menor_y + i}")
                            posicaoTotal.append(posicao)
                            break
                else:
                    print("O tamanho ou direção do barco está incorreto.")
            else:
                print("Coordenadas fora dos limites. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite dois números separados por espaço.")

def escolhas_bot(matriz, count):
    while True:
        x = random.randint(0, h - 1)
        y = random.randint(0, w - 1)
        direcao = random.choice(['H', 'V', 'D'])  # H: horizontal, V: vertical, D: diagonal

        if direcao == 'H' and y + count - 1 < w:
            if all(matriz[x][y + i] == "-" for i in range(count)):
                posicao = []
                for i in range(count):
                    matriz[x][y + i] = "N"
                    posicao.append(f"{x}, {y + i}")
                posicaoTotalBot.append(posicao)
                break
        elif direcao == 'V' and x + count - 1 < h:
            if all(matriz[x + i][y] == "-" for i in range(count)):
                posicao = []
                for i in range(count):
                    matriz[x + i][y] = "N"
                    posicao.append(f"{x + i}, {y}")
                posicaoTotalBot.append(posicao)
                break
        elif direcao == 'D' and x + count - 1 < h and y + count - 1 < w:
            if all(matriz[x + i][y + i] == "-" for i in range(count)):
                posicao = []
                for i in range(count):
                    matriz[x + i][y + i] = "N"
                    posicao.append(f"{x + i}, {y + i}")
                posicaoTotalBot.append(posicao)
                break

# Programa principal
h = 5
w = 10
posicaoTotal = []
posicaoTotalBot = []
matriz = criar_matriz(h, w)
bot_matriz = criar_matriz(h, w)

mostrar_matriz(matriz)
navios()

print("Posições dos navios do jogador:")
print(posicaoTotal)
print("Posições dos navios do bot:")
print(posicaoTotalBot)
