import json 
with open("dados1.json","r") as f:
    data=json.load(f)
def MenorFaturamento(data):
    tamanho=len(data)
    menor_faturamento=data[0]['valor']
    for i in range(tamanho):
        if data[i]['valor']<menor_faturamento:
            menor_faturamento=data[i]['valor']
    return menor_faturamento
print(MenorFaturamento(data))

