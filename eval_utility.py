exp="2 + 7 + (8 * 4) + 9"
data=[]
brackets={")":"("}
operators=["+","-","*","/"]
op=[]
inoperator=[]
check=0
def applyoperator(a,b,op):
    a=int(a)
    b=int(b)
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="*":
        return a*b
    if op=="/":
        return a/b

for item in exp:
    if item.isdigit():
        data.append(item)
    if(item in operators):
        op.append(item)
    if(item in brackets.values()):
        inoperator.append(item)
        check=1
    if(item in brackets.keys() and inoperator[-1]==brackets[item]):
        b=data.pop()
        a=data.pop()
        operator=op.pop()
        print(a,b,operator)
        val=applyoperator(a,b,operator)
        data.append(val)





