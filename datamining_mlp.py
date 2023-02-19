# -*- coding: utf-8 -*-
"""DataMining_MLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kw_gn9u5C4IA1GX9giaw-VmWbXDrsfQL

# **Multilayer Perceptron**

**Import** **Libraries**
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv('data.csv')

data.head()

data.drop([data.columns[32], data.columns[0]],axis=1,inplace=True)
data.rename(columns = {"diagnosis": "target"}, inplace = True)
data["target"] = [1 if i.strip() == 'M' else 0 for i in data["target"]]
data

##these are the 30 features/variables
for i in range(31):
  print(data.columns[i])
print("Number of features: 30")

##lets see the number of milgnant and benign tumor in the dataset
print(data["target"].value_counts())
print("Total:", len(data["target"]))
sns.countplot(x = data["target"])
##0 means benign and 1 means malignant
plt.show()

count1=0
count2=0
for i in data['target']:
  if(i==0): 
    count1=count1+1
  else: 
    count2=count2+1
print("Number of malign tumors:"+ " "+str(count1))
print("Number of benign tumors:"+ " "+str(count2))

corrMatrix = data.corr()

sns.clustermap(corrMatrix, annot = False)
plt.title("Correlation Between the Features")

plt.show()

# simplified correlation matrix

threshold = 0.7

filt = np.abs(corrMatrix["target"]) > threshold
corrFeatures = corrMatrix.columns[filt].tolist()

sns.clustermap(data[corrFeatures].corr(), annot = True, fmt = ".3f")
plt.title("Correlation Between the Features with Threshold 0.7")

plt.show()

###creating a pair plot with the above corelation matrix
sns.pairplot(data[corrFeatures], diag_kind = "kde", markers = '+', hue = "target")

plt.show()

# outlier detection
from sklearn.neighbors import KNeighborsClassifier, NeighborhoodComponentsAnalysis, LocalOutlierFactor
y = data["target"]
x = data.drop(["target"], axis = 1)

clf = LocalOutlierFactor(n_neighbors = 20)
clf.fit_predict(x)
xScore = clf.negative_outlier_factor_

outlierScore = pd.DataFrame()
outlierScore["score"] = xScore

threshold = -2.5
filt = outlierScore["score"] < threshold
outlierIndex = outlierScore[filt].index.tolist()

radius = (xScore.max() - xScore) / (xScore.max() - xScore.min())
outlierScore["radius"] = radius


plt.scatter(x.iloc[:, 0], x.iloc[:, 1], color = 'k', s = 3, label = "Data Points")
plt.scatter(x.iloc[:, 0], x.iloc[:, 1], s = 1000 * radius, edgecolors = 'r', facecolors = "none", label = "Oulier Scores")
plt.scatter(x.iloc[outlierIndex, 0], x.iloc[outlierIndex, 1], color = 'b', s = 50, label = "Outliers")
plt.legend()

plt.show()

# drop outliers

x = x.drop(outlierIndex)
y = y.drop(outlierIndex).values

# split dataset into train and test
from sklearn.model_selection import train_test_split
# creat the train and test split

X_Train, X_Test, Y_Train, Y_Test = train_test_split(x, y, test_size = 0.3, random_state = 42)

# Feature scaling
from sklearn.preprocessing import StandardScaler
# standardization
scaler = StandardScaler()
xTrain =  scaler.fit_transform(X_Train)
xTest = scaler.transform(X_Test)

#implementing PCA
from sklearn.decomposition import PCA
xScaled = scaler.fit_transform(x)
# dimension reduction with PCA

pca = PCA(n_components = 2)
xReducedPca = pca.fit_transform(xScaled)

pcaData = pd.DataFrame(xReducedPca, columns = ["p1", "p2"])
pcaData["target"] = y

sns.scatterplot(x = "p1", y = "p2", hue = "target", data = pcaData)
plt.title("PCA: p1 vs p2")

plt.show()

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score, f1_score, precision_score, roc_auc_score, recall_score, top_k_accuracy_score, ConfusionMatrixDisplay, plot_roc_curve

from sklearn.neural_network import MLPClassifier
classifier = MLPClassifier(max_iter=500, batch_size = 100, hidden_layer_sizes=(12,8), activation = 'logistic', alpha = 0.001)
classifier.fit(X_Train, Y_Train)

y_pred = classifier.predict(X_Test)
y_pred.shape

accuracy = accuracy_score(Y_Test, y_pred)
print("The obtained accuracy =", accuracy*100, "%")

classifier.get_params()

from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
confusionmat = confusion_matrix(Y_Test, y_pred)

print(confusionmat)

target_names = ['0','1']
print(classification_report(Y_Test, y_pred, target_names = target_names))

sns.heatmap(confusionmat/np.sum(confusionmat), fmt = '.2%', annot = True)
confuse=confusion_matrix(Y_Test, y_pred)

##plotting the confusion matrix
fig, ax = plt.subplots(figsize=(7.5, 7.5))
ax.matshow(confuse, cmap=plt.cm.Blues, alpha=0.3)
for i in range(confuse.shape[0]):
    for j in range(confuse.shape[1]):
        ax.text(x=j, y=i,s=confuse[i, j], va='center', ha='center', size='xx-large')
 
plt.xlabel('Predictions', fontsize=18)
plt.ylabel('Actuals', fontsize=18)
plt.title('Confusion Matrix', fontsize=18)
plt.show()

plot_roc_curve(classifier, X_Test, Y_Test) 
plt.show()

precision = confusionmat[0,0]/(confusionmat[0,0] + confusionmat[1,0])
recall = confusionmat[0,0]/(confusionmat[0,0] + confusionmat[0,1])
misrate = confusionmat[1,0] / (confusionmat[1,0] + confusionmat[0,0])

print("Precision = ", round(precision,2))
print("Recall = ", round(recall,2))
print("Miss Rate = ", round(misrate,2))

f1_score = (2*precision * recall) / (precision + recall)
print("F1 Score = ", round(f1_score,2))

accuracy = accuracy_score(Y_Test, y_pred)
print("The obtained accuracy =", accuracy*100, "%")

##miss rate is the ratio of FN/FN+TP
miss_rate=confuse[1][0] / (confuse[0][0] + confuse[1][0])
print("miss Rate is: "+ str(miss_rate))

