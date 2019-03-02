import os.path
import sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# Course: cmps 4883
# Assignemt: A04
# Date: 3/1/19
# Github username: bluefire8421
# Repo url: https://github.com/bluefire8421/4883-SWTools-Beaver
# Name: Sarah Beaver
# Description: 
#   taking a picture and recreating it using a font




def img_to_ascii(**kwargs):
    """ 
    The ascii character set we use to replace pixels. 
    The grayscale pixel values are 0-255.
    0 - 25 = '#' (darkest character)
    250-255 = '.' (lightest character)
    """
    ascii_chars = [ 'b', 'd', 'f', 'r', 'K', 'R', 'A', 'F', 'D', 'L', 'B']

  
   
    path = kwargs.get('path')
    font=kwargs.get('font')
    fontsize=kwargs.get('fontsize')
    output = kwargs.get('output')
    # width = kwargs.get('width',100)

   
    im = Image.open(path)
    # im = resize(im,200)
    im.show()
    width,height = im.size

    imagedata=list(im.getdata())
    count=0
    offset=fontsize//4
    fnt = ImageFont.truetype(font, fontsize)
    newImg = Image.new('RGB', (width*fontsize//2,height*fontsize//2), (255,255,255))
    drawOnMe = ImageDraw.Draw(newImg)


    for i in range(height):
        for k in range(width):
            r,g,b=imagedata[count]
            spot=int((r+g+b)/3)//25
            drawOnMe.text((k*fontsize//2+offset,i*fontsize//2+offset), ascii_chars[spot], font=fnt, fill=(r,g,b))
            count+=1
    
    newImg.show()
    newImg.save(output)
  

    # print(w,h)

    # # im = im.convert("L") # convert to grayscale

    # imlist = list(im.getdata())

    # i = 1
    # for val in imlist:
    #     sys.stdout.write(ascii_chars[val // 25])
    #     i += 1
    #     if i % width == 0:
    #         sys.stdout.write("\n")

    

def resize(img,width):
    """
    This resizes the img while maintining aspect ratio. Keep in 
    mind that not all images scale to ascii perfectly because of the
    large discrepancy between line height line width (characters are 
    closer together horizontally then vertically)
    """
    
    wpercent = float(width / float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((width ,hsize), Image.ANTIALIAS)

    return img


if __name__=='__main__':
    if(len(sys.argv)==5):
        path =sys.argv[1]
        output=sys.argv[2]
        font=sys.argv[3]
        fontsize=int(sys.argv[4])
    else:
        path='dragon.jpeg'
        output='output.jpeg'
        font='dPolyImperial.otf'
        fontsize=12
    if os.path.isfile(path):
        if os.path.isfile(font):
            img_to_ascii(path=path,output=output,font=font,fontsize=fontsize)
            sys.exit()
    print("Problem finding picture or font. Check path and try again")
    # path = 'dragon.jpeg'
    
