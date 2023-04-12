import numpy as np 
import matplotlib.pyplot as plt
from Practice_01 import *
import math


# Function to compute cost
def compute_cost(x,y,w,b):
    m=x.shape[0]
    f_wb=compute_model_ouput(x,w,b)
    total_cost=sum(f_wb-y)**2/(2*m)
    return total_cost

x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])
print(compute_cost(x_train,y_train,0,0))

# Testin Cases
x_train=np.array([1.0,1.7,2.0,2.5,3.0,3.2])
y_train=np.array([250,300,480,430,630,730])



#Gradient Descent Practice
def compute_gradient(x,y,w,b):
    f_wb=compute_model_ouput(x,w,b)
    dj_w=sum((f_wb-y)*x)/m
    dj_b=sum(f_wb-y)/m
    
    return dj_w,dj_b


# Function to execute Gradient Descent on number of iterations
def gradient_descent (x,y,w,b,alpha,num_iter,cost_function,gradient_function):
    J_history=[]
    P_history=[]
    
    for i in range(num_iter):
        dj_w,dj_b=gradient_function(x,y,w,b)
        
        b-=alpha*dj_b
        w-=alpha*dj_w
        
        if i<100000:
            J_history.append(cost_function(x,y,w,b))
    
        if i% math.ceil(num_iter/10)==0:
            print(f'Iteration {i:4} : Cost {J_history[-1]:0.2e}',
                f'dj_w {dj_w: 0.3e}, dj_b {dj_b: 0.3e}',
                f'w: {w: 0.3e}, b:{b: 0.3e}')
    return w,b,J_history,P_history

# Application
if __name__=="__main__":
    w=0
    b=0
    iterations=10000
    alpha=1.0e-2
    print()
    w_final,b_final,J_hist,P_hist=gradient_descent(x_train,y_train,w,b,alpha,iterations,compute_cost,compute_gradient)
    print(f'(w,b) found by gradient descent: ({w_final:8.4f},{b_final:8.4f})') 
    
    fig, (ax1,ax2)= plt.subplots(1,2,constrained_layout=True,figsize=(12,4))
    ax1.plot(J_hist[:100])
    ax2.plot(1000+np.arange(len(J_hist[1000:])),J_hist[1000:])
    ax1.set_title("Cost Vs Iteration - Start"); ax2.set_title("Cost Vs Iteration - End")
    ax1.set_ylabel("Cost") ; ax2.set_ylabel("Cost")
    ax1.set_xlabel("Iteration Step"); ax2.set_xlabel('Iteration Step')
    plt.show()
    
    print(compute_model_ouput(np.array([1200]),w_final,b_final))