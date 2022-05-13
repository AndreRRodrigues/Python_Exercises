val = int(input("Digite um numero Inteiro: "))
print('''Escolha uma das bases para converção:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opção = int(input("Para qual base voce deseja converter? "))

if opção == 1:
    print("{} convertido para BINARIO é ingual a {}".format(val, bin(val)))
elif opção == 2:
    print("{} convertido para OCTAL é igual a {}".format(val, oct(val)))
else:
    print("{} convertido para HEXADECINAL é igual a {}".format(val, hex(val)))
