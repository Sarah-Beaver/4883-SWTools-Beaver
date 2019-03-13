* match.py
    * takes a folder and a path to an image then compares the image to every image in the folder to find the closest match using mean square error
  
  
Suggest using the emojis folder from previous assignment. The folder should have all pictures and nothing else. It compares the name of the image to see if it is the same image so if two images are the same but names differently then it will match the two images together. Run match.py with command lines folder=path1 image=path2 where path1 is equal to the path to the folder with all the images and path2 is the path to the image. 

Ex: python3 match.py folder=emojis image=emojis/wolf.png 

This will return a plot with the image and closest image and the error score.
