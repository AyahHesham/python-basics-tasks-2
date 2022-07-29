'''the library for encoding and decoding messag'''
import base64
from email.mime import base
'''the message that i want to encrypt it'''
sentance=input("Enter the sentance to encribtion: ")
'''encrypt it by assc code '''
encriptsentance=sentance.encode('ascii')
'''after encrybted the message convert to bytes not readable by human
,i but it in variable to decode it into string'''
messagebyte=base64.b64encode(encriptsentance)
'''decode the byte to string by thae same way asc code to raad by human '''
mreadable=messagebyte.decode('ascii')
print(mreadable)
x=input("if you want to decode the sentance press 1 if not press any key")
if int(x)==1:
    '''decription the sentance by asccode too'''
    newsen=mreadable.encode('ascii')
    '''the sentance after decripted but bytes'''
    bytenewsentance=base64.b64decode(newsen)
    '''final sentane after being string with asc code'''
    finsentance=bytenewsentance.decode('ascii')
    print(finsentance)


