nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda note do aluno:"))
nota3 = float(input("Digite a terceira nota do aluno:"))

media = (nota1+nota2+nota3)/3

if media < 5:
    print("O aluno foi REPROVADO")
elif media == 5 or media < 6.9:
    print("o aluno ficou de RECUPERAÇÃO ")
else:
    print("O aluno foi APROVADO")
