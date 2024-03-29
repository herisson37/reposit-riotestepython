from ast import For, If
import copy
from datetime import date
import functools
from genericpath import isdir
import math
import os
import random
from re import X
import re
import sys

def funcTest(a, b):
   for n in range(5):
       print (n)

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

# funcStrings()


def desafioOrdemAlfabetica(palavra1, palavra2):
    if palavra1.upper() < palavra2.upper():
        print(palavra1)
        print(palavra2)
    else:
        print(palavra2)
        print(palavra1)

#desafioOrdemAlfabetica("Xicara", "banana")

#############################################################################

#Lista Vazia
lista = []

#Lista numérica
lista2 = [1, 2, 3]

#Lista de listas
listas = [[1, 2], [True, False]]

#Invocação de trás pra frente quando for índice negativo
# print("Elemento encontrado é: " + str(lista2[-3]))

palavra1 = "abacaxi"

palavra2 = "raiar"

def desafioPalindromo(palavra):
    palavraInversa = ""
    contador = 1
    for letra in palavra:
        palavraInversa += palavra[-contador]
        contador += 1
    if palavra == palavraInversa:
        print(True)
        print(palavraInversa)
    else:
        print(False)
        print(palavraInversa)

# desafioPalindromo(palavra2)

e_par = lambda x: x % 2 == 0

def funcLambda(y):
    if e_par(y):
        print("Po, verdade verdadeira em irmão!")
    else:
        print("Mentira, é par não!")

# funcLambda(10)

listaMaterias = ["Português", "Legislação", "Desenvolvimento", "Adm. de Servidores", "Adm. de SGBD", "Mato Grosso", "Banco de Dados", "Versionamento", "Engenharia de Software"]

def testeRange():
    for item in range(2,10,1):
        print(item)
            
# testeRange()

def desafioDivisor(max, divisor):
    lista = []
    for i in range(max, 1, -1):
        print(i)
        if i % divisor == 0:
            lista.append(i)
    return print(lista)


# desafioDivisor(21, 3)
    
#############################################################################

#Gerador Yield

def geradorQuadrados():
    for x in range(5):
        yield x * x


# for n in geradorQuadrados():
#     if not(n > 2): 
#         print(n)
#     else:
#         break

#Expressão Geradora ()

geradorQuadrados2 = (x*x for x in range(5))

def funcGeradorQuadrados2():
    for n in geradorQuadrados2:
        print(n)

#funcGeradorQuadrados2()
#Gerador de lista []

listaTeste = [x*x for x in range(5)]
# print (listaTeste)


listaCubo22 = [numero*numero*numero for numero in range(5)]
# print(listaCubo22) 

listaElaboradaPares = [x for x in range(10) if x % 2 == 0]
# print(listaElaboradaPares)

#Desafio gerador List Comprehensions

celsius = [39.2, 36.5, 37.3, 37.8]
fahrenheit = [(9 / 5 * x) + 32 for x in celsius]
#print(fahrenheit)
numberAA = [1, 2, 3]
# print(dir(numberAA))
print([x for x in dir(print)])



#############################################################################

#Dicionários

pt_eng = {'Cachorro': 'dog', 'Agua': 'Water'}

#print(pt_eng)

#print (pt_eng["Agua"])

pt_eng["Cachorro"]

pt_eng.get("Agua")

# print(pt_eng.get("Agua"))
# print(pt_eng["Cachorro"])
#pt_eng['Cachorro'] = 'Puppy'
#print(pt_eng)
# pt_eng['Cachorro'] = 'Puppy'
# print(pt_eng["Cachorro"])
#print(pt_eng["Cacharro"])
pt_eng['Cacharro'] = 'Little one'

#print(pt_eng.pop('Cacharro'))

len(pt_eng)

'Cachorro' in pt_eng

valores = pt_eng.values()

pt_eng.keys()

iterador = iter(pt_eng)

next(iterador)

# for x in iterador:
#     print(x, ':', pt_eng[x])

# for x in sorted(pt_eng):
#     print(x)

texto12 = "O sabiá sabia de tudo."

def histograma(texto):
    h = dict()

    for letra in texto:
        if letra.lower() not in h:
            h[letra.lower()] = 1
        else:
            h[letra.lower()] += 1
    return h

# print(histograma(texto12))
    
# Desafio

def buscaChave(dicionario, valor):

    for chave in dicionario:
        if dicionario[chave] == valor:
            return print(chave)
    return None

dicio = {'Chave1': 10, 'Chave2': 20}

# buscaChave(dicio, 10)

#############################################################################

# TUPLAS

tupl = (2,)
# print(type(tupl))

tupl1 = tuple()

tupl2 = tuple('teste')

tupl3 = tuple([1, 2, 3, 4, 5, 6])

tupl4 = ('a',) + tupl3[1:]
# print(tupl4)

tupl * 3

'a' in tupl4

tuplaDiv = divmod(10, 3)
print(tuplaDiv)

tuplaDiv1, tuplaDiv2 = divmod(7, 3)
# print(tuplaDiv1)
# print(tuplaDiv2)


def testeVariosParametros(*variosValores):
    ag = 0
    for i in variosValores:
        ag += i
    print("\n")
    print(ag)

# testeVariosParametros(1, 2, 3, 4)

# Desafio

def media(*variosVal):
    soma = 0
    print(type(variosVal))
    for v in variosVal:
        soma += v
    return soma / len(variosVal)

#print(media(1, 10, 5, 50))

def calcfib(num):
    x, y = 0, 1
    while x < num:
        print(x, end='')
        x, y = y, x+y
    print()

#calcfib(1000)

        
#############################################################################

# Arquivos

# arq = open('palavras.txt')

# print(arq.readline())
# print(arq.readline())

# def forArq():
#     for a in arq:
#         print(a.strip())
    
# forArq()

# arq1 = open('palavras.txt', 'w')
# arq1.write('Agora estou escrevendo isso dentro do arquivo\n') 
# arq1.close() 

# print('Para %d o valor é %g no dia %s' % (10, 5.43, 'dez'))

diretorioAtual = os.getcwd()
# print(diretorioAtual)

os.path.exists('palavras.txt')
os.path.isdir('palavras.txt')

#print(os.listdir(diretorioAtual))

# Exceções

def testTratamento1():
    while True:
        try:
            x = int(input("Digite um valor inteiro: "))
            break
        except ValueError:
            print("O valor digitado é invalido, tente novamente.")

def testTratamento2():
    try:
        x = int(input("Digite número entre 1 e 10: "))
        if not (x >= 1 and x <= 10):
            raise ValueError
    except ValueError:
        print("O valor digitado é invalido, tente novamente.")
    else:
        print("O valor digitado foi %d." % x)
    finally:
            print("FIM.")

# testTratamento2()

# Crie uma função 'percorra' que lista todos os arquivos de um diretório de forma recursiva.

def percorra(diretorio):
    for arquivoOuDiretorio in os.listdir(diretorio):
        caminho = diretorio + '\\' + arquivoOuDiretorio
        if os.path.isfile(caminho):
            print(caminho)
        else:
            percorra(caminho)

#percorra(os.getcwd())


#############################################################################

# Bibliotecas padrões

dir(os)

os.system("")


sys.platform


re.findall(r'\bf[a-z]*', 'faca bala laranja fusca') # Traz palavras que começam com F

re.sub(r'\se\s', ' & ', 'João e Maria') # Substitui sempre que tiver um espaço + letra E + espaço


math.cos(math.pi / 4)

math.log(1024, 2)


random.random()

random.choice(['uva', 'pera', 'banana'])

random.sample(range(100), 10)


hoje = date.today()

meuNasc = date(1995, 8, 7)

tempo = hoje - meuNasc

#############################################################################

# Classes e Objetos

class Tijolo:
    """Legal, assim que cria classe em python."""

class Retangulo:
    """"Só um retângulo."""

t1 = Tijolo()

t1.x = 1
t1.y = 2.0

# print(t1.y)

def trabObj(obj):
    print(obj.x + obj.y)

trabObj(t1)

r = Retangulo()
r.largura = 100
r.altura = 50
r.canto = Tijolo()
r.canto.x = 10.0
r.canto.y = 20.0 

# help(Tijolo)

def achaCentro(ret):
    p = Tijolo()
    p.x = ret.canto.x + ret.largura/2
    p.y = ret.canto.y + ret.altura/2
    return p

p = achaCentro(r)
# (p.x + p.y)

# Alterando o valor do objeto a partir de uma função.

def move_retangulo(ret, dist):
    ret.canto.x += dist
    ret.canto.y += dist

move_retangulo(r, 10)

r.canto.x
r.canto.y


s = copy.copy(r)
s.altura += 15

r.altura
s.altura

r is s

# Desafio

class Circulo:
    """"Classe criada pro desafio."""

circ = Circulo()
circ.raio = 2

def calcula_area(c):
    area = math.pi * c.raio**2
    return area

# calcula_area(circ)

#############################################################################

# Métodos

class Retangulo2:

    def __init__(self, largura=22, altura=13):
        self.largura = largura
        self.altura = altura

    def imprimir(self):
        print ("Largura: %d - Altura: %d" % (self.largura, self.altura))

    def aumentar(self, cm):
        self.altura += cm
        self.largura += cm

    def __str__(self):
        return "Largura: %d - Altura: %d" % (self.largura, self.altura)

    def __add__(self, outro):
        if isinstance(outro, int):
            return Retangulo2(self.altura + outro, self.largura + outro) 
        elif isinstance(outro, Retangulo2):
            return Retangulo2(self.altura + outro.altura, self.largura + outro.largura)
        else:
            raise ValueError

r = Retangulo2(10, 20)

r.aumentar(5)

# r.imprimir()

t = Retangulo2(1, 2)

# t.imprimir()

f = Retangulo2(50, 100)

# print(f)

p = Retangulo2(1, 2)

p1 = p + 100
# print(p1.altura)
# print(p1.largura)

n15 = Retangulo2(5, 6) + Retangulo2(2, 1) 

# print(n15)

# Desafio

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        print(math.pi * self.raio**2)

cir = Circulo(10)
# cir.area()

#############################################################################

# Herança

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        # print('Contruindo Pessoa')


class PessoaFisica(Pessoa):
    def __init__(self, CPF, nome='', idade=0):
        super().__init__(nome, idade)
        # print('Contruindo Pessoa Física')
        self.CPF = CPF

    def getIdade(self):
        return self.idade


class PessoaJuridica(Pessoa):
    def __init__(self, CNPJ, nome='', idade=0):
        super().__init__(nome, idade)
        # print('Contruindo pessoa jurídica')
        self.CNPJ = CNPJ

pf = PessoaFisica('048.897.571-98', 'Herrisson', 27)

# print(pf.nome)

pj = PessoaJuridica(555, 'Empresa', 50)
# print(pj.idade)

isinstance(pf, Pessoa)

isinstance(pf, PessoaFisica)

isinstance(pf, PessoaJuridica)

issubclass(PessoaFisica, Pessoa)

issubclass(PessoaFisica, PessoaJuridica)

# Herança Múltipla

class Estudante:
    def __init__(self, matricula):
        print('Construindo Estudante')
        self.matricula = matricula

class PessoaFisica2(Pessoa, Estudante):
    def __init__(self, CPF, nome='', idade=0, matricula=111):
        Pessoa.__init__(self, nome, idade)
        Estudante.__init__(self, matricula)
        print('Contruindo Pessoa Física')
        self.CPF = CPF

# pf2 = PessoaFisica2(333, 'Harry', 27, 12)


# Programação Funcional

# Map

numeross = [1, 2, 3, 4, 5, 6, 7]

quadrado = list(map(lambda x: x**2, numeross))

# Filter

pares = list(filter(lambda x: x % 2 == 0, numeross))

# Reduce
# Precisa importar a biblioteca 'functools'

somas = functools.reduce(lambda x, y: x + y, numeross)

# Desafio

class Animal:
    def __init__(self, nome):
        self.nome = nome

class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome)

    def miar(self):
        print("%s está miando" % self.nome)

g = Gato("Nina")

# g.miar()

print(quadrado)
print(pares)
print(somas)


p1=[50,40,30,20,10]

p2=[]

def fd(p1,p2):
    for i in range(len(p1)):
        p2.append(p1.pop())



def fb(p1,p2):
    if(len(p1)==0):
        return
    x=p1[len(p1)-1]
    del p1[len(p1)-1]
    fb(p1,p2)
    p2.append(x)

fb(p1, p2)
print(p2)
