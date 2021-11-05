def setbackground(imgpath):
    from PIL import Image, ImageFilter
    #Open existing image 
    OriImage = Image.open ('assets/images/bg.png') 
    OriImage.show () 
    # Apply GaussianBlur filter
    gaussImage = OriImage.filter (ImageFilter.GaussianBlur (5)) 
    gaussImage.show () 
    #Save Gaussian Blur Image 
    gaussImage.save ('assets/bg/0.png')