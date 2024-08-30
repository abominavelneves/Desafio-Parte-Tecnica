### Resolução dos Desafios 
Aqui, neste projeto, o objetivo é resolver e mostrar um pouco do raciocínio por trás de algumas questões pedidas como teste de uma empresa para um cargo específico.
A empresa forneceu cinco questões como desafio na parte técnica, dentro das questões os temas abordados foram raciocínio lógico, o básico de estruturas de dados e manipulação de dados.
### Parte Técnica
Vou abordar questão por questão aqui e vou mostrar um pouco do raciocínio que eu realizei durante cada uma delas.
1. Na primeira questão foi fornecido o seguinte código e foi questionado o qual seria o valor da variável soma.
```python
indice = 13
soma =0
k=0 
while k<indice: 
    k=k+1
    soma=soma+k
print(soma)
```
Esse algoritmo simples altera o valor da Soma da seguinte forma [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91], logo o valor final da variável soma é 91.

2. Nessa questão foi pedido um código capaz de criar a sequência de fibonacci e, também, capaz de descobrir se um determinado númnero pertence a sequência.

3. Na Primeira Parte desse desafio dessa questão foi pedido para percorrer um vetor que possuia todos os valores da empresa e encontrar qual foi o menor e o maior valor. Para isso foi desenvolvida uma função para olhar cada item e retornar qual era o maior ou menor. Outro ponto interessante, o desafio exigiu que trablhasse com um arquivo xml ou json onde os dados estão armazenados.
```python
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
```
Na Segunda Parte foi pedido para calcular a media dos valores disponíveis desconsiderando valores nulos no vetor. Considerando que todos os valores são números reais, basta filtrar os valores diferentes de 0, para isso eu criei uma função que cria um novo array a partir do array dado removendo os valores nulos.
```python
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
```

4. 

5. A questão exigia um programa capaz de inverter uma String sem utlizar funções prontas como reverse. Minha primeira ideia foi percorrer a palavra pelo último índice até chegar ao primeiro.
```python
def inverteString(palavra):
    tamanho=len(palavra)
    palavra_invertida=""
    aux=0
    while aux<=tamanho-1:
        palavra_invertida+=palavra[tamanho-1]
        tamanho-=1
    return palavra_invertida
print(inverteString("Candy Lu"))
```
