##defs
def criar_matriz(tamanho):
    return [["-" for _ in range(tamanho)] for _ in range(tamanho)]

def mostrar_matriz(matriz):
    for linha in matriz:
        print(" ".join(linha))
    print()

def navios():
    count = 4
    for i in range(3):
        print(f"escolha o navio com {count} posicoes")
        colocar_navios(matriz, count)
        count -= 1
        mostrar_matriz(matriz)

def posicoes(x, y):
    posicoes = []
    posicoes.append(x,y)

def colocar_navios(matriz, quantidade):
    for i in range(quantidade):
        while True:
            try:
                entrada = input(f"Escolha a posição {i+1} do seu navio (x y): ")
                x, y = map(int, entrada.split())
                if 0 <= x < len(matriz) and 0 <= y < len(matriz):
                    if matriz[x][y] == "-":
                        matriz[x][y] = "N"  # Marca o navio
                        posicoes(x,y,)
                        break
                    else:
                        print("Já existe um navio nessa posição. Tente novamente.")
                else:
                    print("Coordenadas fora do limite. Tente novamente.")
            except ValueError:
                print("Entrada inválida. Digite dois números separados por espaço.")

# Programa principal

tamanho = 10
matriz = criar_matriz(tamanho)
mostrar_matriz(matriz)
navios()
## Agora preciso que