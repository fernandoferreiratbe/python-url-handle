#url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

# Index from slice are exclusive.
domain_with_resource = url[0:19]
print(domain_with_resource)

parameters = url[20:36]
print(parameters)

# String in Python is Immutable
print(url)
