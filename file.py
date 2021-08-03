file1 = open("intro","r")
data = file1.readlines()
#print(data)

for line in data:
    print(line)

temp = "things cup cars drinks"
print(temp.split(','))

def printmyname(i):
    for a in range(i):
        print("I am Rishi")

#printmyname(1)

def USDintoINR(money):
    print("1 Dollar is equal to 72 Indian rupees")
    print(money*72)   

USDintoINR(500)

def countwords():
    filename = input("Enter your file name")
    f = open(filename,"r")
    total = 0 
    for line in f:
        words = line.split()
        total = total + len(words)
        print("Line:"+str(len(words)))
    print("Total numeber of words ="+str(total))

countwords()
