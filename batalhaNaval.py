##defs
def criar_matriz(h,w):
    return [["-" for _ in range(w)] for _ in range(h)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    print()

def navios():
    count = 4
    for i in range(3):
        print(f"escolha o navio com {count} posicoes")
        colocar_navios(matriz, 1, count)
        count -= 1
        mostrar_matriz(matriz)

def colocar_navios(matriz, quantidade, count):
    for i in range(quantidade):
        while True:
            try:
                entrada = input(f"Escolha a posição inicial do seu navio (x y) com {count} posicoes: ")
                saida = input(f"escolha a posicao final do seu navio (x,y): ")
                x, y = map(int, entrada.split())
                xf, yf = map(int, saida.split())
                if (0 <= x < len(matriz) and 0 <= y < len(matriz)) and (0 <= xf < len(matriz) and 0 <= yf < len(matriz)):
                    if matriz[x][y] == "-":
                        if (x == xf) and (yf - y == count):
                            for i in range(count):
                                matriz[x][(y + i)] = "N"
                                var = f"{x}, {y + i}"
                                posicao.append(var)
                            break
                        elif (yf == y) and (xf - x == count):
                            for i in range(count):
                                matriz[(x + i)][y] = "N"
                                var = f"{x + i}, {y}"
                                posicao.append(var)
                            break
                        elif (x == y) and (xf == yf) and (xf - x == count):
                            for i in range(count):
                                matriz[(x + i)][y + i] = "N"
                                var = f"{x + i}, {y + i}"
                                posicao.append(var)
                            break
                        else:
                            print("o tamanho do barco esta diferente do numero de posicoes")
                    else:
                        print("Já existe um navio nessa posição. Tente novamente.")
                else:
                    print("Coordenadas fora do limite. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite dois números separados por espaço.")

# Programa principal
h = 5
w = 10
posicao = []
matriz = criar_matriz(h, w)
mostrar_matriz(matriz)
navios()
print(posicao)
#atualmente eu faco a lista e armazeno as posicoes, agora tenho que fazer o seguinte, validacao das posicoes E comecar o jogo contra o bot