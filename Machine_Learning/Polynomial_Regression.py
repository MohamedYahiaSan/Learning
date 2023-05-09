import numpy as np
import matplotlib.pyplot as plt





#Creating cost calculation Function
def compute_cost(x,y,w,b):
    cost=0.
    m=x.shape[0]
    for i in range(m):
        cost+=((np.dot(w,x[i])+b)-y[i])**2
    cost=cost/(2*m)
    return cost

#Creating Gradient Calculation Function
def compute_gradient(x,y,w,b):
    m,n=x.shape
    dw=np.zeros((n,))
    db=np.float128(0)
    
    for i in range(m):
        err=((b+np.dot(w,x[i]))-y[i])
        for j in range(n):
            dw[j]+=err*x[i,j]
        db+=err
        
    dw=dw/m
    db=db/m
    return db,dw


def gradient_descent(x,y,w,b,alpha,gradient_function,num_iters):
    J_history=[]
    
    
    for i in range(num_iters):
        dj_db,dj_dw=gradient_function(x,y,w,b)
        
        w=w-alpha*dj_dw
        b=b-alpha*dj_db
        
        if i%(num_iters/20)==0: 
            cost=compute_cost(x,y,w,b)
            print(f'{w} , {b:6.3f} , {cost:6.3f}')
            #if cost<0.25 :return w,b
    return w,b

def zscore_normalize_features(X):
    mu =np.mean(X,axis=0)
    sigma= np.std(X,axis=0)
    x_norm=(X-mu)/sigma
    
    return x_norm

# running Liner regression on polynomial data
# Initializing data
"""if __name__=="__main__":
    x=np.arange(0,8,1)
    y=1+x**2
    X=x.reshape(-1,1)
    w=np.zeros_like(X[0])
    b=0
    model_w,model_b=gradient_descent(X,y,w,b,1e-4,compute_gradient,10000)
    plt.scatter(x,y, marker='x', c='r', label='Actual Value'); plt.title("no feature engineering")
    plt.plot(x,X@model_w +model_b, label="predicted Value"); plt.xlabel("X"); plt.ylabel("y"); plt.legend()
    plt.show()"""
    

#Feature Engineering and rerunning 
"""if __name__=="__main__":
    x=np.arange(0,20,1)
    y=1+x**2
    X=x**2
    X=X.reshape(-1,1)
    w=np.zeros(X.shape[1])
    b=0
    
    model_w,model_b=gradient_descent(X,y,w,b,1e-5,compute_gradient,10000)
    plt.scatter(x,y, marker='x', c='r', label='Actual Value'); plt.title("feature engineering")
    plt.plot(x,np.dot(X,model_w) +model_b, label="predicted Value"); plt.xlabel("X"); plt.ylabel("y"); plt.legend()
    plt.show()"""
    
    
# Adding more features X**3 and x, then analyzing the gradient descent on useless features
if __name__=="__main__":
    x=np.arange(0,20,1)
    y=x**2
    X=np.c_[x,x**2,x**3]
    X_Features=['X','X^2','X^3']
    w=np.zeros(X.shape[1])
    b=0
    X=zscore_normalize_features(X)
    model_w,model_b=gradient_descent(X,y,w,b,1e-1,compute_gradient,100000)

    fig,ax=plt.subplots(nrows=2, ncols=2, figsize=(8,8))
    counter=0
    for i in range(2):
        for j in range(2):
            
            if i==1 and j==1 :
                ax[i][j].scatter(x,y, marker='x', c='r', label='Actual Value')
                ax[i][j].set_title("feature engineering")
                ax[i][j].plot(x,np.dot(X,model_w) +model_b, label="predicted Value")
                ax[i][j].set_xlabel("X")
                ax[i][j].set_ylabel("y")
                ax[i][j].legend() 
                continue 
            ax[i][j].scatter(X[:,counter],y)
            ax[i][j].set_xlabel(X_Features[counter])
            ax[i][j].set_ylabel('Y')
            counter+=1
    fig.subplots_adjust(hspace=0.5, wspace=0.5)
    plt.show()
    

#Trying on a complex Function
if __name__=="__main__":
    x=np.arange(0,20,1)
    y=np.cos(x/2)
    X=np.c_[x,x**2,x**3,x**4,x**5,x**6,x**7,x**8,x**9,x**10,x**11,x**12,x**13]
    w=np.zeros(X.shape[1])
    b=0
    X=zscore_normalize_features(X)
    model_w,model_b=gradient_descent(X,y,w,b,1e-1,compute_gradient,1000000)
    plt.scatter(x,y, marker='x', c='r', label='Actual Value'); plt.title("feature engineering")
    plt.plot(x,np.dot(X,model_w) +model_b, label="predicted Value"); plt.xlabel("X"); plt.ylabel("y"); plt.legend()
    plt.show()