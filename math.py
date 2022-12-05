import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

#Ler dataset
data = pd.read_csv("diabetes.csv")
#Normalizar os dados
mean = np.mean(data,axis=0)
meanReducedData = data - mean

#Matriz de covariância
covMatrix = np.cov(MeanReducedData.T)
#Calcular autovalores e autovetores
eigVal,eigVec = np.linalg.eig(CovMatrix)
#Ordenando os autovalores
eigVal = np.array(np.sort(eigVal))[::-1]
print(eigVal)
#Mostrar as duas maiores colunas
sns.lineplot(x="Pregnancies",y="Glucose",data=data,hue="Outcome")
plt.show()