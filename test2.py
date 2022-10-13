from ast import For, If
from re import X

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
    if palavra == palavraInversa:
        print(True)
    else:
        print(False)

#desafioPalindromo(palavra1)´

e_par = lambda x: x % 2 == 0

def funcLambda(y):
    if e_par(y):
        print("Po, verdade verdadeira em irmão!")
    else:
        print("Mentira, é par não!")

#funcLambda(1)

list = ["Português", "Legislação", "Desenvolvimento", "Adm. de Servidores", "Adm. de SGBD", "Mato Grosso", "Banco de Dados", "Versionamento", "Engenharia de Software"]

def testeRange(y):
    for item in range(1,5,1):
        print(item)
            
#testeRange()

def desafioDivisor(max, divisor):
    lista = []
    for i in range(max, 1, -1):
        if i % divisor == 0:
            lista.append(i)
    return print(lista)


#desafioDivisor(21, 3)
    
#############################################################################

#Gerador Yield

def geradorQuadrados():
    for x in range(5):
        yield x * x

#for n in geradorQuadrados():
#   print(n)


#Expressão Geradora ()

geradorQuadrados2 = (x*x for x in range(5))
for n in geradorQuadrados2:
    print(n)

#Gerador de lista []

#lista = [x for x in range(5)]
#print (lista)

listaCubo22 = [x*x*x for x in range(5)]
#print(listaCubo22) 

listaElaboradaPares = [x for x in range(10) if x % 2 == 0]
#print(listaElaboradaPares)

#Desafio geradir List Comprehensions

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [(9 / 5 * x) + 32 for x in celsius]
#print(fahrenheit)






















