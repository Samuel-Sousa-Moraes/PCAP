from random import randrange

def varglobais():
  global escolhas, Continua
  escolhas = []
  Continua = True
  

def continuar():
  if (cont >= 9):
    Continua = False

def exibir():
  print("+-----------+")
  print("|",tabuleiro[0][0],"|",tabuleiro[0][1],"|",tabuleiro[0][2],"|")
  print("-------------")
  print("|",tabuleiro[1][0],"|",tabuleiro[1][1],"|",tabuleiro[1][2],"|")
  print("-------------")
  print("|",tabuleiro[2][0],"|",tabuleiro[2][1],"|",tabuleiro[2][2],"|")
  print("+-----------+")
  print("\n\n")

def computadorjoga():
  contaux = 0
  n = randrange(1,10)
  if n in escolhas:
    computadorjoga()
  else:
    print("Computador:",n)
    if n == 1:
      tabuleiro[0][0] = "O"
    elif n == 2:
      tabuleiro[0][1] = "O"
    elif n == 3:
      tabuleiro[0][2] = "O"
    elif n == 4:
      tabuleiro[1][0] = "O"
    elif n == 5:
      tabuleiro[1][1] = "O"
    elif n == 6:
      tabuleiro[1][2] = "O"
    elif n == 7:
      tabuleiro[2][0] = "O"
    elif n == 8:
      tabuleiro[2][1] = "O"
    elif n == 9:
      tabuleiro[2][2] = "O"
    else:
      print("O número digitado não corresponde a nenhuma casa.\n\n")
    escolhas.append(n)

def escolhercasa(n):
  contaux = 0
  if n in escolhas:
    print("Essa casa já foi escolhida, escolha outra!")
    x = int(input("Digite um número de 1 a 9: "))
    escolhercasa(x)
  else:
    if n == 1:
      tabuleiro[0][0] = "X"
    elif n == 2:
      tabuleiro[0][1] = "X"
    elif n == 3:
      tabuleiro[0][2] = "X"
    elif n == 4:
      tabuleiro[1][0] = "X"
    elif n == 5:
      tabuleiro[1][1] = "X"
    elif n == 6:
      tabuleiro[1][2] = "X"
    elif n == 7:
      tabuleiro[2][0] = "X"
    elif n == 8:
      tabuleiro[2][1] = "X"
    elif n == 9:
      tabuleiro[2][2] = "X"
    else:
      print("O número digitado não corresponde a nenhuma casa.\n\n")
      x = int(input("Digite um número de 1 a 9: "))
      escolhercasa(x)
    escolhas.append(n)

def ganhador():
  if (tabuleiro[0][0] == "X") and (tabuleiro[0][1] == "X") and (tabuleiro[0][2] == "X"):
    return 1
  elif (tabuleiro[1][0] == "X") and (tabuleiro[1][1] == "X") and (tabuleiro[1][2] == "X"):
    return 1  
  elif (tabuleiro[2][0] == "X") and (tabuleiro[2][1] == "X") and (tabuleiro[2][2] == "X"):
    return 1
  elif (tabuleiro[0][0] == "X") and (tabuleiro[1][0] == "X") and (tabuleiro[2][0] == "X"):
    return 1
  elif (tabuleiro[0][1] == "X") and (tabuleiro[1][1] == "X") and (tabuleiro[2][1] == "X"):
    return 1
  elif (tabuleiro[0][2] == "X") and (tabuleiro[1][2] == "X") and (tabuleiro[2][2] == "X"):
    return 1
  elif (tabuleiro[0][0] == "X") and (tabuleiro[1][1] == "X") and (tabuleiro[2][2] == "X"):
    return 1
  elif (tabuleiro[0][2] == "X") and (tabuleiro[1][1] == "X") and (tabuleiro[2][0] == "X"):
    return 1
  else:
    if (tabuleiro[0][0] == "O") and (tabuleiro[0][1] == "0") and (tabuleiro[0][2] == "O"):
      return 2
    elif (tabuleiro[1][0] == "O") and (tabuleiro[1][1] == "O") and (tabuleiro[1][2] == "O"):
      return 2
    elif (tabuleiro[2][0] == "O") and (tabuleiro[2][1] == "O") and (tabuleiro[2][2] == "O"):
      return 2
    elif (tabuleiro[0][0] == "O") and (tabuleiro[1][0] == "O") and (tabuleiro[2][0] == "O"):
      return 2
    elif (tabuleiro[0][1] == "O") and (tabuleiro[1][1] == "O") and (tabuleiro[2][1] == "O"):
      return 2
    elif (tabuleiro[0][2] == "O") and (tabuleiro[1][2] == "O") and (tabuleiro[2][2] == "O"):
      return 2
    elif (tabuleiro[0][0] == "O") and (tabuleiro[1][1] == "O") and (tabuleiro[2][2] == "O"):
      return 2
    elif (tabuleiro[0][2] == "O") and (tabuleiro[1][1] == "O") and (tabuleiro[2][0] == "O"):
      return 2

    
tabuleiro = [["1","2","3"],["4","5","6"],["7","8","9"]]
varglobais()
cont = 0

exibir()

while True:
  n = int(input("Digite um número de 1 a 9: "))
  escolhercasa(n)
  cont += 1
  if ganhador() == 1:
    print("Parabéns jogador, você ganhou!")
    exibir()
    break
  if cont == 5:
    exibir()
    break
  computadorjoga()
  if ganhador() == 2:
    print("O computador ganhou!")
    exibir()
    break
  exibir()

print("Fim de jogo!")
