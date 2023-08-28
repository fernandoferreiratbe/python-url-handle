import re  # Regular Expression - RegEx

""" 
    CEP - 5 digits + hifen (opcional) + 3 digits 
"""

address = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120."

# pattern = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
pattern = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")


search = pattern.search(address)  # Match

if search:
    cep = search.group()
    print(f"CEP found [{cep}]")
