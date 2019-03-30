import os
import sys
import json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from pprint import pprint
import requests
from difflib import SequenceMatcher


# Course: cmps 4883
# Assignemt: A08
# Date: 3/30/19
# Github username: bluefire8421
# Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
# Name: Sarah Beaver
# Description: 
#   taking an image and recreating it as a mosiac using smaller images



def similar(a, b):
    """takes two strings and returns how similar to strings are
    Arguments:
        a         -- first string
        b         -- second string
    Returns:
        percentange of similarity
    """
    return SequenceMatcher(None, a, b).ratio()


def newImage(imagepath,folderpath,resize):
    """recreates the image using images in the folder that will be the size of resize
    Arguments:
        imagepath        -- the path to the original image
        folderpath       -- the path to the folder that contain subimages
        resize           -- the size the subimages will be
    Returns:
        new mosiac image
    Requres:
        getClosestColor
    """
    # opens the image
    im = Image.open(imagepath)
 
    width,height = im.size
    # get list of pixel before converting and resizing
    pixels=list(im.getdata())
    # converts and resize the image

    im=im.convert('RGBA').resize((width*resize,height*resize))
    #   im = Image.new('RGBA', (width*resize,height*resize), color = 'white')
    # opens ImageInfo.json, contains info about subimages
    with open('ImageInfo.json') as f:
        data = json.load(f)

    count=0
    
    # loop through each pixel from original image
    for i in range(height):
        for k in range(width):
            # gets the closest colors from api
            payload = {'r':pixels[count][0], 'g':pixels[count][1], 'b':pixels[count][2],'d':3}
            r = requests.get('http://cs.mwsu.edu/~griffin/color-api/', params=payload)
            # finds the closest image with the matching colors
            image=getClosestColor(r.json(),folderpath,data)
            image=Image.open(image)
            # converts and resizes the returned image then pastes it over orignal resized image
            image=image.convert('RGBA').resize((resize,resize))
            im.paste(image,(k*resize,i*resize),image)
            count+=1
        
    # shows the image to user before returning new image
    im.show()
    return im
    # newImg.show()
    # newImg.save(output)

    

def getClosestColor(color,folderpath,data):
    """finds the subimage with the closest color 
    Arguments:
        imagepath        -- the path to the original image
        folderpath       -- the path to the folder that contain subimages
        resize           -- the size the subimages will be
    Returns:
        new mosiac image
    Requres:
        getClosestColor
    """
    primcolor=""
    primdist=1
    seccolor=""
    secdist=1
    # gets the cloest matching primary and secondary color
    for result in color["result"]:
        if(result["dist"]<primdist):
            seccolor=primcolor
            secdist=primdist
            primdist=result["dist"]
            primcolor=result["name"]
        elif(result["dist"]<secdist):
            secdist=result["dist"]
            seccolor=result["name"]

    im=""
    percent=0
    im2=""
    percent2=0
    tempim=""
    simcolor=1
    # finds the image with the best match to the primary or secondary color
    for image,values in data.items():
        for item in values:
            for color,value in item.items():
                if(color == primcolor and value>percent):
                    im=image
                    percent=value
                elif(color == seccolor and value>percent2):
                    im2=image
                    percent2=value
                # last resort to find best matching color to primary or secondary color
                # if primary or secondary can not be found
                elif(im=="" and im2==""):
                    percentsim=similar(color,primcolor)
                    if(percentsim<simcolor):
                        tempim=image
                        simcolor=percentsim
                    percentsim=similar(color,seccolor)
                    if(percentsim<simcolor):
                        tempim=image
                        simcolor=percentsim
    
    # check if primary or secondary color found else uses closest match
    if(im!="" or im2!=""):
        if(percent>percent2):
            return folderpath+"/"+im
        else:
            return folderpath+"/"+im2
    else:
        return folderpath+"/"+tempim


if __name__=='__main__':
 
    args = {}
    output=""
    inputfile="flower.jpg"
    inputfolder="emojis"
    size=16
    # loops through arguments to get folder and image paths
    for arg in sys.argv[1:]:
        k,v = arg.split('=')
        if(k=="output_folder"):
            output=v
        elif(k=="input_file"):
            inputfile=v
        elif(k=="input_folder"):
            inputfolder=v
        elif(k=="size"):
            size=v
        args[k] = v
    # try:
    if(os.path.isfile(inputfile)):
        if(os.path.isdir(inputfolder)):
            if(size):
                filename = os.path.basename(inputfile) # get only filename if image is read with a path. 
                image=newImage(inputfile,inputfolder,int(size))
                name,ext = filename.split('.')
                if(os.path.isdir(output)):
                    image.save(output+"/"+name+'.png')
                else:
                    
                    newname = name+'_mosaic'+'.png'
                    image.save(newname)
    # except:
    #     print("There was a problem. Please check the file and folder paths.")
    #     sys.exit()

    
