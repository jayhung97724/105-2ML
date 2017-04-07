import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data', header = None)
y = df.iloc[0:100, 4].values
y = np.where(y == 'Iris-setosa', -1, 1)
x = df.iloc[0:100, [0, 2]].values
print(type(x))
# knn = KNeighborsClassifier(n_neighbors = 5, p = 2, metric = 'minkowski')
# knn.fit(x_train_std, y_train)
# plot_decision_regions(x_combined_std, y_combined, classifier = knn, test_idx=range(105,150))
print(x[:50, 0])
plt.scatter(x[:50, 0], x[:50, 1], color = 'red', marker = 'o', label = 'Setosa')
plt.scatter(x[50:100, 0], x[50:100, 1], color = 'blue', marker = 'X', label = 'Versicolor')
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.legend(loc = 'upper left')
plt.show()
# print(df)
# print(y)