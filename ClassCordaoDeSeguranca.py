class CordaoDeSeguranca:
    def __init__(self,perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas):
        self._perimetro = perimetro
        self._altura = altura
        self._estado = estado
        self._tipologia = tipologia
        self._cantCabinas = cantCabinas
        self._iluminda = iluminda
        self._estadocabinas = estadocabinas
        
        
     
        
         
    def MostrarTipologia(self):
        return self._tipologia
    
    def MostrarEstado(self):
        return self._estado
    
    def MostrarAltura(self):
        return  self._altura
        
    def MostrarPerímetro(self): 
        return self._perimetro
    
    def MostrarQuantidadCabinas(self):
        return self._cantCabinas
    
    def MostrarEstadoCabinas(self):
        return self._MostrarEstado
    
    def Mostrariluminação(self):
        return self._iluminda
     
    