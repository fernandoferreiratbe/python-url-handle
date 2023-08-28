import re


# padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
# match = padrao_url.match(url)
#
# if not match:
#     raise ValueError("A URL não é válida.")
#
# print("A URL é válida")

"""
    Exemplos de URLs válidas:
        - bytebank.com/cambio
        - bytebank.com.br/cambio
        - www.bytebank.com/cambio
        - www.bytebank.com.br/cambio
        - http://www.bytebank.com/cambio
        - http://www.bytebank.com.br/cambio
        - https://www.bytebank.com/cambio
        - https://www.bytebank.com.br/cambio
    Exemplos de URLs inválidas:
        - https://bytebank/cambio
        - https://bytebank.naoexiste/cambio
        - ht://bytebank.naoexiste/cambio
"""
url = "https://www.bytebank.com.br/cambio"
url_pattern = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = url_pattern.match(url)
#
if not match:
    raise ValueError(f"URL {url} is invalid!")

print(f"URL {url} is valid")
