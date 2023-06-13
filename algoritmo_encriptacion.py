# Diccionario encriptado. Puede implementarse un diccionario más completo(invertido y con minúsculas)
encriptador = {"A":"N", "B":"Ñ", "C":"O", "D":"P", "E":"Q", "F":"R", "G":"S", "H":"T", "I":"U", 
               "J":"V", "K":"W", "L":"X", "M":"Y", "N":"Z", "Ñ":"A", "O":"B", "P":"C", "Q":"D", 
               "R":"E", "S":"F", "T":"G", "U":"H", "V":"I", "W":"J", "X":"K", "Y":"L", "Z":"M"}

# Pruebas
prueba1_e = "H4L1 A_d_1_0_s"
prueba1_d = "T4X1 N_p_1_0_f" 
prueba2_e = "Tbxn obyb gq in"
prueba2_d = "Hola como te va"
prueba4 = "Tbxn     Hola_TBXN"
prueba5_e = "Esta cadena esta encriptada!!!" 
prueba5_d = "Qfgn onpqzn qfgn qzoeucgnpn!!!"

def encriptar(cadena, encriptador): # Función que encripta la cadena recibida
    cadena = list(cadena) # Tranforma la cadena a una lista
    lista_encriptada = [] # Lista vacía que guarda la encriptación
    i = 0
    while i <= len(cadena) - 1: # Itera mientras no supere el largo - 1 de la lista-cadena recibida
        if cadena[i].islower(): # Consulta si el caracter recibido esta en minúscula
            cadena[i] = cadena[i].upper() # El carácter es elevado a mayúscula
            encriptado = encriptador.get(cadena[i]) # Devuelve el valor por la Key
            encriptado = encriptado.lower() # El carácter es devuelto a minúscula
            lista_encriptada.append(encriptado) # Agrega el carácter a la lista encriptada
        else:
            encriptado = encriptador.get(cadena[i]) # Si la Key no existe devuelve None
            if encriptado == None: 
                lista_encriptada.append(cadena[i]) # Se agrega el carácter no encotrado en el diccionario a la lista
            else:
                lista_encriptada.append(encriptado)
        i += 1 
    
    mensaje_encriptado = ''.join(map(str,lista_encriptada)) # Transforma la lista encriptada en una cadena encriptada
    return mensaje_encriptado # Retorna la cadena encriptada
        

def desencriptar(cadena, encriptador): # Funcion que desencripta la cadena recibida
    cadena = list(cadena)
    lista_desencriptada= [] # Lista vacía que guarda la desencriptación
    i = 0
    while i <= len(cadena) - 1:
        if cadena[i].islower():
            cadena[i] = cadena[i].upper()
            encriptado = list(encriptador.keys())[list(encriptador.values()).index(cadena[i])] # Devuelve la Key a partir del índice del valor buscado, key[value.index(carácter)]
            encriptado = encriptado.lower()
            lista_desencriptada.append(encriptado)
        else:
            try: # Manejo de excepción, si no existe el caracter buscado
                encriptado = list(encriptador.keys())[list(encriptador.values()).index(cadena[i])] # Devuelve la Key apartir del índice del valor buscado
            except: # Ocurre la excepción
                lista_desencriptada.append(cadena[i]) # Agrega el carácter no encontrado en la lista desencriptada
            else: # Si no ocurre ninguna excepción se agrega la key del cáracter desencriptado buscado
                lista_desencriptada.append(encriptado)
        i += 1
    
    mensaje_desencriptado = ''.join(map(str,lista_desencriptada)) # Transforma la lista en una cadena
    return mensaje_desencriptado # Retorna la cadena desencriptada

print("### ------- Encriptador ------- ###")

cadena_encriptar = input("Ingrese la cadena a encriptar: ")
print("Tu cadena encriptada es:", encriptar(cadena_encriptar, encriptador))

cadena_desencriptar = input("Ingrese la cadena a desencriptar: ")
print("Tu Cadena desencriptada es:", desencriptar(cadena_desencriptar, encriptador))


### Tests
# test_encriptar= encriptar(prueba1_e,encriptador)
# print("Cadena Encriptada:",test_encriptar)

# test_desencriptar = desencriptar(prueba1_d, encriptador)
# print("Cadena Desencriptada:", test_desencriptar)