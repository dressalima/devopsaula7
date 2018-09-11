TAB = []

def validacao() :
	TAB.append(['.','.','.'])
	TAB.append(['.','.','.'])
	TAB.append(['.','.','.'])
def jogar(jogada, linha, coluna):
	if jogada !='X' and jogada != 'O':
		raise RuntimeError('Jogada inválida!')
	valores = list(range(0,3))
	if linha not in valores:
		raise RuntimeError('Linha inválida!')
	if coluna not in valores:
		raise RuntimeError('Coluna inválida!')
	TAB[linha][coluna] = jogada

def tabuleiro():
return TAB

def main():
validacao()
jogar('X', 1, 1)
print(tabuleiro())

if __name__ == "__main__":
main()
