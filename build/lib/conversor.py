def transformar_para_3_digitos(numero):
    numero_str = str(numero)
    
    if len(numero_str) != 4:
        return []

    numero_int = int(numero_str)

    numeros_3_digitos = []

    # Continuar até que o número seja reduzido a 0
    while numero_int > 0:
        if numero_int > 999:
            numeros_3_digitos.append(999)
            numero_int -= 999
        else:
            numeros_3_digitos.append(numero_int)
            numero_int = 0

    return numeros_3_digitos

# Imprime a mensagem de introdução
print("Aplicação desenvolvida por Carlos Eduardo (CADU)\n")

# Solicita o número ao usuário
numero_usuario = input("Digite um número de 4 dígitos: ")

# Converte a entrada para inteiro
numero_usuario = int(numero_usuario)

# Chama a função e armazena o resultado
resultados = transformar_para_3_digitos(numero_usuario)

# Imprime cada número de 3 dígitos em uma nova linha, numerando as linhas
for i, numero in enumerate(resultados, start=1):
    print(f"{i}: {numero}")

input("Aperte Enter para fechar o console...")