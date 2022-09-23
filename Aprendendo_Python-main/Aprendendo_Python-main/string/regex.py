import re

padrao = "[0-9]{4,5}-?[0-9]{4}"

texto0 = "meu numero de telefone é 3124-4689."

texto1 = "Ligue para o numero 99999-9999"

print("Numero de telefone é {} no texto: '{}'".format(re.search(padrao, texto0).group(), texto0))

print("Numero de telefone é {} no texto: '{}'".format(re.search(padrao, texto1).group(), texto1))