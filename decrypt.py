from PIL import Image

def decode_data():
    img = input("Enter image name - to decode data from - with extension: ") #Here we load an image which might have some message encoded in it, either that be the one we just encoded some data in, or an image with data encoded from some other source.
    # we start checking three pixels until the ninth value of the current trio of pixels is 1 which would mean we have reached the end of data being deciphered
    # if an r g b value is 1 (in the trio of pixels - we are checking the eight values for one complete byte whose ascii equivalent would give us the character) then we append 1 to our byte, and 0 if the r g b value being checked is odd. 
    image = Image.open(img, 'r')
    imgdata = list(image.getdata())
    dataBin = []
    for val in range(0, len(imgdata), 3):
        tstr = ''
        if ((imgdata[val][0]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val][1]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val][2]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val+1][0]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val+1][1]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val+1][2]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val+2][0]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        if ((imgdata[val+2][1]%2)==0):
            tstr+=str(0)
        else:
            tstr+=str(1)
        
        dataBin.append(tstr)

        if ((imgdata[val+2][2]%2)==1):
            break
        else:
            continue
    fstr = [(chr(int(val,2))) for val in dataBin]
    print("The decoded message is: ", (''.join(fstr))) #decoded message displayed. 


decode_data()
    

    


