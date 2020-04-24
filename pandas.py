import pandas as pd
import numpy as np

#carrega os dados do excel para um array, squeeze igual a true não adiciona para um dataframe, shee_name carrega a planilha informada

s = pd.read_excel(r'F:\pandas\idades2.xlsx',squeeze = True) #por padrão carrega a primeira planilha

s2 = pd.read_excel(r'F:\pandas\idades2.xlsx', squeeze = True, sheet_name="Planilha2") #carrega a planilha 2 do excel


print(s.dtype) #retorna o tipo da serie
print(s.index) #retorna os indices dessa serie
print(s.name) # retorna os nome da série e não os valores
print(s.nbytes) #informa total de espaço consumido na memoria
print(s.ndim) #quantidade de dimenções
print(s.shape) #informa a quantidade de dimesões, por linha, colunas e paginas
print(s.size) #informa a quantidade de registros em cada linha coluna paginas
print(s.values[s.values>70]) #informa os valores, com filtro

print(s.at["rotulo"]) #acesso os valores dos itens do rótulo informado
print(s["rotulo"]) #acesso os valores do rotulo informado, similar a s.at['']
print(s.iat[0]) # acesso o item apartir do index do item entre 0 e n-1 
print(s.get[0]) # acessa o valor a partir do index informado, é possivel recebe e modicar també o item
s.loc[["rotulo1","rotulo2"]] #acessa os valores apartir da lista de rotulos
s.iloc[[0,1,2]]#acessa os valores apartir da lista de rotulos


s.add(a) #realiza adição dos velores s com a
s.add(3) #realiza adição do vetor pelo escalar 3
s.sub(a) #realiza subtração de s com a
s.sub(3) #realiza subratação do vetor pelo escalar 3
s.mul(a) #realiza multiplicação de s com a
s.mul(3) #realiza multiplicação do vetor pelo escalar 3
s.div(a) #realiza divisão de s com a
s.div(3) #realiza divisão do vetor pelo escalar 3
s.floordiv(a) #realiza divisão de s com a, apenas a parte inteira
s.floordiv(3) #realiza divisão do vetor pelo escalar 3 apenas a parte inteira
s.mod(a) #realiza resto da divisão de s com a, apenas a parte inteira
s.mod(3) #realiza resto da divisão divisão do vetor pelo escalar 3 apenas a parte inteira
s.pow(a) #realiza elver a potencia de de s com a
s.pow(3) #r#realiza elver a potencia de de s com a vetor pelo escalar 3 apenas a parte inteira
s.round(2) #realiza o arredondamento com duas casas decimais

#metodos de comparação
s.lt(a) # < realiza comparação retorno bolean menor que s menor que a
s.gt(a) # > realiza comparação maior que s maior que a
s.ge(a) # >= maior ou igual
s.le(a) # <=
s.ne(a) # != não é igual
s.eq(a) # = operador de igualdade
#metotos de somatorios, absoluto 

s.sum() #soma todos os valores
s.product() # multiplicação
s.abs() # retorna o modulo, absolutos (não retona negativo)

# metodos estatisticos

s.describe() #sumario estatistico
s.mean()# media
s.meadian() #mediana
s.std() #desvio padrao 
s.min # menor valor
s.max # maio valor
s.quantile (.25) # 0.25, 0.5, 0.75 .... retorna o quantil 
s.nlargest(10) #retona os 10 maiores valores da serie
s.nsmallest(10) #retorna os 10 menores valores da serie

s.unique() #lista os valores unicos
s.nunique() #retorna a quantidade de valores unicos
s.count() #quantidade de valores não nulos (none)

 
#manipulação e seleçao

import pickle 
copia = pickle.loads(pickle.dumps(serie_name)) #cria uma copia dos valores e não da referencia, necessário importar pickle.
sb = s.append(b) #adiciona na serie s os valores de b
sb = s.append(b,ignore_index) #adiciona na serie s os valores de b, e os index dos novos dados segiram a mesma sequencia de s
s = s.replace(0,1) #subistitui o valor de 0 pelo valor 1
s.update(a) #realiza o update dos valores de S apartir dos valores A, onde os index são iguais 

s.head(10) #retorna as 10 primeira linhas, por default é 5
s.tail(10) #retorna as 10 ultimas linhas, por default é 5
s.sample(10) # retorna 10 amostras, por padrão é 1 

s.mask(c>3,10)# troca os valores se a condição for VERDADEIRA. Se algum valor for menor que 3 será substituido por 10
s.where(c>3,10) # troca os valores se a condição for FALSA. Se algum valor for menor que 3 será substituido por 10

#trabalhando com dados NA

s.isna() #retorna uma lista booleana informando os valores ausente (true)
s.notna() #retorna uma lista booleana informando os valores que não sao nulas (true)
s.dropna() #retorna uma serie com os valores não nulos
s.dropna(inplace=True) #retorna uma serie com os valores não nulos, incplate = true modifica a serie e remove os valores na
s.fillna(0) #substitui os valores NA por algum valor especificado, nesse caso zero
s.fillna(method="bfill") #retorna os valores NA pelo valor anterior/befor
s.fillna(method="ffill") #retorna os valores NA por algum posterior after 
s.fillna(0,inplace=True) #substistituis os valores NA pelo especificados

s.sort_values() #ordenada a serie pelo valor
s.sort_index() #retorna a serie ordenada pelo indice


#trabalhando com string

s.str.capitalize() #retorna a string com a primeira letra maiuscula
s.str.lower() #retorna a string torda minuscula
s.str.upper()#retona a string toda minuscula
s.str.title() #retorna a serie com as primeira letras de cada palavra em maiusculo

%matplotlib inline
s.plot.hist() #cria grafico de histograma,precisa chamar antes o comando %matplotlib inline
s.plot.hist(bins=101) #cria 101 barras, 

s.plot.line() #cria grafico de linhas,precisa chamar antes o comando %matplotlib inline
s.plot.area()#cria grafico de area,precisa chamar antes o comando %matplotlib inline
s.plot.box()#cria grafico de box,precisa chamar antes o comando %matplotlib inline
s.plot.bar()#cria grafico de bar,precisa chamar antes o comando %matplotlib inline


slinhas = [1,2,3,4,5,6,7,8,9,10] #serie com as linhas (index) que serão cadastradas no dataframe
scolunas = ["A","B","C","D","E"] #serie com os labels das colunas que serão cadastradas no dataframe
dados = np.random.randint(0,100,(10,5)) #será criado uma serie com registros de 0 a 100, no formato 10 linhas e 5 colunas
print(dados) 

df = pd.DataFrame(dados, linhas, colunas) #criando um dataframe



# trabalhando com data frame


import pandas as pd
import numpy as np

linhas = [1,2,3,4,5,6,7,8,9,10] #serie com as linhas (index) que serão cadastradas no dataframe
colunas = ["A","B","C","D","E"] #serie com os labels das colunas que serão cadastradas no dataframe
dados = np.random.randint(0,100,(10,5)) #será criado uma serie com registros de 0 a 100, no formato 10 linhas e 5 colunas
print(dados) 
df = pd.DataFrame(dados, linhas, colunas) #criando um dataframe
type(df) #vê o tipo da variavel df
df.info() #informações do dataframe
print(round(df.describe(),2))

#%matplotlib inline
#df.plot.box() #grafico boxplot
#df.plot.bar() #grafico de barras
df["A"] #seleciona uma coluna apartir do seu label
df[["A","B","C"]] #seleciona as colunas que serão retornadas
df.A #retonar a coluna A (outra maneira)
df["Total"] = df.A + df.B +df.C + df.D + df.E#cria uma nova coluna com o somatorio de A+B
df.sum()#somatorio de todas as colunas com total
df.mean() # media de cada coluna

total_acumulado = pd.DataFrame(np.array(df.sum()).reshape(1,6),index=["total"], columns=df.columns) #cria uma coluna com o somatorio


df2 = df.append(total_acumulado) #adiciona a coluna de dotal acumulado
print(df2)

df3 = df2.append(df.mean(),ignore_index=True) #adiciona uma linha com a media no final do dataset
print(df3)

df4 = df.drop("Total", axis = 1) # remove os registro - axis 1 = coluna / axis = 0 linha (padrão) não altera a original
df.drop("Total", axis=1, inplace = True) #remove a coluna Total da base original
df.drop(10,axis=0,inplace=True) #remove a linha 10 (por padrão exclui a llinha 10)
df.drop([7,8],inplace = True) #remove as linhas 7 e 8 

print(df) 

df.loc[[1,2]] #retona as linhas 1 e 2
df.loc[[1,2],["A","B"]] #retorna as linhas 1 e 2/ colunas A e B
df.iloc[[0,1,2],[0,2]] #retona as linhas e colunas a partir dos indices da lista, difererent do rotulo
df.iloc[9:6:-1,1:3] #retorna as linhas e colunas informadas na seleção

dados = df


pd.pivot() #altera o shape da tabela
pd.melt() # agruapmento criação de ranges
pd.reset_index() #reduz categorias e colunas
pd.sum(axis = 1) #soma horizontalmente, 0 é na vetifical
pd.median(axis = 1) #mediana horizontalmente, 0 é na vetifical
pd.mode()
pd.groupy('acesso')['canal de vendas'].sum() #veja como usar a função agg
pd.cut(dataframe['vendas'], bins=(0,100,200), labels=('1','2','3')) #realiza um agrupamento das valores no range especificado, binarizar
pd = ['x100' if x > 100 else 'x200' for x in dataframe['acesso']]#realiza um agrupamento das valores no range especificado, binarizar com compreensão de lista comprehension

pd.merge(pd2,on='nome_col',how='left') #junta duas colunas onde a coluna nome_col tenha valores iguais
df.to_csv('nome_arquivo.csv',sep=',',decimal='.', index=false)#retona o dataframe, index = false não retorna a coluna index
df.read_csv('nome_arquivo.csv',sep=',',decimal='.', index=false)

df.raname(columns={'x':'y','h':'g'} ) 
