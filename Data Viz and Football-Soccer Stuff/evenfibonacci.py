n= int(input("The sequence length: "))
fterm= 0
x=1
count= 1
fsum=0

#0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 .........

while x<= n:
    x+= 1
    sterm= fterm + count
    fterm= count
    count= sterm
    #print(count)
    if count%2== 0:
        #print(count)
        if fsum<4000000:
            fsum+=count
        else:
            break
            
            
print(fsum)
