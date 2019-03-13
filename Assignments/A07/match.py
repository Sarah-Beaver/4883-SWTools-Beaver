# Course: cmps 4883
# Assignemt: A07
# Date: 3/11/19
# Github username: bluefire8421
# Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
# Name: Sarah Beaver
# Description: 
#   takes a image and a folder then loops through folder to find the closest image


import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image,ImageMath
import os



def mse(imageA, imageB):
    # takes two images and calculates the mean square error between the two

    # have to open images inside
    im=Image.open(imageA)
    im2=Image.open(imageB)
	# the 'Mean Squared Error' between the two images is the
	# sum of the squared difference between the two images;
	# NOTE: the two images must have the same dimension
    err = np.sum(ImageMath.eval("(convert(a,'F') - convert(b,'F'))** 2", a=im,b=im2))
    err /= float(im.size[0] * im.size[1])
	
	# return the MSE, the lower the error, the more "similar"
	# the two images are
    return err


if __name__=='__main__':
    args = {}
    meansquare=sys.maxsize
    currentimage=""
    # loops throug arguments to get folder and image paths
    for arg in sys.argv[1:]:
        k,v = arg.split('=')
        args[k] = v
    #  try catch for any errors
    try:
        # check if the image and the folder exist
        if(os.path.isfile(args['image'])):
            if(os.path.isdir(args['folder'])):
                imagenames=args['image'].split('/')
                imagename=imagenames[-1]
                # loops through images in the directory
                for filename in os.listdir(args['folder']):
                    # check if the filename and image name are the same
                    if(filename!=imagename):
                        error=mse(args['image'],args['folder']+'/'+filename)
                        # check if this image is more similar than previous images
                        if(meansquare>error):
                            meansquare=error
                            currentimage=args['folder']+'/'+filename
                # open images for plot
                im=Image.open(args['image'])
                im2=Image.open(currentimage)
                
                fig = plt.figure("Closest Image Using Mean Square")
                plt.suptitle("%s matches to %s with MSE: %.2f" % (args['image'],currentimage,meansquare))
            
                # show first image
                ax = fig.add_subplot(1, 2, 1)
                plt.imshow(im)
                plt.axis("off")
            
                # show the second image
                ax = fig.add_subplot(1, 2, 2)
                plt.imshow(im2)
                plt.axis("off")
            
                # show the images
                plt.show()
                        
                        
    except:
        print("There was a problem. Please check the file and folder paths.")
        sys.exit()

    
            
        
    
   