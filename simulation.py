import math
XSupply=0
YSupply=0
pool=0
k=200
ratio=24

e=2.718281828459045

def calulate(f,i,o):
    u=f-math.log(abs(2*k+o+f),e)*(k+o)
    l=i-math.log(abs(2*k+o+i),e)*(k+o)
    return u-l
    


while True:
    while True:
        t=input("Command: ")
        if t=="Buy" or t=="Stop":
            break
        else:
            print("Invalid")
    if t=="Stop":
        break
    while True:
        token=input("Token: ")
        if token=="X" or token=="Y":
            break
        else:
            print("Invalid")
    while True:
        size=input("Number of Tokens: ")
        if size.isnumeric():
            size=int(size)
            if (token =="X" and (XSupply+size)/YSupply > ratio) or (token =="Y" and (YSupply+size)/XSupply > ratio):
                print("Ratio Exceeded")
            else:
                break
        else:
            print("Invalid")
    if token=="X":
        cost=calulate(XSupply+size,XSupply,YSupply)
        pool+=cost
        XSupply+=size
    elif token=="Y":
        cost=calulate(YSupply+size,YSupply,XSupply)
        pool+=cost
        YSupply+=size

    print("X Supply:",XSupply,"Y Supply:",YSupply,"Pool",pool,"Cost:",cost,"Cost per Token:",cost/size)
print("X Wins:",pool/XSupply)
print("Y Wins",pool/YSupply)
