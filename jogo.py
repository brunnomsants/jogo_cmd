import os

print("        _            _            _             _                    _              _      _                  _          ")
print("       / /\         /\ \         /\ \     _    / /\                 /\ \           /\ \   /\_\               /\ \     _  ")
print("      / /  \       /  \ \       /  \ \   /\_\ / /  \                \ \ \         /  \ \ / / /         _    /  \ \   /\_\
")
print("     / / /\ \__   / /\ \ \     / /\ \ \_/ / // / /\ \               /\ \_\       / /\ \ \\ \ \__      /\_\ / /\ \ \_/ / /")
print("    / / /\ \___\ / / /\ \_\   / / /\ \___/ // / /\ \ \             / /\/_/      / / /\ \_\\ \___\    / / // / /\ \___/ / ")
print("    \ \ \ \/___// /_/_ \/_/  / / /  \/____// / /  \ \ \           / / /        / / /_/ / / \__  /   / / // / /  \/____/ ")
print("     \ \ \     / /____/\    / / /    / / // / /___/ /\ \         / / /        / / /__\/ /  / / /   / / // / /    / / /")
print(" _    \ \ \   / /\____\/   / / /    / / // / /_____/ /\ \       / / /        / / /_____/  / / /   / / // / /    / / / ")
print("/_/\__/ / /  / / /______  / / /    / / // /_________/\ \ \  ___/ / /__      / / /\ \ \   / / /___/ / // / /    / / /  ")
print("\ \/___/ /  / / /_______\/ / /    / / // / /_       __\ \_\/\__\/_/___\    / / /  \ \ \ / / /____\/ // / /    / / /  ")
print(" \_____\/   \/__________/\/_/     \/_/ \_\___\     /____/_/\/_________/    \/_/    \_\/ \/_________/ \/_/     \/_/   ")
print("")
print('                                ΛPΞЯTΞ "ΞЛTΞЯ" PΛЯΛ ϾФMΞϾ̧ΛЯ Λ SUΛ ΛVΞЛTUЯΛ ÐФ SΞЛΛł!!!')

t = input("")
os.system("cls")
print("Você está dormindo e acaba sendo acordando com gritos...")
print("Depois de alguns segundos, ainda sonolento, percebe que é a sua mãe gritando...")
nome = input("Qual o seu nome?")
print('"' + nome.upper() + ', ACORDAAAAA, VOCÊ VAI SE ATRASAR PARA A SUA AULA NO SENAI!!!!!!", diz sua mãe.')
p = input("")
os.system("cls")
print("Então depois de levantar de sua cama, você acaba reparando que está chovendo, então acaba se perguntando...")
print("Será que eu ainda vou para a aula?")
print("[1] Sim")
print("[2] Não")
vontade= int(100)
op0 = int(input())
while (op0 < 1) or (op0 > 2):
    print("[1] Sim")
    print("[2] Não")
    op0 = int(input())
if op0 == 1:
    print("Depois de pensar um pouco, você se decidiu a ir a sua aula do Senai.")
    u = input("")
    os.system("cls")
    if vontade > 0:
        print("Como está chovendo lá fora, consequentemente está frio. Então você fica na dúvida entre levar um casaco ou não.")
        print("")
        print("[VONTADE DE IR PRA AULA: 100%]")
        print("Você deseja levar um casaco? ")
        print("[1] Sim")
        print("[2] Não")
        op1 = int(input())
        while (op1 < 1) or (op1 > 2):
            print("[1] Sim")
            print("[2] Não")
            op1 = int(input())
        print("")
        print("Mas além de um casaco, você também precisa se proteger da chuva.")
        print("Porém, sua mochila é pequena, então, você pode optar por levar apenas: ")
        print("[1] Guarda chuva")
        print("[2] Capa de chuva")
        print("[3] Ir no louco (não levar nada)")
        op2 = int(input())
        while (op2 < 1) or (op2 > 3):
            print("[1] Guarda chuva")
            print("[2] Capa de chuva")
            print("[3] Ir no louco (não levar nada)")
            if op1 == 2:
                vontade = vontade - 15
            op2 = int(input())
        print("")
    if vontade > 0:
        print("Depois de fazer as suas escolhas, você sai da sua casa em direção ao Senai.")
        h = input("")
        os.system("cls")
        print("Após a algum tempo andando, você se depara com um cachorro raivoso pronto para te atacar.")
        print("Você precisa ser rápido na sua escolha, então o que você irá fazer " + nome + "?")
        print("[1] Se Defender")
        print("[2] Correr")
        if op1 == 2:
            vontade = vontade - 15
        op3 = int(input())
        while (op3 < 1) or (op3 > 2):
            print("[1] Se Defender")
            print("[2] Correr")
            op3 = int(input())
        if op3 == 1 and op2 == 1:
            print("Você usou o guarda-chuva para se defender, então ele se assustou e acabou fugindo!")
            vontade = vontade - 15
        elif op3 == 1 and op2 != 1:
            print("Você foi tentar se defender do cachorro, mas como não tinha nada para se proteger, acabou sendo MORDIDO!!")
            print("Nessas condições acabou voltando para casa triste e machucado.")
            print("[VONTADE DE IR PRA AULA: 0%]")
            print("")
            print("         _        _         _   _       ")
            print("        /\ \     /\ \      /\_\/\_\ _   ")
            print("       /  \ \    \ \ \    / / / / //\_\ ")
            print("      / /\ \ \   /\ \_\  /\ \/ \ \/ / / ")
            print("     / / /\ \_\ / /\/_/ /  \____\__/ /  ")
            print("    / /_/_ \/_// / /   / /\/________/  ")
            print("   / /____/\  / / /   / / /\/_// / /   ")
            print("  / /\____\/ / / /   / / /    / / /   ")
            print(" / / /   ___/ / /__ / / /    / / /   ")
            print("/ / /   /\__\/_/___\\/_/    / / /    ")
            print("\/_/    \/_________/        \/_/     ")
            exit()
        else:
            print("Você correu bastante e conseguiu despistar o cachorro raivoso.")
            vontade = vontade - 20

    if vontade > 0: 
        h = input("")
        os.system("cls")
        print("")           
        print("[VONTADE DE IR PRA AULA: {}%]".format(vontade))
        print("Logo após o imprevisto com o cachorro, você avista dois caminhos, um deles tem uma poça de lama.")
        print("Você tem duas opções, deseja ir pela esquerda ou pela direita")
        print("[1] Esquerda")
        print("[2] Direita")
        if op1 == 2:
            vontade = vontade - 15
        op4 = int(input())
        while (op4 < 1) or (op4 > 2):
            print("[1] Esquerda")
            print("[2] Direita")
            op4 = int(input())
        print("Ops!! Os dois caminhos davam na lama.")
        if op2 == 2:
            print("Por você ter pego a capa de chuva, você não se sujou!")
            vontade = vontade - 10
        else:
            print("Por você não ter pego a capa de chuva, você se sujou!")
            vontade = vontade - 30  
    if vontade > 0:
        h = input("")
        os.system("cls")
        print("[VONTADE DE IR PRA AULA: {}%]".format(vontade))
        print("Depois de mais um imprevisto, você chega em uma avenida movimentada.")
        print("Por conta dos problemas no meio do trajeto, você está atrasado.")
        print("Mas você deparou-se com um atalho calmo, você escolhe: ")
        print("[1] Atalho calmo")
        print("[2] Avenida")
        if op1 == 2:
            vontade = vontade - 15
        op5 = int(input())
        while (op5 < 1) or (op5 > 2):
            print("[1] Atalho calmo")
            print("[2] Avenida")
            op5 = int(input())
        if op5==1:
            print("Parecia um lugar calmo, mas um bandido te esperava e te levou tudo.")
            print("Você ficou só com a roupa do corpo e teve que voltar para casa, {}.".format(nome))
            print("[VONTADE DE IR PRA AULA: 0%]")
            print("")
            print("         _        _         _   _       ")
            print("        /\ \     /\ \      /\_\/\_\ _   ")
            print("       /  \ \    \ \ \    / / / / //\_\ ")
            print("      / /\ \ \   /\ \_\  /\ \/ \ \/ / / ")
            print("     / / /\ \_\ / /\/_/ /  \____\__/ /  ")
            print("    / /_/_ \/_// / /   / /\/________/  ")
            print("   / /____/\  / / /   / / /\/_// / /   ")
            print("  / /\____\/ / / /   / / /    / / /   ")
            print(" / / /   ___/ / /__ / / /    / / /   ")
            print("/ / /   /\__\/_/___\\/_/    / / /    ")
            print("\/_/    \/_________/        \/_/     ")
            exit()
        else:
            print("Você decidiu atravessar a avenida.")
            print("Quando estava chegando na calçada, acabou resbalando no meio-fio e sofreu um pequeno corte.")
            vontade = vontade - 15
    if vontade > 0:
        print("Mas você conseguiu continuar com seu trajeto.")
        h = input("")
        os.system("cls")
        print('''
              
              
              
              
              
              
              
              
              
              
              
              
              ''')
        print('''               █████                                                                                                            
                                                   ░░███                                                                                                             ░░░  
 █████ █████  ██████   ██████   ██████      ██████  ░███████    ██████   ███████  ██████  █████ ████    ████████    ██████      █████   ██████  ████████    ██████   ████ 
░░███ ░░███  ███░░███ ███░░███ ███░░███    ███░░███ ░███░░███  ███░░███ ███░░███ ███░░███░░███ ░███    ░░███░░███  ███░░███    ███░░   ███░░███░░███░░███  ░░░░░███ ░░███ 
 ░███  ░███ ░███ ░███░███ ░░░ ░███████    ░███ ░░░  ░███ ░███ ░███████ ░███ ░███░███ ░███ ░███ ░███     ░███ ░███ ░███ ░███   ░░█████ ░███████  ░███ ░███   ███████  ░███ 
 ░░███ ███  ░███ ░███░███  ███░███░░░     ░███  ███ ░███ ░███ ░███░░░  ░███ ░███░███ ░███ ░███ ░███     ░███ ░███ ░███ ░███    ░░░░███░███░░░   ░███ ░███  ███░░███  ░███ 
  ░░█████   ░░██████ ░░██████ ░░██████    ░░██████  ████ █████░░██████ ░░███████░░██████  ░░████████    ████ █████░░██████     ██████ ░░██████  ████ █████░░████████ █████
   ░░░░░     ░░░░░░   ░░░░░░   ░░░░░░      ░░░░░░  ░░░░ ░░░░░  ░░░░░░   ░░░░░███ ░░░░░░    ░░░░░░░░    ░░░░ ░░░░░  ░░░░░░     ░░░░░░   ░░░░░░  ░░░░ ░░░░░  ░░░░░░░░ ░░░░░ 
                                                                        ███ ░███                                                                                          
                                                                       ░░██████                                                                                           
                                                                        ░░░░░░                                                                                            ''')
        h = input("")
        os.system("cls")
        print("[VONTADE DE IR PRA AULA: {}%]".format(vontade))
        print("")
        print("Depois de você entrar no Senai, você vai para a sala da aula, porém, ela está vazia.")
        print("Você se questiona no que fazer...")
        print("Você deseja: ")
        print("[1] Entrar na sala mesmo assim")
        print("[2] Esperar o professor")
        op6 = int(input())
        while (op6 < 1) or (op6 > 2):
            print("[1] Entrar na sala mesmo assim")
            print("[2] Esperar o professor")
            op6 = int(input())
            print("")
        if op6==1:
            print("Você entra na sala para esperar o professor.")
            print("Um segurança passa pela sala e te avista, indo em sua direção.")
            print("Ele te diz que aquela sala estava reservada e que você não podia estar nela.")
            print("Você acaba sendo expulso pelo segurança e perdendo sua aula.")
            print('''
         _        _         _   _       
        /\ \     /\ \      /\_\/\_\ _   
       /  \ \    \ \ \    / / / / //\_\ 
      / /\ \ \   /\ \_\  /\ \/ \ \/ / / 
     / / /\ \_\ / /\/_/ /  \____\__/ /  
    / /_/_ \/_// / /   / /\/________/   
   / /____/\  / / /   / / /\/_// / /    
  / /\____\/ / / /   / / /    / / /     
 / / /   ___/ / /__ / / /    / / /      
/ / /   /\__\/_/___\\/_/    / / /       
\/_/    \/_________/        \/_/        
                                        
                                        ''')
        else:
            print("Você optou por esperar o professor.")
            print("")
            print("Depois de um tempo esperando ele chegou!")
            print("Ele foi o informar que a aula não era naquela sala, que acabou sendo trocada.")
            print("Depois vocês foram para a sala correta e tiveram a sua aula!")
            print("PARABÉNS, VOCÊ CONSEGUIU {}!!".format(nome.upper()))
            print("")
            print("         _        _         _   _       ")
            print("        /\ \     /\ \      /\_\/\_\ _   ")
            print("       /  \ \    \ \ \    / / / / //\_\ ")
            print("      / /\ \ \   /\ \_\  /\ \/ \ \/ / / ")
            print("     / / /\ \_\ / /\/_/ /  \____\__/ /  ")
            print("    / /_/_ \/_// / /   / /\/________/  ")
            print("   / /____/\  / / /   / / /\/_// / /   ")
            print("  / /\____\/ / / /   / / /    / / /   ")
            print(" / / /   ___/ / /__ / / /    / / /   ")
            print("/ / /   /\__\/_/___\\/_/    / / /    ")
            print("\/_/    \/_________/        \/_/     ")
    else:
        print("SUA VONTADE DE IR PARA A AULA SE ESGOTOU {}".format(nome))
        print("[VONTADE DE IR PRA AULA: 0%]")
        print("")
        print("         _        _         _   _       ")
        print("        /\ \     /\ \      /\_\/\_\ _   ")
        print("       /  \ \    \ \ \    / / / / //\_\ ")
        print("      / /\ \ \   /\ \_\  /\ \/ \ \/ / / ")
        print("     / / /\ \_\ / /\/_/ /  \____\__/ /  ")
        print("    / /_/_ \/_// / /   / /\/________/  ")
        print("   / /____/\  / / /   / / /\/_// / /   ")
        print("  / /\____\/ / / /   / / /    / / /   ")
        print(" / / /   ___/ / /__ / / /    / / /   ")
        print("/ / /   /\__\/_/___\\/_/    / / /    ")
        print("\/_/    \/_________/        \/_/     ")
else:
    print("")
    print("         _        _         _   _       ")
    print("        /\ \     /\ \      /\_\/\_\ _   ")
    print("       /  \ \    \ \ \    / / / / //\_\ ")
    print("      / /\ \ \   /\ \_\  /\ \/ \ \/ / / ")
    print("     / / /\ \_\ / /\/_/ /  \____\__/ /  ")
    print("    / /_/_ \/_// / /   / /\/________/  ")
    print("   / /____/\  / / /   / / /\/_// / /   ")
    print("  / /\____\/ / / /   / / /    / / /   ")
    print(" / / /   ___/ / /__ / / /    / / /   ")
    print("/ / /   /\__\/_/___\\/_/    / / /    ")
    print("\/_/    \/_________/        \/_/     ")