# Projecto 13
from art import *
import os
from ClassCordaoDeSeguranca import *
import inquirer

tprint("Controlo de Camaras Lda")


perguntaprompt= [
        inquirer.List('escolha',
            message ="Quer adicionar equipamentos ?:",
            choices= ['sim', 'nao'],
             ),
            ]
    
resposta= inquirer.prompt(perguntaprompt)
prompt1 = resposta['escolha']

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
            inquirer.List('tipologia',
                           message ="Insira o estado da linha de segurança :",
                           choices= ['muro', 'vedação'],
                         ),
            ]
    
    resposta = inquirer.prompt(perguntatopologia)
    tipologia = resposta['tipologia']
    
    
    # Inserir Altura
    try:
        altura = float(input("insira a altura da linha de segurança:"))
    except ValueError:
        print("Tem que ser decimal")
    
    # Inserir Estado
    
    perguntalinha = [
            inquirer.List('estadolinha',
                           message ="Insira o estado da linha de segurança :",
                           choices= ['bom', 'mau', 'regular'],
                         ),
            ]
    
    answer = inquirer.prompt(perguntalinha)
    estado = answer['estadolinha']
    
    # Inserir Quantidade
    try: 
        quantidade = int(input("insira o número de cabinas pelas quais passa o cordão de segurança:"))
    except ValueError:
        print("tem que ser numero inteiro")
    
    # Inserir Iluminação      
    iluminda = input("insira a  iluminação  [v] se estiver acceso, caso contrário, [f]:")
    
    
    if iluminda== 'v':
        iluminda = True
    elif iluminda == 'f':
        iluminda = False
    else: 
        print("Valor não aceite")
        
    
    perguntacabina = [
            inquirer.List('estadocabina',
                           message="Insira o estado da cabina de segurança :",
                           choices=['bom', 'mau', 'regular'],
                         ),
            ]
    
    answer = inquirer.prompt(perguntacabina)
    estadocabinas = answer['estadocabina']
    
    try: 
         cantCabinas = int(input("insirir quantidade de cabinas"))
    except ValueError:
         print("insira valor inteiro")
    

    obj = CordaoDeSeguranca(perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas)  
    
    lista_de_objectos.append(obj)  
    
    perguntaprompt= [
        inquirer.List('estado',
            message ="Quer adicionar mais  equipamentos ?",
            choices= ['sim', 'nao'],
             ),
            ]
    
    resposta= inquirer.prompt(perguntaprompt)
    prompt1 = resposta['estado']

    os.system('clear')


    
def opcoe(escolha):   
    match escolha:
    
        case "1":
            print("[1]-Verificando o perimetro e altura de todos os objectos:")
            id = 0
            for object in lista_de_objectos:
                    id += 1
                    print(f"Nº {id}, UUID: {object._id}  perimetro : {object.MostrarPerímetro()} | altura : {object.MostrarAltura()} ")
           
            input("Click ENTER para continuar...")                     
            menu()  

        case "2":
            print("[2]Verificando cordões de segurança que necessitam reparação")
            id = 0
            for object in lista_de_objectos:
                
                if object.MostrarEstado() == 'mau':
                    id += 1
                    print (f"Nº {id}, UUID: {object._id} precisa de reparação ,{object.MostrarEstado()}")

            input("Click ENTER para continuar...")                                       
            menu() 
                   
        case "3":
            print("[3]-Cabinas sem iluminação ?")  
            id = 0
            for object in lista_de_objectos:
                
                if object.Mostrariluminação() == False:                
                    id += 1
                    print(f"Nº {id}, UUID: {object._id} precisa de iluminação, o estado é : {object.Mostrariluminação()}")
            
            input("Click ENTER para continuar...")                                 
            menu()
    
        case "4":
            print("[4]-Cabinas que necessitam reparação")
            id = 0 
            for object in lista_de_objectos:
                
                if object.MostrarEstadoCabinas() == 'mau':
                    id += 1
                    print (f"Nº {id}, UUID: {object._id} precisa de reparação , esta em  {object.MostrarEstadoCabinas()} estado")
                  
            input("Click ENTER para continuar...")                     
            menu()
                    
        case "5":
            print("[5]-Lista de linha de segurança")
            id = 0
            
            for object in lista_de_objectos:
                
                if object.MostrarTipologia() == 'muro' and  object.MostrarEstadoCabinas() == 'mau':
                    id += 1
                    print (f"Nº {id}, UUID: {object._id} esta utilizando ,{object.MostrarTipologia()} e as cabinas estao em {object.MostrarEstadoCabinas()} estado")
            
            input("Click ENTER para continuar...")                     
            menu()
        
        case "6":
            print("[6]-Programa terminado adeus")
            exit
            


def menu():
    escolha = input(
                   """
                   O que pretende visualizar:
                   [1]- Conhecer a altura e o perímetro do cordão de segurança dada uma tipologia\n 
                   [2]- Alertar para a necessidade de reparação do cordão de segurança, informando as caraterísticas do mesmo\n 
                   [3]- Saber quantas cabinas não possuem iluminação\n 
                   [4]- Alertar quantas cabinas estão a necessitar de reparação \n
                   [5]- Listar as linhas de segurança do tipo muro, onde o estado construtivo de suas cabinas é ruim \n
                   [6]- Terminar o programa
                   """
                   )
    opcoe(escolha)   
            
            
menu()

    
  
  
 



  

