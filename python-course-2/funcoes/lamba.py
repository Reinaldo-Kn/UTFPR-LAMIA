from functools import reduce

alunos =[
    {'nome': 'Ana', 'nota': 3},
    {'nome': 'Ba', 'nota': 2.1},
    {'nome': 'Ci', 'nota':6},
    {'nome': 'Do', 'nota': 9.1},

]

aprovado = lambda aluno: aluno['nota'] >=6

alunos_aprovados = filter(aprovado,alunos)

print (alunos_aprovados)