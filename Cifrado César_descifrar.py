texto = input("Ingrese el texto a descifrar: ")
desplazamiento = int(input("Ingrese el número del desplazamiento: "))
abecedario = "abcdefghijklmnñopqrstuvwxyz"
texto_cifrado = ""

for caracter in texto:
    if caracter == " ":
        texto_cifrado += " "
    else:
        posicion = abecedario.find(caracter)
        posicion_nueva = posicion - desplazamiento
        texto_cifrado += abecedario[posicion_nueva]

print(f"Texto cifrado: {texto_cifrado}")