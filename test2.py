from ast import For, If

# def funcTest(a, b):
#    For n in range(5):
#        print (n)

# funcTest(5, 4)

# for a in range(5):
#    print(a)

def funcTest2(a):
    for x in range(6):
        
        if x > a :
            break
        else:
            print(x)

texto = "Jesus"

def funcStrings():

    ultimo = len(texto) - 1
    print(texto[ultimo])
    
    #Métodos de string
    metodoFind = texto.find("u")
    print("Método .find: ")
    print(metodoFind)

    metodoJoin = ">".join(texto)
    print("Método .join: ")
    print(metodoJoin)

    metodoSplit = texto.split("e")
    print("Método .split: ")
    print(metodoSplit)

    metodoReplace = texto.replace("s", "S")
    print("Método .replace: ")
    print(metodoReplace)

#funcStrings()


def desafioOrdemAlfabetica(palavra1, palavra2):
    if palavra1.upper() < palavra2.upper():
        print(palavra1)
        print(palavra2)
    else:
        print(palavra2)
        print(palavra1)

#desafioOrdemAlfabetica("Xicara", "banana")

#Lista Vazia
lista = []

#Lista numérica
lista2 = [1, 2, 3]

#Lista de listas
listas = [[1, 2], [True, False]]

#Invocação de trás pra frente quando for índice negativo
#print(lista2[-3])

palavra1 = "abacaxi"

palavra2 = "raiar"

def desafioPalindromo(palavra):
    palavraInversa = ""
    for letra in palavra:
        palavraInversa += palavra[-1]
        palavra.pop()
    if palavra == palavraInversa:
        print(True)
    else:
        print(False)

desafioPalindromo(palavra1)
    





