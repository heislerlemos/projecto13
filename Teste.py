from ClassCordaoDeSeguranca import *

def criar_os_objectos(perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas):
    obj = CordaoDeSeguranca(perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas)
   
   

def test_answer():
    assert criar_os_objectos(23.1,3.5,"mau","muro",10,"v","mau")    ==  None