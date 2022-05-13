from datetime import date

ano = date.today().year

ano_nacsimento = int(input("Qual é o seu ano de nacimento? "))
idade = ano - ano_nacsimento
print("quem nasceu em {} tem {} anos em {}".format(ano_nacsimento, idade, ano))

if idade < 18:
    print("falta {} anos pro seu alistamento".format( 18 - idade ))
elif idade == 18:
    print("Voce tem que se alistar imediatamente!")
elif idade > 18:
    print("Ja passou da idade de voce se alistar voce deveria ter se alistado a {} anos atras".format(idade-18))

