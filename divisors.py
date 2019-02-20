#Akke Vellinga
#adapted from https://stackoverflow.com/a/30260580

for n in range (1000,10000):
    if (n%6==0) and (n%12!=0):
            print (n, end=",")
            #makes horizontal line, not vertical
            #if not, they fall off the screen
    continue