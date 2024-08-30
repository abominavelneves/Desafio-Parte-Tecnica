distribuidora={"SP":67836.43,'RJ' : 36678.66,'MG' : 29229.88,'ES' : 27165.48, 'Outros' :  19849.53}
def Contribuicao(estado,distribuidora):
    soma=0
    for i in distribuidora.keys():
        soma+=distribuidora[i]
    if estado in distribuidora.keys():
        return (distribuidora[estado]/soma)*100
    else:
        return "Chave Inválida"
print(Contribuicao("BA",distribuidora))