import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import RandomizedSearchCV 

df=pd.read_csv('cardata.csv')

print(df.head())

required_dataset = df[['Year', 'Selling_Price', 'Present_Price', 'Kms_Driven',
                       'Fuel_Type', 'Transmission']]

required_dataset['Current_Year']=2023

required_dataset['Years_Old'] = required_dataset['Current_Year'] - required_dataset['Year']

print(required_dataset.head())

required_dataset.drop(['Year'], axis=1, inplace=True)

required_dataset=pd.get_dummies(required_dataset,drop_first=True)

print(required_dataset.head())

print(required_dataset.corr())

plt.figure(figsize=(20, 20))
sns.heatmap(required_dataset.corr(), annot=True, cmap="RdYlGn")
plt.show()

#separating independent and dependent features 
X=required_dataset.iloc[:,1:]
Y=required_dataset.iloc[:,0]

print(X.head())

print(Y.head())

from sklearn.ensemble import ExtraTreesRegressor

model = ExtraTreesRegressor()
model.fit(X, Y)

print(model.feature_importances_)

import pandas as pd
import matplotlib.pyplot as plt

feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.plot(kind='barh')
plt.show()

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=0)


from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()

from sklearn.model_selection import RandomizedSearchCV

n_estimators = [int(x) for x in np.linspace(start=100, stop=1500, num=15)]
max_features = ['sqrt', None]
max_depth = [int(x) for x in np.linspace(5, 40, num=8)]
min_samples_split = [2, 5, 10, 15, 50]
min_samples_leaf = [1, 2, 5, 10] 

parameters = {'n_estimators': n_estimators,
               'max_features': max_features,
               'max_depth': max_depth,
               'min_samples_split': min_samples_split,
               'min_samples_leaf': min_samples_leaf}

print(parameters)

rf_random = RandomizedSearchCV(
    estimator=RandomForestRegressor(),
    param_distributions=parameters,
    scoring='neg_mean_squared_error',
    n_iter=10,
    cv=5,
    verbose=2,
    random_state=10,
    n_jobs=1
)
rf_random.fit(X_train, Y_train) 

print(rf_random.best_params_)

print(rf_random.best_score_)

predictions = rf_random.predict(X_test)

sns.distplot(Y_test - predictions)
plt.show() 

plt.scatter(Y_test, predictions)
plt.xlabel("Actual Values (Y_test)")
plt.ylabel("Predicted Values")
plt.title("Scatter Plot of Actual vs Predicted Values")
plt.show()

