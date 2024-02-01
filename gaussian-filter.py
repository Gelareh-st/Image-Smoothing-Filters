from PIL import Image
import PIL
import numpy as np

########################################################################## Gaussian Matrix
def create_gaussian_matrix(k, sigma):
    x, y = np.meshgrid(np.arange(-k // 2 + 1, k // 2 + 1), np.arange(-k // 2 + 1, k // 2 + 1))
    exponent = - (x**2 + y**2) / (2 * sigma**2)
    gaussian_2d = np.exp(exponent)
    gaussian_matrix = gaussian_2d / (2 * np.pi * sigma**2)
    gaussian_matrix /= np.sum(gaussian_matrix)
    return gaussian_matrix
################################################################ Gaussian Smoothing Filter
def gaussian_smoothing_filter(image,k,sigma):
    # Create gaussian matrix with mask size and sigma
    gaussian_matrix = create_gaussian_matrix(k,sigma)
    # Create a new image 
    im = PIL.Image.new(mode="L", size=(image.width,image.height))
    # Define the edge of the frame from the middle element (1 for 3*3 , 2 for 5*5)
    m=n=int((k-1)/2)
    # For odd frames
    if k%2==0:
        n+=1
    # Loop on image pixels  
    for x in range(image.width):
        for y in range(image.height):
            # New color
            c=0;
            # Loop on frame pixels
            for i in range(-m,n+1):
                for j in range(-m,n+1):
                    if x+i<0 or y+j<0 or x+i>=image.width or y+j>=image.height :
                        continue
                    else:
                        c = c+ (image.getpixel((x+i,y+j)))*(gaussian_matrix[i+int((k-1)/2)][j+int((k-1)/2)])   
            # Add new color to new image            
            im.putpixel((x,y),int(c))
    return im;                   
##############################################################################################
image= Image.open("Smoothing Filters\images\cameraman.png")
image = image.convert('L')
image.show()

mask_size=5
sigma=1.4

image=gaussian_smoothing_filter(image,mask_size,sigma)

image.show()