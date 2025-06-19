'''

## Create a function that takes 1 parameter of type int , then it prints out the result formatted like the following patter (if we give it 5 for example):

**Example Output for `5`**
```
5 4 3 2 1   
4 3 2 1   
3 2 1   
2 1   
1   
```

#### Document the newly created function. describe what it does, then print the documentation. 

'''



def triangle (num:int):
    '''Prints a reverse triangle starting from the given number down to 1.'''

    while num> 0:
        for i in range(num, 0 ,-1):
            print(i ,end=" ")
        print()
        num-=1

triangle(int(input("Enter any number: ")))

print(triangle.__doc__)