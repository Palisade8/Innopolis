print("Добрый день")
print("Лабораторная работа 4")

import seaborn as sns

data = sns.load_dataset('iris')
print (data)

sns.pairplot(data=data)