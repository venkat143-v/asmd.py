def add(a,b):
    print(a+b)
def mul(a,b):
    print(a*b)
def sub(a,b):
    print(a-b)
def div(a,b):
    print(a%b)

a=int(input())
b=int(input())
print('1:add,2:mul,3:sub,4:div')
c=int(input())
if c==1:
  add(a,b)
elif c==2:
   mul(a,b)
elif c==3:
   sub(a,b)
else:
   div(a,b)
