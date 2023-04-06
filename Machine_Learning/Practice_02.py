import numpy as np 
import matplotlib.pyplot as plt
from Practice_01 import *

print(x_train)

f_wb=compute_model_ouput(x_train,w,m,b)

total_cost=(1/(2*m))*(f_wb-y_train)**2

print (total_cost)