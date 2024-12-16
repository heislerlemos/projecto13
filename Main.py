# Projecto 13
from art import *
import os
from ClassCordaoDeSeguranca import *
import inquirer

tprint("Controlo de Camaras Lda")


perguntaprompt= [
        inquirer.List('estado',
            message ="Quer adicionar equipamentos ?:",
            choices= ['sim', 'nao'],
             ),
            ]
    
resposta= inquirer.prompt(perguntaprompt)
prompt1 = resposta['estado']


lista_de_objectos = []

while prompt1 == 'sim':
    print ("Criando o objecto")
    # Inserir Perimetro
    try:
        perimetro = float(input("insira  o perímetro do cordão de segurança:"))    
    except ValueError:
        print("Tem que ser um numero decimal  ")    
        
    # Inserir Topologia            
    perguntatopologia = [
            inquirer.List('estado',
                           message ="Insira o estado da linha de segurança :",
                           choices= ['muro', 'vedação'],
                         ),
            ]
    
    topologia = inquirer.prompt(perguntatopologia)
    
    
    # Inserir Altura
    try:
        altura = float(input("insira a altura da linha de segurança:"))
    except ValueError:
        print("Tem que ser decimal")
    
    # Inserir Estado
    
    perguntalinha = [
            inquirer.List('estado',
                           message ="Insira o estado da linha de segurança :",
                           choices= ['bom', 'mau', 'regular'],
                         ),
            ]
    
    estado = inquirer.prompt(perguntalinha)
    
    # Inserir Quantidade
    try: 
        quantidade = int(input("insira o número de cabinas pelas quais passa o cordão de segurança:"))
    except ValueError:
        print("tem que ser numero inteiro")
    
    # Inserir Iluminação      
    iluminacao = input("insira a  iluminação  [v] se estiver acceso, caso contrário, [f]:")
    
    
    if iluminacao == 'v':
        iluminacao = True
    elif iluminacao == 'f':
        iluminacao = False
    else: 
        print("Valor não aceite")
        
    #estadocabinas = input('insira o estado construtivo das cabinas do cordão de segurança, que pode ser bom, mau ou regular:')
    
    perguntacabina = [
            inquirer.List('estadocabina',
                           message="Insira o estado da linha de segurança :",
                           choices=['bom', 'mau', 'regular'],
                         ),
            ]
    
    estadocabinas = inquirer.prompt(perguntacabina)
    
    
    obj = CordaoDeSeguranca(perimetro,topologia,altura,estado,quantidade,iluminacao,estadocabinas)  
    
    lista_de_objectos.append(obj)  
    
    perguntaprompt= [
        inquirer.List('estado',
            message ="Quer adicionar mais  equipamentos ?",
            choices= ['sim', 'nao'],
             ),
            ]
    
    resposta = inquirer.prompt(perguntaprompt)
    prompt1 = resposta['estado']



    os.system('clear')

visualizar = input("O que pretende visualizar | [1]-Perimetro e altura | [2]- Outro : ")
    
match visualizar:
    case "1":
            print("verificando o perimetro e altura de todos os objectos:")
            for object in lista_de_objectos:
                    print(f"perimetro : {object.MostrarPerímetro()} | altura : {object.MostrarAltura()} ")
    case "2":
                print("adeus")
                exit             


            

    
  
 



  

