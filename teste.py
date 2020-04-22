from calculadora import Calculadora, Pessoa

def imprimir():
    print("Valor A: {}".format(calculo.get_a()))
    print("Valor B: {}".format(calculo.get_b()))
    print(" * = {}".format(calculo.multiplicar()))
    print(" / = {}".format(calculo.dividir()))
    print(" + = {}".format(calculo.somar()))
    print(" - = {}".format(calculo.subtrair()))
    print("************************")

#Instanciar a minha classe:
calculo = Calculadora(1,2)

#Imprimir dados
imprimir()

#Alteracao dos dados
calculo.set_a(4)
calculo.set_b(5)

#Imprimir os dados novamente
imprimir()

pessoa = Pessoa("andre", "22 2222-3333")
