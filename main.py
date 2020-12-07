# funcao que calcula o tamanho de uma string

def Calcula(s):
    string = s
    y = 1
    for x in string:
        y = y + 1
    return y - 1


s = input("Insira a string para calculo...: ")

retorno = Calcula(s)
print(retorno)
