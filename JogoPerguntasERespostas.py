import time
class Jogo:
    def __init__(self):
        try:
            self.menu()
        except ValueError:
            print("Escolha uma opção válida!")
            self.menu()  

    def menu(self):
        print("Bem vindo ao Perguntados da programação!")
        while True:
            print("""\n1 - Iniciar jogo
2 - Como jogar / Objetivo do jogo
3 - Sair""")
            comando = int(input("Escolha sua opção digitando o número correspondente: "))  
            if comando == 1:
                self.iniciar()
                break
            elif comando == 2:
                self.mostrarInstrucoes()
            elif comando == 3:
                self.sair()
            else:
                print("Escolha uma opção válida!")
                self.menu()
                  

    def iniciar(self):  
        try:
            print("""\n1 - Único Jogador
2 - Multiplayer Local""")
            comando = int(input('Escolha seu modo de jogo: '))
            if comando == 1:
                self.jogador1 = Jogador()
                self.tipoDeObjeto = Pergunta #aqui é decidido o tipo de objeto que será criado
            elif comando == 2:
                self.jogador1 = Jogador()
                self.jogador2 = Jogador()
                self.tipoDeObjeto = PerguntaMultiplayer #aqui é decidido o tipo de objeto que será criado
            else:
                print("Escolha uma opção válida!")
                self.iniciar()
        except ValueError:
            print("Escolha uma opção válida!!")
            self.iniciar()  

    def mostrarInstrucoes(self):
        print("""\nInstruções do jogo:
1 - O jogo consiste em acertar as perguntas sobre conteúdos da programação.
2 - Assim que iniciar o jogo, aparecerá uma pergunta e 4 alternativas, sendo apenas uma delas a correta.
3 - Pode ser jogado no modo 'Um Jogador' ou 'Dois Jogadores'.
4 - No modo 'Um Jogador', o jogador possui 3 vidas, onde cada vez que ele errar um questão, ele perde uma vida. Caso chegue a 0, o jogo acaba.
5 - O jogador deve OBRIGATORIAMENTE responder a pergunta com letra minúscula.
6 - Cada pergunta respondida corretamente garante ao jogador 100 pontos, no fim, quem tiver mais pontos vence.""")

    def sair(self):
        print("Encerrando o jogo...")
        quit()

    def finalizar(self):
        if self.tipoDeObjeto == Pergunta: 
            self.finalUmJogadorGanha()
            
        elif self.tipoDeObjeto == PerguntaMultiplayer: 
            self.finalMultiplayer()

    def finalUmJogadorGanha(self): #final jogo sozinho quando ele n perde nehuma vida
        if self.jogador1.vidas == 3:
            print("\nParabéns, você zerou o jogo!\nAcertou todas as perguntas.") 
            print(f"\nResultado final\n{self.jogador1}")

        elif self.jogador1.vidas < 3:
            print("\nParabéns, você ganhou!") 
            print(f"\nResultado final\n{self.jogador1}\nVidas: {self.jogador1.vidas}")
            

    def finalMultiplayer(self):
        print("Fim de jogo!!")
        if jogo.jogador1.getPontosJ1() > jogo.jogador2.getPontosJ2():  #jogador 1 ganhou
            print("\nO vencedor é...")
            self.tempo()
            print(f"===== {jogo.jogador1.nome} =====")
            self.tempo()
            print("\nResultado final")
            print(jogo.jogador1)
            print(jogo.jogador2)
           
        elif jogo.jogador2.getPontosJ2() > jogo.jogador1.getPontosJ1(): #jogador 2 ganhou
            print("\nO vencedor é...")
            self.tempo()
            print(f"===== {jogo.jogador2.nome} =====")
            self.tempo()
            print("\nResultado final")
            print(jogo.jogador1)
            print(jogo.jogador2)
            
        elif jogo.jogador1.getPontosJ1() == jogo.jogador2.getPontosJ2(): 
            if jogo.jogador1.getPontosJ1() and jogo.jogador2.getPontosJ2() == 0:
                print("\nO vencedor é...")
                self.tempo()
                print("Todos perderam!! Ninguém pontuou.")
                self.tempo()
                print("\nResultado final")
                print(jogo.jogador1)
                print(jogo.jogador2)
            else:
                print("\nO vencedor é...")
                self.tempo()
                print(f"===== {jogo.jogador1.nome} e {jogo.jogador2.nome} ===== empate!!")
                self.tempo()
                print("\nResultado final")
                print(jogo.jogador1)
                print(jogo.jogador2)
                
    def tempo(self):
        time.sleep(3)  
    
class Jogador:
    i = 1
    def __init__(self, p=0, v=3):
        self.nome = input(f"{Jogador.i}º jogador digite o seu nome: ")
        Jogador.i += 1
        self.__pontos = p #encapsulamento
        self.__vidas = v #encapsulamento

    def __str__(self):
        return (f"Nome: {self.nome}\nPontos: {self.__pontos}")

    
    def getVidasJ1(self):
        return jogo.jogador1.__vidas
    def getPontosJ1(self):
        return jogo.jogador1.__pontos
    def getPontosJ2(self):
        return jogo.jogador2.__pontos
    

    def ganharPontos(self):
        self.__pontos += 100
    def perderVidas(self):
        self.__vidas -= 1 
        if self.__vidas == 0: 
            print(f"Fim de Jogo!\nResultado Final\n{jogo.jogador1}")
            quit()

class Pergunta: #classe mae
    numeroQuestao = 1  #variavel de classe
    def __init__(self, questao, respostaCorreta):
        self.questao = questao
        self.respostaCorreta = respostaCorreta
        if jogo.tipoDeObjeto == Pergunta: #verificação: se for modo 1 jogador roda as perguntas, caso contrário n faz nd.
            self.rodarPergunta()
        
    def rodarPergunta(self):
        print(f"\n{Pergunta.numeroQuestao}ª Pergunta")
        print(f"{self.questao}")
        resposta = str(input("Escolha a alternativa correta: "))
        if resposta == self.respostaCorreta:
            Pergunta.numeroQuestao += 1
            jogo.jogador1.ganharPontos() #agregação: chama o metodo de outra classe
            print("\nResposta correta")
        
        else:
            jogo.jogador1.perderVidas() #agregação
            Pergunta.numeroQuestao += 1
            print("\nResposta errada")
                

#multiplayer local
class PerguntaMultiplayer(Pergunta): #classe filha
    numeroQuestao = 1  #variavel de classe
    def __init__(self, questao, respostaCorreta):
        Pergunta.__init__(self, questao, respostaCorreta)
        self.rodarPergunta()
        
    def rodarPergunta(self): #polimorfismo: o método tem o mesmo nome da classe mãe, mas faz coisas diferentes
        print(f"\n{PerguntaMultiplayer.numeroQuestao}ª Pergunta")
        print(f"{self.questao}")
        respJ1 = str(input(f"{jogo.jogador1.nome}, escolha a alternativa correta: "))
        respJ2 = str(input(f"{jogo.jogador2.nome}, escolha a alternativa correta: "))
        if respJ1 == self.respostaCorreta:
            if respJ2 == self.respostaCorreta:
                #os dois acertaram
                jogo.jogador1.ganharPontos() #agregaçao
                jogo.jogador2.ganharPontos() #agregaçao
                PerguntaMultiplayer.numeroQuestao += 1
                print(f"\n{jogo.jogador1.nome} e {jogo.jogador2.nome} acertaram a resposta!!")
                
                    
            else:
                #j1 acertou e o j2 errou
                jogo.jogador1.ganharPontos() #agregaçao
                PerguntaMultiplayer.numeroQuestao += 1
                print(f"\n{jogo.jogador1.nome} acertou a resposta!!")
                print(f"{jogo.jogador2.nome} errou a resposta!!")
                
                    
            
            if respJ2 == self.respostaCorreta:
                if respJ1 != self.respostaCorreta:
                    #j2 acertou e o j1 errou
                    jogo.jogador2.ganharPontos() #agregaçao
                    PerguntaMultiplayer.numeroQuestao += 1
                    print(f"\n{jogo.jogador1.nome} errou a resposta!!")
                    print(f"{jogo.jogador2.nome} acertou a resposta!!")
                
                
            if respJ1 != self.respostaCorreta:
                if respJ2 != self.respostaCorreta:
                    #os dois erraram
                    PerguntaMultiplayer.numeroQuestao += 1
                    print(f"\n{jogo.jogador1.nome} e {jogo.jogador2.nome} erraram a resposta!!")
                
                    
            
                    


jogo = Jogo()
x = jogo.tipoDeObjeto #Determina se o modo de jogo é 1 jogador ou se é multiplayer local

pergunta1 = x("""Qual é o significado de "código" no contexto da programação?\na) Uma forma de encriptar dados
b) Uma senha que usamos para ativar o Python
c) Um conjunto de regras de estilo para programas em Python
d) Uma sequência de instruções em uma linguagem de programação""", "d")

pergunta2 = x("""Em Python, quando mais de um operador aparece em uma expressão, a ordem de avaliação depende das regras de precedência de cada linguagem. Assim, ao programar em Python, além de observar essas regras, é preciso considerar, ainda, a forma como a linguagem representa seus operadores, conforme demonstrado nos comandos a seguir.
x = 7*3**2%4\nAssinale o resultado impresso:\na) 1
b) 3
c) 7
d) 15.75""", "b")

pergunta3 = x("""Qual a função que transforma algo em string no python?\na) str()
b) int()
c) float()
d) string()""", "a")

pergunta4 = x("""Sobre o Paradigma Orientado a Objetos, responda a alternativa que melhor o define:
a) Organiza o código em procedimentos conhecidos como rotinas, subrotinas, funções ou métodos
b) Organiza o código em blocos lógicos usando estruturas de controle de fluxo
c) Orgabiza o código em grupos de objetos, chamados de métodos, que contém variáveis e classes próprias
d) Organiza o código em grupos de objetos, chamados de classes, que contém variáveis e funções próprías""","d" or "D")

pergunta5 = x("""Ao criar um sistema ou resolver um problema com Programação Orientada a Objetos, é comum a análise da descrição do sistema ou problema. Nesse contexto, para definir os potenciais métodos de uma classe em qual classe de palavras é importante estar atento?
a) Substantivos
b) Verbos
c) Adjetivos
d) Artigos""", "b")

pergunta6 = x("""Substitua os asteriscos com o comando de método especial que mais se adequa a situação a seguir para obter o resultado proposto:
class Fruta:
    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade
    def *******(self):
        return (f'Nome da Fruta: {self.nome}\\nQuantidade: {self.quantidade}')
banana = Fruta('banana', 10)
print(banana)

Resultado:
Nome da Fruta: banana
Quantidade: 10

a) __init__
b) print()
c) __str__
d) __eq__""", "c")

pergunta7 = x("""Considere o programa em Python abaxo:
\nnum1 = int(input('Informe o número de Processos:'))
num2 = int(input('Informe o número de Juízes:'))

..I..
    resultado = numero1 / numero2
    print("Há ",resultado, " processos a serem julgados por cada Juiz")
..II..
    print("Não é possível divisão por zero")
Para tratar a exceção que será lançada se o valor contido na variável num2 for zero, as lacunas I e II deverão ser corretamente preenchidas por:

a) if: e except ZeroDivisionError:
b) try e except ZeroDivisionError:
c) if: e except ValueError:
d) try: e except ZeroDivisionError:""", "d")

pergunta8 = x("""frutas = ["banana" , "laranja" , "manga" , "uva"]

for k in range( -1, -4, -2 ):
    print frutas [ k ]

O conjunto de palavras exibidas pela execução desse código, na ordem, é:
a) uva, laranja
b) banana, laranja, manga
c) laranja, manga
d) uva, banana, manga""", "a")

pergunta9 = x("""class Cliente:
    I
        self.nome = nome
        self.renda = renda

p1 = Cliente("Adriano", 5700.98)

print(p1.nome)
print(p1.renda)

Para que o código seja compilado e executado corretamente, a lacuna I deverá ser preenchida com:
a) _init_(self, nome, renda):
b) def _init_(self, nome, renda):
c) def _str_(self):
d) def _eq_(self, Cliente):""", "b")

pergunta10 = x("""Sobre as linguagens de programação orientada a obejtos, marque V para as afirmativas verdadeiras e F para as falsas.
( ) Os 4 pilares fundamentais da programação orientada a objetos são: Encapsulamento, Abstração, Polimorfismo e Herança.
( ) Mesmo quando um método possui o parâmetro 'self', ele não receberá automaticamente como argumento uma referência para o objeto que está tentando usá-lo.
( ) O método _eq_ compara dois objetos e retorna True se seus valores forem os mesmos.
( ) Atributo é um elemento dentro do sistema que é a execução de uma classe.
( ) Os métodos também podem ser chamados de 'comportamento dos objetos de uma classe', pois são ações que esses objetos podem executar.

a) V - V - V - F - F
b) V - F - V - F - V
c) F - F - F - V - V
d) V - V - F - V - F""", "b")

jogo.finalizar()
