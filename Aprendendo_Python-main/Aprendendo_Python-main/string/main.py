from extrator_argumentos_url import ExtratorArgumentosUrl

url_byte_bank0 = ExtratorArgumentosUrl("https://www.bytebank.com.br/cambio?moedaorigem=oi&moedadestino=dolar&valor=700%E2%80%9D")
moeda_origem, moeda_destino = url_byte_bank0.obter_nome_moedas()

print("Moeda Origem: {}".format(moeda_origem.capitalize()))
print("Moeda Destino: {}".format(moeda_destino.capitalize()))

url_byte_bank1 = ExtratorArgumentosUrl("https://www.bytebank.com.br/cambio?moedaorigem=oi&moedadestino=dolar&valor=700%E2%80%9D")

url_byte_bank2 = ExtratorArgumentosUrl("https://www.bytebank.com.br/")

print("URL0 é igual ao URL1? {}".format(url_byte_bank0.__eq__(url_byte_bank1)))

print("URL1 é igual ao URL2? {}".format(url_byte_bank1.__eq__(url_byte_bank2)))