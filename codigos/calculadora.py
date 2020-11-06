#classe calculadora


class Calculadora:
    
    def __init__(self):
        res = 0.0
        
    def __str__(self):
        return str("Sou uma calculadora, você pode fazer operações de soma, subtracao, multiplica, divide  e potencia. o que vai querer?")

    def soma(self,a,b):
        return a + b
    
    def subtracao(self,a,b):
        return a - b
    
    def multiplica(self,a,b):
        return a*b

    def divide(self,a,b):
        return a/b

    def potencia(self,a,b):
        return a**b
    









#classe impressora
class Impressora:
  def __init__(self):
    pass

  def __str__(self):
    return str("Sou uma Impressora")
  
  def imprime(self,frase):
    print(frase)


#
#Checagem de escopo de execução
if __name__ == '__main__':
  c = Calculadora()
  c.soma(45,23)
