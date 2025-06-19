'''Rewrite the previous function so that it returns the pattern as a string, 
then assign the result to a variables and print it.'''

def triangle (num:int) ->str:
    '''returns reverse triangle starting from the given number down to 1.'''
    result=""
    while num> 0:
        for i in range(num, 0 ,-1):
            result+=str(i) + " "
        result+="\n"
        num-=1
    return result

uesrinput=(int(input("Enter any number: ")))
print(triangle(uesrinput))

print(triangle.__doc__)