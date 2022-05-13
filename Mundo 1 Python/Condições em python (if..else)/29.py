velo=int(input('Qual a velocidade do carro? '))
lim=80
m=7

if velo > lim:
    mu=(velo-lim)*m
    print('Voce  foi multado em {}Reais por esta {}km acima da velocidade permitida'.format(mu, (velo-lim)))
else:
    print('voce nao esta acima da velocidade')