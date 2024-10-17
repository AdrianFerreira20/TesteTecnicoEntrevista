def verifica_letra_a(texto):
    # Converte o texto para minúsculas e conta o número de vezes que a letra 'a' aparece
    contador = texto.lower().count('a')

    # Verifica se a letra 'a' está presente e retorna a mensagem correspondente
    if contador > 0:
        return f"A letra 'a' aparece {contador} vezes no texto."
    else:
        return "A letra 'a' não está presente no texto."


# Exemplo de uso
texto = input("Informe um texto: ")
resultado = verifica_letra_a(texto)
print(resultado)
