def inverteString(palavra):
    tamanho=len(palavra)
    palavra_invertida=""
    aux=0
    while aux<=tamanho-1:
        palavra_invertida+=palavra[tamanho-1]
        tamanho-=1
    return palavra_invertida
print(inverteString("Candy Lu"))