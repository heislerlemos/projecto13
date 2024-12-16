# Projecto 13
from art import *
import os
from ClassCordaoDeSeguranca import *

tprint("Controlo de Camaras Lda")

prompt1 = input ("quer adicionar um novo equipamento ? [sim]][no]")
lista_de_objectos = []

while prompt1 == 'sim':
    print ("Criando o objecto")
    
    try:
        perimetro = int(input("insira  o perímetro do cordão de segurança:"))    
    except ValueError:
        print("Tem que ser um numero inteiro ")    
        
    topologia = input("insira tipologia do cordão de segurança, que pode ser uma vedação ou um muro:")
    altura = input("insira a altura da linha de segurança:")
    estado = input("insira o estado da linha de segurança, que pode ser: bom, mau ou regular:")
    quantidade = input("insira o número de cabinas pelas quais passa o cordão de segurança:")
    iluminacao = input("insira a  iluminacaoverdadeiro se estiver aceso, caso contrário, falso:")
    estadocabinas = input('insira o estado construtivo das cabinas do cordão de segurança, que pode ser bom, mau ou regular:')
    
    obj = CordaoDeSeguranca(perimetro,topologia,altura,estado,quantidade,iluminacao,estadocabinas)  
    lista_de_objectos.append(obj)  
    prompt1 = input ("quer continuar a adicionar novos equipamentos ? [sim][nao]")

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


            

    
  
 



  

