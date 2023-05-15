import numpy as np 
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.preprocessing import StandardScaler
from Training_Data import X_features,X_train,y_train


#Applying Gradient Descent using Scikit-learn
scaler=StandardScaler()
X_norm=scaler.fit_transform(X_train)

# Printing the peak to peak difference after and before normalization using scikit
print(f'peak to peak Raw x:{np.ptp(X_train,axis=0)}')
print(f'peak to peak Normalized x:{np.ptp(X_norm,axis=0)}')


#Applying regression using scikit, and printing the output parameters w,b
sgdr=SGDRegressor(max_iter=1000)
sgdr.fit(X_norm,y_train)
print(sgdr)
print(f'number of iterations completed: {sgdr.n_iter_}, number of weight updates: {sgdr.t_}')
b_norm=sgdr.intercept_
w_norm=sgdr.coef_
print(f'model parameters: {b_norm,w_norm}')


#Making a prediction
y_pred=sgdr.predict(X_norm)
y_pred_para=np.dot(X_norm,w_norm)+b_norm
print(f'checking if both methods match: {(y_pred==y_pred_para).all()}')

#printig prediction and comparing to training data
print(f'Prediction till 8th train set: {y_pred[:8]}')
print(f'Actual result from data set till 8th: {y_train[:8]}')

#Ploting the prediction vs original features
fig,ax=plt.subplots(1,4,figsize=(12,4),sharey=True)
for i in range(len(ax)):
    ax[i].scatter(X_train[:,i],y_train,label='target')
    ax[i].set_xlabel(X_features[i])
    ax[i].scatter(X_train[:,i],y_pred,c='#e377c2',label='predict')
ax[0].set_ylabel("price")
ax[0].legend()
fig.suptitle("Target VS Prediction Using Z-score normalized model with scikit")
plt.show()