# Practice 01 (Model Representation)
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

def compute_model_ouput(x,w,b):
    m=x.shape[0]
    tmp_w=np.full((m,),w)
    tmp_b=np.full((m,),b)
    f_wb=x*tmp_w+tmp_b
    return f_wb
#print(compute_model_ouput(x_train,w,m,b))

if __name__=="__main__":
    tmp_f_wb=compute_model_ouput(x_train,w,b)


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


if __name__=="__main__":
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

