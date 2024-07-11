#Arguments default and non-default 

#Parametro --> Argumento 
# Default = aquele que você define o valor do parametro
# Non - default = aquele que você não define o valor no parametro

def boas_vindas(quantidade, nome = "Linda"): #default sempre deve vir depois do non-default
    print(f'Olá {nome}.')
    print(f'Temos {str(quantidade)} laptops em estoque. ')

boas_vindas(6) #Non-default 
