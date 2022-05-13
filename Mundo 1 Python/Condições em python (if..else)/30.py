c=str(input("digite sim para começar: "))

while c == "sim":
    n=int(input("Digite um numero para ver se ele é par ou impar: "))

    if (n%2) == 0:
        print("Esse numero é par")
        c=str(input("deseja continuar? digite sim"))
        
    else:
        print("Esse numero é impar")
        c=str(input("deseja continuar? digite sim"))

print("voce decidiu parar.")

