* ascii_image.py
    * changes a image into font characters
* dPolyImperial.otf
   * the default font style if another is not given
* dragon.jpeg
     * default picture if another is not given
* output.jpg
     * example of what the picture may look like
  
    
Download all the files. When running the python file please enter the path to image to change, then output name, then path to font to use, then the fontsize. If image or font does not exist then it will run using the default which is the two files given and a fontsize of 12 and outputs to output.jpg. All files should be at the same level.

ascii_image.py takes an image and converts it to characters using a font.

The program will automatically change the picture to resize to 200Xx where x is made so the image is not skewed. If this is not wanted go in and comment out im=resize(im,200). Also any font chosen should have the characters b, d, f, r, K, R, A, F, D, L, B as these are the characters used in this program.

