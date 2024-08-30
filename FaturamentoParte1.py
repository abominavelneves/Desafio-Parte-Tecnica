import json 
with open("dados.json","r") as f:
    data=json.load(f)
def MenorFaturamento(data):
    menor_faturamento=data["faturamento"][0]
    for i in data["faturamento"]:
        if i<menor_faturamento:
            menor_faturamento=i
    return menor_faturamento
print(MenorFaturamento(data))
def MaiorFaturamento(data):
    maior_faturamento=data["faturamento"][0]
    for i in data["faturamento"]:
        if i>maior_faturamento:
            maior_faturamento=i
    return maior_faturamento
print(MaiorFaturamento(data))
