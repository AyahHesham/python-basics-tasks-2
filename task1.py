import base64
from email.mime import base
sentance=input("Enter the sentance to encribtion: ")
encriptsentance=sentance.encode('ascii')
messagebyte=base64.b64encode(encriptsentance)
mreadable=messagebyte.decode('ascii')
print(mreadable)
x=input("if you want to decode the sentance press 1 if not press any key")
if int(x)==1:
    newsen=mreadable.encode('ascii')
    bytenewsentance=base64.b64decode(newsen)
    finsentance=bytenewsentance.decode('ascii')
    print(finsentance)
if x!=1:
    break

