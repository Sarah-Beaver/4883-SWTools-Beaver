* ImageInfo.json
    * has the subimages information about colors and percentage
* BeforImage.zip
    * zip file that contains images that were used 
* FinalImages.zip
    * zip file that has the final product of the images after they have gone through mosaic.py
* emojis.zip
    * zip file that has the emojis that I used for subimages, after extracted it is default for subimages for mosaic.py
* mosiac.py
    * the file that takes a input file, input folder that contains subimages, size for subimages, and a output folder for where to store the final image. This file uses ImageInfo.json that contains info on the subimages
* processSubimages.py
    * take a folder that will be the subimages, it loops through the folder and gets the colors of each image and stores it in ImageInfo.json
* flower.jpg
    * default for input image for mosaic.py
   
  
If you do not want to use the emojis as the subimages then run processSubimages.py on the folder that contains the images desired as the subimages. This will create the ImageInfo.json file which will contain information about the colors of each of the images.

Ex: python3 processSubimages.py folder=emojis 


Afterwards or otherwise run mosiac.py. This will take the input file and using the folder provided will loop through and replace each pixel with one of the images from the folder. IMPORTANT: the folder provided should have already been processed using processSubimages.py unless using emojis and the default I provided. Can enter a size that the subimages will be resized to and a output folder on where to store the final image. If no output folder provided it will take the form OriginalName_mosiac.png else it will be placed in the folder like OriginalName.png. The defualts for mosiac.py is input_file=flower.jpg, input_folder=emojis, output_folder is none, size=16. If want to use different values use following format.

Ex: python3 mosaic.py input_file=pathToImage/ImageName.ext input_folder=emojis size=24 output_folder=finalImages 



