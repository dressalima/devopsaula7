import jogovelha
import sys
erroIniciali = False

jogovelha.inicializar()
jogar = jogovelha.tabuleiro()

if len(jogar) != 3:
  erroIniciali = True
else:
  for linha in jogar:
    if len(linha) != 3:
      erroIniciali= True
    else:
       for elemento in linha:
          if elemento != '.':
              erroIniciali = True

if erroIniciali:
    print('Erro!')
    sys.exit(1)
else:
    sys.exit(0)

