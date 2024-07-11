#Multiple arguments xargs naming parameters

#Varios argumentos (xatgs identificando o parametro)

def agencia(**carro):
    return carro

print(agencia(marca = 'Gol', cor =  'Branca', motor = 1.0, placa = 1234))
print(agencia(marca = 'Gol', cor =  'Azul', motor = 1.0,))
print(agencia(marca = 'Gol', cor =  'Preto'))