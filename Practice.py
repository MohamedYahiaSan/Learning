import numpy as np 

x=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]])
print(x)

mu=np.mean(x,axis=0)
#print(mu)

sigma=np.std(x,axis=0)
#print(sigma)

z=np.array(55)
result=np.dot([666],z)
print(result)
z+=4
print(z)