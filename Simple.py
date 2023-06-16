def up_low(s):

    upper=0;lower=0

    for i in s:

        if i.isupper():

            upper+=1

        elif i.islower() :

            lower+=1

    return(upper,lower)

s = "Hello Mr. Rogers, how are you this fine Tuesday?"

print(up_low(s))
