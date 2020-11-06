#atributos de classe/instância
class Cachorro:

    tipo = "mamífero" #isso é um atributo de classe
 
    def __init__(self,nome,peso,nascimento):
        self.nome = nome
        self.peso = peso
        self.nascimento  = nascimento
#         self.tipo = tipo
        #o self indica que o atributo pertence somente à instância
    
    
    def latir(self):
        if self.peso >= 15.0:
            return 'ruf ruf'
        else:
            return "au au"

    
    
if __name__ == '__main__':
    meudog = Cachorro("Pankeka",34.5,"20/10/2017")
    meudog.tipo = "estranho"
    print(meudog.tipo)

