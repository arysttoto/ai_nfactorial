import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
from diseases_dictionary import dict_diseases

# df = pd.read_csv('Training.csv')
# print(list(df.columns))
# df = df.drop('Unnamed: 133', axis='columns')

# le_diagnosis = LabelEncoder()

# df['diagnosis'] = le_diagnosis.fit_transform(df['prognosis']) using label encoder
# df = df.drop(['prognosis'], axis='columns')

# y = pd.get_dummies(df['prognosis']) using dummies
#
# X = df.drop('prognosis', axis='columns')

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2) (100%)

# model = tree.DecisionTreeClassifier()
#
# model.fit(X, y)

# save the ai model for future use
# filename = 'decision_tree_model.joblib'
# joblib.dump(model, filename)

# prediction = model.predict(df2.drop(['prognosis'], axis='columns'))
# print('Prediction accuracy is: ', accuracy_score(pd.get_dummies(df2['prognosis']), prediction)) (97.61904761904762%)

# print(X_test.head())
# print(model.predict(X_test.head()))
# 185 413 2951 4875 3706

################# check the final model ###################
# df2 = pd.read_csv('Testing.csv')
# loaded_model = joblib.load('decision_tree_model.joblib')
#
# # Use the loaded model to make predictions on new data
# y_pred = loaded_model.predict(df2.drop(['prognosis'], axis='columns'))
#
# # Evaluate the accuracy of the model
# accuracy = accuracy_score(pd.get_dummies(df2['prognosis']), y_pred)
# print('Accuracy:', accuracy)
# nice! 98% accuracy as before
###########################################################
# all resources got from kaggle...
######################################################################
# make the heart risk model, not for use
# df = pd.read_csv('data.csv')
# X = df.drop('Score', axis='columns')
# y = df['Score']
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# model = tree.DecisionTreeClassifier()
# model.fit(X_train, y_train)
# prediction = model.predict(X_test)
# accura accuracy_score(y_test, prediction))
