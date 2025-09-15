import tabulate
#Mensagem
def boas_vindas():
    mensagem = """\
========================================
    BEM-VINDO AO PROGRAMA DE ENSINO
========================================

Este programa vai ajudar você a:

- Lançar notas de cada matéria
- Calcular a média por matéria
- Calcular a média geral
- Verificar se você está APROVADO ou REPROVADO em alguma materia
- Ver media final e se passou de ano nas materias

"""
    print(mensagem)
boas_vindas()
#menu de interacao
def menu():
    print("""
+------------------------------------------+
|              MENU ESCOLAR                |
+------------------------------------------+
| 1 - Lançar nota de uma determinada matéria |
| 2 - Calcular a média por matéria           |
| 3 - Calcular a média geral de todas        |
| 4 - Verificar aprovação em uma matéria     |
| 5 - Verificar se passou de ano             |
| 0 - Sair do programa                       |
+------------------------------------------+
""")

menu()

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
#loop do programa (Menu)
while True:
    print("Selecione qual ação deseja executar:")
    menu()
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
                resposta_materia = int(input('Digite qual materia ira adicionar a nota: '))
                if 1 <= resposta_materia <= len(materias_notas):
                    break
                else:
                    print(f'Digite um valor válido entre 1 e {len(materias_notas)}.')
            except ValueError:
                print(f'Digite um valor válido entre 1 e {len(materias_notas)}.')
        

        
            


       
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if resposta == 0:
        break   
print('Até logo') 