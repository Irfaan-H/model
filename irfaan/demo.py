#x=["irfaan,2,1.8"]
av=80
x=int(input("how many pen you want"))

i=1
while i<=x:

    if i>av:
        print("out of stock")
        break

    print("INK pen",i)
    i+=1

print("finished")