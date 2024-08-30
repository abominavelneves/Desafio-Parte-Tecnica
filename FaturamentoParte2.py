import json
with open("dados.json","r") as f:
    data=json.load(f)
def ValoresNulos(array):
    novo_array=[]
    for i in array:
        if i!=0:
            novo_array.append(i)
    return novo_array
data=ValoresNulos(data["faturamento"])
def MediaFaturamento(array):
    soma=0
    for i in array:
        soma+=i
    return soma/(len(array))
