n = int(input("input your nummber"))

print(n)
divisor = 0
divi = []
for i in range(1,n+1):
    if n%i == 0:
        divisor = divisor + 1
        divi.append(i) 
print("your number of divisor are ",divisor)
print("your divisor are ",divi)
