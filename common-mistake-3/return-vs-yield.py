# When defining a function with iteration, for example, list, strings or even files under the same directory, yield is recommended 
# and that keyword returns a generator 
# Remember yield is only a generator with no code actually runs 

def createGenerator():
    mylist = range(3)
    for i in mylist:
        yield i*i

myGenerator = createGenerator()

for i in myGenerator:
    print(i) # print the result of i*i 
    
# Common mistake is to use return instead of yield, which terminates the iteration once the very first instance is captured 
