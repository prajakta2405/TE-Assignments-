#%%
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix,accuracy_score, f1_score, precision_score, recall_score

data=pd.read_csv(r"D:\TE-Assignments\DSBDA\Assignment-5\Social_Network_Ads (1).csv")
print(data.head())

x= data.iloc[:,:-1].values
y= data.iloc[:,-1].values
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=0.25,random_state=0)

sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.transform(x_test)

classifier=LogisticRegression(random_state=0)
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)

def plot_decision_boundary(X, y, classifier, resolution = 0.01):
    
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    
    
    xx, yy = np.meshgrid(np.arange(x_min, x_max, resolution), np.arange(y_min, y_max, resolution))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    
    
    plt.contourf(xx, yy, Z, alpha = 0.5, cmap = plt.cm.RdYlBu)
    plt.scatter(X[:, 0], X[:, 1], c = y, cmap = plt.cm.RdYlBu_r, edgecolors = 'black')


plt.figure(figsize = (8, 6))
plot_decision_boundary(x_test, y_test, classifier)
plt.title("Logistic Regression Decision Boundary")
plt.xlabel("Age")
plt.ylabel("Estimated Salary")
plt.show()

cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", cm)

plt.figure(figsize = (6, 6))
plt.imshow(cm, cmap = plt.cm.RdYlBu)
plt.colorbar()
plt.title("Confusion Matrix")
plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.xticks([0, 1], ["No", "Yes"])
plt.yticks([0, 1], ["No", "Yes"])
plt.show()
TN, FP, FN, TP = cm.ravel()

accuracy = accuracy_score(y_test, y_pred)
print("Accuracy: ", accuracy)

error_rate = 1 - accuracy
print("Error Rate: ", error_rate)


precision = precision_score(y_test, y_pred)
print("Precision: ", precision)


recall = recall_score(y_test, y_pred)
print("Recall: ", recall)

f1 = f1_score(y_test, y_pred)
print("F1 Score: ", f1)


#%%
