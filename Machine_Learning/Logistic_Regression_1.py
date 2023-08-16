import numpy as np 
import matplotlib.pyplot as plt

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
#fig,ax=plt.subplots(1,1,figsize=(5,3))
#ax.plot(z,y,c="b")
#ax.set_title("Sigmoid Function")
#ax.set_ylabel("sigmoid(z)")
#ax.set_xlabel("z")
#plt.show()

X=np.array([[0.5,1.5],[1,1],[1.5,0.5],[3,0.5],[2,2],[1,2.5]])
y=np.array([0,0,0,1,1,1]).reshape(-1,1)
print(np.c_[X,y])

