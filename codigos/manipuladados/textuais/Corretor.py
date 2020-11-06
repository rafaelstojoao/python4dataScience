# Cria dicionário para correção


listaDePalavras = ['pão', 'de', 'queijo', 'casa', 'trem', 'bom']

def criaDicionario(listaDePalavras):
    Corretor = {}
    for palavra in listaDePalavras:
        Termo = {palavra[0:x] + palavra[x+1:len(palavra)]:palavra for x in range(0, len(palavra))}
        for chave in Termo:
            Corretor[chave] = Termo[chave] # Incluir correção para a variação da palavra pão  
    return Corretor



Corretor = criaDicionario(listaDePalavras)

def consultaFrase(Corretor,frase):
    #Consultando o corretor
    cont = 0
    for palavra in frase:
        if palavra in Corretor:
            frase[cont] = Corretor[palavra]
        cont += 1 
  

    corrigido = ' '.join(frase)
    return(corrigido)



for chave in Termo:
  Corretor[chave] = Termo[chave]

print(Corretor)

consultaFrase(Corretor,frase = "pão de quijo é um trem bm".split(' '))