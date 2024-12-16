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
    
    answer = inquirer.prompt(perguntalinha)
    estado = answer['estado']
    
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
        
    #estadocabinas = input('insira o estado construtivo das cabinas do cordão de segurança, que pode ser bom, mau ou regular:')
    
    perguntacabina = [
            inquirer.List('estadocabina',
                           message="Insira o estado da linha de segurança :",
                           choices=['bom', 'mau', 'regular'],
                         ),
            ]
    
    estadocabinas = inquirer.prompt(perguntacabina)
    try: 
         cantCabinas = int(input("insirir quantidade de cabinas"))
    except ValueError:
         print("insira valor inteiro")
    
    tipologia = input("insira typologia")
    
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

visualizar = input(
                  """
                    O que pretende visualizar:
                   [1]- Conhecer a altura e o perímetro do cordão de segurança dada uma tipologia\n 
                   [2]- Alertar para a necessidade de reparação do cordão de segurança, informando as caraterísticas do mesmo\n 
                   [3]- Saber quantas cabinas não possuem iluminação\n 
                   [4]- Alertar quantas cabinas estão a necessitar de reparação \n
                   [5]- Listar as linhas de segurança do tipo muro, onde o estado construtivo de suas cabinas é ruim \n
                   """
                   )



    
match visualizar:
    case "1":
            print("[1]-Verificando o perimetro e altura de todos os objectos:")
            for object in lista_de_objectos:
                    print(f"Nº {id}, UUID: {object._id}  perimetro : {object.MostrarPerímetro()} | altura : {object.MostrarAltura()} ")
                    

    case "2":
            print("[2]Verificando cordões de segurança que necessitam reparação")
            id = 0
            for object in lista_de_objectos:
                
                if object.MostrarEstadoCabinas() == 'mau':
                    id += 1
                    print (f"Nº {id}, UUID: {object._id} precisa de reparação ,{object.MostrarEstadoCabinas()}")
                    


    case "3":
            print("[3]-Cabinas sem uluminação ?")  
            id = 0
            for object in lista_de_objectos:
                
                if object.Mostrariluminação() == False:                
                    id += 1
                    print(f"Nº {id}, UUID: {object._id} precisa de iluminação, {object.Mostrariluminação()}")

    
   



            

    
  
  
 



  

