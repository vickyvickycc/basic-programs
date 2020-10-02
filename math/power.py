def power(a,b):
    """
        power(a,b) => finds value of a^b
        parameters: 
            a => integer
            b => integer
        returns: the value of a^b
    """
    if(b==0):
        return 1
    elif(b==1):
        return a;
    else:
        val=a**(b//2);
        if(b%2==0):
            return val*val;
        else:
            return a*val*val

if(__name__ == "__main__"):
    a=2
    b=2
    print(str(a)+"^"+str(b)+" is: "+str(power(a,b)));