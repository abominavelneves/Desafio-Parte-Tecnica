import json 
with open("dados1.json","r") as f:
    data=json.load(f)
def DiasAcimaDaMedia(data):
    soma=0
    tamanho=len(data)
    dias_acima=0
    dias_nao_nulos=0
    for j in range(tamanho):
        if data[j]['valor']!=0.0:
            dias_nao_nulos+=1
            soma+=data[j]['valor']
    media=soma/dias_nao_nulos
    for i in range(tamanho):
        if data[i]['valor']>media:
            dias_acima+=1
    return dias_acima
print(DiasAcimaDaMedia(data))

    