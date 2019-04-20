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

bem = {1:{"um Ninja":"ataque"},2:{"um amigo":"ataque"},3:{"um cachorro":"defesa"},
       4:{"uma marmita":"defesa"},5:{"uma máquina de café":"energia"}}

mal = {1:{"um veterano" : {"Iniciar Batalha":"batalha"}},
2:{"um 'amigo'" : {"Ele copiou seu trabalho":"dano"}},
3:{"uma nota ruim":{"Você ficou desanimado": "defesa"}},
4:{"um professor":{"Ele te lembrou de outro trabalho":"dano"}},
5:{"uma goteira":{"Você se molhou e ficou lento":"ataque"}}}

itens = {1:"E-mail do atendimento",2:"Caixa de chocolate",3:"Vida extra"}
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
    print('***')
    print("Faça suas escolhas em 'Digite aqui'. Atenção: você tem 30 rodadas disponíveis, mas as opções "
          "'stats' e 'inventário' não gastam rodadas. ")
    print('***')
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()
    def Quantidade_de_ataque(ataque):
        força = 1 + ataque
        return força

    def Quantidade_de_defesa(defesa):
        defence = 1 + defesa
        return defence   
        
    def Health_bar(energia,dano_total):
        life  = 3 + energia - (dano_total)
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
    dano_total = 0.0
    sistema_de_batalha = False 
    inventario ={}
    item_drop = False
    vitoria = False
    rodadas = 0
    maximo_de_rodadas = 30
    retry = True
    uma_vez = False
    
    while retry == True:
        if game_over == True:
                game_over = False
                encontros = False
                defesa = 0
                energia = 0
                ataque = 0
                dano = 0
                dano_total = 0.0
                sistema_de_batalha = False 
                inventario ={}
                item_drop = False
                vitoria = False
                uma_vez = False
                rodadas = 0
                maximo_de_rodadas = 30
                nome_cenario_atual = "inicio"
                print("Limpando Salas...")
                print("Restaurando Mobs...")
                print("Retirando Itens...")
                print("Reinicio Pronto")
                start = input("Digite algo para iniciar: ")
                if start == True:
                    print("Not here")
                else:
                    print(tracinho(("Na hora do sufoco!")))
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
        
        while not game_over and rodadas <= maximo_de_rodadas:
            cenario_atual = cenarios[nome_cenario_atual]
            titulo = cenario_atual['titulo']
            descricao = cenario_atual['descricao']
            if nome_cenario_atual == "barbara":
                inventario["EP finalizado"] = 1
                print(tracinho("Você ganhou: EP finalizado"))
                print("Parabéns!")
                print("Você ganhou: EP finalizado")
                print(tracinho("Você ganhou: EP finalizado"))
            print(tracinho("Você tem {0} rodada(s) restante(s)".format(maximo_de_rodadas-rodadas)))
            print("Você tem {0} rodada(s) restante(s)".format(maximo_de_rodadas-rodadas))
            print(tracinho("Você tem {0} rodada(s) restante(s)".format(maximo_de_rodadas-rodadas)))
            print()        
            print (titulo)
            print (tracinho(titulo))
            print (descricao)
            print()
            
            
            
            dano = 0
            if item_drop == True:
                chance_item = random.randint(1,5)
                qual_item = random.randint(1,3)
                if chance_item == 1:
                    item = itens[qual_item]
                    print(tracinho("Você encontrou: {0}".format(item)))
                    print("Parabéns!")
                    print("Você encontrou: {0}".format(item))
                    print(tracinho("Você encontrou: {0}".format(item)))
                    if not item in inventario:
                        inventario[item] = 1
                    else:
                        inventario[item] = 1
                item_drop = False
            
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
                                    if Quantidade_de_defesa(defesa) > 0 :
                                        dano += azar
                                        dano_total += (dano/Quantidade_de_defesa(defesa))
                                        encontro_ruim = ('Perdeu {0} de vida'.format(dano/Quantidade_de_defesa(defesa)))
                                    else:
                                        dano += azar
                                        dano_total += dano
                                        encontro_ruim = (('Perdeu {0} de vida'.format(dano)))
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
            if sistema_de_batalha == True:
                vida_inimigo = 5
                dano = 0
                while sistema_de_batalha == True :
                    dano = 0
                    vida_inimigo = vida_inimigo - Quantidade_de_ataque(ataque)
                    print ("> Vida do seu Inimigo ==> {0}".format(vida_inimigo))
                    if vida_inimigo <= 0:
                        sistema_de_batalha = False
                        print ('> Você venceu') 
                    else:
                        if Quantidade_de_defesa(defesa) > 0 :
                            dano += 1
                            dano_total += (dano/Quantidade_de_defesa(defesa))
                        else:
                            dano += 1 
                            dano_total += dano
                        if Health_bar(energia,dano_total) <= 0:
                            print('> Você perdeu a batalha')
                            sistema_de_batalha = False
                            print("> Sua vida ==> {0}".format(Health_bar(energia,dano_total)))
                   
            encontros = True
            item_drop = True
            opcoes = cenario_atual['opcoes']
            if len(opcoes) == 0:
                print("Acabaram-se suas opções! Mwo mwo mwooooo...")
                game_over = True
            elif Health_bar(energia,dano_total) <= 0:
                for i in inventario:
                    if i == "Vida extra":
                        if inventario[i] <= 0:
                
                            game_over = True
                        else:
                            print("Você usou sua vida extra")
                            print("Não morra de novo")
                            print("\_(^-^)_/")
                            inventario["Vida extra"] = 0
                            dano_total = 0
                            energia = 0 
            if cenario_atual == 'teleportar':
                rodadas+=1
                encontros = False
                item_drop = False
            else:
                escolha = ""
                print ()
                print ('Qual será sua escolha?')
                print ()
                for opcao in opcoes:
                    if cenario_atual == 'teleportar':
                        escolha = input("Digite aqui =>")
                        nome_cenario_atual = escolha
                    else:
                        print ()
                        print ('"{0}" : {1}'.format(opcao,opcoes[opcao]))
                        print ()
                
                escolha = input('Digite aqui => ')
                if escolha in opcoes:
                    if escolha == 'stats':
                        encontros = False
                        item_drop = False
                        print()
                        print("Sua vida é {0}".format(Health_bar(energia,dano_total)))
                        print("Sua defesa é {0}".format(Quantidade_de_defesa(defesa)))
                        print("Seu ataque é {0}".format(Quantidade_de_ataque(ataque)))
                    elif escolha =='inventario':
                        encontros = False
                        item_drop = False
                        if len(inventario) == 0:
                            print()
                            print ("* * * * *  * * * ")
                            print ("Inventario vazio")
                            print ("* * * * *  * * * ")
                        else:
                            print ()
                            print (inventario)
                    elif escolha == 'relaxar':
                        print("E a DP veio com tudo!")
                        print("Quem mandou não se empenhar")
                        print("¯\_(ツ)_/¯")
                        game_over = True
                    elif escolha == "estudar":
                        rodadas +=1
                        print ("você finalmente entendeu como usar "
                               "a função 'print' "'\n'"*ganhou 1 de ataque*"'\n'"*ganhou 1 de defesa*")
                        ataque += 1
                        defesa += 1
                    elif escolha == 'barbara':
                        encontros = False
                        item_drop = False
                        rodadas +=1
                        for i in inventario:
                            if "Caixa de chocolate" not in inventario:
                                print()
                                print("VOCÊ ESQUECEU DO PRESENTE!")
                                print("Você devia ter me escutado")
                                print("Bárbara: Você achou que eu ia te ajudar sem ganhar nada?")
                                print("Você foi completamento destruído pela Bárbara")
                                print("Sua vida é de {0}".format(Health_bar(0,9999999999999999999999999999999999)))
                                game_over = True
                            else:
                                nome_cenario_atual = escolha
                                    
                    elif escolha == "andar professor":
                        rodadas += 1
                        encontros = False
                        item_drop = False
                        nome_cenario_atual = escolha
                    elif escolha == "professor":
                        encontros = False
                        item_drop = False
                        nome_cenario_atual = escolha
                    elif  escolha == "atendimento":
                        rodadas +=1
                        for i in inventario:
                            if "E-mail do atendimento" not in inventario:
                                print()
                                print("Você foi avisado. "
                                      "Um veterano te chamou para jogar truco, e sem o e-mail, "
                                      "você não tinha como provar que teria atendimento. ")
                                print("(ლ‸－)")
                                game_over = True
                            else:
                                nome_cenario_atual = escolha
                    elif escolha == "entregar EP":
                        if len(inventario) == 0 :
                            print("Você não tinha o EP pronto")
                            print("Sua alma foi devorada")
                            game_over = True
                        else:    
                            for i in inventario:
                                if "EP finalizado" not in inventario:
                                    if uma_vez == False:
                                        print()
                                        print("Você não tinha o EP pronto")
                                        print("Sua alma foi devorada")
                                        game_over = True
                                        uma_vez = True
                                else:    
                                    if i == "EP finalizado":
                                        if inventario[i] <= 0:
                                            print()
                                            print("Você não tinha o EP pronto")
                                            print("Sua alma foi devorada")
                                            game_over = True
                                        else:
                                            print("Parabéns você entregou o EP a tempo")
                                            print("Você derrotou o monstro do Python")
                                            print("(>'-')> <('-'<) ^('-')^ v('-')v(>'-')>")
                                            game_over = True
                                            vitoria = True                            
                            
                                
                    else:
                        rodadas +=1
                        nome_cenario_atual = escolha
                    print()
                else:
                    print(" ----------------------------")
                    print("Sua indecisão foi sua ruína!")
                    print(" ----------------------------")
                    game_over = True
        if vitoria == True:
            print("Você venceu")
        elif rodadas >= maximo_de_rodadas:
            print("Acabaram suas rodadas")
            print("Você atrasou o EP")
            print("Você morreu de tão frustrado")
            print("Onde você morreu: {0}".format(nome_cenario_atual))
            print()
            recomeco = input("Deseja recomeçar? ")
            print("Digite 'Sim' para recomeçar")
            print("Digite qualquer outra coisa para sair")
            if recomeco == "Sim" or recomeco == "sim":
                retry = True
            else:
                retry = False
        else:
            print("Você morreu!")
            print()
            print("Digite 'Sim' para recomeçar")
            print("Digite qualquer outra coisa para sair")
            recomeco = input("Deseja recomeçar? ")
            print()
            
            if recomeco == "Sim" or recomeco == "sim":
                retry = True
            else:
                retry = False
    
# Programa principal.
if __name__ == "__main__":
    main()
