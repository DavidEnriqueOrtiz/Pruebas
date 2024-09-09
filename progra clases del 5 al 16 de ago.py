# No iterable: float, int, bool
# iterable: str, dic, list, tuple
x = (9.0,7,8,6)
print(x[0])

l = [1,7,0,1.6,2]

print(type(l))

print(l[-1])
#imprime el ultimo elemento de una lista

print(len(l))

l.append(0)
# agregamos un elemento a la lista, la tupla no puede hacer eso

print(l)

l[5] = 15
#cambiamos el sexto elemento de la lista

print(l)

#son iterables porque podemos usar una serie de indices para malipular los elementos

t = 0
#no podemos acceder a elementos porque es un entero y probocaria error

#cadenas de caracteres

cadena = "hola mundo!7"

print(cadena[-1])
print(type(int(cadena[-1])))
print((int(cadena[-1])))
#ahora el 7 no es str, paso a ser int

x,y = "124",12
print(type(x))
print(type(y))

tup = "56",
print(type(tup))
#se puede hacer una tupla de un solo elemento agregando una coma al final

print(tup[0])

#regresando a cadena

print(cadena[1:4])
#recuerda que la h no aparce porque se inicia a contar desde 0,
#esta impresion pide los caracteres desde el segundo hasta el 5

#Diccionarios, se utilizan {}

diccionario  = {"llave":"valor","hola":"mundo"}
print(diccionario["hola"])

personas = {"peso":[50,48,76],"altura":[1.60,1.45,.69]}
print(len(personas["peso"]))

#clase del 14/08/24
#jerarquia de operadoes:
#La asociatividad de los operadores es de izquierda
#a derecha, salvo casos especificos

#expresiones dentro de parentesis
print((5+7)+(3+4)+(5+6))

#extraccion de elementos, referencias o atributos
l2 = [10,20,30,40,50,60]
print(l2[(0*3+1):(1+1+1+1)])
#aqui se le pide a la lista l2 que imprima sus elementos
#desde 0*3+1 que es 1 hasta el 1+1+1+1 que es el 4, inicia contando desde
#0 y por eso el 1 es el 20 y termina en el 4 pero es excluyente y lo
#imprime hasta el 3 *que si es la cuarta posicion)

#exponenciacion (de derecha a izquierda)
print(2**81)

print((2**3)**4)

#multiplicacion, division, division de enteros y resto
print(4*2//3.0)
#divide en enteros redondiando  hacia abajo

print(2//3*4)

print(2*3//3)

print(3//3.0%4)
#investigar rl %

#Adicion y sustraccion
print(2+4-1)

#Comparacion (<,>,==,<=,>=),identidad (is, is not)
#y pertenencia (in, not in)

x2 = 3
y2 = 3

print(x2 is y2)
#el operador is nos arrojara un valor True si y solo si
#ambos objetos son lo mismo, en otro caso regresara false

print(len('e') == len('4'))
#imprime true debido a que solo son un caracter en ambos casos

print(x2 == y2)
#el operador == nos dira true si ambos objetos tienen el mismo valor

x3 = 2
y3 = 4
print(x3 is y3)

print(3>2)

#Negacion booleana (de derecha a izquierda)
print(not 3==2)
#imprime True debido a que no son iguales y justo preguntas
#si No son iguales

#Conjuncion booleana

print(3 == 3 and 3<5)
#imprime true devido a que se cumplen ambas condiciones

#Disyuncion booleana
print(8 < 3 or  3 < 5)
#imprime true debido a que se cumple minimo uno de las condiciones

#Expresion condicional
x4 = 3 if 3 < 2 else 0
print(x4)
#x4 vale 0 ya que 3 es mayor a dos entonces no se cumple la
#condicion para que x4 valga 3 y vale 0

#Notacion lambda
f = lambda a : a + 10
#definicion de una funcion anonima

print(f(1))
print(f(5))
#f funciona como funcion debido a la lambda y suma 10 a los valores

