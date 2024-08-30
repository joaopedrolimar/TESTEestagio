def count_a_in_string(input_string):
    # Converte a string para minúscula e conta a ocorrência da letra 'a'
    count = input_string.lower().count('a')
    return count

# Solicita ao usuário a palavra ou frase de entrada
input_string = input("Digite uma palavra ou frase: ")

# Conta a letra 'a' e imprime o resultado
count = count_a_in_string(input_string)

if count > 0:
    print(f"A letra 'a' aparece {count} vezes na palavra ou frase digitada.")
else:
    print("A letra 'a' não aparece na palavra ou frase digitada.")
