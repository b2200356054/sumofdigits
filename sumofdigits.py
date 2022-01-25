import sys

inputnumber = int(sys.argv[1])
powernumber = int(sys.argv[2])
actualnumber = int(inputnumber**powernumber)
repeatoption = 1
checkbox = [x for x in str(actualnumber)]
lastoutput = "{}^{} = {}".format(inputnumber, powernumber, actualnumber)

if len(checkbox) != 1:
    lastoutput = lastoutput + " = "
  
while len(checkbox)>1:
    sum = 0
    digitsumstr = ""
    for digits in checkbox:
        sum = sum + int(digits)
    for digitsstr in range(len(checkbox)):
        term = checkbox[digitsstr]
        if digitsstr == len(checkbox)-1:
            digitsumstr = digitsumstr + term
        else:
            digitsumstr = digitsumstr + term + " + "
    if len(checkbox) == 2:
        lastoutput = lastoutput + digitsumstr + " = " + "{}".format(sum)
    else: 
        lastoutput = lastoutput + digitsumstr + " = " + "{}".format(sum) + " = "
    checkbox = [i for i in str(sum)]
print(lastoutput)
    
    

    
    
        
    
