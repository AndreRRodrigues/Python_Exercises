c = str(input("Digite sim para começar: "))

while c == "sim":

    ano=int(input("digite um ano: "))

    if (ano % 4) == 0 and ano % 100 != 0 or ano % 400 == 0:
        print("É um ano bisexto")

    else:
        print("Nao e um ano bisexto")