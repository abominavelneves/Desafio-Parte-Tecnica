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
def AcimaMediaFaturamento(array):
    soma=0
    for i in array:
        soma+=i
    media=soma/(len(array))
    print(media)
    quantidade=0
    for i in array:
        if i>media:
            quantidade+=1
    return quantidade

