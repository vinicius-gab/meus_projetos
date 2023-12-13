def aperte_enter():
    input("Pressione Enter para continuar...")

#Introdução do escape room

def mesa():
    print("Ao chegar perto da mesa você se depara com alguns papéis sendo iluminados por um abajur, mas não tem nada demais neles")
    ação = input("Desejar olhar mais um pouco?(sim/não):").lower()
    if ação == "sim":
        print("Você também acha uma gaveta onde se encontra um pouco aberta")
        acao = input("Deseja abrir a gaveta já meio aberta?(sim/não): ").lower()
        if acao == "sim":
            print("Você acha um envelope que contém uma carta com algo escrito")
            aperte_enter()
            cartas_coletados.append("Pedaço de carta")
            cartas_coletados[0] = True
            print("'Eu adoraria continuar ao seu lado, mas minha partida é necessária, mas eu quero que vc lembre eu vou semp'")
            aperte_enter()
            print(f"{nome}: Mas que legal rasgaram a carta pela metade, mas eu acho que devo completar essa carta para sair daqui...talvez pelo menos...")
            aperte_enter()
            print("Bem isso deve ser apenas algum tipo de quebra-cabeça")
            vericar_carta()
        else:
            print(f"{nome}: Acho que não devo mexer nisso")
            print("Narrador: Você volta para o centro sala")

    else:
        print(f"{nome}: Acho melhor não mexer nisso... pelo menos por hora...")
        print("Narrador: Você volta para o centro sala")

def piano():
    print("Narrador: você decide ir investigar o piano")
    aperte_enter()
    print("Ao chegar no piano você nem se atreve a tentar tocar ele já que não sabe tocar piano, mas acha uma abertura que parece ser um painel de senha")
    aperte_enter()
    print(f"{nome}: Posso até não saber tocar piano, mas provavelmente não deveria ter um painel de senha em um piano")
    print("Aparentemente é um senha de 6 dígitos...")
    senha = input("Digite o código(dd/mm/aa): ").lower()
    if  senha == "25/12/95":
        print("Isso a senha é a data daquele casal")
        evento_piano()
    else:
        print("'Senha incorreta. Tente mais uma vez.")
        print("Narrador: Você volta para o centro sala")

def armario():
    print("Ao chegar no armário você encontra vê seu próprio reflexo por um espelho que tem no armário")
    ação = input("Você quer abrir as portas do armário? (sim/não): ").lower()
    if ação == "sim":
        print("Você acha um pedaço de papel e nele está escrito o que parece uma carta")
        aperte_enter()
        print("pre amar você. E para isso preciso que você lembre de quando nos encontramos a primeira vez, Alex. 25 de Dezembro de 1979")
        print(f"{nome}: Isso deve ser alguma coisa de importante")
        cartas_coletados.append("Outro pedaço de carta")
        cartas_coletados[1] = True
        vericar_carta() #fazer essa verificação para seguir com o evento da mesa
    else:
        print("Você volta para o centro da sala")
        print("Narrador: Você volta para o centro sala")
        
def relogio():
    print("Você fica de frente ao relógio de pêndulo enquanto escuta o tic tac do relógio vê um pedaço de papel no chão")
    ação = input("Você quer pegar o pedaço de papel? (sim/não): ").lower()
    if ação == "sim":
        print("No pedaço de papel tem um enigma")
        aperte_enter()
        print("'Tempo é o mestre desta sala, mas somente entendendo o passado, você encontrará a chave para o futuro.")
        print("Olhe para as mãos que avançam incansavelmente. Agora, pense sobre o passado e")
        print("encontre a resposta para seguir adiante.")
        print("Com sabedoria do passado, descubra o caminho a seguir o caminho para o que está por vir.'Feito em 25/12/1995")
        aperte_enter()
        print(f"{nome}: Espera isso tem haver com qualquer outra coisa? Talvez isso sirva para algo" )
        print("Narrador: Você volta para o centro sala")
    else:
        print(f"{nome}: Melhor não fazer isso")
        print("Narrador: Você volta para o centro sala")

def evento_mesa():
        print("Você decide seguir a pista e encontra a chave escondida embaixo de um tapete.")
        print(f"{nome}: Encontrei a chave! Agora posso sair desta sala.")
        aperte_enter()
        final_1()

def evento_piano():
    print("Após colocar a data presente na carta você percebe que o parte superior do piano se abre")
    resposta = input("Deseja olhar o que acaboou de abir?(sim/não): ").lower()
    if resposta == "sim":
        print("Narrador: Após olhar o que liberou do piano, você percebe que tem um pequeno cofre que também pede uma senha, mas essa senha é um ano")
        ano = input("Coloque o ano correto: ").lower()
        if ano == "1776":
            print("Narrador: Após inserir o ano correto o cofre se abre e libera uma chave branca")
            print(f"{nome}: Onde eu devo colocar essa chave? Ela não parece ser a chave da porta de saída")
            print("Narrador: Quando você coleta a chave aparece uma porta branca de luz e ao colocar a chave nessa portal você se depaara em outra sala")
            final_2()
        else:
            print("Narrador: Você decide não olhar para o que acabou de descobrir")
            print("Narrador: Você volta para o centro sala")
        sala()
    else:
        print("Você decide não mexer mais no piano por enquanto.")
        print("Narrador: Você volta para o centro sala")
        sala()

def sala():
    print("Narrador: Ao olhar ao redor da sala, você vê uma mesa, um piano, um armário, e um relógio de pêndulo.")

#final 1

def Verificar_chave():
    if all(chave for chave in chave):
        print("Narrador: Ao girar a chave para destrancar a porta")
        print("Você se depara com uma nova sala, como se fosse uma sala de vigilância")
        print(f"{nome}: Então era daqui que aquela voz vinha me observado")
        evento_porta()
    else:
        print("Narrador: Você volta para o inicio")
        inicio()

def inicio():
    print("Narrador: Quando você olha a sala você vê uma mesa com muitos papéis em cima dela,\num enorme espelho,um piano ainda maior que o da última sala")
    print("Uma enorme porta de marfim com adornos de ouro em conjuto de outras pedras preciosas, como safiras e rubis, e uma estante com alguns post it")

def porta():
    print("Narrador: Você se aproxima da enorme porta")
    print("A porta tem uma elegante e bela fechadura para a chave")
    print(f"{nome}: Inpressiontante essa porta de tão bela, mas para fugir de vez preciso achar a chave dela")
    Verificar_chave()
    print("Narrador: Você volta para o inicio")
    inicio()

def espelho(): 
    print("Narrrador: Você se aproxima do espelho")
    print(f"{nome}: Isso sou eu...")
    aperte_enter()
    print("Narrador: Você volta para o centro da sala")
    inicio()

def piano2():
    print("Narrador: Ao se aproximar do piano você percebe que algumas tecclas estão com marcações, além de um post-it")
    resposta = input("Deseja se aproximar mais ainda do piano?(sim/não): ").lower()
    if resposta == "sim":
        print("Narrador: Quando você pega o post-it percebe a estranha mensagem escrita nele")
        aperte_enter()
        print("'Não sei se tenho coragem para fazer tal ato, mas se todas essas anotações estiverem certas...")
        print("Então minha liberdade está mais perto do que nunca...'")
    else:
        print("Você não pega lê o post-it")
    print(f"{nome}: Eu acho que talvez eu tenha que mexer ccom esse piano, mas o que devo fazer? Tocar as notas marcadas?")
    resposta = input("Tocar a piano?(sim/não): ").lower()
    if resposta == "sim":
        #tocar piano()
        pass
    else:
        print("Narrador: Você decide não tocar no piano")

def papeis():
    print("Narrador: Você se aproxima da mesa")
    print(f"{nome}: Esses papéis são muito diferentes dos da sala anterior...")
    aperte_enter()
    print(f"{nome}: São muitos papeis, então devo focar nos que parecem mais importantes...")
    aperte_enter()
    print("'Mesmo com a tecnologia existente seria impossivel tal coisa se realizar'")
    aperte_enter()
    print("'A saída de tudo isso se resume em mim, mas a-")
    print(f"{nome}: E novamente começa a deixar os papeis em pedaços...")
    aperte_enter()
    resposta = input("Ler mais papeis?(sim/não): ").lower()
    if resposta == "sim":
        print("'O sacrificio para MINHA liberdade é algo muito pouco a se pagar...'")
        aperte_enter()
        print(f"{nome}: Deve ter mais coisas por aqui, não posso desistir...")
        print("'O código para liberar a passagem é :  Sol, Dó, Sol")
        print(f"{nome}: Isso não é as notas musicais? Então acho que sei onde devo ir...")
        piano2()
    else:
        print(f"{nome}: Acho que isso deve o mais importante")
        print("Narrador: Você volta para o inicio da sala...")
        inicio()

def estante():
    print("Narrador: Você se aproxima da estante")
    aperte_enter()
    print(f"{nome}: Essa estante possui muitos livros, acho que eu levaria meses até eu conseguir ler todos eles,")
    print("mas o que mais me chama atenção são esses post-it")
    aperte_enter()
    print("'A cada segundo aqui a minha mente fica mais destruida por essa sala'")
    aperte_enter()
    print("'Se todas as minhas teorias estiverem certas então o culpado já não deve estar mais nesse local, talvez nem nesse tempo...'")
    aperte_enter()
    print("'O dono daquela voz é a pessoa que eu mais odeio, espero que ele morra da pior forma possivel...'")
    print(f"{nome}: OK, esse é o último bilhete que irei lê, isso tá ficando muito estranho")
    print("E os livros aparentemente não tem nada demais")

def evento_espelho():
    print("Narrador: Quando você se aproxima do espelho percebe algo...")
    print(f"{nome}: Esse sou eu...")
    print("Mas eu pareço tão diferente do que eu me lembro...do pouco que eu consigo lembrar...")
    print("Mas eu devo encontrar a chave por aqui se o bilhete estiver correto")
    print("Narrador: Ao olhar mais atentamente no redor do espelho você percebe que existe uma chave rodeado de algumas pétalas de flores azuis")
    aperte_enter()
    print(f"{nome}: Finalmente! A chave da porta finalmente vou conseguir fugir!")
    chave[0] = True

def evento_piano2():
    print("Narrador: Ao chegar no piano e olhar as notas que você deve tocar percebe que tem que as marcaações são nas notas que você vai tocar")
    print(f"{nome}: Eu não consigo acreditar que estou tão perto de sair desse lugar")
    aperte_enter()
    print("Narrador: Quando você termina de tocar a melodia a parte de cima do piano se abre e libera um pequeno papel...")
    aperte_enter()
    print("'passagem se encontra no espelho, mas não sei exatamente onde vai está, na verdade não sei nada sobre esse lugar.'")
    print(f"{nome}: Então é no espelho que eu vou achar a chave para me livrar desse lugar")

def evento_porta():
    print("Narrador: A primeira coisa que você observa ao entrar nessa sala é a existência de um enorme portal")
    aperte_enter()
    print(f"{nome}: Tenho que achar alguma forma de ligar esse portal")
    print("Narrador: Ao olhar ao redor você percebe que tem uma alavanca com um bilhete")
    aperte_enter()
    print("'Quando se liga esse portal outra versão de mim de quando eu cheguei aparece e automaticamente toca uma gravação que não sei onde está,")
    print("Mas não posso intervir até porque o portal vai fechando sozinho...")
    aperte_enter()
    print(f"{nome}: Então quer dizer que tudo isso é um paradoxo temporal, no qual sempre \nterá uma versão de mim mesmo aqui que vai passar por tudo isso novamente...")
    print("Então era a consequência que eu gravei para mim mesmo...Mas eu sei que eu vou conseguir realizar tudo então não devo me preocupar")
    aperte_enter()
    print("Narrador: Ao abrir a alavanca você abre o portal e consegue fugir novamente...")
    final()

def final_1():
    print("Narrador: Ao entrar na nova sala você escuta uma voz vinda do alto falante")
    print("Voz Misteriosa: Eu sabia que você conseguiria sair daquela primeira sala")
    print("mas só para você saber isso é uma mensagem de voz gravada, mas se lembre se você quiser sair daqui...")
    print("FAÇA TUDO PARA SAIR DESSE LOCAL NÃO IMPORTA AS CONSEQUÊNCIAS COM-")
    aperte_enter()
    print(f"{nome}: Pela primeira vez eu me sinto com mais medo dessa sala")
    print("Mas o que ele queria dizer com as consequências que eu tenho que está disposto a pagar...")
    aperte_enter()
    inicio()
    while True: 
        resposta = input("Onde deseja ir?(mesa, espelho, piano, estante, porta, ou sair): ").lower()
        if resposta == "mesa":
            papeis()
        elif resposta == "espelho":
            espelho()
        elif resposta == "piano":
            piano2()
        elif resposta == "estante":
            estante()
        elif resposta == "porta":
            porta()
        elif resposta == "sair":
            print("Você decide sair do jogo!")
            break
        else:
            print("Desculpe, opção inválida. Tente novamente.")

#Final 2

def centro():
    print("Você vê uma estante, um relógio digital, vários posters nas paredes, um tapete, um armário, e uma mesa com ccomputador")

def computador():
    print("Narrador: Você se aproximou da mesa em que o computador se encontra")
    print(f"{nome}: Por que teria uma mesa com computador nesse lugar?")
    resposta = input("Deseja mexer no computador?(sim/não): ").lower()
    if resposta == "sim":
        print("Narrador: Após ligar o computador você percebe que ele já está aberto em um vídeo")
        print(f"{nome}: Estranho é como se ele já estivesse pronto para exibir esse vídeo")
        resposta = input("Você quer dar play no vídeo?(sim/não): ").lower()
        if resposta == "sim":
            print(f"{nome}: Acho que devo dar play nisso logo")
            print("Narrador: Ao dar play no vídeo ele é um vídeo seu quando criança brincando com alguns brinquedos, ")
            print("mas especialmente uma pequena lua de brinquedo")
            aperte_enter()
            print(f"{nome}: Parando para pensar eu tenho uma breve lembrança desses brinquedos, mas parece até um dejavú ")
            print("Narrador: E de repente o vídeo para e o computador desliga")
            fragmentos_coletados[0] = True
            verificar_revelacao()
            aperte_enter()
            print("Narrador: Você volta para o centro")
            centro()
        else:
            print(f"{nome}: Eu não acho que dar o play nisso vai ser legal ")
            print("Narrador: Você volta para o centro")
            centro()
    else:
        print(f"Isso é não seria considerado invasão de privacidade, até porque esse quarto parece ser de alguém, diferente da sala anteior")
        print("Narrador: Você volta para o centro")
        centro()

def relógio():
    print("Narrador: Você decide se aproximar do relógio")
    print(f"{nome}: Esse relógio é totalmente diferente daquele outro")
    aperte_enter()
    print("Ele é digital, mas me parece tão estranho...")
    resposta = input("Você quer investigar o relógio mais um pouco?(sim/não): ").lower()
    if resposta == "sim":
        print(f"{nome}: Se tem uma coisa que eu aprendi nesse pouco tempo que eu tô aqui é que tudo que parece estranho deve olhado")
        print("Olhando mais de perto você acha algo esccrito, aparetemente,em código morse")
        print("O código diz para olhar no tapete")
        resposta = input("Deseja seguir pro tapete?(sim/não): ").lower()
        if resposta == "sim":
            tapete()
        else:
            print(f"{nome}: Acho que devo olhar o tapete depois...")
            centro()
    else:
        print("Narrador: Você volta para o centro")
        centro()

def posters():
    print("Narrador: Você olha os posters e sente algo estranho...")
    aperte_enter()
    print(f"{nome}: Por que eu me sinto tão estranho em relação...")
    aperte_enter()
    print("\n Espera! Esses não são alguns posters de bandas que eu amava?")
    fragmentos_coletados[1] = True
    verificar_revelacao()
    print("Por que eu não me lembrava disso?...Essas salas já estão mexendo com a minha mente")
    aperte_enter()
    print("Narrador: Você volta para o centro")
    centro()

def armário():
    print("Narrador: Ao se aproximar do armário você percebe que ele é maior do que aparenta")
    print(f"{nome}: Ele é maior do que pensava, parece que cabe até alguém ai dentro")
    resposta = input("Abrir as portas?(sim/não): ").lower()
    if resposta == "sim":
        print(f"{nome}: Eu preciso abrir essa porta para fugir dessa maluquice")
        aperte_enter()
        print(f"{nome}: Por que eu não estou surpreso de não ter nada dentro desse armário?")
        print("Narrador: Ao abrir as portas você decide entrar dentro do armário")
        resposta = input("Investigar esse armário?(sim/não): ").lower()
        if resposta == "sim":
            print("Narrador: Ao olhar um pouco mais você percebe um pedaço de papel")
            print("Após pegar o papel você lê o que está escrito nele")
            aperte_enter()
            print("Caso leia isso use o código 191519 no c")
            aperte_enter()
            print(f"{nome}: Que legal já estava demorando para um pedaço de papel não me ajudar muito...")
            print("Ou talvez ajude, mas não tem nenhum sinal de nenhum lugar para colocar esse código")
            resposta = input("Procurar mais alguma coisa?(sim/não): ").lower()
            if resposta == "sim":
                print(f"{nome}: Aparentemente não tem mais nada aqui dentro, além desse peddaço de papel e eu, é claro")
                print("Narrador: Você pula e fecha as portas sem se preocupar...")
                aperte_enter()
                print("Narrador: Você volta para o centro")
                centro()
            elif resposta == "não":
                print(f"{nome}: Bem acho que não tem mais nada aqui mesmo...")
                print("Espera oq é aquela brecha ali no fundo?")
                aperte_enter()
                print("Narrador: Ao se aproximar mais ainda no fundo você percebe que ele na verdade é falso")
                print("Quando tira o fundo você acha um pequeno cofre atrás dele")
                print(f"{nome}: Acho que já sei onde eu devo usar aquele código, mas qual era mesmo ele?")
                código = input("Insira o código para abir o cofre: ")
                if código == "191519":
                    print("Narrador: Ao colocar a senha você acha uma carta um pouco amassada")
                    aperte_enter()
                    print("Quando você lê a carta perce ser uma carta romântica")
                    print(f"{nome}: Acho que isso é meio familiar pra mim...eu lembrei,")
                    print("eu escrevi isso para o primeito garoto que eu gostei... isso não aconteceu durante a minha adolescência ou não?")
                    print("Eu sinceramente tô com minhas memórias muinto borradass desde que cheguei aqui")
                    fragmentos_coletados[2] = True
                    verificar_revelacao()
                    print("Narrador: Você volta para o centro")
                    centro()
                else:
                    print("Essa não era a senha. Tente novamente")
                    print("Narrador: Você volta para o centro")
                    centro()
            else:
                print("Opção inválida Tente algo que esteja nas opções")
        else:
            print("Narrador: Você volta para o centro")
            centro()
    else:
        print("Narrador: Você volta para o centro")
        centro()

def tapete():
     print("Narrador: Você se aproxima do tapete")
     print(f"{nome}: O tapete é bonito mesmo, mas não tem nada de estranho nele")
     resposta = input("Deseja investigar o tapete?(sim/não): ").lower()
     if resposta == "sim":
         print("Narrador: Após  olhar atentamente, você decide olhar debaixo do tapete...")
         aperte_enter()
         print(f"{nome}: Uou... Mesmo com as bizarrices desse lugar é a primeiira vez que eu me deparo com algo nesse nível...")
         print("Eu esperava achar qualquer coisa aqui menos sangue debaixo desse tapete...")
         aperte_enter()
         print("Narrador: Mesmo com todas as manchas de sangue você encontrar um papel...")
         resposta = input("Deseja ler o que tem escrito no papel?(sim/não): ").lower()
         if resposta == "sim":
             print("Sem corpo, sem alma, sem respirar,\nSem vida, sem pulso, sem se mexer.")
             print("O destino inevitável que todos enfrentarão,\nNo final de tudo, meu nome você conhecerá.")
             aperte_enter()
             print(f"{nome}: Isso seria algum tipo de piada? Ou o que?")
             print("Esse enigma se refere... a morte... isso somado com todo esse sangue...")
             fragmentos_coletados[3] = True
             verificar_revelacao()
             
def estante():
    print("Narrador: Você observa atentamente a estante, mas não acha nada de interresante")
    ação = input("Deseja investigar um poucco mais?(sim/não): ").lower()
    if ação == "sim":
        print("Você acha um brinquedo da lua")
        ação = input("Você deseja pegar o briquedo?(sim/não): ").lower()
        if ação == "sim":
            print("Acho que vou levar isso comigo, pelo menos vou me sentir um pouco mais seguro")
            print("Narrador: Você acaba de colocar a lua de brinquedo no seu bolso")
            fragmentos_coletados[4] = True
            verificar_revelacao()
        else:
            print(f"{nome}: Acho melhor deixar isso ai mesmo")
    else:
        print("Narrador: Você decide voltar pro centro da sala")
        centro()

def final_2():
    print("\nVoz Misteriosa: Parabéns por conseguir sair daquela primeirra sala ")
    print(f"Ela era muito mais simples do que o espera você {nome}")
    aperte_enter()
    print(f"{nome}: Será que agora você poderia me contar onde estou ou como cheguei aqui?")
    print("Voz Misteriosa: As respostas que tanto espera serão reveladas, então boa sorte...ou morra...")
    aperte_enter()
    print("Narrador: Você olha nova sala que se encontra e percebe que ela é muito reconfortante por algum motivo")
    print("Você olha ao redor da sala e encontra uma sala de fato maior que a anterior")
    centro()
    while True:
        resposta = input("Onde deseja ir?(estante, relógio, posters, tapete, armário, computador): ").lower()

        if resposta == "computador":
            computador()  
        elif resposta == "tapete":
            tapete()      
        elif resposta == "armário":
            armário()     
        elif resposta == "relógio":
            relógio()     
        elif resposta == "estante":
            estante()     
        elif resposta == "posters":
            posters()     
        elif resposta == "sair":
            print("Você decide sair do jogo!")
            break
        else:
            print("Desculpe, opção inválida. Tente novamente.")

#Parte Tecnicas

fragmentos_coletados = [False, False, False, False] 
cartas_coletados = [False, False]
chave = [False]

def verificar_revelacao():
    if all(fragmento for fragmento in fragmentos_coletados):
        print("Parabéns! Você coletou todos os fragmentos de memória.")
        print("Agora a verdade será revelada!")
        aperte_enter()
        print(f"{nome}: Isso é só não passa de uma farsa de uma farsa não é?")
        print("Tudo o que eu fiz até agora não serviu de nada não é? Afinal...e-eu...já morri")
        print("Morte: Infelizmente sua hora chegou ao fim, mas espero que tenha se assustado com sua morte...")
        print("Sem levar nenhum deles")
        aperte_enter()
        print(f"{nome}: Bem...pelo menos eu me sinto um pouco melhor")
        aperte_enter()
        final()
    else:
        pass

def vericar_carta():
    if all(cartas for cartas in cartas_coletados):
        print("Parabéns! Você completou a carta")
        print("Ao juntar os dois pedaços de carta você percebe que o verso da carta mostra uma pista")
        resposta = input("Deseja seguir a pista da carta?(sim/não): ").lower()
        if resposta == "sim":
            evento_mesa()
        else:
            print(f"{nome}: Acho que devo explorar um pouco mais")
    else:
        print("Continue explorando para completar a carta.")

def final():
    print("Fim de jogo! Parabéns por completar um dos 2 finais")
    print("Tente realizar o outro final seguindo um caminho diferente")

nome = input("Digite o seu nome, por favor: ")
print("\nNarrador: Você desperta em um ambiente desconhecido, cercado por paredes que parecem sussurrar mistérios.")
aperte_enter()
print("De repente, uma voz ressoa pela sala vinda de um alto-falante oculto, preenchendo o silêncio.")
aperte_enter()
print(f"Voz Misteriosa: Saudações, {nome}. Bem-vindo ao desafio que agora se desenha diante de você.")
aperte_enter()
print(f"{nome}: Espera, onde estou? Como cheguei aqui?")
print("Voz Misteriosa: Suas perguntas são compreensíveis, mas por enquanto, elas permanecerão sem resposta.")
print("Voz Misteriosa: Sua única saída é encontrar a chave para sobreviver. Boa sorte...")
aperte_enter()

while True:
    sala()
    resposta = input("Onde você deseja investigar agora? (mesa, piano, armário, relógio, sair): ").lower()

    if resposta == "mesa":
        mesa()
    elif resposta == "piano":
        piano()
    elif resposta == "armário":
        armario()
    elif resposta == "relógio":
        relogio()
    elif resposta == "sair":
        print("Você decide sair do jogo!")
        break
    else:
        print("Desculpe, opção inválida. Tente novamente.")