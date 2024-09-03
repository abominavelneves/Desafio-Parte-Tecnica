import json 
with open("dados1.json","r") as f:
    data=json.load(f)
def DiaMaiorFaturamento(data):
    tamanho=len(data)
    maior_faturamento=data[0]['valor']
    dia_maior={}
    for i in range(tamanho):
        if data[i]['valor']>maior_faturamento:
            maior_faturamento=data[i]['valor'] 
            dia_maior=data[i]  
    return dia_maior
print(DiaMaiorFaturamento(data))

