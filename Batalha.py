# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 07:38:52 2019

@author: gabri
"""



def batalhas(sistema_de_batalha,Health_bar):
    if sistema_de_batalha == True:
        print('Inicia Batalha')
        vida_inimigo = 5
        dano = 0
    while sistema_de_batalha == True :
        vida_inimigo = vida_inimigo - Quantidade_de_ataque(ataque)
        print ("Vida do seu Inimigo ==> {0}".format(vida_inimigo))
        if vida_inimigo <= 0:
            sistema_de_batalha = False
            return ('Você venceu')
        else:
            if Quantidade_de_defesa(defesa) > 0 :
                dano += 1
                dano_total += (dano/Quantidade_de_defesa(defesa))
            else:
                dano += 1 
                dano_total += dano
            if Health_bar(energia,dano,defesa) <= 0:
                print('Você perdeu a batalha')
                sistema_de_batalha = False
                game_over = True
            print(Health_bar(energia,dano,defesa))
            

        
