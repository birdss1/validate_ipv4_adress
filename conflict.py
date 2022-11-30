event1= [x for x in input().split()]
event2= [x for x in input().split()]
def convert_into_second(x):
    a=(x).split(":")
    print(a)
    b=int(a[0])*60
    return (b*60 + int(a[1])*60)
x=(convert_into_second(event1[1]))
y=(convert_into_second(event2[0]))
if x >= y:
    print("true")
else:
    print("false")


