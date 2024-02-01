from PIL import Image
import PIL

################################################# Mean Smoothing Filter
def mean_smoothing_filter(image,k):
    # Make a new image 
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
                        c = c+ (image.getpixel((x+i,y+j)))*(1/pow(k,2))   
            # Add new color to new image            
            im.putpixel((x,y),int(c))
    return im;                   
#########################################################################
image= Image.open("Smoothing Filters\images\cameraman.png")
image = image.convert('L')
image.show()

mask_size=3
image=mean_smoothing_filter(image,mask_size)

image.show()