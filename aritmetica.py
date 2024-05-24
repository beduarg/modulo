##### ARITMETICA.PY #####

def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    return a / b

if __name__ == "__main__":
    import sys
    ops = dict(add=add, sub=sub, mul=mul, div=div)

    choice = input("seleziona un'operazione [add/sub/mul/div]: ")

    if choice not in ops:
        sys.exit('Operazione non valida!')
        
    op = ops[choice]
    try:
        a = float(input('Inserisci il primo valore: '))
        b = float(input('Inserisci il secondo valore: '))
    except ValueError as err:
        sys.exit('Valore non valido: {}'.format(err))

    print('Il risultato è:', op(a, b))