# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriel Pascua de Freitas Moreira, gabrielpfm@al.insper.edu.br
# - aluno B: Gabriel Huerta Façanha, gabrielhf@al.insper.edu.br
import json
import random

def carregar_cenarios():
    with open('cenarios.json','r',encoding = 'utf-8') as arquivo:
        cenarios = json.load(arquivo)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

bem = {1 : {'um Ninja': 'ataque' } , 2 : {'um amigo': 'ataque'  } , 3 : {'um cachorro': 'defesa' } , 4 : {'uma marmita': 'defesa' } , 5: {'uma máquina de café':'energia'} }
mal = {1: {'um veterano':{'Iniciar batalha':'batalha'}},2:{'um "amigo"':{'Ele copiou seu trabalho':"dano"}},3:{'uma nota ruim':{'Você ficou desanimado': 'defesa'}} ,4: {'um professor':{'Ele te lembrou de outro trabalho':'dano'}},5:{'uma goteira':{'Você se molhou e ficou lento':'ataque'}}}

def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    def Quantidade_de_ataque(ataque):
        força = 1 + ataque
        return força

    def Quantidade_de_defesa(defesa):
        defence = 1 + defesa
        return defence   
        
    def Health_bar(energia,dano,defesa):
        life  = 3 + energia - (dano/Quantidade_de_defesa(defesa))
        return life 
    
    def tracinho(nome_cenario_atual):
        traco = '-' * len(nome_cenario_atual)
        return traco
    game_over = False
    encontros = False
    defesa = 0
    energia = 0
    ataque = 0
    dano = 0
    dano_total = 0
        
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        titulo = cenario_atual['titulo']
        descricao = cenario_atual['descricao']
                
        print (titulo)
        print (tracinho(titulo))
        print (descricao)
        print()
        print("Stats")
        print("Sua vida é {0}".format(Health_bar(energia,dano,defesa)))
        print("Sua defesa é {0}".format(Quantidade_de_defesa(defesa)))
        print("Seu ataque é {0}".format(Quantidade_de_ataque(ataque)))
        dano = 0
        if encontros == True:
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
                        if stat == "ataque":
                            ataque += sorte
                            
                        elif stat == "defesa":
                            defesa += sorte
                            
                        elif stat == "energia":
                            energia += sorte
                            
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
                                
                                dano += azar
                                dano_total += dano
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
                            if stat == "ataque":
                                ataque += (-azar)
                                
                            elif stat == "defesa":
                                 defesa += (-azar)
                                
                    encontros = False
       
        encontros = True
        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            escolha = ""
            print ()
            print ('Qual será sua escolha?')
            print ()
            for opcao in opcoes:
                print ('"{0}" : {1}'.format(opcao,opcoes[opcao]))
                print ()
            
            escolha = input('Digite aqui => ')
            if escolha in opcoes:
                if escolha == 'relaxar':
                    print()
                    print(' nao implementado ')
                    print(' aqui, aparece algo como: "perdeu tempo à toa!"')
                    print()
                elif escolha == 'estudar':
                    print()
                    print(' nao implementado ')
                    print('aqui, vai aparecer o mob "amigo"')
                    print()
                elif  escolha == 'atendimento':
                    print()
                    print(' nao implementado ')
                    print('aqui, vai entrar no modo luta e ganhar um item')
                    print()                    
                else:    
                    nome_cenario_atual = escolha
                print()
            else:
                print(" ----------------------------")
                print("Sua indecisão foi sua ruína!")
                print(" ----------------------------")
                game_over = True

    print("Você morreu!")
    print()
    
# Programa principal.
if __name__ == "__main__":
    main()
