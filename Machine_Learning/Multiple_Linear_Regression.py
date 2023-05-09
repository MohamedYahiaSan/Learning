import numpy as np
import matplotlib.pyplot as plt
import math

# Initializing Data
x_train=np.array([[2104,5,1,45],[1416,3,2,40],[852,2,1,35]])
y_train=np.array([460,232,178])
b=785.1811367994083
w=np.array([0.39133535,18.75376741,-53.36032453,-26.42131618])

# Prediction function in the form f(x)=wn*xn....+b for 1 example only
def predict(x,w,b):
    p=np.dot(x,w)+b
    return p

# Computing the cost with multiple variables
def compute_cost(x,y,w,b):
    m=x.shape[0]
    cost=0.0
    for i in range(m):
        f_wb_i=np.dot(x[i],w)+b
        cost+=(f_wb_i-y[i])**2
    cost=cost/(2*m)
    return cost

if __name__=="__main__":
    tmp_cost=compute_cost(x_train,y_train,w,b)
    print(tmp_cost)


# Function to compute the gradient dj_dw dj_db
def compute_gradient(x,y,w,b):
    m,n=x.shape
    dj_dw=np.zeros((n,))
    dj_db=0.
    
    for i in range(m):
        err=(np.dot(x[i],w)+b)-y[i]
        
        for j in range(n):
            dj_dw[j]+=err*x[i,j]
            
        dj_db+=err
    dj_db=dj_db/m
    dj_dw=dj_dw/m
    
    return dj_db,dj_dw


if __name__=="__main__":
    tmp_dj_db,tmp_dj_dw=compute_gradient(x_train,y_train,w,b)
    print(tmp_dj_db,tmp_dj_dw)
    
    
# Gradiend descent with multiple factors
def gradient_descent(x,y,w,b,alpha,cost_function,gradient_function,num_iters):
    J_history=[]
    
    
    for i in range(num_iters):
        dj_db,dj_dw=gradient_function(x,y,w,b)
        
        w=w-alpha*dj_dw
        b=b-alpha*dj_db
        
        
        if i<100000:
            J_history.append(cost_function(x,y,w,b))
            
            
        if i%math.ceil(num_iters/10)==0:
            print(f'Iteration {i:4d}: Cost {J_history[-1]:8.2f}')
            
    return w,b,J_history

if __name__=="__main__":
    w=np.zeros_like(w)
    b=0.
    
    iterations=1000
    alpha=8.0e-7
    w_final,b_final,hist=gradient_descent(x_train,y_train,w,b,alpha,compute_cost,compute_gradient,iterations)
    
    print(f'b,w found by the gradient descent: {b_final:0.2f}, {w_final}')
    
    # Comparing the results of the module with the data
    m=x_train.shape[0]
    for i in range(m):
        print(f'Prediction: {np.dot(x_train[i],w_final)+b_final:0.2f}, Target: {y_train[i]}')
    
    
    # Plotting
    fig,(ax1,ax2)=plt.subplots(1,2,constrained_layout=True,figsize=(12,4))
    ax1.plot(hist)
    ax2.plot(100+np.arange(len(hist[100:])),hist[100:])
    ax1.set_title("Cost Vs Iteration"); ax2.set_title("Cost Vs Iteration (Tail)")
    ax1.set_ylabel('Cost'); ax2.set_ylabel('Cost')
    ax1.set_xlabel('Iteration Step'); ax2.set_xlabel('Iteration Step')
    plt.show()
    
    
def zscore_normalize_features(X):
    mu =np.mean(X,axis=0)
    sigma= np.std(X,axis=0)
    x_norm=(X-mu)/sigma
    
    return (x_norm,sigma,mu)

