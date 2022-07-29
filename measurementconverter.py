def convertCtoF(ccelesius)->int:
    f=(ccelesius*1.8)+32
    print(f"the tembreature by Fahrenheit is :{f} F°")
def convertFtoC(cFahrenheit)->int:    
    c=((cFahrenheit+ 40)/1.8)-40
    print(f"the tembreature by celesius is :{c} c°")
def convertENCHtoCM(ENCH):
    enchtocm=ENCH*2.45
    print(f"the measure by cm is :{enchtocm} cm")
def convertCMtoENCH(CM):
    Cmtoench=CM/2.45
    print(f"the measure by ench is :{Cmtoench} ench")

userchoice=int(input('''1:convert tembrature from celesius to Fahrenheit 
                         2:convert tembrature from Fahrenheit to celesius
                         3:convert measure from inch to cm
                         4:convert measure from cm to ench'''))
if userchoice==1:
    ccelesius=int(input('Enter the tembrature by celesius: '))
    convertCtoF(ccelesius)
elif userchoice==2:
    cFahrenheit=int(input('Enter the tembrature by Fahrenheit: '))
    convertFtoC(cFahrenheit)
elif userchoice==3:
    ENCH=int(input('Enter the tembrature by ENCH: '))
    convertENCHtoCM(ENCH)
elif userchoice==4:
    CM=int(input('Enter the tembrature by CM: '))
    convertCMtoENCH(CM)





