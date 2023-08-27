#url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"
url = "bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

print(url)

# Find returns character index
question_mark_index = url.find('?')

# Index from slice are exclusive.
domain_with_resource = url[:question_mark_index]
print(domain_with_resource)

parameters = url[(question_mark_index+1):]
print(parameters)

# String in Python is Immutable
print(url)

# Get the parameter value
value_to_be_found = "moedaDestino"
# value_to_be_found = "moedaOrigem"
# value_to_be_found = "quantidade"

# Returns index from initial position from text
value_to_be_found_index = url.find(value_to_be_found)

# Find method always returns index value for first occurrence.
# We use find with a second parameter to indicate the initial position it should be start
concatenation_parameter_index = url.find('&', value_to_be_found_index)

if concatenation_parameter_index == -1:
    value_found = url[value_to_be_found_index + len(value_to_be_found) + 1:]
else:
    value_found = url[value_to_be_found_index + len(value_to_be_found) + 1:concatenation_parameter_index]

print(f"Value found '{value_found}'")

