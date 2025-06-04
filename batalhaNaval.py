import random
def criar_matriz(h, w):
    return [["-" for _ in range(w)] for _ in range(h)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    print()

def navios():
    count = 5
    counter = 5
    for i in range(5):
        ## PLAYER
        print(f"Escolha o navio com {count} posições")
        colocar_navios(matriz, count)
        count -= 1
        mostrar_matriz(matriz)
    for i in range(5):
        ## BOT
        escolhas_bot(matriz_bot, counter)
        counter -= 1

def colocar_navios(matriz, count):
    while True:
        try:
            entrada = input(f"Escolha a posição inicial do seu navio (x y) com {count} posições: ")
            saida = input(f"Escolha a posição final do seu navio (x y): ")
            x, y = map(int, entrada.split())
            xf, yf = map(int, saida.split())

            if x > xf:
                x, xf = xf, x
            if y > yf:
                y, yf = yf, y

            if (0 <= x < len(matriz) and 0 <= y < len(matriz[0]) and 
                0 <= xf < len(matriz) and 0 <= yf < len(matriz[0])):

                if matriz[x][y] == "-":
                    posicao = []

                    if (x == xf) and abs(yf - y) == count - 1:
                        for i in range(count):
                            matriz[x][y + i] = "N"
                            posicao.append(f"{x}, {y + i}")
                        posicaoTotal.append(posicao)
                        break
                    elif (y == yf) and abs(xf - x) == count - 1:
                        for i in range(count):
                            matriz[x + i][y] = "N"
                            posicao.append(f"{x + i}, {y}")
                        posicaoTotal.append(posicao)
                        break
                    elif abs(xf - x) == count - 1 and abs(yf - y) == count - 1:
                        for i in range(count):
                            matriz[x + i][y + i] = "N"
                            posicao.append(f"{x + i}, {y + i}")
                        posicaoTotal.append(posicao)
                        break
                    else:
                        print("O tamanho do barco está diferente do número de posições.")
                else:
                    print("Já existe um navio nessa posição. Tente novamente.")
            else:
                print("Coordenadas fora do limite. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite dois números separados por espaço.")

def escolhas_bot(matriz, count):
    while True:
        x = random.randint(0, h - 1)
        y = random.randint(0, w - 1)
        orientacao = random.choice(["H", "V"])

        posicao = []

        if orientacao == "H" and y + count <= w:
            if all(matriz[x][y + i] == "-" for i in range(count)):
                for i in range(count):
                    matriz[x][y + i] = "N"
                    posicao.append(f"{x}, {y + i}")
                posicaoTotalBot.append(posicao)
                break
        elif orientacao == "V" and x + count <= h:
            if all(matriz[x + i][y] == "-" for i in range(count)):
                for i in range(count):
                    matriz[x + i][y] = "N"
                    posicao.append(f"{x + i}, {y}")
                posicaoTotalBot.append(posicao)
                break

def atirar():
    while True:
        try:
            tiro = input("Onde deseja atirar (x, y): ")
            x, y = map(int, tiro.split(","))
            if not (0 <= x < h and 0 <= y < w):
                print("Coordenadas fora dos limites.")
                continue
            valor = f"{x}, {y}"
            acertou = any(valor in navio for navio in posicaoTotalBot)
            if acertou:
                print("Acertou!")
                for navio in posicaoTotalBot:
                    if valor in navio:
                        navio.remove(valor)
                        if not navio:
                            posicaoTotalBot.remove(navio)
                matriz_tiro_player[x][y] = "X"
                break
            else:
                print("Errou!")
                matriz_tiro_player[x][y] = "O"
                break
        except ValueError:
            print("Entrada inválida. Use o formato: x, y")

def atirarBot():
    while True:
        tirox = random.randint(0, h - 1)
        tiroy = random.randint(0, w - 1)
        valor = f"{tirox}, {tiroy}"
        print(f"Bot atirou na posição {valor}")
        acertou = any(valor in navio for navio in posicaoTotal)
        if acertou:
            print("Bot acertou!")
            for navio in posicaoTotal:
                if valor in navio:
                    navio.remove(valor)
                    if not navio:
                        posicaoTotal.remove(navio)
            matriz_tiro_bot[tirox][tiroy] = "X"
        else:
            print("Bot errou!")
            matriz_tiro_bot[tirox][tiroy] = "O"
        break

def jogar():
    while posicaoTotal and posicaoTotalBot:
        mostrar_matriz(matriz_tiro_player)
        print("Sua vez:")
        atirar()
        if not posicaoTotalBot:
            print("Parabéns! Você venceu!")
            break
        print("\nVez do bot:")
        atirarBot()
        mostrar_matriz(matriz_tiro_bot)
        if not posicaoTotal:
            print("O bot venceu! Fim de jogo.")
            break
        sumLenPlayer = len(posicaoTotal)
        sumLenBot = len(posicaoTotalBot)
        print(f"Seus navios restantes: {sumLenPlayer}")
        print(f"Navios do bot restantes: {sumLenBot}")

# Programa principal
h = 10
w = 10
posicaoTotal = []
posicaoTotalBot = []

matriz = criar_matriz(h, w)
matriz_bot = criar_matriz(h, w)
matriz_tiro_player = criar_matriz(h,w)
matriz_tiro_bot = criar_matriz(h,w)
mostrar_matriz(matriz)
navios()

# Começar o jogo
jogar()