# Projecto 13
from art import *
from ClassCordaoDeSeguranca import *

 
""""
Testando os objectos

"""""
Camara1 =   CordaoDeSeguranca(140.23, 5.2, 'regular', 'muro', 20, True, 'mau' )
Camara1.MostrarAltura()
Camara1.MostrarEstado()
# ........

Camara2 =   CordaoDeSeguranca(110.20, 2.2, 'mau', 'muro', 10 ,False, 'regular' )
Camara3 =   CordaoDeSeguranca(50.21, 5.2, 'bom', 'vedacao', 5 ,False, 'bom')
Camara3 =   CordaoDeSeguranca(490.21, 5.2, 'mau', '', 5 ,False, 'bom')


tprint("Controlo de Camaras Lda")

prompt1 = input ("quer adicionar um novo equipamento ? [sim]][no]")
lista_de_objectos = []
while prompt1 == 'sim':

    perimetro = input("insira  o perímetro do cordão de segurança.\n")
    topologia = input("insira tipologia do cordão de segurança, que pode ser uma vedação ou um muro. \n")
    altura = input("insira a altura da linha de segurança\n")
    estado = input("insira o estado da linha de segurança, que pode ser: bom, mau ou regular \n")
    quantidade = input("insira o número de cabinas pelas quais passa o cordão de segurança\n")
    iluminacao = input("insira a  iluminacaoverdadeiro se estiver aceso, caso contrário, falso.\n")
    estadocabinas = input('insira o estado construtivo das cabinas do cordão de segurança, que pode ser bom, mau ou regular \n')
    
    obj = CordaoDeSeguranca(perimetro,topologia,altura,estado,quantidade,iluminacao,estadocabinas)  
    lista_de_objectos.append(obj)     
    prompt1 = input ("quer continuar a adicionar novos equipamentos ? [sim][nao]")


print("Foram criados os seguintes objectos :", lista_de_objectos)
    
prompt2 = print ("quer executar mais alguma ação ? [sim][nao]")
 
if prompt2 == 'sim':
             
 print("seleciona [1]-MostrarTipologia [2]-MostrarEstado [3]-MostrarAltura[4]-MostrarPerímetro [5]-MostrarQuantidadCabinas [6]-MostrarEstadoCabinas [7]-Mostrariluminação")
    
    

  
  

