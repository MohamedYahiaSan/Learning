import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from Training_Data import X_features,X_train,y_train


#Applying Gradient Descent using Scikit-learn
sgdr=SGDRegressor(max_iter=1000)
sgdr.fit(X_train,y_train)
print(sgdr)


