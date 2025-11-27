# basic approach:
# setting the varible
a,b=1,2 # s
total =0
#looping statement
while a<4000000:
    if a%2==0:
        total +=a
    a,b = b, a+b
print(total)

    