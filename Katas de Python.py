# Generated from: Katas de Python.ipynb
# Converted at: 2026-08-05T20:03:02.829Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

# ## 01 Escribe una función que reciba una cadena de texto como parámetro y devuelva un diccionario con las frecuencias de cada letra en la cadena. Los espacios no deben ser considerados. ##


from functools import reduce

def contar_letras(cadena):
    
    frecuencias = dict()
    
    for letra in cadena:
        if letra != " ":
            letra = letra.lower()
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
                
    return frecuencias
    


texto = "Hola que tal todo"

contar_letras(texto)


# ## 02 Dada una lista de números, obtén una nueva lista con el doble de cada valor. Usa la función map() ##
# 


lista = [1,2,3,4,5,6,7,8,9,10]


lista_doble = list(map(lambda x: x*2, lista))
print(lista_doble)

# ## 03 Escribe una función que tome una lista de palabras y una palabra objetivo como parámetros. La función debe devolver una lista con todas las palabras de la lista original que contengan la palabra objetivo. ##


def fam_semantica(lista,objetivo):
    resultado = []
    
    for palabra in lista:
        if objetivo in palabra:
            resultado.append(palabra)

    return resultado
        


lista = ("amar", "mama", "amarre", "amable", "amado", "mar" , "palabras", "amistad", "barra")

fam_semantica(lista, "ama")

# ## 04 Genera una función que calcule la diferencia entre los valores de dos listas. Usa la función map() ##


def diferencia (x, y):

    return x-y


lista_1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
lista_2 = (2, 3, 4, 5, 6, 7, 8, 9, 10)

list(map(diferencia, lista_1, lista_2))

list(map(lambda x, y: x - y, lista_1, lista_2))

# ## 05 Ecribe una función que tome una lista de números como parámetro y un valor opcional nota_aprobado, que por defecto es 5. La función debe calcular la media de los números en la lista y determinar si la media es mayor o igual que nota aprobado. Si es así, el estado será "aprobado", de lo contrario, será "suspenso". La función debe devolver una tupla que contenga la media y el estado. ##


def media_aprobada (lista, nota_aprobado = 5):
    suma_total = 0

    for x in lista:
        suma_total += x

    resultado = suma_total / len(lista)

    if resultado >= nota_aprobado:
        estado = "Aprobado"
    else:
        estado = "Suspenso"

    
    return (resultado, estado)
        


lista = (5, 7, 7, 8, 7, 3, 5, 6, 6, 5, 4, 3, 3, 3, 1)

media_aprobada(lista)

# ## 06 Escribe una función que calcule el factorial de un número de manera recursiva. ##
# 


def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

factorial(5)

# ## 07 Genera una función que convierta una lista de tuplas a una lista de strings. Usa la función map () ##
# 


def tupla_to_str (tupla):
    return list(map(str,tupla))

lista= ([(1, 2), (3, 4), (5, 6)])

tupla_to_str(lista)

# ## 08 Escribe un programa que pida al usuario dos números e intente dividirlos. Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje indicando si la división fue exitosa o no. ##


try:

    n1 = float(input(f"por favor introduce el numerador:"))
    n2 = float(input(f"por favor introduce el denominador:"))
    
    resultado = n1/n2

except ZeroDivisionError:

    print(f"No se puede dividir entre 0")

except ValueError:
    
    print(f"Por favor, introduce valores numéricos")

else:
    print(f"El valor de la división es {resultado}")


# ## 09 Escribe una función que tome una lista de nombres de mascotas como parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas en España. La lista de mascotas a excluir es ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"].Usa la función filter() ##


##def lista_mascotas (mascotas):
##    mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
##    mascotas_permitidas = []
##   for i in x:
##        if i in mascotas_prohibidas:
##            pass
##        else:
##            mascotas_permitidas.append(i)
##    return mascotas_permitidas


mascotas_prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]

def lista_mascotas (mascotas):
    
    return mascotas not in mascotas_prohibidas



lista_animales = ["Perro", "Gato", "Pajaro", "Tigre"]

resultado = list(filter(lista_mascotas, lista_animales))

print(f"El resultado de la función filter es: {resultado}")

lista_mascotas(lista_animales)

# ## 10 Escribe una función que reciba una lista de números y calcule su promedio. Si la lista está vacía, lanza una excepción personalizada y maneja el error adecuadamente. ##


def media_lista (lista):
    try:
        suma_total = 0
    
        for x in lista:
            suma_total += x
    
        resultado = suma_total / len(lista)

        return (resultado)

    except ZeroDivisionError:
    
        return print("Por favor, añada una lista con valores")
    


lista = (4,4)

media_lista(lista)

# ## 11 Escribe un programa que pida al usuario que introduzca su edad. Si el usuario ingresa un valor no numérico o un valor fuera del rango esperado (por ejemplo, menor que 0 o mayor que 120, maneja las excepciones adecuadamente. ##


while True:
    try:
        
        edad = float(input("Introduce tu edad: "))

        if 0 <= edad <= 120:
            break
        else:
            print("Por favor, introduzca una edad real.")
            
    except ValueError:
        
        print("Por favor, introduzca un valor numérico")
    


# ## 12 Genera una función que al recibir una frase devuelva una lista con la longitud de cada palabra. Usa la función map() ##
# 


def letras_frase (frase):
    
    palabras = frase.split()
        
    return list(map(len, palabras))


frase = "Buenos días mundo"
letras_frase(frase)

# ## 13 Genera una función la cual, para un conjunto de caracteres, devuelva una lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no pueden estar repetidas .Usa la función map() ##


def min_masc (caracteres):
    caracteres = set(caracteres)
    return list(map(lambda x: (x.upper(), x.lower()), caracteres))

lista = ("Hola")
print (min_masc(lista))

# ## 14 Crea una función que retorne las palabras de una lista de palabras que comience con una letra en especifico. Usa la función filter() ##


def comienzo_palabras (lista, letra):
    
    return list(filter(lambda palabra: palabra.startswith(letra), lista))
        
    

lista = ("Avión, árbol, cabez, pez, centauro")

print(comienzo_palabras(lista, "c"))

# ## 15 Crea una función lambda que  sume 3 a cada número de una lista dada ##
# 


lista = (5, 3, 2, 65, 62)

list(map(lambda x: x + 3, lista))

# ## 16 Escribe una función que tome una cadena de texto y un número entero n como parámetros y devuelva una lista de todas las palabras que sean más largas que n. Usa la función 


def funcion_16 (texto, num):

    palabras = texto.split()
    
    return list(filter(lambda palabra: len(palabra) > num, palabras))

lista = "Hoy puede ser un día maravilloso"

funcion_16(lista, 2)

# ## 17 Crea una función que tome una lista de dígitos y devuelva el número correspondiente. Por ejemplo, 5,7,2 corresponde al número quinientos setenta y dos 572. Usa la función reduce() ##


def código (lista):
    acum = 0

    for num in lista:
        
        acum = acum*10 + num


    return acum

def código (lista):
    
    return reduce(lambda acum, x: acum*10 + x, lista)
    
    

lista = (1, 4, 6)

código(lista)

# ## 18 Escribe un programa en Python que cree una lista de diccionarios que contenga información de estudiantes 
#  (nombre, edad, calificación) y use la función filter para extraer a los estudiantes con una calificación mayor o igual a 
#  90. Usa la función filter()


alumnos = []

def reg_alumno(nombre, edad, calificación):
    
    alumnos.append(
        {"Nombre": nombre,
         "Edad": edad,
         "Calificación": calificación}
    )

    return f"El alumno {nombre} ha sido registrado."


reg_alumno("Juan", 30, 90)
reg_alumno("Alberto", 25, 87)
reg_alumno("Sofía", 27, 100)
reg_alumno("María F", 28, 90)
reg_alumno("Alejandro", 29, 70)
reg_alumno("Estefanía", 29, 86)
reg_alumno("María G", 27, 92)

def filter_alumnos(nota, lista):
    
    return list(filter(lambda alumno: alumno["Calificación"] >= nota, lista))

filter_alumnos(90, alumnos)

# ## 19 Crea una función lambda que filtre los números impares de una lista dada ##


lista_numeros = [4, 6, 3, 1, 7, 8]
impares = list(filter(lambda x: x % 2 != 0, lista_numeros))

print(impares)

# ## 20 Para una lista con elementos tipo integer y string obtén una nueva lista sólo con los valores int. Usa la función filter() ##


lista = [1, "hola", 45, "Caraculo", 5]

list(filter(lambda x: isinstance(x, int), lista))


# ## 21 Crea una función que calcule el cubo de un número dado mediante una función lambda


cubo = lambda x: x**3

cubo(2)

# ## 22 Dada una lista numérica, obtén el producto total de los valores de dicha lista.Usa la función reduce() ## 
# 


def sum_lista (lista):
    return reduce(lambda acum, x: acum + x, lista)

lista = (1, 5, 6, 7, 8)
print(sum_lista(lista))

# ## 23 Concatena una lista de palabras.Usa la función reduce() ##


def concat (lista_palabras):
    return reduce (lambda acum, palabra: acum + palabra, lista_palabras)

lista_palabras = ("Hola", "Buenas", "Perro", "Gato", "Pájaro")
concat(lista_palabras)

# ## 24 Calcula la diferencia total en los valores de una lista. Usa la función reduce() . ##




def diferencia_valores(lista):
    return reduce(lambda acum, x: acum - x, lista)

lista = [20, 6, 5, 1, 5]
print(diferencia_valores(lista))

# ## 25 Crea una función que cuente el número de caracteres en una cadena de texto dada. ##
# 


def contar_caracteres (cadena):
    
        if isinstance(cadena, str):
            
            return len(cadena)
        else:
            raise TypeError("El argumento debe de ser una cadena de texxto")
    

contar_caracteres("Hola mundo, estoy haciendo una Kata de python")

# ## 26 Crea una función lambda que calcule el resto de la división entre dos números dados. ##


resto = lambda x, y: x%y
resto(50, 10)

# ## 27 Crea una función que calcule el promedio de una lista de números ##
# 


def media_num (lista):
    
    return reduce(lambda acum, x: acum + x, lista) / len(lista)


lista = (1, 6, 7, 8, 8)
media_num(lista)

# ## 28 Crea una función que busque y devuelva el primer elemento duplicado en una lista dada.
# 


def busqueda_rep (lista):
    lista_append = []
    duplicado = []
    for x in lista:
        if x not in lista_append:
            lista_append.append(x)
        else:
            duplicado.append(x)
            break

    return duplicado


lista = ("Hola", 5, "reloj", "llaves", 3, "Pajaro", 3, "mochila")
print(busqueda_rep(lista))

# ## 29 Crea una función que convierta una variable en una cadena de texto y enmascare todos los caracteres  con elcarácter '#', excepto los últimos cuatro.


def ocultar(cadena_texto):

    
    cadena_texto = str(cadena_texto)
    almoadillas = (len(cadena_texto) - 4) * "#"
    texto = cadena_texto [-4:]
    cadena_oculta = almoadillas + texto
        
        
    return cadena_oculta
    

ocultar("la contraseña es contraseña")

# ## 30 Crea una función que determine si dos palabras son anagramas, es decir, si están formadas por las mismas letras pero en diferente orden. ##


def anagrama (palabra_1, palabra_2):

    coinciden = []
    
    palabra_1 = palabra_1.lower()
    palabra_2 = palabra_2.lower()
    
    if len(palabra_1) == len(palabra_2):
        
        for x in palabra_1:
                
            if x in palabra_2:
                coinciden.append(x)
            else:
                pass
                    
        if len(coinciden) == len(palabra_1):
                
            resultado = f"La palabra {palabra_1} y la palabra {palabra_2} son anagramas"
        else: 
            resultado = f"La palabra {palabra_1} y la palabra {palabra_2} no son anagramas"
    else:
            resultado = f"La palabra {palabra_1} y la palabra {palabra_2} no son anagramas"
    return resultado


        
   

    

anagrama("Caraculo", "Oreja")

# ## 31 Crea una función que solicite al usuario ingresar una lista de nombres y luego solicite un nombre para buscar en esa lista. Si el nombre está en la lista, se imprime un mensaje indicando que fue encontrado, de lo contrario, se lanza una excepción. ##


def buscador_nombre():
    
    lista_nombre = input("Por favor, añada una lista de nombres:").split(",")
    lista_nombre_ = [nombre.strip().lower() for nombre in lista_nombre]

    nombre = input("Por vaor, añada una nombre a buscar:")
    if nombre.lower() in lista_nombre_:
        return f"El nombre {nombre}  ha sido encontrado en la lista"
    else:
        raise Exception(f"{nombre} no se encuentra en la lista.")

buscador_nombre()

# ## 32 Crea una función que tome un nombre completo y una lista de empleados, busque el nombre completo en la lista y devuelve el puesto del empleado si está en la lista, de lo contrario, devuelve un mensaje indicando que la persona no trabaja aquí.


class Empleado:
    
    empleados = []
    
    def __init__(self, nombre, posición):
        self.nombre = nombre
        self.posición = posición
        Empleado.empleados.append(self)
        
    

Lola = Empleado("Lola", "reponedor")
Manuel = Empleado("Manuel", "Gerente")
Lucas = Empleado("Lucas", "Reponedor")
Javier = Empleado("Javier", "Cajero")
Sara = Empleado("Sara", "Administrativo")
Alba = Empleado("Alba", "Gerente")
Mario = Empleado("Mario", "Cajero")

def buscador_empleados(nombre, empleados):
    
    for empleado in empleados:
        if empleado.nombre == nombre:
            return f"{nombre} trabaja como {empleado.posición}"
            
    return f"{Nombre} no trabaja aquí"
    

buscador_empleados("Mario", Empleado.empleados)

# ## 33 Crea una función lambda que sume elementos correspondientes de dos listas dadas.


lista_1 = [1, 2, 4, 5, 6, 8]
lista_2 = [2, 1, 1, 1 ,1 ,1]

list(map(lambda x, y: x + y, lista_1, lista_2))

# ## 34 Crea la clase árbol


class árbol:
    def __init__(self, ramas = None, tronco = 1):
        self.ramas = [] if ramas is None else ramas
        self.tronco = tronco
         
    def crecer_tronco(self, crecimiento):
        self.tronco += crecimiento
        return f"El árbol ha crecido {crecimiento} cm"

    
    def nueva_rama(self, n_ramas, t_ramas = 1):
        for i in range(n_ramas):
            self.ramas.append(t_ramas)
        return f"Al árbol le han crecido un total de {n_ramas} nuevas rama"
        
    def crecer_ramas(self, C_ramas = 1):
        self.ramas = list(map(lambda x: x + C_ramas, self.ramas))
        
        return [f"rama de {rama} cm" for rama in self.ramas]
        
    def quitar_rama(self, p_ramas = 0):
        self.ramas.pop(p_ramas)
        
    def info_arbol(self):
        
        return f"El árbol tiene un total de {len(self.ramas)} ramas ({[f'rama de {rama} cm' for rama in self.ramas]}). El tronco mide {self.tronco} cm"

manzano = árbol()

manzano.crecer_tronco(1)

manzano.nueva_rama(1)

manzano.crecer_ramas()

manzano.info_arbol()

manzano.nueva_rama(2)

manzano.quitar_rama(2)

manzano.info_arbol()

# ## 36 Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario y agregar dinero al saldo.


class UsuarioBanco:
    lista_usuarios =  []
    def __init__ (self, usuario, saldo, cc = True):
        self.usuario = usuario
        self.saldo = saldo
        if not isinstance(cc, bool):
            raise ValueError("El valor de la cuenta corriente tiene que ser True o False")
        self.cc = cc
        UsuarioBanco.lista_usuarios.append(self)
        
    def retirar_dinero (self, dinero_retirado):
        
        if dinero_retirado <= self.saldo:
            
            self.saldo -= dinero_retirado
            
            print(f"El nuevo saldo de {self.usuario} es {self.saldo}€.")
            
        else:
            
            raise Exception(f"{self.usuario} no tiene saldo sufieciente.")


    def trasferencia_dinero (self, usuario_destino, dinero_transferido):
        
        if dinero_transferido <= self.saldo:
            
            self.saldo -= dinero_transferido
            usuario_destino.saldo += dinero_transferido
            print(f"Transferencia realizada. El nuevo saldo de {self.usuario} es {self.saldo}€.")
            
        else:
             
            raise Exception(f"{self.usuario} no tiene saldo sufieciente.")
                      
    def agregar_dinero (self, dinero_sumado):
        self.saldo += dinero_sumado
        print(f"El nuevo saldo de {self.usuario} es {self.saldo}€.")


Bob = UsuarioBanco("Bob", 50)
Alicia = UsuarioBanco("Alicia", 100)

for usuario in UsuarioBanco.lista_usuarios:
    print(usuario.usuario, usuario.saldo, usuario.cc)

Bob.agregar_dinero(20)

Bob.trasferencia_dinero(Alicia, 80)

Alicia.retirar_dinero(50)

for usuario in UsuarioBanco.lista_usuarios:
    print(usuario.usuario, usuario.saldo)

# ## 37. Crea una función llamada procesar_texto que procesa un texto según la opción especificada: contar_palabras,reemplazar_palabras, eliminar_palabra . Estas opciones son otras funciones que tenemos que definir primero y llamar dentro de la función procesar_texto .
# 


# Código a seguir:
# 
# Crear una función 
# contar_palabras para contar el número de veces que aparece cada palabra en el texto. Tiene 
# que devolver un diccionario.
#     
# Crear una función 
# reemplazar_palabras para remplazar una 
# que devolver el texto con el remplazo de palabras.
#     
# Crear una función 
# palabra_original del texto por una 
# palabra_nueva . Tiene 
# eliminar_palabra para eliminar una palabra del texto. Tiene que devolver el texto con la palabra 
# eliminada.
# 
# Crear la función 
# procesar_texto que tome un texto, una opción(entre "contar", "reemplazar", "eliminar") y un 
# número de argumentos variable según la opción indicada.
# Caso de uso:
# Comprueba el funcionamiento completo de la función 
# procesar_texto


def contar_palabras (texto):
    
    recuento = {}
    texto = texto.lower().split()
    caracteres= (",",".",";",":","!","¡","?","¿")
    texto_limpio= []

    for palabra in texto:
        for caracter in caracteres:
            palabra = palabra.replace(caracter, "")
        texto_limpio.append(palabra)
        
    for palabra in texto_limpio:
        if palabra in recuento:
            recuento[palabra] +=1
        else:
            recuento[palabra] = 1
            
    
    return recuento
    
#quiero que por cada palabra que haya en texto la incluya en un

def remplazar_palabras(texto, p_reemplazar, p_remplazo):
    
    texto = texto.split()
    nuevo_texto = []

    for palabra in texto:
        
        palabra_limpia = palabra.strip(".,;:!?¡¿")
        puntuacion = palabra[len(palabra_limpia):]

        
        if palabra_limpia.lower() == p_reemplazar.lower():
            nuevo_texto.append(p_remplazo + puntuacion)

        else:
            nuevo_texto.append(palabra)

    return " ".join(nuevo_texto)

def elimiar_palabra(texto, p_eliminar):

    texto = texto.split()
    
    texto_filtrado = [palabra for palabra in texto if palabra.lower() != p_eliminar.lower()]

    return " ".join(texto_filtrado)

def procesar_texto (opción, *args):
    
    
    if opción.lower() == "contar":
        return contar_palabras(args[0])

    if opción.lower() == "reemplazar":
        return remplazar_palabras(args[0], args[1], args[2])

    if opción.lower() == "eliminar":
        return eliminar_palabra(args[0], args[1])

    else:
        raise TypeError("La opción deberá ser una entre reemplazar, contar o eliminar")
        



procesar_texto("reemplazar", texto, "oscuro", "Hitler")

texto =( 
"""Tres Anillos para los Reyes Elfos bajo el cielo Siete para los Señores Enanos en palacios de piedra.
Nueve para los Hombres Mortales condenados a morir.
Uno para el Señor Oscuro, sobre el trono oscuro
en la Tierra de Mordor donde se extienden las Sombras.
Un Anillo para gobernarlos a todos.
Un Anillo para encontrarlos,
un Anillo para atraerlos a todos y atarlos en las tinieblas
en la Tierra de Mordor donde se extienden las Sombras. """)

# ## 38 Genera un programa que nos diga si es de noche, de día o tarde según la hora proporcionada por el usuario.
# 


import datetime


Hora = (input("¿Qué hora es? introduce la hora (HH:MM)"))
Hora = datetime.datetime.strptime(Hora, "%H:%M")

#meter función lamba 
if 5 <= Hora.hour < 12:
    
    print("Es por la mañana")
    
elif 12 <= Hora.hour < 21:
    
    print("Es por la tarde")

elif 21 <= Hora.hour <= 24 or 1 <= Hora.hour < 5:

    print("Es por la noche")








# ## 39 Escribe un programa que determine qué calificación en texto tiene un alumno en base a su calificación numérica. 
#  Las reglas de calificación son:
#  
#  0 - 69 insuficiente
#  
#  70 -79 bien
#  
#  80 - 89 muy bien
#  
#  90 - 100 excelente
# 
# 


alumnos

for alumno in alumnos:
    
    if alumno["Calificación"] >= 0 and alumno["Calificación"] <= 69:
        
        alumno["Califiación_texto"] = "Insuficiente"
        
    elif alumno["Calificación"] >= 70 and alumno ["Calificación"] <= 79:
        
        alumno["Califiación_texto"] = "Bien"

    elif alumno["Calificación"] >= 80 and alumno ["Calificación"] <= 89:
        
        alumno["califiación_texto"] = "Muy Bien"

    elif alumno["Calificación"] >= 90 and alumno ["Calificación"] <= 100:

        alumno["califiación_texto"] = "Excelente"

    else:
        pass

alumnos

# ## 40  Escribe una función que tome dos parámetros: datos (una tupla con los datos necesarios para calcular el área de la figura). y figura (una cadena que puede ser "rectangulo" , "circulo" o "triangulo" )
# 


import math


def areas (figura, *datos):
    """ La función calcula el área de tras posibles figuras geométricas: rectangulo, circulo y triangulo. 
    
    Para ello hay que elegir la figura y definir por orden la base y la altura. A excepción del ciruclo que se definira solo el radio"""
    
    figuras = ("rectangulo", "circulo", "triangulo")
    figura = figura.lower()
    pi = math.pi
    
    if figura == "rectangulo":
        base = datos[0]
        altura = datos[1]
        
        area = base * altura
        return area
            
    if figura == "circulo":
        radio = datos[0] 
        
        area = pi * radio **2
        return area

    if figura == "triangulo":
        base = datos[0]
        altura = datos[1]
        
        area = (base * altura)/2
        return area
    else:
        raise Exception (f"Selecione una figura entre {figuras}")
        
        
        


areas("circulo", 5)

# ## 41 En este ejercicio, se te pedirá que escribas un programa en Python que utilice condicionales para determinar el monto final de una compra en una tienda en línea, después de aplicar un descuento.
# 
# 


# 1. Solicita al usuario que ingrese el precio original de un artículo.
# 2. Pregunta al usuario si tiene un cupón de descuento (respuesta sí o no).
# 3. Si el usuario responde que sí, solicita que ingrese el valor del cupón de descuento.
# 4. Aplica el descuento al precio original del artículo, siempre y cuando el valor del cupón sea válido (es decir, mayor 
# a cero). Por ejemplo, descuento de 15€. 
# 5. Muestra el precio final de la compra, teniendo en cuenta el descuento aplicado o sin él. 
# 6. Recuerda utilizar estructuras de control de flujo como if, elif y else para llevar a cabo estas acciones en tu 
# programa de Python


mensaje = "Por favor, introduce el precio del artículo:"
while True:
   
    try:
        articulo = float(input(mensaje))
        break
    
    except ValueError:
        mensaje = "Por favor, introduce un valor numérico:"

resultado = ["si", "no"]
mensaje = "¿Tienes algun descuento?"

while True:
    
    descuento = input(mensaje).lower()
    
    if descuento in resultado:
        break
        
    mensaje = "Por vavor, diga si o no"

if descuento in resultado:
    
    if descuento == "si":
        
        mensaje ="Por favor, introduzca el valor del descuento:"
        
        while True:
            try:
                valor_descuento = float(input(mensaje))

                if valor_descuento > 0:
                
                    precio_final = articulo - valor_descuento
                    
                    break
                else:
                    mensaje = "Por favor, introduzca un descuento mayor a 0"
                
            except ValueError:
                mensaje = "Por favor, introduce un valor numérico:"
                
        print(f"El precio de la compra es igual a {precio_final}")
              
    elif descuento == "no":
        
        print(f"El precio de la compra es igual a {articulo}")