# Blurring Img with Numpy slicing
import matplotlib.pyplot as plt
import numpy as np 
import os


#Reading Img data with plt.imread                       <<<===========(Make Sure to path to your img PROPERLY)
path=os.path.dirname(os.path.realpath(__file__))
img_path=os.path.join(path,'img.png')
img_path2=os.path.join(path,'img_2.png')
img= plt.imread(img_path)
img_2=plt.imread(img_path2)

#Blurring function with blurring factor
def blurr(img,factor:int):
    avg_img=np.array( 
        img[:-factor*2,factor:-factor,:]+ #Top
        img[factor:-factor,:-factor*2,:]+ #Left
        img[factor*2:,factor:-factor,:]+ #Bottom
        img[factor:-factor,factor*2:,:]+ #Right
        img[factor:-factor,factor:-factor,:] #Center
    )/5.0

    
    
    return avg_img


#Applyign on our 2 selected images, this can be repeated with smaller factor to output a finer blur
blur=blurr(img,5)
blur_2=blurr(img_2,3)


#Plotting
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(8, 8), constrained_layout=True, 
                         subplot_kw={'xticks': [], 'yticks': []},
                         gridspec_kw={'hspace': 0.2, 'wspace': 0.4})

# Displaying the images
axes[0, 0].imshow(img, cmap=plt.cm.hsv)
axes[0, 0].set_title('Original Image 1')

axes[0, 1].imshow(blur, cmap=plt.cm.hsv)
axes[0, 1].set_title('Blurred Image 1')

axes[1, 0].imshow(img_2, cmap=plt.cm.hsv)
axes[1, 0].set_title('Original Image 2')

axes[1, 1].imshow(blur_2, cmap=plt.cm.hsv)
axes[1, 1].set_title('Blurred Image 2')

plt.show()