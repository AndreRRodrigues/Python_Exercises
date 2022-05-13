from cgitb import reset
from pdb import Restart
from pydoc import doc
import random
print('Tente advinhar qual numero eu escoli.')
n=int(input('digite um numero: '))
r=[1, 2, 3, 4, 5]
rd=random.choice(r)
if n == rd :
    print('Você acertou o numero escolhido foi {}'.format(n))
else:
    print('voce errou mais sorte da proxima vez.')
