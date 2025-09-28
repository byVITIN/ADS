from main import resposta_materia 
def lancar():
    while True:
        try:
            print("Digite suas notas para serem armazanadas:")
            notas = float(input())
            resposta_materia["notas"].append(notas)
        except ValueError:
            print('Digite um numero valido.')