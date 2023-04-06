import sys
import matplotlib.pyplot as plt
import numpy as np 

x_train=np.array([1.0,2.0])
y_train=np.array([300.0,500.0])
m=x_train.shape[0]

w=200
b=100

#plt.figure(num='Kishou-01')
#plt.scatter(x_train,y_train,marker='o',c='r',label='Actual Values')
#plt.title("Housing Prices")
#plt.ylabel('Price in 1000s of USD')
#plt.xlabel('size in 1000 sqt')
#plt.show()

def compute_model_ouput(x,w,m,b):
    f_wb =np.zeros(m)
    for i in range(m):
        f_wb[i]=w*x[i]+b
    return f_wb
#print(compute_model_ouput(x_train,w,m,b))

tmp_f_wb=compute_model_ouput(x_train,w,m,b)


#plt.figure(num='Kishou-02')
#plt.plot(x_train,tmp_f_wb,c='b',label='Our Prediction')
#plt.scatter(x_train,y_train,c='r',marker='o',label='Actual Values')
#plt.title("Housing Prices")
#plt.ylabel('Price in 1000s of USD')
#plt.xlabel('size in 1000 sqt')
#plt.legend()
#plt.show()


x_case=1.2
y_case=x_case*w+b


plt.figure(num='Kishou-03')
plt.plot(x_train,tmp_f_wb,c='b',label='Our Prediction')
plt.scatter(x_train,y_train,c='r',marker='o',label='Actual Values')
plt.scatter(x_case,y_case,c='y',marker='x',label='Case Values')
plt.plot([0,x_case,x_case],[y_case,y_case,0],c='y',label='Case Prediction')
plt.axis([1,2,300,500])
plt.title("Housing Prices")
plt.ylabel('Price in 1000s of USD')
plt.xlabel('size in 1000 sqt')
plt.legend()
plt.show()

