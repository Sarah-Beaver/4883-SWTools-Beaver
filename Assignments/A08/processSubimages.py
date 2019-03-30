# Course: cmps 4883
# Assignemt: A07
# Date: 3/30/19
# Github username: bluefire8421
# Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
# Name: Sarah Beaver
# Description: 
#   assigns colors to images and puts info into json 


import matplotlib.pyplot as plt
import numpy as np
import sys
from PIL import Image,ImageMath
import os
import cv2
from sklearn.cluster import KMeans
from pprint import pprint
import requests
from math import sqrt
import json


def brightness(r,g,b):
    """A function to return the calculated "brightness" of a color.
    http://www.nbdtech.com/Blog/archive/2008/04/27/Calculating-the-Perceived-Brightness-of-a-Color.aspx
    Arguments:
        r: [int]
        g: [int]
        b: [int]
    Returns:
        Values between 0-1 (percent of 0-255)
    Used By:
        get_dominant_colors
    """
    return sqrt(pow(r,2) * .241  + pow(g,2) * .691 + pow(b,2) * .068 ) / 255

def find_histogram(clt):
    """ Create a histogram with k clusters
    Arguments:
        :param: clt
        :return:hist
    Used By:
        get_dominant_colors
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist


def get_color_data(r,g,b,d=3):
    """Get color name and hsv from color api.
    Arguments:
        r -- red   [int]
        g -- green [int]
        b -- blue  [int]
    Returns:
        json
    """
    payload = {'r':r, 'g':g, 'b':b,'d':d}
    r = requests.get('http://cs.mwsu.edu/~griffin/color-api/', params=payload)
    return r.json()


def extract_cluster_color_values(hist, centroids,ignore_background=False):
    """Get the dominant colors of an image.
    Arguments:
        hist        -- [numpy.ndarray]
        centroids   -- [numpy.ndarray] 
    Returns:
        dictionary of color values
    Used By:
        get_dominant_colors
    """

    colors = []
    
    for (percent, color) in zip(hist, centroids):
        rgb = []
        total = 0
        for c in color:
            c = round(float(c))
            total += c
            rgb.append(c)
        if ignore_background:
            if total > 15 and total < 750:
                colors.append({'percent':round(float(percent),2),'rgb':rgb})
        else:
            colors.append({'percent':round(float(percent),2),'rgb':rgb})

    return colors

def plot_colors(hist, centroids):
    """Get the dominant colors of an image.
    Arguments:
        hist        -- [numpy.ndarray]
        centroids   -- [numpy.ndarray] 
    Returns:
        plot image
    """
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50),
                      color.astype("uint8").tolist(), -1)
        startX = endX

    # return the bar chart
    return bar


def get_dominant_colors(img,save_path=None,n=3):
    """Get the dominant colors of an image.
    Arguments:
        img         -- the image [string, numpy.ndarray]
        save_path   -- out path for saving [string] (default None)
        n           -- number of clusters [int] (default 3)
    Returns:
        dictionary of colors
        load_subimages_data
    Requres:
        extract_cluster_color_values
        query_color
        brightness
    """

    #bg,_ = determine_background(img_path)

    # if its string open it
    if isinstance(img,str):
        if os.path.isfile(img):
            img = cv2.imread(img)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        else:
            usage("Error: image path not valid")

    img = img.reshape((img.shape[0] * img.shape[1],3)) #represent as row*column,channel number

    clt = KMeans(n_clusters=n) #cluster number
    clt.fit(img)

    hist = find_histogram(clt)
    colors = extract_cluster_color_values(hist, clt.cluster_centers_)

    if save_path != None:
        bar = plot_colors(hist, clt.cluster_centers_)
        cv2.imwrite(save_path,bar)
        # plt.axis("off")
        # plt.imshow(bar)
        # plt.show()

    start_delta = 3
    
    # loop through each cluster
    for i in range(len(colors)):
        c = []
        d = start_delta
        # while we haven't found a named color match (increment delta)
        while len(c) < 1:
            #c = query_color(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2],d)
            c = get_color_data(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2],d)
            d += 3
        colors[i]['named_data'] = c
        colors[i]['brightness'] = brightness(colors[i]['rgb'][0],colors[i]['rgb'][1],colors[i]['rgb'][2])
    
    return colors


if __name__=='__main__':
    args = {}
    images={}

    # loops throug arguments to get folder and image paths
    for arg in sys.argv[1:]:
        k,v = arg.split('=')
        args[k] = v
     
 
    #  try catch for any errors
    try:
        # check if the folder exist
        if(os.path.isdir(args['folder'])):
            # loops through images in the directory
            for filename in os.listdir(args['folder']):
                # returns dominant colors
                colors=get_dominant_colors(args['folder']+'/'+filename)
                percent=colors[0]["percent"]
                dist=1
                # loops through the returned colors in first one
                for color in colors[0]["named_data"]["result"]:
                    if(color["dist"]<dist):
                        dist=color["dist"]
                        colorname=color["name"]

                images[filename]=[]
                images[filename].append({colorname:percent})
                
                percent1=colors[1]["percent"]
                dist=1
                # assigns the colors into the list based on percent 0 highest 2 is lowest
                for color in colors[1]["named_data"]["result"]:
                    if(color["dist"]<dist):
                        dist=color["dist"]
                        colorname=color["name"]
                if(percent>percent1):
                    images[filename].insert(1,{colorname:percent1})
                else:
                    images[filename].insert(0,{colorname:percent1})
                
                percent2=colors[2]["percent"]
                dist=1
                for color in colors[2]["named_data"]["result"]:
                    if(color["dist"]<dist):
                        dist=color["dist"]
                        colorname=color["name"]
                if(percent>percent2 and percent1>percent2):
                    images[filename].insert(2,{colorname:percent2})
                elif(percent2>percent and percent2>percent1):
                    images[filename].insert(0,{colorname:percent2})
                else:
                    images[filename].insert(1,{colorname:percent2})
            f=open("ImageInfo.json",'w')
            f.write(json.dumps(images))
            f.close() 
                               
    except:
        print("There was a problem. Please check the file and folder paths.")
        sys.exit()