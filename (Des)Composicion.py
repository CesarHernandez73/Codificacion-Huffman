# Cesar Hernandez Rodriguez

# Codificacion Huffman
# Para hacerlo necesitamos una palabra, frase o texto, sacar que simbolos son los que salen y su frecuencia, construir un arbol basado en las
# frecuencias de cada simbolo, le asignamos un codigo binario a cada simbolo del estilo ('a' : 1110) que ocupa menos que el propio simbolo y
# codificamos la palabra en base a esos codigos en binario
#
#

# Obtener distribucion
def get_frecuencias(cadena):
    prob = {}                                       # Diccionario
    for letra in cadena:
        prob[letra] = 0
    for letra in cadena:
        prob[letra] += 1                            #Nos pone en el diccionario las veces que se repite cada letra en la cadena
    return prob                                     #Nos devuleve un diccionario

#Convertimos el diccionario en conjunto de tuplas y ordenamos las tuplas por frecuencias de pequeña a grande
def ordenarFrec (dict) :
    letra = dict.keys()                             #Sacas las llaves del diccionario
    tuplas = []
    for let in letra:                               #Por cada letra creas una tupla del estilo ('letra', frec)
        tuplas.append((dict[let],let))
    tuplas.sort()                                   #Ordenas la lista de las tuplas por frecuencias
    return tuplas

#Metodo para ordenar una lista de tuplas por el primero elemento de cada tupla
def primero(elem):
    return(elem[0])

#Construimos a partir de los nodos con menos frecuencia juntandolos de 2 en 2 y añadiendo un nuevo nodo con la frecuencia sumada de amnbos
def const_arbol(lista) :
    while len(lista) > 1 :
        primeros = tuple(lista[0:2])                  # cogemos los 2 primeros
        resto  = lista[2:]                            # cogemos el resto de tuplas
        combFrec = primeros[0][0] + primeros[1][0]    # cogemos la frecuencia del nuevo nodo
        lista  = resto + [(combFrec,primeros)]        # añadimos el nuevo nodo creado a la lista
        lista.sort(key=primero)                       # volvemos a ordenar la lista por frecuencias
    return lista[0]

#Recortamos el arbol para quitar las frecuencias y obtener una lista con solo los conjuntos de nodos y como estan colocados en el arbol
def recortar_arbol(arbol):
    p = arbol[1]                                      #ignoramos las frecuencias arbol[0]
    if type(p) == type(""):                           #cuando p sea str devolvemos p
        return p
    else:
        return (recortar_arbol(p[0]), recortar_arbol(p[1]))

codes = {}                                            #Diccionario para crear los codigos para poder codificar
#Asigmanos a cada nodo del arbol el codigo que se le corresponde dependiendo de donde este situado en el arbol (izq '0', dcha '1')
def asignar_codes (nodo, camino='') :
    if type(nodo) == type("") :                       #Cuando sea str y no tupla le pones el camino a cada nodo
        codes[nodo] = camino
    else  :
        asignar_codes(nodo[0], camino+"0")            # Si el nodo hijo esta a la izquierda se le pone un 0
        asignar_codes(nodo[1], camino+"1")            # Si el nodo hijo esta a la izquierda se le pone un 1
    return codes



#Codificamos el texto original en base a la codificacion en binario obtenida por el metodo anterior
def codificar(dic,texto):
    res = ""
    for let in texto:
        codigo = dic[let]
        res = res + codigo
    return res                                        #Lo pasamos como str

#Aqui terminamos la primera parte del algoritmo, la codificacion de la palabra
#La segunda parte es decodificar el numero binario que tenemos para ello primero damos la vuelta al diccionario y decodificamos


#Invertir el diccionario para poder
def invertir(dict):
    new_dic = {}
    for i,j in dict.items():
        new_dic[j] = i
    return new_dic


#Decodificar

def decodificar (dict, texto):
    res = ""
    while len(texto)>1:
        for k in dict:
            if texto.startswith(k):                          #cogemos el inicio del texto que coincida con k
                res += dict[k]                        #decodificamos la parte del texto
                texto = texto[len(k):]                        #Volvemos a repetir el proceso anterior quitando la parte k del texto
    return res

#texto="j´aime aller sur le bord de l'eau les jeudis ou les jours impairs"
texto="aabbbcddeeeeee"
print("numero de bits del texto sin codificar",len(texto)*8)
freq = get_frecuencias(texto)
print("paso 1",freq)
ordenar =  ordenarFrec(freq)
print ("paso 2", ordenar)
arbol = const_arbol(ordenar)
print ("paso 3", arbol)
recorte = recortar_arbol(arbol)
print ("paso 4", recorte)
codigo = asignar_codes(recorte)
print ("paso 5", codigo)
huffman = codificar(codigo,texto)
print ("paso 6", huffman)
print("numero de bist del texto codificado por huffman",len(huffman))
r = invertir(codigo)
print ("paso 7", r)
new_texto = decodificar(r,huffman)
print ("paso 8", new_texto)




