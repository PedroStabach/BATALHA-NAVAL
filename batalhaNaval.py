##imports
import random

##defs
def criar_matriz(h,w):
    return [["-" for _ in range(w)] for _ in range(h)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    print()

def navios():
    count = 4
    counter = 4
    for i in range(3):
        ##PLAYER
        print(f"escolha o navio com {count} posicoes")
        colocar_navios(matriz, count)
        count -= 1
        mostrar_matriz(matriz)
    for i in range(3):
        ##BOT
        escolhas_bot(counter)
        counter -= 1
        mostrar_matriz(matriz)
        


def colocar_navios(matriz, count):
    while True:
        try:
            entrada = input(f"Escolha a posição inicial do seu navio (x,y) com {count} posicoes: ")
            saida = input(f"escolha a posicao final do seu navio (x,y): ")
            x, y = map(int, entrada.split())
            xf, yf = map(int, saida.split())
            if (0 <= x < len(matriz) and 0 <= y < len(matriz)) and (0 <= xf < len(matriz) and 0 <= yf < len(matriz)):
                if matriz[x][y] == "-":
                    posicao = []
                    if (x == xf) and (yf - y == (count - 1)):
                        for i in range((count)):
                            matriz[x][(y + i)] = "N"
                            var = f"{x}, {y + i}"
                            posicao.append(var)
                        posicaoTotal.append(posicao)
                        break
                    elif (yf == y) and (xf - x == (count - 1)):
                        for i in range((count)):
                            matriz[(x + i)][y] = "N"
                            var = f"{x + i}, {y}"
                            posicao.append(var)
                        posicaoTotal.append(posicao)
                        break
                    elif (x == y) and (xf == yf) and (xf - x == (count - 1)):
                        for i in range((count)):
                            matriz[(x + i)][y + i] = "N"
                            var = f"{x + i}, {y + i}"
                            posicao.append(var)
                        posicaoTotal.append(posicao)
                        break
                    else:
                        print("o tamanho do barco esta diferente do numero de posicoes")
                else:
                    print("Já existe um navio nessa posição. Tente novamente.")
            else:
                print("Coordenadas fora do limite. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite dois números separados por espaço.")

def escolhas_bot(count):
    matriz = [["-" for _ in range(w)] for _ in range(h)]
    while True:
        escolha = [f"{i}"for i in range(5)], [f"{i}"for i in range(10)]
        x = int(random.choice(escolha[0]))
        y = int(random.choice(escolha[1]))
        xf = int(random.choice(escolha[0]))
        yf = int(random.choice(escolha[1]))
        if (0 <= x < len(matriz) and 0 <= y < len(matriz)) and (0 <= xf < len(matriz) and 0 <= yf < len(matriz)):
            if matriz[x][y] == "-":
                posicao = []
                if (x == xf) and (yf - y == (count - 1)):
                    for i in range((count)):
                        matriz[x][(y + i)] = "N"
                        var = f"{x}, {y + i}"
                        posicao.append(var)
                    posicaoTotalBot.append(posicao)
                    break
                elif (yf == y) and (xf - x == (count - 1)):
                    for i in range((count)):
                        matriz[(x + i)][y] = "N"
                        var = f"{x + i}, {y}"
                        posicao.append(var)
                    posicaoTotalBot.append(posicao)
                    break
                elif (x == y) and (xf == yf) and (xf - x == (count - 1)):
                    for i in range((count)):
                        matriz[(x + i)][y + i] = "N"
                        var = f"{x + i}, {y + i}"
                        posicao.append(var)
                    posicaoTotalBot.append(posicao)
                    break

# Programa principal
h = 5
w = 10
posicaoTotal = []
posicaoTotalBot = []
matriz = criar_matriz(h, w)
mostrar_matriz(matriz)
navios()
print(posicaoTotal)
print(posicaoTotalBot)
#comecar o jogo contra o bot