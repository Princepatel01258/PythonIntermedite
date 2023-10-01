#DEFAULT ARGUEMENTS
def average(a, b):
    print("the average is", (a+b)/2)
average(4, 5)

#DEFAULT ARGUEMENTS
def average1(c=9, d=1):
    print("the average is", (c+d)/2)
average1(1,6)

#KEYWORD ARGUEMENTS

def average2(e=9, f=1):
    print("the average is", (e+f)/2)
average2(9,21)

#REQUIRED ARGUEMENTS

def average3(g, h=1,i=2):
    print("the average is", (g+h+i)/2)
average3(1)

#ARBITARY ARGUEMENTS

def averege4(*numbers):
    for i in numbers:
        sum = 0
        sum = sum + i
        print("Average is:", sum/len(numbers))
averege4(6,8,10,15)

#KEYWORD ARBITARY ARGUEMENTS

def name(**name):
    print( "Hello, ",name["fname"],
        name["mname"],name[ "lname"] )
name( mname = "Buchanan",lname = "Barnes",fname = "James" )





