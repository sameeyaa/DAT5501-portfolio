from ucimlrepo import fetch_ucirepo 
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import pandas as pd
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 

#set the target species we are looking at
le = LabelEncoder()
le.fit(y.iloc[:, 0])
y_encoded = le.transform(y.iloc[:, 0])

#train the decision tree
clf = DecisionTreeClassifier(max_depth= 3, random_state= 50)
clf.fit(X, y_encoded)

#plot decision tree
plt.figure(figsize = (14, 8))
plot_tree(clf,
         feature_names= X.columns,
          class_names= le.classes_,
           filled = True,
            rounded = True,
             fontsize = 12 )
plt.show()
