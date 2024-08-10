import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()

print(iris.feature_names)

# select the first two columns
X = iris.data[:, :2]
df = pd.DataFrame(X, columns=iris.feature_names[:2])
model = KMeans(n_clusters=3)
model.fit(df)
df['cluster'] = model.predict(df)
sns.scatterplot(x='sepal length (cm)', y='sepal width (cm)', data=df, hue='cluster')
plt.savefig('scatterplot_iris_clustered.png')

#df_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
#df_temp = df_iris.copy()
#sns.pairplot(df_temp)
#plt.savefig('pairplot_iris.png')
#
#model = KMeans(n_clusters=3)
#model.fit(df_iris)
#df_iris['cluster'] = model.predict(df_iris)
#sns.pairplot(df_iris, hue='cluster')
#plt.savefig('pairplot_iris_clustered.png')

#df = pd.read_csv('./diamonds.csv')
#
#print(df.head())
#print(df.shape)
#print(df.columns)
#
#sns.pairplot(df)
#
## save the plot
##plt.savefig('pairplot.png')
#
#model = KMeans(n_clusters=3)
#cls_data = pd.get_dummies(df[['cut', 'color', 'clarity']])
#model.fit(cls_data)
#
#df['cluster'] = model.predict(cls_data)
#sns.pairplot(df, hue='cluster')
#plt.savefig('pairplot_clustered.png')
