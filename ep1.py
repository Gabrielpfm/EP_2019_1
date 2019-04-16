# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Gabriel Pascua de Freitas Moreira, gabrielpfm@al.insper.edu.br
# - aluno B: Gabriel Huerta Façanha, gabrielhf@al.insper.edu.br
import json
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
def carregar_cenarios():
    with open('cenarios.json','r') as arquivo:
        cenarios = json.load(arquivo)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


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

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        titulo = cenario_atual['titulo']
        descricao = cenario_atual['descricao']
                
        print (titulo)
        print (tracinho(titulo))
        print (descricao)
        
       
    
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
                print(" |Sua indecisão foi sua ruína!")
                print(" ----------------------------")
                game_over = True

    print("Você morreu!")
    print()
    
# Programa principal.
if __name__ == "__main__":
    main()
