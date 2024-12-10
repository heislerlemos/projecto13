class CordaoDeSeguranca:
    def __init__(self,perimetro,altura,estado,tipologia,cantCabinas,iluminda,estadocabinas):
        self.id = id 
        self.perimetro = perimetro
        self.altura = altura
        self.estado = estado
        self.tipologia = tipologia
        self.cantCabinas = cantCabinas
        self.iluminda = iluminda
        self.estadocabinas = estadocabinas
        
        global dic 
        dic = {}    
        dic['perimetro'] = self.perimetro
        dic['altura'] = self.altura
        dic['estado'] = self.estado
        dic['tipologia'] = self.tipologia
        dic['cantCabians'] = self.cantCabinas
        dic['iluminda'] = self.iluminda
        dic['estadocabinas'] = self.estadocabinas
        
         
    def MostrarTipologia(self):
        return dic['tipologia']
    
    def MostrarEstado(self):
        return dic['estado']
    
    def MostrarAltura(self):
        return  dic['altura']
        
    def MostrarPerímetro(self): 
        return dic['perimetro']
    
    def MostrarQuantidadCabinas(self):
        return dic['cantCabians']
    
    def MostrarEstadoCabinas(self):
        return dic['estadocabinas']
    
    def Mostrariluminação(self):
        return dic['iluminda']
     
    