#import necessary libraries
from ucimlrepo import fetch_ucirepo 
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
  
# fetch dataset 
estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition = fetch_ucirepo(id=544) 
  
# data (as pandas dataframes) 
X = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.features 
y = estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.data.targets 
  
# metadata 
print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.metadata) 
  
# variable information 
print(estimation_of_obesity_levels_based_on_eating_habits_and_physical_condition.variables)

#set the target variables that are being analysed:
#target variables include normal_weight, obesity_type, insufficient_weight
le = LabelEncoder()
le.fit(y.iloc[:, 0])
y_encoded = le.transform(y)

#put all the category columns as an x variable
#gender,CALC

category_columns = X.select_dtypes(include = ["object"]).columns
numerical_columns = X.select_dtypes(exclude = ["object"]).columns
preprocess = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), category_columns),
        ("num", "passthrough", numerical_columns)
    ]
)


#training the decision tree
#add a pipeline to precheck data
clf = Pipeline(steps = [("preprocess", preprocess), ("model", DecisionTreeClassifier(max_depth = 5, random_state = 50
                                                                                     ))])
clf.fit(X, y_encoded)

#plot decision tree
plt.figure(figsize = (20, 12))
plot_tree(
    clf.named_steps["model"],
    feature_names=clf.named_steps["preprocess"].get_feature_names_out(),
    class_names=le.classes_,
    filled=True,
    rounded=True,
    fontsize=8
)
plt.title("Decision Tree for Predicting Obesity Levels")
plt.show()

 