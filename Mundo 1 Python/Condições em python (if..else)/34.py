salario = float(input("qual é o seu salario? R$ "))

if salario >= 1250:
    sal = salario * (10/100)
    print(salario + sal)

else:
    sal = salario * (15/100)
    print(salario + sal)