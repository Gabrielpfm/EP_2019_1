# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 08:53:13 2019

@author: gabri
"""

def Quantidade_de_ataque(ataque):
    força = 1 + ataque
    return força

def Quantidade_de_defesa(defesa):
    defence = 1 + defesa
    return defence   
    
def Health_bar(energia,dano,defesa):
    life  = 3 + energia - (dano/Quantidade_de_defesa(defesa))
    return life 

