def soma(*nums):
    total =0
    for n in nums :
        total +=n
    return total

def provas(**kargs):
    status = 'aprovado' if kargs['nota'] >=6 else 'reprovado'   
    return f'{kargs["nome"]} foi {status} devido a sua nota ser {kargs["nota"]}'