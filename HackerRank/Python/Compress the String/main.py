# Enter your code here. Read input from STDIN. Print output to STDOUT
value = input()
count = 0 
a = value[0]

for i in value:
    #print(i, " ", a)
    if i != a or i == value[len(value)-1]:
        count +=1
        print("(",a ,",", str(count),")",end=" ")
        count=0
        a=i
    else:
        count +=1


