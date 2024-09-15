#Realizar comentarios en Python
print("Hola, Bienvenidos este archivo tiene como proposito afianzar los conceptos de los Identificadores, variables y los tipos de datos primitivos!")

# Utilizo Camel Case y Snake Case para la nomenclatura al declar variables

"""
Este es un bloque de texto grande
que puede ser utilizado como un comentario
de varias líneas.
"""

#Numeros Enteros - en Python se codifican con la palabra Reservada Int
anio = 29
codigoEstudiante = 71221109
dias_del_mes = 30
semestre = 6
celular = 3128309000

# En Python, el tipo de dato int puede contener un número ilimitado de dígitos.
numeroAtomos = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000
#Función type() para verificar el tipo de cualquier objeto en Python
# Imprimir el texto junto con el valor formateado
#print(f"numero de atomos: {int(numeroAtomos)}")



# Entero a cadena
entero_a_cadena = str(543)
print(entero_a_cadena, type(entero_a_cadena))  # Resultado: '100' <class 'str'>

# Cadena a entero
cadena_a_entero = int("123")
print(cadena_a_entero, type(cadena_a_entero))  # Resultado: 123 <class 'int'>

# Flotante a cadena
flotante_a_cadena = str(3.14)
print(flotante_a_cadena, type(flotante_a_cadena))  # Resultado: '3.14' <class 'str'>

# Cadena a flotante
cadena_a_flotante = float("45.67")
print(cadena_a_flotante, type(cadena_a_flotante))  # Resultado: 45.67 <class 'float'>

# Entero a flotante
entero_a_flotante = float(10)
print(entero_a_flotante, type(entero_a_flotante))  # Resultado: 10.0 <class 'float'>

# Flotante a entero
flotante_a_entero = int(10.7)
print(flotante_a_entero, type(flotante_a_entero))  # Resultado: 10 <class 'int'>


# Usando comillas dobles triples
texto_multilinea1 = """Este es un ejemplo de
una cadena de texto
que abarca varias líneas."""
print(texto_multilinea1)

# Usando comillas simples triples
texto_multilinea2 = '''Otro ejemplo de
cadena de texto
multilínea.'''
print(texto_multilinea2)

texto_multilinea_concatenado = (
    "Este es otro ejemplo de "
    "cadena de texto que abarca "
    "varias líneas por concatenación implícita."
)
print(texto_multilinea_concatenado)


texto_multilinea_concatenado = (
    "Este es otro ejemplo de "
    "cadena de texto que abarca "
    "varias líneas por concatenación implícita."
)
print(texto_multilinea_concatenado)


lineas = [
    "Este es un ejemplo de",
    "una cadena de texto",
    "que abarca varias líneas usando join()."
]
texto_multilinea_join = "\n".join(lineas)
print(texto_multilinea_join)

# Uso de la función len() para obtener la longitud de una cadena
cadena = "Aprendiendo Python"
longitud = len(cadena)
print(f"La longitud de la cadena '{cadena}' es: {longitud}")

cadena = "Aprendiendo a Python"
n = 11
primeros_n_caracteres = cadena[:n]
print(f"Los primeros {n} caracteres son: '{primeros_n_caracteres}'")

cadena = "Aprendiendo a Python"
inicio = 3
fin = 10
caracteres_medio = cadena[inicio:fin]
print(f"Los caracteres del medio de la cadena '{cadena}' son: '{caracteres_medio}'")

cadena = "Programación"
n = 5
ultimos_n_caracteres = cadena[-n:]
print(f"Los últimos {n} caracteres son: '{ultimos_n_caracteres}'")


# Uso de la función upper() para convertir una cadena a mayúsculas
cadena = "Aprendiendo"
cadena_mayusculas = cadena.upper()
print(f"'{cadena}' en mayúsculas es: '{cadena_mayusculas}'")


# Uso de la función lower() para convertir una cadena a minúsculas
cadena = "TERMINANDO PARCIAL"
cadena_minusculas = cadena.lower()
print(f"'{cadena}' en minúsculas es: '{cadena_minusculas}'")


# Ejemplo  de strip()
cadena_con_espacios = "   Hola, Python!   "
cadena_sin_espacios = cadena_con_espacios.strip()
print(f"Cadena original: '{cadena_con_espacios}'")
print(f"Cadena sin espacios: '{cadena_sin_espacios}'")

# Eliminando caracteres específicos
cadena_con_guiones = "---Python---"
cadena_sin_guiones = cadena_con_guiones.strip('-')
print(f"Cadena sin guiones: '{cadena_sin_guiones}'")


# Ejemplo de replace()
texto = "Funcion, replace!"
texto_reemplazado = texto.replace("Funcion", "Aprediedno a usar ")
print(f"Texto original: '{texto}'")
print(f"Texto reemplazado: '{texto_reemplazado}'")

# Reemplazando caracteres específicos
texto_con_guiones = "Funcion-replace-Python"
texto_sin_guiones = texto_con_guiones.replace("-", " ")
print(f"Texto con guiones: '{texto_con_guiones}'")
print(f"Texto sin guiones: '{texto_sin_guiones}'")


# Ejemplo  de split()
frase = "Python es un lenguaje de programación"
palabras = frase.split()
print(f"Frase original: '{frase}'")
print(f"Palabras separadas: {palabras}")

# Usando un delimitador específico
datos = "nombre,apellido,edad"
elementos = datos.split(',')
print(f"Datos originales: '{datos}'")
print(f"Elementos separados: {elementos}")



# Ejemplo de F-String
nombre = "Python"
version = 3.10
mensaje = f"Estás aprendiendo {nombre} versión {version}."
print(mensaje)

# Usando expresiones dentro de F-Strings
a = 5
b = 10
resultado = f"La suma de {a} y {b} es {a + b}."
print(resultado)

# Formato con múltiples líneas
multilinea_fstring = f"""
Nombre del lenguaje: {nombre}
Versión actual: {version}
"""
print(multilinea_fstri



