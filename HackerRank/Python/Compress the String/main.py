# Enter your code here. Read input from STDIN. Print output to STDOUT
value = input()
num = 0 
for i in value:
    print(i)
    if i == "a":
        num +=1

print("num:"+ str(num))