from PIL import Image
"""
We have created a Steganography tool here. Most basic of the encryption tools used by Germany during WWII. Hiding messages within the pixels of the image. 

"""
def encode_data():
    img = input("Enter image -name to encode data in- with extension: ") # LOAD IMAGE WITH EXTENSION - ANY IMAGE - PRESENT IN THE SAME DIRECTORY 
    enData = input("Enter encoding message: ")  
    dataBin = [format(ord(i),'08b') for i in enData] #Every character of the data including space is converted to its ascii value which is then converted to its binary equivalent (8 bits) and stored in the list with one complete byte being one value of the list as string
    
    image = Image.open(img, 'r') #the image specified being opened to encode data in it
    imagef = Image.new(image.mode, image.size) #a copy of the image being created to encode data in and then to save it 

    imgdatat = list(image.getdata()) # pixels of the image gathered in 1D form 
    track = 0

    imgdata = [list(change) for change in imgdatat] #since the rgb values would need to be changed as per the data being encoded, we change the rgb tuples to lists too

    pixels = len(dataBin) * 3 #the data to be encoded must have its characters including space times three, <= no. of pixels of image
    for val in range(0, pixels, 3): #the logic is this: every bit of the byte (element of the list you are currently accessing) would be mapped to a corresponding value of the pixel: r g or b. For every complete byte, we use three pixels and thus 9 values. If the bit to be encoded is 1 then the rgb value it is being mapped to should be odd (if its even, we increment to make it odd) or if the bit is 0, then the rgb value it is being mapped to should be even (or decremented if its odd)
        #the ninth pixel corresponds to continuation of data: 0 if more data is to be encoded (a byte proceeding the current one) and 1 if the data to be encoded is finished (no more bytes after the current one)
        # this way, LSB of the rgb values is being changed so there would be no significant difference in the overall outlook of the image, but there would indeed be a message hidden in from the plain eye
        if (dataBin[track][0]==str(0) and ((imgdata[val][0])%2)==1):
            imgdata[val][0]= (imgdata[val][0]) - 1
        elif (dataBin[track][0]==str(1) and ((imgdata[val][0])%2)==0):
            if ((imgdata[val][0])!=0):
                imgdata[val][0]= (imgdata[val][0]) - 1
            else:
                imgdata[val][0]= (imgdata[val][0]) + 1

        if ((dataBin[track][1]==str(0)) and (((imgdata[val][1])%2)==1)):
            imgdata[val][1]= (imgdata[val][1]) - 1
        elif (dataBin[track][1]==str(1) and ((imgdata[val][1])%2)==0):
            if ((imgdata[val][1])!=0):
                imgdata[val][1]= (imgdata[val][1]) - 1
            else:
                imgdata[val][1]= (imgdata[val][1]) + 1

        if (dataBin[track][2]==str(0) and ((imgdata[val][2])%2)==1):
            imgdata[val][2]= (imgdata[val][2]) - 1
        elif (dataBin[track][2]==str(1) and ((imgdata[val][2])%2)==0):
            if ((imgdata[val][2])!=0):
                imgdata[val][2]= (imgdata[val][2]) - 1
            else:
                imgdata[val][2]= (imgdata[val][2]) + 1
        
        if (dataBin[track][3]==str(0) and ((imgdata[val+1][0])%2)==1):
            imgdata[val+1][0]= (imgdata[val+1][0]) - 1
        elif (dataBin[track][3]==str(1) and ((imgdata[val+1][0])%2)==0):
            if ((imgdata[val+1][0])!=0):
                imgdata[val+1][0]= (imgdata[val+1][0]) - 1
            else:
                imgdata[val+1][0]= (imgdata[val+1][0]) + 1
        
        if (dataBin[track][4]==str(0) and ((imgdata[val+1][1])%2)==1):
            imgdata[val+1][1]= (imgdata[val+1][1]) - 1
        elif (dataBin[track][4]==str(1) and ((imgdata[val+1][1])%2)==0):
            if ((imgdata[val+1][1])!=0):
                imgdata[val+1][1]= (imgdata[val+1][1]) - 1
            else:
                imgdata[val+1][1]= (imgdata[val+1][1]) + 1

        if (dataBin[track][5]==str(0) and ((imgdata[val+1][2])%2)==1):
            imgdata[val+1][2]= (imgdata[val+1][2]) - 1
        elif (dataBin[track][5]==str(1) and ((imgdata[val+1][2])%2)==0):
            if ((imgdata[val+1][2])!=0):
                imgdata[val+1][2]= (imgdata[val+1][2]) - 1
            else:
                imgdata[val+1][2]= (imgdata[val+1][2]) + 1

        if (dataBin[track][6]==str(0) and ((imgdata[val+2][0])%2)==1):
            imgdata[val+2][0]= (imgdata[val+2][0]) - 1
        elif (dataBin[track][6]==str(1) and ((imgdata[val+2][0])%2)==0):
            if ((imgdata[val+2][0])!=0):
                imgdata[val+2][0]= (imgdata[val+2][0]) - 1
            else:
                imgdata[val+2][0]= (imgdata[val+2][0]) + 1


        if (dataBin[track][7]==str(0) and ((imgdata[val+2][1])%2)==1):
            imgdata[val+2][1]= (imgdata[val+2][1]) - 1
        elif (dataBin[track][7]==str(1) and ((imgdata[val+2][1])%2)==0):
            if ((imgdata[val+2][1])!=0):
                imgdata[val+2][1]= (imgdata[val+2][1]) - 1
            else:
                imgdata[val+2][1]= (imgdata[val+2][1]) + 1
    

        if track == (len(dataBin)-1):
            if ((imgdata[val+2][2]) % 2) == 0:
                if (imgdata[val+2][2])!=0: 
                    (imgdata[val+2][2]) = (imgdata[val+2][2]) - 1
                else:
                    (imgdata[val+2][2]) = (imgdata[val+2][2]) + 1
        else:
            if ((imgdata[val+2][2]) % 2) == 1:
                (imgdata[val+2][2]) = (imgdata[val+2][2]) - 1
        track = track + 1
    imgdataf = [tuple(changef) for changef in imgdata]
    imagef.putdata(imgdataf)

    newImage = input("Enter name of final image with extension: ")
    imagef.save(newImage, str(newImage.split(".")[1].upper()))


encode_data()

