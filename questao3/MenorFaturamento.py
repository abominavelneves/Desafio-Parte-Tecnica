import json 
with open("dados1.json","r") as f:
    data=json.load(f)
def DiaMenorFaturamento(data):
    tamanho=len(data)
    menor_faturamento=data[0]['valor']
    dia_menor={}
    for i in range(tamanho):
        if data[i]['valor']<menor_faturamento:
            menor_faturamento=data[i]['valor'] 
            dia_menor=data[i]  
    return dia_menor
print(DiaMenorFaturamento(data))

