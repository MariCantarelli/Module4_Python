#Arguments default and non-default 

#Parametro --> Argumento 
# Default = aquele que você define o valor do parametro
# Non - default = aquele que você não define o valor no parametro

def welcome(quantity, name = "Linda"): #default must always come after non-default
    print(f'Hello {name}.')
    print(f'We have {str(quantity)} laptops in stock. ')

welcome(6) #Non-default
