texto = input("Ingrese el texto a descifrar: ")
desplazamiento = int(input("Ingrese el número del desplazamiento: "))

def descifrar_cesar(texto, desplazamiento):
    abecedario = "abcdefghijklmnñopqrstuvwxyz"
    texto_descifrado = ""

    for caracter in texto.lower():
        if caracter == " ":
            texto_descifrado += " "
        else:
            posicion = abecedario.find(caracter)
            posicion_nueva = (posicion - desplazamiento) % len(abecedario)
            texto_descifrado += abecedario[posicion_nueva]

    print(f"Texto cifrado: {texto}")
    print(f"Texto descifrado: {texto_descifrado}")

descifrar_cesar(texto, desplazamiento)