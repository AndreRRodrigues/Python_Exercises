'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da 
passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

km=int(input("quantos km e a viagem? "))
menor=0.50
maior=0.45

if km <= 200:
    me=menor*km
    print("A sua viagem de {}km custará R${} por ser menor ou igual a 200km".format(km, me))
else:
    ma=maior*km
    print("sua viagem de {}km cuatará R${} por ser maior que 200km".format(km, ma))