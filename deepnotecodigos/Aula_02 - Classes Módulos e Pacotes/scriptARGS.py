#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
 
import sys


def __str__():
	return 	"eu faço médias"


def media(valores):
	media 	= 0.0
	soma 	= 0.0

	for i in range(1,len(valores)):
		soma += float(valores[i])

	return soma/(len(valores)-1)

 
def processador(args):

    # print(args[0]) #o argumento na posição 0 é o nome do script
    
    print("A média dos valores:\n")
    
    for i in range(1,len(args)):
    	print(args[i])

    print("\nÉ...",str(media(args)))
     
    return 0
 



if __name__ == '__main__':
    sys.exit(processador(sys.argv))