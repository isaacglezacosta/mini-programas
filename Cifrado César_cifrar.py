texto = input("Ingrese el texto a cifrar: ")
desplazamiento = int(input("Ingrese el número del desplazamiento: "))

def cifrar_cesar(texto, desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto_cifrado = ""

    for caracter in texto.lower():
        if caracter == " ":
            texto_cifrado += " "
        else:
            posicion = abecedario.find(caracter)
            posicion_nueva = (posicion + desplazamiento) % len(abecedario)
            texto_cifrado += abecedario[posicion_nueva]

    print(f"Texto original: {texto}")
    print(f"Texto cifrado: {texto_cifrado}")

cifrar_cesar(texto, desplazamiento)