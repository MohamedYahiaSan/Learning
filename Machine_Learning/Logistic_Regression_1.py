import numpy as np 
import matplotlib.pyplot as plt
import copy, math
from sklearn.linear_model import LogisticRegression

# sigmoid function calculations
def sigmoid(z):
    g=1/(1+np.exp(-z))
    return g

# testing
z_tmp=np.arange(-100,101,10)

y=sigmoid(z_tmp)

np.set_printoptions(precision=3)
#print(np.c_[z_tmp,y])

# plotting 
#fig,ax=plt.subplots(1,1,figsize=(5,3))
#ax.plot(z_tmp,y,c="b")
#ax.set_title("Sigmoid Function")
#ax.set_ylabel("sigmoid(z)")
#ax.set_xlabel("z")
#plt.show()


# Training data
x_train=np.array([0,1,2,3,4,5])
y_train=np.array([0,0,0,1,1,1])

w_in=np.arange(-3,3)
b_in=1


# applying that
z=x_train*w_in+b_in

y=sigmoid(z)
#print(z,y)


# plotting 
#fig,ax=plt.subplots(1,1,figsize=(5,5))
#ax.plot(z,y,c="b")
#ax.set_title("Sigmoid Function")
#ax.set_ylabel("sigmoid(z)")
#ax.set_xlabel("z")
#plt.show()

X=np.array([[0.5,1.5],[1,1],[1.5,0.5],[3,0.5],[2,2],[1,2.5]])
y=np.array([0,0,0,1,1,1]).reshape(-1,1)
print(np.c_[X,y])



X_train = np.array([[0.5, 1.5], [1,1], [1.5, 0.5], [3, 0.5], [2, 2], [1, 2.5]])  #(m,n)
y_train = np.array([0, 0, 0, 1, 1, 1])
                                           #(m,)
# Loss function and Cost calculation for Logistic Regression
def compute_cost_logistic(X,y,w,b):
    m=X.shape[0]
    cost=0.0

    for i in range(m):
        z_i=np.dot(X[i],w)+b
        f_wb_i=sigmoid(z_i)
        cost+= -y[i]* np.log(f_wb_i) - (1-y[i]) * np.log(1-f_wb_i)

    cost=cost/m

    return cost

#small test
w_tmp=np.array([1,1])
b_tmp=-3
print('cost is:', compute_cost_logistic(X_train,y_train,w_tmp,b_tmp))


# Computing Gradient descent for Logistic regression
def compute_gradient_logistic(X,y,w,b):
    m,n=X.shape
    dj_dw=np.zeros((n,))
    dj_db=0

    for i in range(m):
        f_wb_i=sigmoid(np.dot(X[i],w)+b)
        err_i=f_wb_i-y[i]
        for j in range(n):
            dj_dw[j]=dj_dw[j]+err_i*X[i,j]
        
        dj_db = dj_db + err_i

    dj_db=dj_db/m
    dj_dw=dj_dw/m

    return dj_db, dj_dw

# Testing the gradient with the training data
w_tmp = np.array([2.,3.])
b_tmp = 1.
dj_db_tmp, dj_dw_tmp = compute_gradient_logistic(X_train, y_train, w_tmp, b_tmp)
print(f"dj_db: {dj_db_tmp}" )
print(f"dj_dw: {dj_dw_tmp.tolist()}" )


# Gradient descent for Logistic regression 
def gradient_descent (X,y, w_in, b_in, alpha,num_iters):

    J_history=[]
    w=copy.deepcopy(w_in)
    b=b_in


    for i in range(num_iters):
        dj_db,dj_dw=compute_gradient_logistic(X,y,w,b)

        w-=alpha*dj_dw
        b-=alpha*dj_db

        if i<100000:
            J_history.append(compute_cost_logistic(X,y,w,b))

        if i% math.ceil(num_iters/10)==0:
            print(f'Iteration {i:4d}: Cost {J_history[-1]}')

    
    return w,b,J_history

#Resetting the paremeters and running gradient descent
w_tmp=np.zeros_like(X_train[0])
alpha=0.1
iters=10000

w_out,b_out,empty=gradient_descent(X_train,y_train,w_tmp,b_tmp,alpha,iters)
print(f'\nupdated paras: w:{w_out} b:{b_out}')

# Implementation using Schikit-learn
lr_model=LogisticRegression()
lr_model.fit(X_train,y_train)
y_pred= lr_model.predict(X_train)
print("prediction on training set:", y_pred,"\n actuall data:",y_train)
print('Accuracy:,',lr_model.score(X_train,y_train))