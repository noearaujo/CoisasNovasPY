# Essa é a nova formatação de strings do Python 3

#Variaveis
n = 'Noé' #nome 
s = 'Araújo' #sobrenome

#1. Metodo simples de usar format com f (f-strings)
f'Meu nome é {n} de {s}' #forma que exibe direto, no sonsole do Python
print(f'Meu nome é {n} de {s}') #Vou mostrar na tela

#1.1 As aspas triplas (''' ou """) tambem pode ser usada para expressar varias linhas aos inves de quebralas (\n)
f'''Meu nome é {n}
de {s}"""
print(f'''Meu nome é {n}
de {s}''')

#2. Metodo de usar o format com .format(), sendo que as chaves {} seriam mascaras
'Meu nome é {} de {}'.format(n, s)
print('Meu nome é {} de {}'.format(n, s))

#2.1 Usando as aspas triplas
'''Meu nome é {} 
de {}'''.format(n, s)
print('''Meu nome é {}
de {}'''.format(n, s))

#3.
'''
Não entendi, como é que se quebra as linhas com \n?
É  muito simples! 
Ao inves de você quebrar a linha manualmente, como fiz anteriomente (Enter), 
eu faço 1 linha só e coloco \n nos lugares que quero quebrar.
'''
f'Meu nome é {n} \n de {s}'
