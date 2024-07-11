#Multiple arguments xargs naming parameters

#Varios argumentos (xatgs identificando o parametro)

def agency(**car):
    return car

print(agency(brand = 'Gol', color = 'White', engine = 1.0, plate = 1234))
print(agency(brand = 'Gol', color = 'Blue', engine = 1.0,))
print(agency(brand = 'Gol', color = 'Black'))