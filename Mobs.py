# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 14:43:49 2019

@author: gabri

"""

bem = {1 : {'um Ninja': 'ataque' } , 2 : {'um amigo': 'ataque'  } , 3 : {'um cachorro': 'defesa' } , 4 : {'uma marmita': 'defesa' } , 5: {'uma máquina de café':'energia'} }
mal = {1: {'um veterano':{'Iniciar batalha':'batalha'}},2:{'um "amigo"':{'Ele copiou seu trabalho':"dano"}},3:{'uma nota ruim':{'Você ficou desanimado': 'defesa'}} ,4: {'um professor':{'Ele te lembrou de outro trabalho':'dano'}},5:{'uma goteira':{'Você se molhou e ficou lento':'ataque'}}}
import random
MOBS = random.randint(1,11)
mob = random.randint(1,5)
encontro = random.randint(1,2)
if encontro == 2:
    if MOBS % 2 == 0:
        sorte = random.randint(1,2)
        quem = bem[mob]
        for nome in quem:
            pessoa = nome
            stat = quem[pessoa]
        encontro_bom = ('Ganhou {0} de {1}'.format(sorte,stat))
        print('Voce encontrou {0}'.format(pessoa))
        print()
        print ('*' * len(encontro_bom))
        print(encontro_bom)
        print ('*' * len(encontro_bom))
    else:
        azar = random.randint(1,2)
        quem = mal[mob]
        for nome in quem:
            pessoa = nome
            ação = quem[pessoa]
            for action in ação:
                oque = action
                stat = ação[oque]
            if stat == 'dano':
                dano = azar
                encontro_ruim = ('Perdeu {0} de vida'.format(dano/Quantidade_de_defesa(defesa)))    
            else:        
                encontro_ruim = ('Perdeu {0} de {1}'.format(azar,stat))
        print ('Voce encontrou {0}'.format(pessoa))
        print(oque)
        if stat == 'batalha':
            sistema_de_batalha = True
        else:
            print()
            print('*'*len(encontro_ruim))
            print(encontro_ruim)
            print('*'*len(encontro_ruim))
        