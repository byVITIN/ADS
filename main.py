import tabulate
from dev_bem_vindo import boas_vindas
from dev_menu import menu
from dev_lancar import lancar

#Mensagem
boas_vindas()

materias_notas = [
    {"materia": "Português / Língua Portuguesa", "notas": []},
    {"materia": "Literatura","notas": []},
    {"materia": "Redação","notas": []},
    {"materia": "Língua Estrangeira (Inglês)","notas": []},
    {"materia": "Arte","notas": []},
    {"materia": "Educação Física","notas": []},
    {"materia": "Matemática","notas": []},
    {"materia": "Física","notas": []},
    {"materia": "Química","notas": []},
    {"materia": "Biologia","notas": []},
    {"materia": "História","notas": []},
    {"materia": "Geografia","notas": []},
    {"materia": "Filosofia","notas": []},
    {"materia": "Sociologia","notas": []}
]
#menu de interacao
print("Selecione qual ação deseja executar:")
menu()
#loop do programa (Menu)
while True:
    # loop para entrar na acao do programa
    while True:
        try:
            resposta = int(input())
            if resposta in [0, 1, 2, 3, 4, 5]:
                break
            else:
                print('Digite um valor valido entre 0 e 5: ')
        except ValueError:
            print('Digite um valor valido entre 0 e 5: ')

#IFS PARA DETERMINAR AS ACOES DE CADA VALOR        
    if resposta == 1:
        print('Selecione a materia que quer adicionar a nota.')
        for c, item in enumerate(materias_notas, start = 1):
            print(f"{c} - {item['materia']}")
        while True:
            try:
                resposta_materia = int(input('Digite qual materia ira adicionar a nota: ')) - 1
                if 0 <= resposta_materia < len(materias_notas):
                    resposta_materia = materias_notas[resposta_materia]
                    print('materia escolhida', resposta_materia["materia"])
                    break
                else:
                    print(f'Digite um valor válido entre 1 e {len(materias_notas)}.')
            except ValueError:
                print(f'Digite um valor válido entre 1 e {len(materias_notas)}.')
        lancar()
        
 
    if resposta == 0:
        break   
print('Até logo') 