def verificar_numero_de_tarjeta(numero_tarjeta):
    numero_tarjeta_volteada = numero_tarjeta[::-1]
    suma_digitos_impares = 0
    digitos_impares = numero_tarjeta_volteada[::2]
    
    for digito in digitos_impares:
        suma_digitos_impares += int(digito)
    
    suma_digitos_pares = 0
    digitos_pares = numero_tarjeta_volteada[1::2]

    for digito in digitos_pares:
        numero = int(digito) * 2
        if numero >= 10:
            numero = (numero // 10) + (numero % 10)
        suma_digitos_pares += numero
    
    total = suma_digitos_impares + suma_digitos_pares

    return total % 10 == 0

def main():
    numero_tarjeta = input("Ingresa un número de tarjeta: ")
    translation_table = str.maketrans({"-": "", " ": ""})
    numero_tarjeta_modificada = numero_tarjeta.translate(translation_table)
    
    if verificar_numero_de_tarjeta(numero_tarjeta_modificada):
        print("TARJETA VÁLIDA")
    else:
        print("TARJETA INVÁLIDA")
    
main()