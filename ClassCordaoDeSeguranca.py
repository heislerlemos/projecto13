import uuid

class CordaoDeSeguranca:
    def __init__(self,perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas,id=None):
        self._perimetro = perimetro
        self._altura = altura
        self._estadoLinha = estado
        self._tipologia = tipologia
        self._quantCabinas = cantCabinas
        self._iluminda = iluminda
        self._estadocabinas = estadocabinas
        self._id =  id if id else uuid.uuid4()

            
         
    def MostrarTipologia(self):
        return self._tipologia
    
    def MostrarEstado(self):
        return self._estadoLinha
    
    def MostrarAltura(self):
        return  self._altura
        
    def MostrarPerímetro(self): 
        return self._perimetro
    
    def MostrarQuantidadCabinas(self):
        return self._quantCabinas
    
    def MostrarEstadoCabinas(self):
        return self._estadocabinas
        
    def Mostrariluminação(self):
        return self._iluminda
     
    